from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    """A simple Event to keep track of managing Observations."""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    observation = models.ForeignKey(
        "core.Observation",
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name=_("observation"),
        help_text=_("The observation this event belongs to."),
    )
    date = models.DateField(
        default=timezone.localdate,
        verbose_name=_("date"),
        help_text=_("The date the event happened."),
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("A short description of the event."),
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["date", "created"]

    def __str__(self) -> str:
        return self.description
