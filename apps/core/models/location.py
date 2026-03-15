from anyascii import anyascii
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils import alphabets
from .alphabet import Alphabet
from .country import Country
from .region import PLACE_TO_COUNTRY, Region


class Location(models.Model):
    """A location where a bird was marked. or later seen.

    Unlike the region or country, the name of a Location is not translated.
    Instead the name is entered in the local alphabet (alphabet), along with
    transliterations, mainly to Latin, and storied in a JSONField using
    the ISO 15924 code as a key.

    The most important piece of location data are the coordinates of the
    bird's position. Coordinates are not user-friendly, so a location is
    given a name, and a place (region, and country).

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

    It is worth noting that a Observation also records coordinates. This
    overrides the coordinates from the Location, allowing for the (more)
    accurate position of the bird to be recorded. Whether these are recorded
    depends on the observer. If the flock of birds is roosting on a beach,
    and is slightly further north, then the accuracy may decrease to 100-200m.
    As a result, the true position of the bird is proably within 250m of the
    reported position. Much less than the precision of the coordinates implies,
    but given that birds are highly mobile, and commonly long-distance migrants,
    the error is not that important.

    The name is stored per alphabet (see core.models.Alphabet) rather than per
    language, e.g. {"Latn": "Sofia", "Cyrl": "София"}, since the
    same name is usually shared by every language written in that alphabet.
    If a alphabet's name isn't given, it's transliterated automatically from
    whichever alphabet is available, as a starting point for an administrator
    to correct rather than a guaranteed-accurate translation.

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
            'The name of the Location, keyed by alphabet, e.g. {"Latn": "Sofia", "Cyrl": "София"}.'
        ),
    )
    region = models.CharField(
        max_length=4,
        choices=Region.choices,
        verbose_name=_("region"),
        help_text=_("The EURING region (or, for a coarser record, country) for the Location."),
    )
    latitude = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        verbose_name=_("latitude"),
        help_text=_("The latitude of the centre of this location, in decimal degrees."),
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        verbose_name=_("longitude"),
        help_text=_("The longitude of the centre of this location, in decimal degrees."),
    )
    accuracy = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("accuracy"),
        help_text=_(
            "The radius, in metres, of a circle around the coordinates that "
            "approximates the area of this location. Used as the default for an "
            "Observation or Origin at this site when more precise coordinates "
            "and accuracy aren't given."
        ),
    )
    notes = models.TextField(
        blank=True,
        help_text=_("Notes about the Location."),
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.get_name()

    def save(self, *args, **kwargs):
        if not self.name.get(Alphabet.LATIN):
            source = next((value for value in self.name.values() if value), "")
            if source:
                self.name[Alphabet.LATIN] = anyascii(source)
        super().save(*args, **kwargs)

    def get_name(self, alphabet: str | None = None) -> str:
        """The name in the given (or currently active) alphabet.

        Falls back to Latin, then to whatever alphabet is available, if
        the requested alphabet isn't.
        """
        alphabet = alphabet or alphabets.get_alphabet()
        name = self.name.get(alphabet) or self.name.get(Alphabet.LATIN)
        if name:
            return name
        return next(iter(self.name.values()), "")

    def get_country_code(self) -> str:
        """The country this Location's region belongs to, derived from
        PLACE_TO_COUNTRY -- country isn't stored separately, since a
        region always implies exactly one country.
        """
        return PLACE_TO_COUNTRY[self.region]

    def get_country_display(self) -> str:
        return Country(self.get_country_code()).label
