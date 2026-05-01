"""Observation model."""

from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class Observation(BaseModel):
    """A record of where and when a colour-tagged bird was seen in the field."""

    class Event(models.TextChoices):
        NONE = "", ""
        CAPTURE = "c", _("Capture")
        RECAPTURE = "r", _("Recapture")
        OBSERVATION = "o", _("Observation")

    class Status(models.TextChoices):
        OPEN = "open", _("Open")
        SUBMITTED = "submitted", _("Submitted")
        CLOSED = "closed", _("Closed")

    event = models.CharField(
        max_length=1,
        choices=Event,
        default=Event.NONE,
        verbose_name=_("event"),
        help_text=_("The type of observation: capture, recapture, observation")
    )
    bird = models.ForeignKey(
        "core.Bird",
        on_delete=models.PROTECT,
        related_name="observations",
        verbose_name=_("bird"),
        help_text=_("The colour-ringed observed."),
    )
    tags = models.JSONField(
        default=dict,
        verbose_name=_("tags"),
        help_text=_(
            "A dictionary of all tags observed and their positions, keyed by position code. "
            'For example: {"LA": "WN(ABC)", "RA": "M"}.'
        ),
    )
    date = models.DateField(
        verbose_name=_("date"),
        help_text=_("The date the observation was made."),
    )
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_("time"),
        help_text=_("The time the observation was made."),
    )
    location = models.ForeignKey(
        "core.Location",
        on_delete=models.PROTECT,
        related_name="observations",
        verbose_name=_("location"),
        help_text=_("The location where the observation was made."),
    )
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_("latitude"),
        help_text=_("The precise latitude of the bird, overriding the location coordinates."),
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_("longitude"),
        help_text=_("The precise longitude of the bird, overriding the location coordinates."),
    )
    photo = models.ImageField(
        upload_to="observations/%Y/%m/%d/",
        blank=True,
        verbose_name=_("photo"),
        help_text=_("A photo of the bird at the time of observation, used to verify that the tags were read correctly."),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("notes"),
        help_text=_("Any additional notes about the observation."),
    )
    observer = models.ForeignKey(
        "core.Observer",
        on_delete=models.PROTECT,
        related_name="observations",
        verbose_name=_("observer"),
        help_text=_("The person who made this observation."),
    )
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.OPEN,
        verbose_name=_("status"),
        help_text=_(
            "The progress made in identifying and linking the origin. "
            "open: no project identified yet; "
            "submitted: project identified and observation submitted to coordinator; "
            "closed: origin linked."
        ),
    )

    class Meta:
        verbose_name = _("observation")
        verbose_name_plural = _("observations")

    def __str__(self):
        return f"{self.species} — {self.code} ({self.date})"
