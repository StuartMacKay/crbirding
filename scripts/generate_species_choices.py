#!/usr/bin/env python3
"""Generate apps/core/models/species.py from EURING's own species-code
list -- the same approach as scripts/generate_region_choices.py, and
for the same reason: EURING's code list is itself the closed,
authoritative set of species a ring or observation record can name, so
baking it in as a plain TextChoices means nothing needs importing or
initialising before a Capture or Observation can be recorded.

Only rows in current use are included -- EURING's own Status column
distinguishes:
    sp  - a current species (the vast majority of rows)
    a   - an aggregate/uncertain code (e.g. "Gavia sp.", "Unknown species")
    h   - a hybrid between two species
    f   - a domesticated form
    ssp - a subspecies -- excluded; this app doesn't track subspecies
    o   - an obsolete/renamed code -- excluded

Common names come from the CSV's own English_Name column, which is
already cross-referenced to IOC -- rows without one (mostly the "a"/
"h"/"f" rows above) fall back to the scientific name as their label.
Translations of the common names into other languages are generated
separately -- see scripts/generate_species_translations.py -- from
IOC's own multilingual names file, keyed by the IOC column here.

Run by project maintainers occasionally (when EURING publish an
update) -- not by individual deployers or end users.

Source: https://euring.org/files/documents/EURING_SpeciesCodes_IOC15_1_2.csv
"""

import argparse
import csv
import io
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_URL = "https://euring.org/files/documents/EURING_SpeciesCodes_IOC15_1_2.csv"
SPECIES_OUTPUT = REPO_ROOT / "apps" / "core" / "models" / "species.py"

INCLUDED_STATUSES = {"sp", "a", "h", "f"}


def read_source(source: str) -> str:
    if source.startswith("http://") or source.startswith("https://"):
        request = urllib.request.Request(source, headers={"User-Agent": "crbirding-sync/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            if response.status != 200:
                raise SystemExit(f"Failed to fetch {source}: HTTP {response.status}")
            return response.read().decode("utf-8-sig")
    path = Path(source)
    if not path.exists():
        raise SystemExit(f"No such file: {path}")
    return path.read_bytes().decode("utf-8-sig")


def parse_rows(text: str) -> list[dict[str, str]]:
    rows = [row for row in csv.DictReader(io.StringIO(text)) if row["Status"] in INCLUDED_STATUSES]
    codes = [row["EURING_Code"] for row in rows]
    duplicates = {code for code in codes if codes.count(code) > 1}
    if duplicates:
        raise SystemExit(f"Duplicate EURING codes in source: {sorted(duplicates)}")
    return rows


def to_identifier(name: str, seen: set[str]) -> str:
    ident = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").upper()
    if not ident or ident[0].isdigit():
        ident = f"SP_{ident}"
    unique, n = ident, 2
    while unique in seen:
        unique = f"{ident}_{n}"
        n += 1
    seen.add(unique)
    return unique


def render_choices_class(entries: list[tuple[str, str]]) -> str:
    seen: set[str] = set()
    lines = [
        "class Species(models.TextChoices):",
        '    """Every current EURING species code -- see',
        "    scripts/generate_species_choices.py.",
        '    """',
        "",
    ]
    for code, label in entries:
        escaped = label.replace("\\", "\\\\").replace('"', '\\"')
        identifier = to_identifier(label, seen)
        line = f'    {identifier} = "{code}", _("{escaped}")'
        if len(line) > 100:
            line = f'    {identifier} = (\n        "{code}",\n        _("{escaped}"),\n    )'
        lines.append(line)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate the Species TextChoices from EURING's species-code list."
    )
    parser.add_argument("--source", default=SOURCE_URL)
    options = parser.parse_args()

    rows = parse_rows(read_source(options.source))

    entries = []
    scientific_names = {}
    for row in rows:
        code = row["EURING_Code"]
        scientific_name = row["Current_Name"]
        english_name = row["English_Name"]
        label = english_name if english_name and english_name != "NA" else scientific_name
        entries.append((code, label))
        scientific_names[code] = scientific_name
    entries.sort(key=lambda pair: pair[1])

    source = f'''"""EURING species codes -- see scripts/generate_species_choices.py,
which generates this file wholesale from EURING's own species-code
list. Don't hand-edit; re-run that script when EURING publishes an
update.

Translations of the common names below come from
scripts/generate_species_translations.py, which writes them straight
into the locale .po files from IOC's own multilingual names -- there's
nothing for a translator (or an administrator) to do by hand.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


{render_choices_class(entries)}


SPECIES_SCIENTIFIC_NAME: dict[str, str] = {{
{chr(10).join(f'    "{code}": "{name}",' for code, name in sorted(scientific_names.items()))}
}}
'''

    SPECIES_OUTPUT.write_text(source, encoding="utf-8")
    print(f"{len(entries)} species written to {SPECIES_OUTPUT}.")


if __name__ == "__main__":
    sys.exit(main())
