import pytest
from core.tests.factories import UserFactory
from django.test import Client
from django.urls import reverse

from users.views import LOGIN_RATE_LIMIT


@pytest.mark.django_db
class TestLoginView:
    def test_valid_login_still_works(self, client: Client):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()

        response = client.post(
            reverse("account_login"),
            {"username": user.email, "password": "original-password-1"},
        )

        assert response.status_code == 302

    def test_rate_limited_after_repeated_attempts(self, client: Client):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()

        for _ in range(LOGIN_RATE_LIMIT):
            client.post(reverse("account_login"), {"username": user.email, "password": "wrong"})

        response = client.post(
            reverse("account_login"),
            {"username": user.email, "password": "original-password-1"},
        )

        assert response.status_code == 302
        assert response.url == reverse("account_login")
        # Blocked before authentication even ran -- not logged in.
        assert "_auth_user_id" not in client.session
