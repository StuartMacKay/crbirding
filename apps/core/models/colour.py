"""Tag colours - the background colour, or the colour of the code."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Colour(models.TextChoices):
    NONE = "", _("None")
    RED = "R", _("Red")
    PALE_BLUE = "P", _("Pale Blue")
    WHITE = "W", _("White")
    ORANGE = "O", _("Orange")
    DARK_GREEN= "G", _("Dark Green")
    DARK_PINK = "C", _("Dark Pink (Carmine)")
    LIGHT_GREEN = "L", _("Light Green (Lime)")
    LIGHT_PINK = "K", _("Light Pink")
    BLACK = "N", _("Black (Niger)")
    DARK_BLUE = "B", _("Blue (Dark)")
    METAL = "M", _("Metal Ring")
    VIOLET = "V", _("Violet/Mauve/Purple")
    YELLOW = "Y", _("Yellow")
    SILVER = "S", _("Silver/Grey")
    OTHER = "A", _("Other metal ring")
    BROWN = "U", _("Brown (Umber)")
    TURQUIOSE= "Q", _("Turquoise")
