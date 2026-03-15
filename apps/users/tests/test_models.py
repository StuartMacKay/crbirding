import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user("Jo@EXAMPLE.com", "s3cret-pass")

        assert user.email == "Jo@example.com"  # the domain is normalised
        assert user.check_password("s3cret-pass")
        assert not user.is_staff
        assert not user.is_superuser
        assert str(user) == "Jo@example.com"

    def test_create_user_without_a_password_is_unusable(self):
        user = User.objects.create_user("jo@example.com")
        assert not user.has_usable_password()

    def test_create_user_requires_an_email(self):
        with pytest.raises(ValueError, match="email address must be provided"):
            User.objects.create_user("", "s3cret-pass")

    def test_create_superuser(self):
        user = User.objects.create_superuser("admin@example.com", "s3cret-pass")

        assert user.is_staff
        assert user.is_superuser
        assert user.check_password("s3cret-pass")

    @pytest.mark.parametrize("flag", ["is_staff", "is_superuser"])
    def test_create_superuser_refuses_to_turn_a_flag_off(self, flag):
        with pytest.raises(ValueError, match=f"Superuser must have {flag}=True"):
            User.objects.create_superuser("admin@example.com", "s3cret-pass", **{flag: False})
        assert not User.objects.exists()

    def test_createsuperuser_command_uses_email(self, monkeypatch):
        """manage.py createsuperuser -- the path that actually depends on
        the manager, since there's no username field to fall back on.
        """
        monkeypatch.setenv("DJANGO_SUPERUSER_PASSWORD", "s3cret-pass")
        call_command("createsuperuser", "--noinput", "--email", "admin@example.com")

        user = User.objects.get()
        assert user.email == "admin@example.com"
        assert user.is_superuser
        assert user.check_password("s3cret-pass")
