from django.db import models
from django.utils.translation import gettext_lazy as _


class Age(models.TextChoices):
    """The age of a bird, using the EURING (EURING2000+) age codes.

    Codes alternate between an exact calendar-year age and "after" that
    calendar-year, for use when the bird is clearly older than a pullus
    or first-year bird but the precise year cannot be determined.

    """

    UNKNOWN = "0", _("Age unknown")
    PULLUS = "1", _("Pullus")
    FULL_GROWN = "2", _("Full-grown")
    FIRST_YEAR = "3", _("1st calendar-year")
    AFTER_FIRST_YEAR = "4", _("After 1st calendar-year")
    SECOND_YEAR = "5", _("2nd calendar-year")
    AFTER_SECOND_YEAR = "6", _("After 2nd calendar-year")
    THIRD_YEAR = "7", _("3rd calendar-year")
    AFTER_THIRD_YEAR = "8", _("After 3rd calendar-year")
    FOURTH_YEAR = "9", _("4th calendar-year")
    AFTER_FOURTH_YEAR = "A", _("After 4th calendar-year")
