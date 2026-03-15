from django.views.generic import ListView

from ..models import Observation, Species
from ..utils.formatting import describe_journey


class HomeView(ListView):
    """Home page: a paginated feed of recent observations whose origin
    has been identified, headlined by the 'ringed here, seen here' story
    -- the engaging part for visitors who aren't the observer, per the
    site's two goals of helping users manage their own records and
    inspiring others to go look for birds. An observation nobody's
    matched to a Origin yet has no such story to tell, so it's left
    off this feed entirely rather than shown half-complete.

    Filterable by species; more filters (place, country, ...) will
    follow the same pattern -- add the GET param handling here and the
    matching option list in get_context_data().
    """

    template_name = "core/home.html"
    context_object_name = "observations"
    paginate_by = 20

    def _identified_observations(self):
        """The base feed, before any of the user's own filter choices --
        every observation linked to a Origin. Shared between the
        queryset itself and the option lists in get_context_data(), so
        a filter never offers a choice that would empty the list.
        """
        return Observation.objects.filter(origin__isnull=False)

    def get_queryset(self):
        qs = self._identified_observations().select_related(
            "location",
            "origin",
            "origin__location",
        )

        species_code = self.request.GET.get("species")
        if species_code:
            qs = qs.filter(species=species_code)

        return qs.order_by("-date", "-created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for observation in context["observations"]:
            observation.journey = describe_journey(observation)

        context["project_name"] = "CRBirding"
        context["project_description"] = (
            "A website for managing observations of colour-ringed birds. "
            "Record and track individual birds identified by their unique colour ring combinations."
        )

        used_species_codes = set(self._identified_observations().values_list("species", flat=True))
        context["species_options"] = sorted(
            ((code, Species(code).label) for code in used_species_codes),
            key=lambda pair: pair[1],
        )

        context["selected_species"] = self.request.GET.get("species", "")

        params = self.request.GET.copy()
        params.pop("page", None)
        context["querystring"] = params.urlencode()

        return context
