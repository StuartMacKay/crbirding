import pytest
from django.test import Client
from django.urls import reverse

from autocomplete.registry import register


@pytest.fixture(autouse=True)
def _sample_field():
    def search(query, **parents):
        data = [("fr", "France"), ("gb", "United Kingdom"), ("de", "Germany")]
        return [(v, label) for v, label in data if query.lower() in label.lower()]

    register("sample", search)
    yield


@pytest.mark.django_db
class TestAutocompleteView:
    def test_returns_matching_results(self, client: Client):
        response = client.get(reverse("autocomplete:search", args=["sample"]), {"q": "fra"})
        assert response.json() == {"results": [{"value": "fr", "label": "France"}]}

    def test_empty_query_returns_everything(self, client: Client):
        response = client.get(reverse("autocomplete:search", args=["sample"]), {"q": ""})
        assert len(response.json()["results"]) == 3

    def test_unknown_field_is_a_404(self, client: Client):
        response = client.get(reverse("autocomplete:search", args=["nonexistent"]))
        assert response.status_code == 404

    def test_parent_values_are_passed_through_as_kwargs(self, client: Client):
        seen = {}

        def search(query, **parents):
            seen.update(parents)
            return []

        register("with-parent", search)

        client.get(reverse("autocomplete:search", args=["with-parent"]), {"q": "x", "country": "fr"})

        assert seen == {"country": "fr"}
