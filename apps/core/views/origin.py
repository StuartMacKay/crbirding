from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import DetailView

from ..forms import LocationForm, OriginForm
from ..models import Observation, Origin
from ..utils.events import record_origin_linked
from ..utils.formatting import describe_journey, format_colour_marks, format_tags
from ..utils.matching import link_same_bird


class SubmitOriginView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Record an Origin -- where and when a bird was ringed.

    Usually reached from an Open observation's own page ("Add ringing
    details", with ?observation=<pk>): that observation is then linked
    to the new Origin, and so is every other Open sighting of the same
    species with exactly the same tags (see link_same_bird) -- the same
    bird seen again. Its species and colour marks are filled in as a
    starting point for the Origin's own species and label.

    Staff-only: unlike a Observation, a Origin is authoritative marking
    data tied to a Project, not something any signed-up birder should
    be able to assert on their own say-so.
    """

    template_name = "core/origin_form.html"

    def test_func(self):
        return self.request.user.is_staff

    def _redirect_target(self, request) -> str:
        """Where to send staff back to once the origin is saved --
        e.g. the My Observations page they followed an "Add ringing
        details" link from -- falling back to the home page if there's
        no ?next= (or it isn't a safe local URL to send them to).
        """
        next_url = request.POST.get("next") or request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
        ):
            return next_url
        return reverse("core:home")

    def _observation(self, request) -> Observation | None:
        """The Open observation these ringing details were added from."""
        pk = request.POST.get("observation") or request.GET.get("observation")
        if not pk:
            return None
        return get_object_or_404(Observation, pk=pk, origin__isnull=True)

    def _render(self, request, form, location_form, observation):
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "location_form": location_form,
                "observation": observation,
                "observation_tags": format_tags(observation.tags.all()) if observation else None,
                "next": request.POST.get("next") or request.GET.get("next", ""),
            },
        )

    def get(self, request):
        observation = self._observation(request)
        initial = {}
        if observation is not None:
            initial = {
                "species": observation.species,
                "label": format_colour_marks(observation.tags.all()) or "",
            }
        return self._render(request, OriginForm(initial=initial), LocationForm(), observation)

    def post(self, request):
        observation = self._observation(request)
        form = OriginForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)

        if not (form.is_valid() and location_form.is_valid()):
            return self._render(request, form, location_form, observation)

        with transaction.atomic():
            origin = form.save(commit=False)
            origin.location = location_form.resolve()
            overrides = location_form.observation_coordinate_overrides()
            origin.latitude = overrides.get("latitude")
            origin.longitude = overrides.get("longitude")
            origin.save()

            others = []
            if observation is not None:
                observation.origin = origin
                observation.save(update_fields=["origin"])
                record_origin_linked(observation)
                others = link_same_bird(observation)

        message = "Ringing details recorded."
        if others:
            message += (
                f" {len(others)} other sighting(s) with exactly the same tags were linked too."
            )
        messages.success(request, message)
        return redirect(self._redirect_target(request))


class LifeHistoryView(DetailView):
    """Every observation of one bird, across every observer who's ever
    reported it -- not just the current user's own (see
    core.utils.bulk_import for how a life history's other observers'
    rows end up correctly attributed to them, not the importer).

    Public, like the home page: an Observation's `owner` marks whose
    personal collection it belongs to, not who's allowed to see it --
    there's no privacy mechanism in this app that would make hiding it
    from a visitor meaningful (see core.views.home).
    """

    model = Origin
    template_name = "core/origin_history.html"
    context_object_name = "origin"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        origin = self.object

        observations = (
            origin.observations.select_related("location")
            .prefetch_related("tags", "observers")
            .order_by("date", "time", "created")
        )
        rows = []
        for observation in observations:
            rows.append(
                {
                    "observation": observation,
                    "journey": describe_journey(observation),
                    "colour_marks": format_colour_marks(observation.tags.all()),
                    "observer_names": ", ".join(
                        observer.name for observer in observation.observers.all()
                    ),
                    "is_mine": (
                        self.request.user.is_authenticated
                        and observation.owner_id == self.request.user.id
                    ),
                }
            )

        context["rows"] = rows
        return context
