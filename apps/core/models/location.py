from anyascii import anyascii
from django.db import models
from django.utils.translation import gettext_lazy as _

from .. import scripts
from .script import Script


class Location(models.Model):
    """A location where a bird was marked. or later seen.

    Unlike the region or country, the name of a Location is not translated.
    Instead the name is entered in the local script (alphabet), along with
    transliterations, mainly to Latin, and storied in a JSONField using
    the ISO 15924 code as a key.

    The most important piece of location data are the coordinates of the
    bird's position. Coordinates are not user-friendly, so a location is
    given a name, and a place (region, and country). A location can be
    given a label so different observation points, at the same location,
    but with different coordinates, can be distinguished.

    The latitude and longitude are recorded to four decimal places. This
    gives an resolution of approximately 11m. (In Western Europe, between
    40-50 degrees North, the latitide resolution is 11.1m, and the
    longitude, 7.5m (7.1-7.9m). The precision allows decimal coordinates
    to be converted to degrees, minutes and seconds without a loss of
    accuracy due to rounding.

    The coordinates are also given an accuracy. This is the estimated
    distance in metres from the coordinates to the bird's actual position.
    Although the coordinates have a precision of 1m, the accuracy is much
    less than that. Imagine a observer, standing 50m from a flock of birds,
    100m across. If the coordinates of the centre of the flock are recorded,
    then the actual position of any bird is with 50m of those. If coordinates
    of the observer are recorded, then the accuracy will be between 50m and
    150m. Mapping applications on mobile phones make the recorded coordinate
    more accurate. However the only way to ensure the coordinates are as
    accurate as the precision allows, would be to take surveying equipment
    into the field, which is not remotely practical.

    It is worth noting that a Resighting also records coordinates. This
    overrides the coordinates from the Location, allowing for the (more)
    accurate position of the bird to be recorded. Whether these are recorded
    depends on the observer. If the flock of birds is roosting on a beach,
    and is slightly further north, then the accuracy may decrease to 100-200m.
    As a result, the true position of the bird is proably within 250m of the
    reported position. Much less than the precision of the coordinates implies,
    but given that birds are highly mobile, and commonly long-distance migrants,
    the error is not that important.

    The name is stored per script (see core.models.Script) rather than per
    language, e.g. {"Latn": "Sofia", "Cyrl": "София"}, since the
    same name is usually shared by every language written in that script.
    If a script's name isn't given, it's transliterated automatically from
    whichever script is available, as a starting point for an administrator
    to correct rather than a guaranteed-accurate translation.

    The label is a convenience, letting an observer pick between sub-sites
    at the same named location without re-entering coordinates. It is not
    translated and not normally shown to other users.

    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated"),
        help_text=_("When was the record last updated."),
    )
    name = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_("name"),
        help_text=_(
            'The name of the Location, keyed by script, e.g. {"Latn": "Sofia", "Cyrl": "София"}.'
        ),
    )
    label = models.TextField(
        blank=True,
        help_text=_(
            "Label is used to distinguish between sub-sites, "
            "which share the name, but have different coordinates."
        ),
    )
    place = models.ForeignKey(
        "core.Place",
        on_delete=models.PROTECT,
        related_name="locations",
        verbose_name=_("place"),
        help_text=_("The region, and country, for the Location."),
    )
    latitude = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name=_("latitude"),
        help_text=_("The latitude of this location in decimal degrees."),
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        verbose_name=_("longitude"),
        help_text=_("The longitude of this location in decimal degrees."),
    )
    accuracy = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("accuracy"),
        help_text=_(
            "The estimated distance in metres, from the coordinates, "
            "to the actual position of the bird."
        ),
    )
    description = models.TextField(
        blank=True,
        help_text=_("The description of the Location."),
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return f"{self.get_name()} ({self.label})" if self.label else self.get_name()

    def save(self, *args, **kwargs):
        if not self.name.get(Script.LATIN):
            source = next((value for value in self.name.values() if value), "")
            if source:
                self.name[Script.LATIN] = anyascii(source)
        super().save(*args, **kwargs)

    def get_name(self, script: str | None = None) -> str:
        """The name in the given (or currently active) script.

        Falls back to Latin, then to whatever script is available, if
        the requested script isn't.
        """
        script = script or scripts.get_script()
        name = self.name.get(script) or self.name.get(Script.LATIN)
        if name:
            return name
        return next(iter(self.name.values()), "")
