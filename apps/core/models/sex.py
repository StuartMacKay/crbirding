from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.TextChoices):
    """The sex of a bird.

    It's worth noting that "unknown" is synomymous with "not recorded",
    so there's no way to disntinguish between "couldn't tell" and "did
    not look".

    """

    UNKNOWN = "U", _("Unknown")
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
