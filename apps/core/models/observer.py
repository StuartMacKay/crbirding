from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Observer(models.Model):
    """A person who made the Observation."""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
        help_text=_("When was the record last updated."),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="observer",
        verbose_name=_("user"),
        help_text=_(
            "The registered user this Observer is, if any -- leave blank for a "
            "historical or unregistered observer."
        ),
    )
    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The full name of the observer."),
    )

    class Meta:
        verbose_name = _("observer")
        verbose_name_plural = _("observers")
        ordering = ["name"]

    def __str__(self):
        return self.name
