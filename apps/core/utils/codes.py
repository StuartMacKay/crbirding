"""The colour-mark notation for what's worn at one Position on a bird --
e.g. "R,WN(KY)": a red ring above a white one with a black inscription
"KY". See core.models.Tag, which stores one of these per Position.

A code is a comma-separated stack of marks, top to bottom. Each mark is:

    colour letters -- one, or two for a striped ring (see Colour)
    "F"            -- anywhere in the letters, if it's a flag not a ring
    (inscription)  -- optional; with it, the *last* colour letter is the
                      inscription's own colour, e.g. "BW(A123)" is a blue
                      ring with white letters. Always written as read top
                      to bottom, even when the letters are stacked -- which
                      way they read isn't part of the code; anything worth
                      saying about it goes in the Observation's notes.
    ?              -- optional, last: some part of it wasn't clearly read

Nothing here is stored broken down -- it's parsed only to check a code
is well-formed, to write it one standard way (normalise_code), and to
strip what shouldn't affect matching against a Rule (match_code).
"""

from dataclasses import dataclass

from ..models import Colour

_COLOURS = set(Colour.values)
_METAL = {Colour.METAL, Colour.OTHER}


@dataclass(frozen=True)
class Mark:
    """One ring, flag, etc. within a code."""

    colour: str
    second_colour: str = ""
    flag: bool = False
    inscription: str = ""
    inscription_colour: str = ""
    uncertain: bool = False

    @property
    def is_metal(self) -> bool:
        return self.colour in _METAL and not self.second_colour

    def format(self, *, include_uncertain: bool = True) -> str:
        code = self.colour + self.second_colour + ("F" if self.flag else "")
        if self.inscription:
            code += f"{self.inscription_colour}({self.inscription})"
        if include_uncertain and self.uncertain:
            code += "?"
        return code


def parse_mark(code: str) -> Mark:
    """One mark, e.g. "BW(A123)". Raises ValueError, quoting `code`, on
    anything it can't confidently read.

    Where an inscription follows two colour letters, the second is the
    inscription's colour, not a stripe -- "BW(A123)" is a blue ring
    with white letters, the established convention; a striped ring with
    lettering needs all three, e.g. "OYW(A123)".
    """
    original = code
    code = code.strip()
    uncertain = code.endswith("?")
    if uncertain:
        code = code[:-1]
    if not code:
        raise ValueError(f"{original!r}: empty mark")

    head, inscription = code, ""
    if "(" in code:
        head, _, rest = code.partition("(")
        if ")" not in rest:
            raise ValueError(f"{original!r}: missing closing bracket")
        inscription, _, suffix = rest.partition(")")
        if not inscription:
            raise ValueError(f"{original!r}: empty inscription")
        if suffix:
            raise ValueError(
                f"{original!r}: unexpected {suffix!r} after the inscription -- "
                "write the letters as read top to bottom, and anything about "
                "which way they read in the notes"
            )
    elif ")" in code:
        raise ValueError(f"{original!r}: missing opening bracket")

    head = head.upper()
    flag = "F" in head
    head = head.replace("F", "", 1)
    if not head:
        raise ValueError(f"{original!r}: missing colour")
    for letter in head:
        if letter not in _COLOURS:
            raise ValueError(f"{original!r}: {letter!r} is not a known colour code")
    if len(head) > (3 if inscription else 2):
        raise ValueError(f"{original!r}: too many colour letters")

    colour, second_colour, inscription_colour = head[0], "", ""
    if inscription and len(head) >= 2:
        inscription_colour = head[-1]
        second_colour = head[1] if len(head) == 3 else ""
    elif len(head) == 2:
        second_colour = head[1]

    return Mark(
        colour=colour,
        second_colour=second_colour,
        flag=flag,
        inscription=inscription.upper(),
        inscription_colour=inscription_colour,
        uncertain=uncertain,
    )


def parse_code(code: str) -> list[Mark]:
    """Every mark in a code, top to bottom. Raises ValueError."""
    if not code.strip():
        raise ValueError("empty code")
    return [parse_mark(part) for part in code.split(",")]


def normalise_code(code: str) -> str:
    """`code` written the one standard way -- upper-case, no spaces --
    so the same marks always give the same text. Raises ValueError if it
    isn't well-formed.
    """
    return ",".join(mark.format() for mark in parse_code(code))


def match_code(code: str) -> str:
    """`code` without its "?"s -- what a Rule is matched against: being
    unsure of a reading doesn't change which project a scheme belongs to.
    """
    return ",".join(mark.format(include_uncertain=False) for mark in parse_code(code))
