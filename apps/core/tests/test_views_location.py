import pytest
from django.test import Client
from django.urls import reverse

from .factories import LocationFactory


@pytest.mark.django_db
class TestLocationDetailView:
    def test_returns_region_country_and_coordinates(self):
        location = LocationFactory(
            region="FR--",
            latitude="51.5000",
            longitude="-0.1000",
            accuracy=50,
            notes="Access via the north gate only.",
        )
        client = Client()

        response = client.get(reverse("core:location-detail", args=[location.pk]))

        assert response.status_code == 200
        data = response.json()
        assert data["region"] == "FR--"
        assert data["country"] == "FR--"
        assert data["region_label"] == "France"
        assert data["country_label"] == "France"
        assert data["latitude"] == "51.5000"
        assert data["longitude"] == "-0.1000"
        assert data["accuracy"] == 50
        assert data["notes"] == "Access via the north gate only."

    def test_404_for_unknown_location(self):
        client = Client()
        response = client.get(reverse("core:location-detail", args=[999999]))
        assert response.status_code == 404

    def test_no_login_required(self):
        location = LocationFactory()
        client = Client()
        response = client.get(reverse("core:location-detail", args=[location.pk]))
        assert response.status_code == 200
