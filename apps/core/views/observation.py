from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.text import smart_split, unescape_string_literal
from django.views import View
from django.views.generic import ListView

from ..forms import (
    EventFormSet,
    LocationForm,
    ObservationForm,
    ObservationImportForm,
    PhotoFormSet,
    TagFormSet,
)
from ..models import PLACE_TO_COUNTRY, Country, Location, Observation, Observer, Origin, Species
from ..utils.bulk_import import import_observations_csv
from ..utils.events import record_origin_linked
from ..utils.formatting import (
    describe_journey,
    describe_recovery,
    describe_sighting,
    format_colour_marks,
    format_recovery_report,
)
from ..utils.matching import (
    find_candidate_projects,
    find_claimable_observer,
    link_to_known_bird,
    possible_sightings,
)


class SubmitObservationView(LoginRequiredMixin, View):
    """Let a logged-in birder record a observation themselves, tags and
    all, without needing the admin.

    Tags are typed in as colour-mark codes, one row per Position (see
    core.forms.TagForm); rows beyond the first are added on demand via
    AddTagRowView, an HTMX endpoint. If they exactly match an already
    identified sighting of the same species, the new one is linked to
    that bird straight away (see link_to_known_bird).

    A new Observation is private to the submitting user (see
    core.models.Observation.owner) -- publishing it anywhere is a
    separate, later choice, not implied by recording it here.
    """

    template_name = "core/observation_form.html"

    def get(self, request):
        form = ObservationForm()
        location_form = LocationForm()
        formset = TagFormSet(instance=Observation())
        photo_formset = PhotoFormSet(instance=Observation())
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "location_form": location_form,
                "formset": formset,
                "photo_formset": photo_formset,
            },
        )

    def post(self, request):
        form = ObservationForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)
        formset = TagFormSet(request.POST, instance=Observation())
        photo_formset = PhotoFormSet(request.POST, request.FILES, instance=Observation())

        if (
            form.is_valid()
            and location_form.is_valid()
            and formset.is_valid()
            and photo_formset.is_valid()
        ):
            with transaction.atomic():
                observation = form.save(commit=False)
                observation.location = location_form.resolve()
                overrides = location_form.observation_coordinate_overrides()
                observation.latitude = overrides.get("latitude")
                observation.longitude = overrides.get("longitude")
                observation.accuracy = overrides.get("accuracy")
                observation.owner = request.user
                observation.save()
                observation.observers.add(self._observer_for(request.user))

                formset.instance = observation
                formset.save()

                photo_formset.instance = observation
                photo_formset.save()

                link_to_known_bird(observation)

            messages.success(request, "Thanks -- your observation has been recorded.")
            return redirect("core:observation-send", pk=observation.pk)

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "location_form": location_form,
                "formset": formset,
                "photo_formset": photo_formset,
            },
        )

    def _observer_for(self, user) -> Observer:
        """The Observer this user's sightings are credited to -- created
        on first use, the fallback for a user who skips
        accounts.ObserverSetupView and submits an observation directly.
        Observer.user is a one-to-one field, so there's always exactly
        one Observer identity for a given account, but that identity
        might already exist unlinked (e.g. imported from a historical
        life history) -- claim a matching one rather than blindly
        creating a duplicate (see find_claimable_observer).
        """
        observer = Observer.objects.filter(user=user).first()
        if observer is not None:
            return observer

        name = user.get_full_name() or user.email
        observer = find_claimable_observer(name)
        if observer is not None:
            observer.user = user
            observer.save(update_fields=["user"])
            return observer

        return Observer.objects.create(name=name, user=user)


