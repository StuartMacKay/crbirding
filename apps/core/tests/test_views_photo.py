import pytest
from django.test import Client
from django.urls import reverse

from .factories import UserFactory


@pytest.mark.django_db
class TestAddPhotoRowView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("core:add-photo-row"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_returns_a_form_row_at_the_given_index(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:add-photo-row"), {"index": 3})
        assert response.status_code == 200
        content = response.content.decode()
        assert "photos-3-" in content

    def test_bumps_total_forms_out_of_band(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:add-photo-row"), {"index": 3})
        content = response.content.decode()
        assert 'id="id_photos-TOTAL_FORMS"' in content
        assert 'value="4"' in content
        assert "hx-swap-oob" in content

    def test_defaults_to_index_zero(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:add-photo-row"))
        assert "photos-0-" in response.content.decode()
