from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Observer(models.Model):
    """A person who made the Resighting."""

    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The full name of the observer."),
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated"),
        help_text=_("When was the record last updated."),
    )

    class Meta:
        verbose_name = _("observer")
        verbose_name_plural = _("observers")
        ordering = ["name"]

    def __str__(self):
        return self.name
