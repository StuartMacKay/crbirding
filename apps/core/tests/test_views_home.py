import pytest
from django.test import Client
from django.urls import reverse

from core.models import Species

from .factories import ObservationFactory, OriginFactory, TagFactory


@pytest.mark.django_db
class TestHomeView:
    def test_returns_200(self, client: Client):
        assert client.get(reverse("core:home")).status_code == 200

    def test_uses_correct_template(self, client: Client):
        response = client.get(reverse("core:home"))
        assert "core/home.html" in [t.name for t in response.templates]

    def test_lists_recent_identified_observations(self, client: Client):
        observation = ObservationFactory(origin=OriginFactory())
        TagFactory(observation=observation)
        response = client.get(reverse("core:home"))
        assert observation in response.context["observations"]

    def test_excludes_observations_without_an_identified_origin(self, client: Client):
        unidentified = ObservationFactory(origin=None)
        TagFactory(observation=unidentified)
        response = client.get(reverse("core:home"))
        assert unidentified not in response.context["observations"]

    def test_filters_by_species(self, client: Client):
        wanted = ObservationFactory(species=Species.COMMON_OSTRICH, origin=OriginFactory())
        other = ObservationFactory(species=Species.RED_THROATED_LOON, origin=OriginFactory())
        TagFactory(observation=wanted)
        TagFactory(observation=other)

        response = client.get(reverse("core:home"), {"species": wanted.species})

        results = list(response.context["observations"])
        assert wanted in results
        assert other not in results

    def test_species_options_only_include_identified_observations(self, client: Client):
        identified = ObservationFactory(species=Species.COMMON_OSTRICH, origin=OriginFactory())
        unidentified = ObservationFactory(species=Species.RED_THROATED_LOON, origin=None)
        for observation in (identified, unidentified):
            TagFactory(observation=observation)

        response = client.get(reverse("core:home"))

        codes = [code for code, _ in response.context["species_options"]]
        assert Species.COMMON_OSTRICH in codes
        assert Species.RED_THROATED_LOON not in codes

    def test_context_has_project_metadata(self, client: Client):
        response = client.get(reverse("core:home"))
        assert response.context["project_name"] == "CRBirding"
        assert response.context["project_description"]