class EditObservationView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Edit an existing Observation's own fields, tags, and photos --
    reachable from the observation's own page, the counterpart to
    SubmitObservationView's create. Restricted the same way
    SendToProjectView is: the owner, or staff.

    Doesn't touch `observers` -- that's who registered the sighting in
    the first place, fixed at creation time, not something an edit
    should be able to change.
    """

    template_name = "core/observation_form.html"

    def test_func(self):
        observation = self._get_observation()
        return observation.owner_id == self.request.user.id or self.request.user.is_staff

    def _get_observation(self) -> Observation:
        return get_object_or_404(Observation, pk=self.kwargs["pk"])

    def get(self, request, pk):
        observation = self._get_observation()
        form = ObservationForm(instance=observation)
        location_form = LocationForm(
            initial={
                "search": str(observation.location_id),
                "country": observation.location.get_country_code(),
                "region": observation.location.region,
                # This observation's own override, if it has one -- not
                # prefilling it would silently drop it on the next save,
                # since the field would just look untouched/blank.
                "latitude": observation.latitude,
                "longitude": observation.longitude,
                "accuracy": observation.accuracy,
            }
        )
        formset = TagFormSet(instance=observation)
        photo_formset = PhotoFormSet(instance=observation)
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "location_form": location_form,
                "formset": formset,
                "photo_formset": photo_formset,
                "editing": True,
            },
        )

    def post(self, request, pk):
        observation = self._get_observation()
        form = ObservationForm(request.POST, request.FILES, instance=observation)
        location_form = LocationForm(request.POST)
        formset = TagFormSet(request.POST, instance=observation)
        photo_formset = PhotoFormSet(request.POST, request.FILES, instance=observation)

        if (
            form.is_valid()
            and location_form.is_valid()
            and formset.is_valid()
            and photo_formset.is_valid()
        ):
            with transaction.atomic():
                form.instance.location = location_form.resolve()
                overrides = location_form.observation_coordinate_overrides()
                form.instance.latitude = overrides.get("latitude")
                form.instance.longitude = overrides.get("longitude")
                form.instance.accuracy = overrides.get("accuracy")
                form.save()

                formset.save()
                photo_formset.save()
                link_to_known_bird(observation)

            messages.success(request, "Observation updated.")
            return redirect("core:observation-detail", pk=observation.pk)

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "location_form": location_form,
                "formset": formset,
                "photo_formset": photo_formset,
                "editing": True,
            },
        )


class MyObservationsView(LoginRequiredMixin, ListView):
    """A signed-in birder's own observations, for managing them without
    needing admin access -- the "very similar to the Django admin"
    equivalent of the change list, scoped to what this user owns.

    Unlike the public home page (which only shows observations whose
    Origin has been identified, since that's the story worth telling
    a visitor), this shows every observation the user owns regardless
    -- identifying the origin is exactly the thing they'd come here to
    finish doing, via "Add ringing details" on a row that doesn't have
    one yet.

    Filterable by status (Open: no Origin linked yet; Closed: linked),
    species, place, or country -- the latter the same "either side
    of the observation" matching as the old home page filters (see
    core.views.home) had, before they moved here. Also searchable by
    tag code, matching ObservationAdmin's search_fields (see
    _search_by_tag_code()).
    """

    template_name = "core/my_observations.html"
    context_object_name = "observations"
    paginate_by = 20

    def _owned_observations(self):
        """This user's observations, before any of their own filter
        choices -- shared between the queryset and the option lists in
        get_context_data(), so a filter never offers a choice that
        would empty the list.
        """
        return Observation.objects.filter(owner=self.request.user)

    def get_queryset(self):
        qs = (
            self._owned_observations()
            .select_related(
                "location",
                "origin",
                "origin__location",
            )
            .prefetch_related("tags")
        )

        species_code = self.request.GET.get("species")
        if species_code:
            qs = qs.filter(species=species_code)

        location_id = self.request.GET.get("place")
        if location_id:
            qs = qs.filter(Q(location_id=location_id) | Q(origin__location_id=location_id))

        country_code = self.request.GET.get("country")
        if country_code:
            regions_in_country = [
                code for code, cc in PLACE_TO_COUNTRY.items() if cc == country_code
            ]
            qs = qs.filter(
                Q(location__region__in=regions_in_country)
                | Q(origin__location__region__in=regions_in_country)
            )

        status = self.request.GET.get("status")
        if status == "open":
            qs = qs.filter(origin__isnull=True)
        elif status == "closed":
            qs = qs.filter(origin__isnull=False)

        search = self.request.GET.get("q", "").strip()
        if search:
            qs = self._search_by_tag_code(qs, search)

        return qs.order_by("-date", "-created")

    @staticmethod
    def _search_by_tag_code(qs, search):
        """The same matching as ObservationAdmin's search_fields =
        ("tags__code",): every whitespace-separated term (or quoted
        phrase) must appear, case-insensitively, in the code of one of
        the observation's tags -- not necessarily the same tag.
        """
        for term in smart_split(search):
            if term.startswith(('"', "'")) and term[0] == term[-1]:
                term = unescape_string_literal(term)
            qs = qs.filter(tags__code__icontains=term)
        return qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for observation in context["observations"]:
            observation.journey = describe_journey(observation)
            observation.colour_marks = format_colour_marks(observation.tags.all())

        owned = self._owned_observations()

        used_species_codes = set(owned.values_list("species", flat=True))
        context["species_options"] = sorted(
            ((code, Species(code).label) for code in used_species_codes),
            key=lambda pair: pair[1],
        )

        context["place_options"] = sorted(
            Location.objects.filter(
                Q(pk__in=owned.values_list("location_id", flat=True))
                | Q(pk__in=owned.values_list("origin__location_id", flat=True))
            ).distinct(),
            key=lambda location: location.get_name(),
        )

        used_region_codes = set(owned.values_list("location__region", flat=True)) | set(
            owned.exclude(origin__isnull=True).values_list("origin__location__region", flat=True)
        )
        used_country_codes = {PLACE_TO_COUNTRY[code] for code in used_region_codes if code}
        context["country_options"] = sorted(
            ((code, Country(code).label) for code in used_country_codes),
            key=lambda pair: pair[1],
        )

        context["selected_species"] = self.request.GET.get("species", "")
        context["selected_place"] = self.request.GET.get("place", "")
        context["selected_country"] = self.request.GET.get("country", "")
        context["search"] = self.request.GET.get("q", "")
        context["selected_status"] = self.request.GET.get("status", "")

        params = self.request.GET.copy()
        params.pop("page", None)
        context["querystring"] = params.urlencode()

        # Remembered -- filters, search, and page -- so an observation's
        # own page can link back to this same view of the list, however
        # many edits/events round trips happen in between (see
        # my_observations_url()).
        self.request.session[MY_OBSERVATIONS_QUERY_KEY] = self.request.GET.urlencode()

        return context


MY_OBSERVATIONS_QUERY_KEY = "my_observations_query"


def my_observations_url(request) -> str:
    """My Observations as the user last left it -- same filters, search,
    and page -- as remembered by MyObservationsView.
    """
    url = reverse("core:my-observations")
    query = request.session.get(MY_OBSERVATIONS_QUERY_KEY, "")
    return f"{url}?{query}" if query else url


class ObservationDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    """One observation's own page, reached from My Observations' "View"
    link -- everything needed to follow it up in one place:

    1. The observation laid out for an email (core/_observation_email.html),
       ready to copy, with a link to edit the observation.
    2. Its events -- sent, submitted, ringing details added, etc. -- see
       core.models.Event and ObservationEventsView.
    3. Who marked the bird: the recovery (core/_recovery.html), its
       life history, and -- for staff -- other Open sightings that may be
       the same bird, to review and link (LinkObservationView), if
       there's a linked Origin; otherwise the projects whose Rules match
       its colour marks (see find_candidate_projects()).

    Restricted the same way SendToProjectView is: the owner, or staff.
    """

    template_name = "core/observation_detail.html"

    def test_func(self):
        observation = self._get_observation()
        return observation.owner_id == self.request.user.id or self.request.user.is_staff

    def _get_observation(self) -> Observation:
        return get_object_or_404(Observation, pk=self.kwargs["pk"])

    def get(self, request, pk):
        observation = self._get_observation()
        report = format_recovery_report(observation)
        origin = observation.origin

        context = {
            "observation": observation,
            "sighting": describe_sighting(observation),
            "recovery": describe_recovery(observation),
            # Still plain text for the mailto: links' body, which can't
            # carry the HTML snippet above.
            "report_text": "\n".join(report.lines),
            "subject": (
                f"{observation.get_species_display()}, "
                f"{observation.location.get_region_display()}, "
                f"{observation.location.get_country_display()}"
            ),
            "events": observation.events.all(),
            "origin": origin,
            "matches": [] if origin else find_candidate_projects(observation),
            "possible_sightings": (
                possible_sightings(origin) if origin and request.user.is_staff else []
            ),
            "back_url": my_observations_url(request),
        }
        return render(request, self.template_name, context)


class LinkObservationView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Link an Open observation to an Origin after a person has reviewed
    it -- one offered up as a possible sighting of that bird because its
    tags match once "?" is ignored (see
    core.utils.matching.possible_sightings). Staff-only, like adding
    ringing details in the first place.
    """

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, pk):
        observation = get_object_or_404(Observation, pk=pk, origin__isnull=True)
        origin = get_object_or_404(Origin, pk=request.POST.get("origin"))
        if observation.species != origin.species:
            messages.error(request, "That sighting is of a different species.")
        else:
            observation.origin = origin
            observation.save(update_fields=["origin"])
            record_origin_linked(observation, "Linked after review")
            messages.success(request, f"Sighting of {observation.date:%d-%b-%Y} linked.")

        next_url = request.POST.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
        ):
            return redirect(next_url)
        return redirect("core:observation-detail", pk=observation.pk)


