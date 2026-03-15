from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .age import Age
from .sex import Sex
from .species import Species


class Observation(models.Model):
    """A record of where and when a colour-marked bird was seen in the field."""

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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="observations",
        verbose_name=_("owner"),
        help_text=_("The user this record is private to. Leave blank to share it with everyone."),
    )
    species = models.CharField(
        max_length=5,
        choices=Species.choices,
        verbose_name=_("species"),
        help_text=_("The species observed."),
    )
    age = models.TextField(
        blank=True,
        choices=Age.choices,
        verbose_name=_("age"),
        help_text=_("The age of the bird, using the EURING age code."),
    )
    sex = models.TextField(
        blank=True,
        choices=Sex.choices,
        verbose_name=_("sex"),
        help_text=_("The sex of the bird, using the EURING sex code."),
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
        max_digits=6,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name=_("latitude"),
        help_text=_("The precise latitude of the bird, overriding the location coordinates."),
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name=_("longitude"),
        help_text=_("The precise longitude of the bird, overriding the location coordinates."),
    )
    accuracy = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("coordinates accuracy"),
        help_text=_(
            "The estimated distance in metres, from the coordinates, "
            "to the actual position of the bird."
        ),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("notes"),
        help_text=_("Any additional notes."),
    )
    observers = models.ManyToManyField(
        "core.Observer",
        related_name="observations",
        verbose_name=_("observers"),
        help_text=_("The people who made this observation."),
    )
    origin = models.ForeignKey(
        "core.Origin",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="observations",
        verbose_name=_("origin"),
        help_text=_("The details of where the bird was marked."),
    )

    class Meta:
        verbose_name = _("observation")
        verbose_name_plural = _("observations")

    def __str__(self) -> str:
        return str(Species(self.species).label)
