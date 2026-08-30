"""
Views for the core app.
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone
from django.views import View
from django.views.generic import ListView

from .formatting import describe_journey
from .forms import (
    CaptureForm,
    CaptureTagFormSet,
    ResightingForm,
    TagForm,
    TagFormSet,
    assign_tag_order,
)
from .matching import link_matching_resightings
from .models import Capture, Location, Observer, Resighting, Species


class HomeView(ListView):
    """Home page: a paginated feed of recent resightings, headlined by
    the 'ringed here, seen here' story -- the engaging part for visitors
    who aren't the observer, per the site's two goals of helping users
    manage their own records and inspiring others to go look for birds.

    Filterable by species, place, or country. Place and country match
    against *either* side of a resighting (where it was seen, or -- if
    known -- where it was ringed), rather than being separate "seen at"
    and "ringed at" filters. That's deliberate: picking a place you watch
    birds at surfaces the diversity of countries they were ringed in, and
    picking a place birds are ringed at surfaces the diversity of
    countries they've since been seen in -- the same filter serves both
    stories.
    """

    template_name = "core/home.html"
    context_object_name = "resightings"
    paginate_by = 20

    def get_queryset(self):
        qs = Resighting.objects.select_related(
            "species",
            "location",
            "location__place",
            "capture",
            "capture__location",
            "capture__location__place",
        ).prefetch_related("species__names")

        species_id = self.request.GET.get("species")
        if species_id:
            qs = qs.filter(species_id=species_id)

        location_id = self.request.GET.get("place")
        if location_id:
            qs = qs.filter(Q(location_id=location_id) | Q(capture__location_id=location_id))

        country_code = self.request.GET.get("country")
        if country_code:
            qs = qs.filter(
                Q(location__place__country__code=country_code)
                | Q(capture__location__place__country__code=country_code)
            )

        return qs.order_by("-date", "-created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for resighting in context["resightings"]:
            resighting.journey = describe_journey(resighting)

        context["project_name"] = "CRBirding"
        context["project_description"] = (
            "A website for managing observations of colour-ringed birds. "
            "Record and track individual birds identified by their unique colour ring combinations."
        )

        context["species_options"] = sorted(
            Species.objects.prefetch_related("names"), key=lambda s: s.get_common_name()
        )
        context["place_options"] = sorted(
            Location.objects.select_related("place"), key=lambda location: location.get_name()
        )
        used_countries = set(
            Resighting.objects.values_list(
                "location__place__country__code", "location__place__country__name"
            )
        ) | set(
            Resighting.objects.exclude(capture__isnull=True).values_list(
                "capture__location__place__country__code",
                "capture__location__place__country__name",
            )
        )
        used_countries.discard((None, None))
        context["country_options"] = sorted(used_countries, key=lambda pair: pair[1])

        context["selected_species"] = self.request.GET.get("species", "")
        context["selected_place"] = self.request.GET.get("place", "")
        context["selected_country"] = self.request.GET.get("country", "")

        params = self.request.GET.copy()
        params.pop("page", None)
        context["querystring"] = params.urlencode()

        return context


class SubmitResightingView(LoginRequiredMixin, View):
    """Let a logged-in birder record a resighting themselves, tags and
    all, without needing the admin.

    Structured entry (dropdowns for position/kind/colour) is primary,
    per apps.core.forms.TagForm -- the interchange notation is generated
    from this, not typed in directly. The tag rows beyond the first
    couple are added on demand via AddTagRowView, an HTMX endpoint, so
    the form starts uncluttered but isn't capped at a fixed number.
    """

    template_name = "core/resighting_form.html"

    def get(self, request):
        form = ResightingForm()
        formset = TagFormSet(instance=Resighting())
        return render(request, self.template_name, {"form": form, "formset": formset})

    def post(self, request):
        form = ResightingForm(request.POST, request.FILES)
        formset = TagFormSet(request.POST, request.FILES, instance=Resighting())

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                resighting = form.save(commit=False)
                resighting.observer = self._observer_for(request.user)
                resighting.submitted = timezone.now()
                resighting.save()

                formset.instance = resighting
                tags = formset.save(commit=False)
                assign_tag_order(tags)
                for tag in tags:
                    tag.save()
                for obj in formset.deleted_objects:
                    obj.delete()

            messages.success(request, "Thanks -- your resighting has been recorded.")
            return redirect("core:home")

        return render(request, self.template_name, {"form": form, "formset": formset})

    def _observer_for(self, user) -> Observer:
        if user.observer_id is None:
            user.observer = Observer.objects.create(name=user.get_full_name() or user.email)
            user.save(update_fields=["observer"])
        return user.observer


class SubmitCaptureView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Record a Capture (where and when a bird was ringed) with its
    tags, then link any already-recorded Resighting whose tags match --
    see apps.core.matching.

    Staff-only: unlike a Resighting, a Capture is authoritative ringing
    data tied to a Project, not something any signed-up birder should
    be able to assert on their own say-so.
    """

    template_name = "core/capture_form.html"

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        form = CaptureForm()
        formset = CaptureTagFormSet(instance=Capture())
        return render(request, self.template_name, {"form": form, "formset": formset})

    def post(self, request):
        form = CaptureForm(request.POST)
        formset = CaptureTagFormSet(request.POST, instance=Capture())

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                capture = form.save()

                formset.instance = capture
                tags = formset.save(commit=False)
                assign_tag_order(tags)
                for tag in tags:
                    tag.save()
                for obj in formset.deleted_objects:
                    obj.delete()

            linked = link_matching_resightings(capture)
            note = ""
            if linked:
                note = f" {linked} existing resighting(s) with matching tags were linked."
            messages.success(request, f"Capture recorded.{note}")
            return redirect("core:home")

        return render(request, self.template_name, {"form": form, "formset": formset})


