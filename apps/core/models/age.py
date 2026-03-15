from django.db import models
from django.utils.translation import gettext_lazy as _


class Age(models.TextChoices):
    """The age of a bird, using the EURING (EURING2000+) age codes.

    Codes alternate between an exact calendar-year age and "after" that
    calendar-year, for use when the bird is clearly older than a pullus
    or first-year bird but the precise year cannot be determined.

    """

    NESTLING = "1", _("Nestling")
    FULL_GROWN = "2", _("Full-grown")
    FIRST_YEAR = "3", _("1CY")
    AFTER_FIRST_YEAR = "4", _("1CY+")
    SECOND_YEAR = "5", _("2CY")
    AFTER_SECOND_YEAR = "6", _("2CY+")
    THIRD_YEAR = "7", _("3CY")
    AFTER_THIRD_YEAR = "8", _("3CY+")
    FOURTH_YEAR = "9", _("4CY")
    AFTER_FOURTH_YEAR = "A", _("4CY+")
