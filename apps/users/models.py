from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import Script


class UserManager(BaseUserManager):
    """Custom manager that uses email instead of username."""

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("An email address must be provided."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model that uses email address as the unique identifier
    instead of a username.
    """

    username = None

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
        help_text=_("The date and time when this account was created."),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at"),
        help_text=_("The date and time when this account was last updated."),
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("email address"),
        help_text=_("The email address used to log in."),
    )
    language = models.CharField(
        max_length=10,
        default="en",
        verbose_name=_("language"),
        help_text=_("The language code used to display the user interface."),
    )
    script = models.CharField(
        max_length=4,
        choices=[("", _("Automatic (based on language)"))] + Script.choices,
        blank=True,
        default="",
        verbose_name=_("script"),
        help_text=_(
            "The preferred script for displaying place names, e.g. Latin or "
            "Cyrillic for a Serbian user. Leave as automatic to use the "
            "default for the selected language."
        ),
    )
    observer = models.OneToOneField(
        "core.Observer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user",
        verbose_name=_("observer"),
        help_text=_("The observer associated with this user."),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email
