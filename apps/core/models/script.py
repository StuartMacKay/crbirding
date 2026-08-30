from django.db import models
from django.utils.translation import gettext_lazy as _


class Script(models.TextChoices):
    """Writing systems, using the ISO 15924 code, used in the Western Palearctic."""

    ARABIC = "Arab", _("Arabic")
    ARMENIAN = "Armn", _("Armenian")
    CYRILLIC = "Cyrl", _("Cyrillic")
    GEORGIAN = "Geor", _("Georgian")
    GREEK = "Grek", _("Greek")
    HEBREW = "Hebr", _("Hebrew")
    LATIN = "Latn", _("Latin")
