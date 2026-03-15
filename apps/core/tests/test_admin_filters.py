import pytest
from django.test import Client
from django.urls import reverse

from .factories import LocationFactory, ProjectFactory, SuperUserFactory


@pytest.fixture
def admin_client(db) -> Client:
    client = Client()
    client.force_login(SuperUserFactory())
    return client


@pytest.mark.django_db
class TestLocationCountryFilter:
    def test_only_lists_countries_actually_used(self, admin_client):
        LocationFactory(region="FR--")
        LocationFactory(region="GB--")

        response = admin_client.get(reverse("admin:core_location_changelist"))

        content = response.content.decode()
        assert "France" in content
        assert "United Kingdom" in content
        # Germany is a real Country choice, but no Location uses it.
        assert "Germany" not in content

    def test_filtering_by_country_narrows_the_list(self, admin_client):
        france = LocationFactory(region="FR--", name={"Latn": "Paris"})
        LocationFactory(region="GB--", name={"Latn": "London"})

        response = admin_client.get(
            reverse("admin:core_location_changelist"), {"country": "FR--"}
        )

        results = list(response.context["cl"].result_list)
        assert results == [france]


@pytest.mark.django_db
class TestProjectCountryFilter:
    def test_only_lists_countries_actually_used(self, admin_client):
        ProjectFactory(country="FR--")

        response = admin_client.get(reverse("admin:core_project_changelist"))

        content = response.content.decode()
        assert "France" in content
        assert "Germany" not in content
