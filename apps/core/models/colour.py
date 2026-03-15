from django.db import models
from django.utils.translation import gettext_lazy as _


class Colour(models.TextChoices):
    """Colours used for colour marks.

    Metal (rings) are also included in the set of colours, allowing all
    the markers on a bird to be recorded (encoded).

    """
    RED = "R", _("Red")
    LIGHT_BLUE = "P", _("Light Blue")
    WHITE = "W", _("White")
    ORANGE = "O", _("Orange")
    DARK_GREEN= "G", _("Dark Green")
    DARK_PINK = "C", _("Dark Pink (Carmine)")
    LIGHT_GREEN = "L", _("Light Green (Lime)")
    LIGHT_PINK = "K", _("Light Pink")
    BLACK = "N", _("Black (Niger)")
    DARK_BLUE = "B", _("Dark Blue")
    METAL = "M", _("Metal Ring")
    VIOLET = "V", _("Violet/Mauve/Purple")
    YELLOW = "Y", _("Yellow")
    SILVER = "S", _("Silver/Grey")
    OTHER = "A", _("Other metal ring")
    BROWN = "U", _("Brown (Umber)")
    TURQUIOSE= "Q", _("Turquoise")
