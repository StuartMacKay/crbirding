from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

euring_code_validator = RegexValidator(
    regex=r"^\d{5}$",
    message=_("The code must be the 5-digit EURING species code, e.g. '00020'."),
)


class Species(models.Model):
    """The species of bird marked or observed.

    The code is the EURING species code. EURING allocates codes in multiples
    of 10 following taxonomic order, leaving gaps for later insertions (e.g.
    subspecies, or species split from an existing entry), so sorting by code
    also gives the taxonomic order.
    """

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
    code = models.TextField(
        unique=True,
        validators=[euring_code_validator],
        verbose_name=_("code"),
        help_text=_("The 5-digit EURING code used to uniquely identify this species."),
    )
    scientific_name = models.TextField(
        verbose_name=_("scientific name"),
        help_text=_("The scientific (Latin) name for the species."),
    )

    class Meta:
        verbose_name = _("species")
        verbose_name_plural = _("species")
        ordering = ["code"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(code__regex=r"^\d{5}$"),
                name="species_code_is_5_digit_euring_code",
            ),
        ]

    def __repr__(self) -> str:
        return str(self.code)

    def __str__(self) -> str:
        return self.get_common_name()

    def get_common_name(self, language_code: str | None = None) -> str:
        """The common name in the given (or currently active) language.

        Falls back to English, then to the scientific name, if no
        translation is available.
        """
        language_code = language_code or get_language()
        names = {name.language_code: name.common_name for name in self.names.all()}
        return names.get(language_code) or names.get("en") or self.scientific_name


class SpeciesName(models.Model):
    """The common name of a Species in a given language."""

    species = models.ForeignKey(
        "core.Species",
        on_delete=models.CASCADE,
        related_name="names",
        verbose_name=_("species"),
        help_text=_("The species this name belongs to."),
    )
    language_code = models.CharField(
        max_length=7,
        verbose_name=_("language"),
        help_text=_("The ISO 639-1 language code for this name, e.g. 'en' or 'pt-br'."),
    )
    common_name = models.TextField(
        verbose_name=_("common name"),
        help_text=_("The common name for the species in this language."),
    )

    class Meta:
        verbose_name = _("species name")
        verbose_name_plural = _("species names")
        constraints = [
            models.UniqueConstraint(
                fields=["species", "language_code"], name="unique_species_language"
            ),
        ]

    def __str__(self) -> str:
        return f"{self.common_name} ({self.language_code})"
