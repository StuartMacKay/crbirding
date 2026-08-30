from django.db import models
from django.utils.translation import gettext_lazy as _


class TagType(models.TextChoices):
    """The physical type of a colour tag, independent of its Position --
    a ring and a flag can both be worn on the same leg segment, and only
    the type tells them apart.
    """

    RING = "R", _("Ring")
    FLAG = "F", _("Flag")
    SADDLE = "S", _("Nasal saddle")
    WING_TAG = "W", _("Wing tag")
    COLLAR = "C", _("Neck collar")
