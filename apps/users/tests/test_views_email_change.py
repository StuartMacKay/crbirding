import re

import pytest
from core.tests.factories import UserFactory
from django.core import mail
from django.test import Client
from django.urls import reverse


def _confirm_url() -> str:
    body = mail.outbox[-1].body
    match = re.search(r"http://\S+/accounts/email/change/confirm/\S+", body)
    assert match, body
    return match.group(0)


@pytest.mark.django_db
class TestChangeEmailView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("accounts:email_change"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_wrong_current_password_is_rejected(self, client: Client):
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        response = client.post(
            reverse("accounts:email_change"),
            {"new_email": "new@example.com", "current_password": "wrong-password"},
        )

        assert response.status_code == 200
        assert "current_password" in response.context["form"].errors
        assert len(mail.outbox) == 0

    def test_email_already_taken_is_rejected(self, client: Client):
        UserFactory(email="taken@example.com")
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        response = client.post(
            reverse("accounts:email_change"),
            {"new_email": "taken@example.com", "current_password": "original-password-1"},
        )

        assert response.status_code == 200
        assert "new_email" in response.context["form"].errors

    def test_valid_submission_does_not_change_email_until_confirmed(self, client: Client):
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)

        response = client.post(
            reverse("accounts:email_change"),
            {"new_email": "new@example.com", "current_password": "original-password-1"},
        )

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        user.refresh_from_db()
        assert user.email == "old@example.com"
        assert len(mail.outbox) == 1
        assert mail.outbox[0].to == ["new@example.com"]

    def test_confirming_updates_the_email_and_notifies_both_addresses(self, client: Client):
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)
        client.post(
            reverse("accounts:email_change"),
            {"new_email": "new@example.com", "current_password": "original-password-1"},
        )
        url = _confirm_url()

        response = client.get(url)

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        user.refresh_from_db()
        assert user.email == "new@example.com"
        assert len(mail.outbox) == 3  # confirmation link + old-address + new-address notices
        recipients = {tuple(msg.to) for msg in mail.outbox[1:]}
        assert recipients == {("old@example.com",), ("new@example.com",)}

    def test_email_taken_by_someone_else_since_requesting_is_rejected_at_confirmation(
        self, client: Client
    ):
        """A race: someone else claims the new address between the
        confirmation link being sent and it being clicked.
        """
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)
        client.post(
            reverse("accounts:email_change"),
            {"new_email": "new@example.com", "current_password": "original-password-1"},
        )
        url = _confirm_url()
        UserFactory(email="new@example.com")

        response = client.get(url)

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        user.refresh_from_db()
        assert user.email == "old@example.com"

    def test_confirmation_link_only_works_for_the_requesting_user(self, client: Client):
        user = UserFactory(email="old@example.com")
        user.set_password("original-password-1")
        user.save()
        client.force_login(user)
        client.post(
            reverse("accounts:email_change"),
            {"new_email": "new@example.com", "current_password": "original-password-1"},
        )
        url = _confirm_url()
        client.logout()

        other_user = UserFactory(email="someone-else@example.com")
        client.force_login(other_user)
        response = client.get(url)

        assert response.status_code == 302
        user.refresh_from_db()
        assert user.email == "old@example.com"

    def test_invalid_token_is_rejected(self, client: Client):
        user = UserFactory(email="old@example.com")
        client.force_login(user)

        response = client.get(reverse("accounts:email_change_confirm", args=["not-a-real-token"]))

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        user.refresh_from_db()
        assert user.email == "old@example.com"
