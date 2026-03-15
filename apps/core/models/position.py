from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.TextChoices):
    """The position of a tag on the bird."""
    LEFT_ABOVE = "LA", _("Left Above")
    LEFT_BELOW = "LB", _("Left Below")
    LEFT_WING = "LW", _("Left Wing")
    NASAL_SADDLE = "S", _("Nasal Saddle")
    NECK_COLLAR = "C", _("Neck Collar")
    RIGHT_ABOVE = "RA", _("Right Above")
    RIGHT_BELOW = "RB", _("Right Below")
    RIGHT_WING = "RW", _("Right Wing")
