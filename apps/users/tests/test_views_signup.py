import re

import pytest
from core.tests.factories import UserFactory
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import Client
from django.urls import reverse

User = get_user_model()


def _verification_url() -> str:
    body = mail.outbox[-1].body
    match = re.search(r"http://\S+/accounts/verify/\S+", body)
    assert match, body
    return match.group(0)


def _signup_data(**overrides) -> dict:
    data = {
        "email": "new@example.com",
        "first_name": "New",
        "last_name": "Person",
        "alphabet": "",
        "website": "",
        "password1": "a-strong-password-1",
        "password2": "a-strong-password-1",
    }
    data.update(overrides)
    return data


@pytest.mark.django_db
class TestSignupView:
    def test_no_user_is_created_until_verified(self, client: Client):
        response = client.post(
            reverse("account_signup"),
            {
                "email": "new@example.com",
                "first_name": "New",
                "last_name": "Person",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            },
        )

        assert response.status_code == 302
        assert response.url == reverse("accounts:signup_sent")
        assert User.objects.filter(email="new@example.com").exists() is False
        assert len(mail.outbox) == 1
        assert mail.outbox[0].to == ["new@example.com"]

    def test_honeypot_trips_silently(self, client: Client):
        response = client.post(
            reverse("account_signup"),
            {
                "email": "bot@example.com",
                "first_name": "",
                "last_name": "",
                "alphabet": "",
                "website": "http://spam.example.com",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            },
        )

        assert response.status_code == 302
        assert response.url == reverse("accounts:signup_sent")
        assert User.objects.filter(email="bot@example.com").exists() is False
        assert len(mail.outbox) == 0

    def test_valid_link_creates_and_logs_in_and_redirects_to_observer_setup(self, client: Client):
        client.post(
            reverse("account_signup"),
            {
                "email": "new@example.com",
                "first_name": "New",
                "last_name": "Person",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            },
        )
        url = _verification_url()

        response = client.get(url)

        assert response.status_code == 302
        assert response.url == reverse("accounts:observer_setup")
        user = User.objects.get(email="new@example.com")
        assert user.is_active is True
        assert user.check_password("a-strong-password-1")
        # Logged in as the new user.
        assert int(client.session["_auth_user_id"]) == user.pk

    def test_invalid_token_shows_the_invalid_page(self, client: Client):
        response = client.get(reverse("accounts:verify_email", args=["not-a-real-token"]))

        assert response.status_code == 400
        assert "expired" in response.content.decode().lower()
        assert User.objects.count() == 0

    def test_verifying_twice_shows_a_friendly_message_instead_of_crashing(self, client: Client):
        client.post(
            reverse("account_signup"),
            {
                "email": "new@example.com",
                "first_name": "",
                "last_name": "",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            },
        )
        url = _verification_url()
        client.get(url)
        client.logout()

        response = client.get(url)

        assert response.status_code == 302
        assert response.url == reverse("account_login")
        assert User.objects.filter(email="new@example.com").count() == 1

    def test_rejects_an_email_already_in_use(self, client: Client):
        UserFactory(email="taken@example.com")

        response = client.post(
            reverse("account_signup"),
            {
                "email": "taken@example.com",
                "first_name": "",
                "last_name": "",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            },
        )

        assert response.status_code == 200
        assert "email" in response.context["form"].errors
        assert len(mail.outbox) == 0

    def test_rate_limited_after_repeated_attempts(self, client: Client):
        from users.views import SIGNUP_RATE_LIMIT

        for n in range(SIGNUP_RATE_LIMIT):
            client.post(reverse("account_signup"), _signup_data(email=f"user{n}@example.com"))

        response = client.post(
            reverse("account_signup"), _signup_data(email="one-too-many@example.com")
        )

        assert response.status_code == 302
        assert response.url == reverse("account_signup")
        assert User.objects.filter(email="one-too-many@example.com").exists() is False
        assert len(mail.outbox) == SIGNUP_RATE_LIMIT


@pytest.mark.django_db
class TestResendVerificationView:
    def test_resends_a_working_link_for_the_pending_signup(self, client: Client):
        client.post(reverse("account_signup"), _signup_data())

        response = client.post(reverse("accounts:resend_verification"))

        assert response.status_code == 302
        assert response.url == reverse("accounts:signup_sent")
        assert len(mail.outbox) == 2

        # The resent link works and creates the account.
        response = client.get(_verification_url())
        assert response.status_code == 302
        assert User.objects.filter(email="new@example.com").exists()

    def test_no_pending_signup_redirects_to_signup(self, client: Client):
        response = client.post(reverse("accounts:resend_verification"))

        assert response.status_code == 302
        assert response.url == reverse("account_signup")
        assert len(mail.outbox) == 0

    def test_already_verified_redirects_to_login(self, client: Client):
        """logout() isn't called here -- it flushes the whole session,
        which would also wipe the pending-signup token this view reads,
        defeating the point of the test.
        """
        client.post(reverse("account_signup"), _signup_data())
        client.get(_verification_url())  # verifies and logs in

        response = client.post(reverse("accounts:resend_verification"))

        assert response.status_code == 302
        assert response.url == reverse("account_login")

    def test_rate_limited_after_repeated_attempts(self, client: Client):
        from users.views import RESEND_VERIFICATION_RATE_LIMIT

        client.post(reverse("account_signup"), _signup_data())
        for _ in range(RESEND_VERIFICATION_RATE_LIMIT):
            client.post(reverse("accounts:resend_verification"))

        mail.outbox.clear()
        response = client.post(reverse("accounts:resend_verification"))

        assert response.status_code == 302
        assert len(mail.outbox) == 0
