from django.db import models
from django.utils.translation import gettext_lazy as _


class Direction(models.TextChoices):
    """The direction (orientation) of an inscription on a colour mark,
    when it is read from left to right.

    The direction, in principle, ould allow two different projects to use the
    same set of codes, as long as the direction was different. However rings
    get put on the wrong way round so this does not work in practice. However,
    it is useful for ambiguous codes such as "8H" which could also be read as
    "H8". In these cases a dot "." is often used to separate the characters,
    i.e. "8.H" which serves to define the direction.

    The dictionaries, ENCODING, and DECODING are used when writing and reading
    the coded colour mark(s). For example, a red ring with a white inscription
    "A123", reading from top to bottom, is encoded as: RW(A123↓). The number
    of characters used in an inscription varies so the symbol avoids the
    direction being confused for a character in the code.
    """

    DOWN = "D", _("Downward")
    HORIZONTAL = "H", _("Horizontal")
    UP = "U", _("Upward")


# Kept outside the class body: any attribute assigned inside a TextChoices
# class is swallowed by Python's Enum machinery as an extra member, so a
# dict here would silently become part of Direction.choices.
ENCODING: dict[str, str] = {
    Direction.DOWN: "↓",
    Direction.HORIZONTAL: "→",
    Direction.UP: "↑",
}

DECODING: dict[str, str] = {symbol: code for code, symbol in ENCODING.items()}
