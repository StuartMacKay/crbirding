from django.db import models
from django.utils.translation import gettext_lazy as _


class Direction(models.TextChoices):
    """The direction (orientation) of an inscription on a colour mark,
    when it is read from left to right.

    The direction, in principle, would allow two different projects to use
    the same set of codes, as long as the direction was different. However
    rings get put on the wrong way round so this does not work in practice.
    However, it is useful for ambiguous codes such as "8H" which could also
    be read as "H8". In these cases a dot "." is often used to separate the
    characters, i.e. "8.H" which serves to define the direction.

    In the compact colour-mark notation (see apps.core.formatting.format_tag),
    the direction is the lowercase of this class's own code, appended right
    after the inscription's closing bracket -- e.g. a red ring with a white
    inscription "A123", reading top to bottom, is "RW(A123)d". Earlier this
    used arrow symbols (↓ → ↑) instead, but those aren't a universal
    convention and are a nuisance to type by hand; a plain letter there is
    unambiguous since it can only ever follow a closing bracket, never a
    colour code, which always comes before the opening one.
    """

    DOWN = "D", _("Downward")
    HORIZONTAL = "H", _("Horizontal")
    UP = "U", _("Upward")
