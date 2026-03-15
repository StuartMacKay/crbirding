import pytest
from django.test import Client
from django.urls import reverse

from core.autocomplete import search_location

from .factories import LocationFactory


@pytest.mark.django_db
class TestSearchLocation:
    def test_matches_by_name(self):
        LocationFactory(name={"Latn": "Harbour Wall"})
        LocationFactory(name={"Latn": "Somewhere Else"})

        results = search_location("harbour")

        assert len(results) == 1
        assert "Harbour Wall" in results[0][1]

    def test_filters_by_region_when_given(self):
        LocationFactory(name={"Latn": "In France"}, region="FR--")
        LocationFactory(name={"Latn": "In Britain"}, region="GB--")

        results = search_location("", region="FR--")

        names = [label for _, label in results]
        assert any("In France" in name for name in names)
        assert not any("In Britain" in name for name in names)


@pytest.mark.django_db
class TestLocationAutocompleteEndpoint:
    def test_returns_matching_locations(self):
        location = LocationFactory(name={"Latn": "Endpoint Test Place"})
        client = Client()

        response = client.get(reverse("autocomplete:search", args=["location"]), {"q": "Endpoint"})

        assert response.status_code == 200
        results = response.json()["results"]
        assert any(r["value"] == str(location.pk) for r in results)
