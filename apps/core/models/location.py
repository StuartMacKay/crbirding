"""Location model."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

from .base import BaseModel


class Location(BaseModel):
    """A place where an Observation was made or where birds were tagged."""

    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The name of the location."),
    )
    region = models.CharField(
        max_length=6,
        blank=True,
        verbose_name=_("region"),
        help_text=_(
            "The ISO 3166-2 subdivision code for the region or district "
            "where this location is situated."
        ),
    )
    country = CountryField()
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_("latitude"),
        help_text=_("The latitude of this location in decimal degrees."),
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name=_("longitude"),
        help_text=_("The longitude of this location in decimal degrees."),
    )
    accuracy = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("accuracy"),
        help_text=_("The estimated distance in metres between the coordinates and the actual position."),
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        parts = [self.name]
        if self.region:
            parts.append(self.region)
        parts.append(self.get_country_display())
        return ", ".join(parts)
