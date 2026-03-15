import pytest
from core.tests.factories import UserFactory
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestSettingsView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("accounts:settings"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_updating_details_shows_a_success_message(self, client: Client):
        user = UserFactory(first_name="Old", last_name="Name")
        client.force_login(user)

        response = client.post(
            reverse("accounts:settings"),
            {"first_name": "New", "last_name": "Name", "alphabet": ""},
            follow=True,
        )

        assert response.status_code == 200
        user.refresh_from_db()
        assert user.first_name == "New"
        messages = [str(m) for m in response.context["messages"]]
        assert "Your details were updated successfully." in messages

    def test_invalid_submission_shows_no_success_message(self, client: Client):
        user = UserFactory()
        client.force_login(user)

        response = client.post(
            reverse("accounts:settings"),
            {"first_name": "New", "last_name": "Name", "alphabet": "not-a-real-alphabet"},
        )

        assert response.status_code == 200
        messages = [str(m) for m in response.context["messages"]]
        assert messages == []
