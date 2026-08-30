from anyascii import anyascii
from django.db import models
from django.utils.translation import gettext_lazy as _

from .. import scripts
from .script import Script


class Place(models.Model):
    """The Euring Place (region, and country) where the bird  was marked
    or observed.

    Unlike Species, this isn't multi-language translated data from an
    authoritative source -- EURING's place-code file gives one name per
    place, not one per language, and its quality varies (some entries
    have no name at all, or have unrecoverably lost accented characters).
    name is keyed by Script rather than language: regions don't usually
    have translated names the way cities or countries do, but still need
    to be readable across alphabets, so treat what's loaded as a
    best-effort transliteration, not an authoritative translation.

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
    published = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("published"),
        help_text=_("When was the place last updated by Euring."),
    )
    active = models.BooleanField(
        verbose_name=_("active"),
        help_text=_("Is the Place currently used."),
    )
    name = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_("name"),
        help_text=_(
            'The name of the Place, keyed by script, e.g. {"Latn": "Sofia", "Cyrl": "София"}.'
        ),
    )
    code = models.TextField(
        db_index=True,
        unique=True,
        verbose_name=_("code"),
        help_text=_("The Euring Place code for a region."),
    )
    country = models.ForeignKey(
        "core.Country",
        on_delete=models.PROTECT,
        related_name="places",
        verbose_name=_("country"),
        help_text=_("The country, or other area, for the Place."),
    )

    class Meta:
        verbose_name = _("place")
        verbose_name_plural = _("places")

    def __repr__(self) -> str:
        return str(self.code)

    def __str__(self):
        return f"{self.get_name()}, {self.country}"

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