class AddTagRowView(LoginRequiredMixin, View):
    """HTMX endpoint backing the "Add another tag" button: renders one
    more blank TagForm at the next index and, via an out-of-band swap,
    bumps the formset's TOTAL_FORMS count to match -- so the result is
    an ordinary Django formset submission, nothing HTMX-specific to
    unpick server-side.
    """

    def get(self, request):
        index = int(request.GET.get("index", 0))
        form = TagForm(prefix=f"tags-{index}")
        row_html = render_to_string("core/_tag_form_row.html", {"form": form}, request=request)
        total_forms_input = (
            f'<input type="hidden" name="tags-TOTAL_FORMS" id="id_tags-TOTAL_FORMS" '
            f'value="{index + 1}" hx-swap-oob="true">'
        )
        return HttpResponse(row_html + total_forms_input)


def handler403(request: HttpRequest, exception=None) -> HttpResponse:
    """Custom 403 Forbidden handler."""
    return render(request, "403.html", status=403)


def handler404(request: HttpRequest, exception=None) -> HttpResponse:
    """Custom 404 Not Found handler."""
    return render(request, "404.html", status=404)


def handler500(request: HttpRequest) -> HttpResponse:
    """Custom 500 Internal Server Error handler."""
    return render(request, "500.html", status=500)


# Development-only views for testing error pages and Sentry
if settings.DJANGO_ENV == "development":

    def test_403(request: HttpRequest) -> HttpResponse:
        """Test view for 403 page (development only)."""
        return render(request, "403.html", status=403)

    def test_404(request: HttpRequest) -> HttpResponse:
        """Test view for 404 page (development only)."""
        return render(request, "404.html", status=404)

    def test_500(request: HttpRequest) -> HttpResponse:
        """Test view for 500 page (development only)."""
        return render(request, "500.html", status=500)

    def test_sentry(request: HttpRequest) -> HttpResponse:
        """Test view to trigger a Sentry error (development only)."""
        raise ValueError("This is a test error to verify Sentry is configured correctly.")
