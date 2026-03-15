import pytest
from core.tests.factories import UserFactory

from users.forms import ChangeEmailForm, SignupForm


@pytest.mark.django_db
class TestSignupForm:
    def test_website_honeypot_field_is_optional(self):
        form = SignupForm(
            {
                "email": "new@example.com",
                "first_name": "",
                "last_name": "",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            }
        )
        assert form.is_valid(), form.errors

    def test_name_fields_are_optional(self):
        form = SignupForm(
            {
                "email": "new@example.com",
                "first_name": "",
                "last_name": "",
                "alphabet": "",
                "website": "",
                "password1": "a-strong-password-1",
                "password2": "a-strong-password-1",
            }
        )
        assert form.is_valid(), form.errors


@pytest.mark.django_db
class TestChangeEmailForm:
    def test_requires_correct_current_password(self):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()

        form = ChangeEmailForm(user, {"new_email": "new@example.com", "current_password": "wrong"})

        assert form.is_valid() is False
        assert "current_password" in form.errors

    def test_rejects_email_already_used_by_someone_else(self):
        UserFactory(email="taken@example.com")
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()

        form = ChangeEmailForm(
            user,
            {"new_email": "taken@example.com", "current_password": "original-password-1"},
        )

        assert form.is_valid() is False
        assert "new_email" in form.errors

    def test_valid_with_correct_password_and_free_email(self):
        user = UserFactory()
        user.set_password("original-password-1")
        user.save()

        form = ChangeEmailForm(
            user,
            {"new_email": "new@example.com", "current_password": "original-password-1"},
        )

        assert form.is_valid(), form.errors
