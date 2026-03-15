"""Per-request active alphabet, mirroring django.utils.translation's
activate()/get_language() pattern for the active language.

Language and alphabet are related but distinct: a language like Serbian
can be written in more than one alphabet, so the active alphabet can't
always be derived from the active language alone. AlphabetMiddleware sets
a default from the active language, then overrides it with the user's
explicit preference if they have one.
"""

import threading

from ..models.alphabet import Alphabet

_active = threading.local()

# Best-effort default alphabet per language, for users with no explicit
# preference set. Anything not listed here defaults to Latin.
LANGUAGE_TO_ALPHABET = {
    "be": Alphabet.CYRILLIC,
    "bg": Alphabet.CYRILLIC,
    "el": Alphabet.GREEK,
    "mk": Alphabet.CYRILLIC,
    "ru": Alphabet.CYRILLIC,
    "sr": Alphabet.CYRILLIC,
    "uk": Alphabet.CYRILLIC,
}


def default_alphabet_for_language(language_code: str) -> str:
    base_code = (language_code or "").split("-")[0].lower()
    return LANGUAGE_TO_ALPHABET.get(base_code, Alphabet.LATIN)


def activate(alphabet: str) -> None:
    _active.value = alphabet


def deactivate() -> None:
    if hasattr(_active, "value"):
        del _active.value


def get_alphabet() -> str:
    return getattr(_active, "value", Alphabet.LATIN)
