"""Pieces shared by every CSV bulk-import in core.utils -- reading a
CSV file with a normalised header, the small value parsers, and the
choice/country/region resolution rules, plus the ImportReport each
import reports its results through.

See core.utils.bulk_import (Observation), core.utils.location_import
(Location), core.utils.project_import (Project), and
core.utils.rule_import (Rule) for the importers themselves.
"""

import csv
import io
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation

from django.db import models

from ..models import PLACE_TO_COUNTRY, SPECIES_SCIENTIFIC_NAME, Country, Region, Species


@dataclass
class ImportReport:
    created: int = 0
    duplicates: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)
    # Per-row explanations for *some* duplicates -- e.g.
    # core.utils.bulk_import notes exactly which earlier row (and when)
    # a same-day resighting matches, so a duplicate reads as an
    # intentional, understood outcome rather than a silent count that
    # could be mistaken for a bug. Optional: an import that has nothing
    # useful to say about a given duplicate just leaves this empty.
    duplicate_details: list[str] = field(default_factory=list)


def normalized_dict_reader(file) -> csv.DictReader:
    """A csv.DictReader over `file`, with the header row's own column
    names stripped and lowercased -- so a column like "Time" or "time "
    (easy to end up with from a spreadsheet export) is still recognised,
    rather than silently treated as absent.
    """
    text = file.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames:
        reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
    return reader


def parse_decimal(value: str) -> Decimal | None:
    if not value:
        return None
    try:
        return Decimal(value)
    except InvalidOperation:
        raise ValueError(f"{value!r} is not a valid coordinate") from None


def parse_int(value: str) -> int | None:
    return int(value) if value else None


def _match_by_code_or_label(value: str, choices: list[tuple[str, str]], label: str) -> str:
    """The code from `choices` (a list of (code, label) pairs) matching
    `value` -- either exactly, as a code, or case-insensitively, as a
    display label.
    """
    if value in dict(choices):
        return value

    matches = {code for code, choice_label in choices if str(choice_label).lower() == value.lower()}
    if len(matches) == 1:
        return matches.pop()
    if len(matches) > 1:
        raise ValueError(f"{value!r} matches more than one {label}")
    raise ValueError(f"no {label} matching {value!r}")


def resolve_choice(
    value: str, choices: type[models.TextChoices], label: str, *, default: str | None = None
) -> str:
    """The choice from `choices` matching `value` -- by its own code, or
    by its display label. `label` names the field for error messages
    (e.g. "age", "position"). Blank stays `default` if one is given,
    otherwise it's an error -- some fields (age, sex) are fine left
    unknown, others (position) aren't.
    """
    value = value.strip()
    if not value:
        if default is not None:
            return default
        raise ValueError(f"no {label} given")

    return _match_by_code_or_label(value, choices.choices, label)


def resolve_species(value: str) -> str:
    """The EURING code matching `value` -- by code, scientific name, or
    common name (in any language the site has translations for).
    """
    value = value.strip()
    if not value:
        raise ValueError("no species given")

    if len(value) == 5 and value.isdigit() and value in Species.values:
        return value

    matches = {
        code for code, name in SPECIES_SCIENTIFIC_NAME.items() if name.lower() == value.lower()
    }
    matches |= {code for code, label in Species.choices if str(label).lower() == value.lower()}
    if len(matches) == 1:
        return matches.pop()
    if len(matches) > 1:
        raise ValueError(f"{value!r} matches more than one species; use its EURING code")
    raise ValueError(f"no species matching {value!r}")


def resolve_country(value: str) -> str:
    """The EURING country-level code matching `value` -- by code, or by
    its display label.
    """
    return resolve_choice(value, Country, "country")


def resolve_region(value: str, country_code: str) -> str:
    """The EURING region code matching `value` within `country_code` --
    by code, or by its display label. Narrowing by country first is
    what makes a name like "Central" resolvable at all: region labels
    aren't unique across countries, only within one.
    """
    value = value.strip()
    if not value:
        raise ValueError("no region given")

    choices = [
        (code, label) for code, label in Region.choices if PLACE_TO_COUNTRY[code] == country_code
    ]
    try:
        return _match_by_code_or_label(value, choices, "region")
    except ValueError as exc:
        raise ValueError(f"{exc} in that country") from exc