class ObservationEventsView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Add, edit, or delete an observation's events -- reached from the
    events panel on ObservationDetailView, and back there on save.
    Restricted the same way: the owner, or staff.
    """

    template_name = "core/observation_events.html"

    def test_func(self):
        observation = self._get_observation()
        return observation.owner_id == self.request.user.id or self.request.user.is_staff

    def _get_observation(self) -> Observation:
        return get_object_or_404(Observation, pk=self.kwargs["pk"])

    def get(self, request, pk):
        observation = self._get_observation()
        formset = EventFormSet(instance=observation)
        return render(request, self.template_name, {"observation": observation, "formset": formset})

    def post(self, request, pk):
        observation = self._get_observation()
        formset = EventFormSet(request.POST, instance=observation)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Events updated.")
            return redirect("core:observation-detail", pk=observation.pk)
        return render(request, self.template_name, {"observation": observation, "formset": formset})


class ImportObservationsView(LoginRequiredMixin, View):
    """Bulk-import observations from a CSV file -- the public,
    non-admin equivalent of ObservationAdmin's own CSV import, sharing
    the same core.utils.bulk_import.import_observations_csv(). Reachable
    from My Observations, which is also where it sends the user back to.

    Not staff-only: recording an Observation one at a time already
    isn't (see SubmitObservationView) -- this is just a faster way to
    do the same thing for many rows at once. A row's owner is derived
    from its own observer, not whoever ran the import (see
    bulk_import's docstring), so importing a life history that spans
    several observers attributes each row correctly rather than to
    whoever happened to run the import.
    """

    template_name = "core/observation_import.html"

    def get(self, request):
        return render(request, self.template_name, {"form": ObservationImportForm()})

    def post(self, request):
        form = ObservationImportForm(request.POST, request.FILES)
        if form.is_valid():
            report = import_observations_csv(form.cleaned_data["csv_file"])
            if report.created:
                messages.success(request, f"Imported {report.created} observation(s).")
            if report.duplicates:
                messages.info(
                    request, f"Skipped {report.duplicates} row(s) already imported previously."
                )
                for detail in report.duplicate_details:
                    messages.info(request, detail)
            if report.skipped:
                messages.warning(request, f"Skipped {report.skipped} row(s); see below.")
            for error in report.errors[:50]:
                messages.error(request, error)
            if not report.errors:
                return redirect("core:my-observations")

        return render(request, self.template_name, {"form": form})


class SendToProjectView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Where a logged-in birder sends a Observation on to whoever needs
    to see it -- the marking project's coordinator, if one can be
    identified. Recording that it's been sent is an Event, added on the
    observation's events page (see ObservationEventsView).

    Doesn't send anything itself: a mailto: link (or the project's own
    submission page), and the report text to go with it, are handed to
    the browser -- the actual email is composed and sent by the user's
    own mail client, nothing this app needs to see or store.
    """

    template_name = "core/observation_send.html"

    def test_func(self):
        observation = self._get_observation()
        return observation.owner_id == self.request.user.id or self.request.user.is_staff

    def _get_observation(self) -> Observation:
        return get_object_or_404(Observation, pk=self.kwargs["pk"])

    def get(self, request, pk):
        observation = self._get_observation()
        report = format_recovery_report(observation)

        project = observation.origin.project if observation.origin else None
        if project is not None:
            matches = [(project, True)]
        else:
            matches = [(candidate, False) for candidate in find_candidate_projects(observation)]

        context = {
            "observation": observation,
            "report_text": "\n".join(report.lines),
            "origin": (
                f"Colour-ring observation: {observation.get_species_display()} {observation.date}"
            ),
            "matches": matches,
        }
        return render(request, self.template_name, context)
