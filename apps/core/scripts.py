"""Per-request active script, mirroring django.utils.translation's
activate()/get_language() pattern for the active language.

Language and script are related but distinct: a language like Serbian
can be written in more than one script, so the active script can't
always be derived from the active language alone. ScriptMiddleware sets
a default from the active language, then overrides it with the user's
explicit preference if they have one.
"""

import threading

from .models.script import Script

_active = threading.local()

# Best-effort default script per language, for users with no explicit
# preference set. Anything not listed here defaults to Latin.
LANGUAGE_TO_SCRIPT = {
    "be": Script.CYRILLIC,
    "bg": Script.CYRILLIC,
    "el": Script.GREEK,
    "mk": Script.CYRILLIC,
    "ru": Script.CYRILLIC,
    "sr": Script.CYRILLIC,
    "uk": Script.CYRILLIC,
}


def default_script_for_language(language_code: str) -> str:
    base_code = (language_code or "").split("-")[0].lower()
    return LANGUAGE_TO_SCRIPT.get(base_code, Script.LATIN)


def activate(script: str) -> None:
    _active.value = script


def deactivate() -> None:
    if hasattr(_active, "value"):
        del _active.value


def get_script() -> str:
    return getattr(_active, "value", Script.LATIN)
