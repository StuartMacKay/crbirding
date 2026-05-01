"""Observer model."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import BaseModel


class Observer(BaseModel):
    """A person who makes an Observation."""

    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The full name of the observer."),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="observer",
        verbose_name=_("user"),
        help_text=_("The user account associated with this observer, if any."),
    )

    class Meta:
        verbose_name = _("observer")
        verbose_name_plural = _("observers")
        ordering = ["name"]

    def __str__(self):
        return self.name
