import re

import pytest
from core.tests.factories import UserFactory
from django.core import mail
from django.test import Client
from django.urls import reverse


def _reset_url() -> str:
    body = mail.outbox[-1].body
    match = re.search(r"http://\S+/accounts/password/reset/\S+", body)
    assert match, body
    return match.group(0)


@pytest.mark.django_db
class TestPasswordChangeView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("password_change"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_change_requires_current_password(self, client: Client):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        response = client.post(
            reverse("password_change"),
            {
                "old_password": "wrong-password",
                "new_password1": "a-new-password-2",
                "new_password2": "a-new-password-2",
            },
        )

        assert response.status_code == 200
        assert "old_password" in response.context["form"].errors
        user.refresh_from_db()
        assert user.check_password("original-password-1")

    def test_successful_change_updates_password_and_sends_notification(self, client: Client):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        response = client.post(
            reverse("password_change"),
            {
                "old_password": "original-password-1",
                "new_password1": "a-new-password-2",
                "new_password2": "a-new-password-2",
            },
        )

        assert response.status_code == 302
        assert response.url == reverse("password_change_done")
        user.refresh_from_db()
        assert user.check_password("a-new-password-2")
        assert len(mail.outbox) == 1
        assert mail.outbox[0].to == [user.email]
        assert "password" in mail.outbox[0].subject.lower()

    def test_session_stays_valid_after_change(self, client: Client):
        """update_session_auth_hash (called by Django's own
        PasswordChangeView.form_valid, which we call via super()) keeps
        the current session logged in despite the password hash changing.
        """
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        client.post(
            reverse("password_change"),
            {
                "old_password": "original-password-1",
                "new_password1": "a-new-password-2",
                "new_password2": "a-new-password-2",
            },
        )

        response = client.get(reverse("accounts:settings"))
        assert response.status_code == 200


@pytest.mark.django_db
class TestPasswordResetFlow:
    def test_full_round_trip(self, client: Client):
        user = UserFactory(email="reset-me@example.com")
        user.set_password("original-password-1")
        user.save()

        response = client.post(reverse("password_reset"), {"email": "reset-me@example.com"})
        assert response.status_code == 302
        assert len(mail.outbox) == 1

        confirm_url = _reset_url()
        response = client.get(confirm_url, follow=True)
        assert response.status_code == 200

        # Django's PasswordResetConfirmView stashes the validated token in
        # the session and redirects to a URL with "set-password" in place
        # of the token -- follow that before posting the new password.
        set_password_url = response.redirect_chain[-1][0]
        response = client.post(
            set_password_url,
            {"new_password1": "brand-new-password-3", "new_password2": "brand-new-password-3"},
        )
        assert response.status_code == 302
        assert response.url == reverse("password_reset_complete")

        user.refresh_from_db()
        assert user.check_password("brand-new-password-3")

    def test_unknown_email_does_not_reveal_whether_an_account_exists(self, client: Client):
        response = client.post(reverse("password_reset"), {"email": "nobody@example.com"})

        assert response.status_code == 302
        assert response.url == reverse("password_reset_done")
        assert len(mail.outbox) == 0

    def test_rate_limited_after_repeated_attempts(self, client: Client):
        from users.views import PASSWORD_RESET_RATE_LIMIT

        for _ in range(PASSWORD_RESET_RATE_LIMIT):
            client.post(reverse("password_reset"), {"email": "nobody@example.com"})

        response = client.post(reverse("password_reset"), {"email": "nobody@example.com"})

        assert response.status_code == 302
        assert response.url == reverse("password_reset")
        assert len(mail.outbox) == 0
