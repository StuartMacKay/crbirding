#!/usr/bin/env python3
"""Generate apps/core/models/region.py and apps/core/models/country.py
from EURING's own place-code list.

Unlike species (a database table, populated via admin CSV import from
whatever subset a deployer wants), Region and Country are baked in as
plain TextChoices here -- there's no meaningful "just the ones you
need" for a personal deployment to curate, since which region a bird
turns up in isn't something you decide in advance. Having the full
EURING list available at all times means nothing needs importing or
initialising before a Location can be recorded; the Django admin's
list_filter is what keeps this from cluttering a small deployment (see
apps.core.admin.filters.UsedValueListFilter), not a smaller choice set.

The source file is EURING's own place-code export -- pipe-delimited,
encoding is Latin-1 (or at least decodes cleanly as such), with real
data-quality problems inherited from upstream: a handful of rows split
a place name across extra "|" separators instead of quoting it, and a
few names have already lost an accented character to a stray "?"
upstream. Both are handled/tolerated below rather than fixed, since
there's no way to recover the second from this file alone.

Columns: Country|Region|Place Code|Current|Notes|Date Updated -- Region
is blank for a row describing the country as a whole. "Current" is Y/N;
only current rows are included; obsolete/renamed codes are dropped.

Run by project maintainers occasionally (when EURING updates their
place list) -- not by individual deployers or end users.

Source: https://www.euring.org/files/documents/ECPlacePipeDelimited_0.csv
"""

import argparse
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_URL = "https://www.euring.org/files/documents/ECPlacePipeDelimited_0.csv"
REGION_OUTPUT = REPO_ROOT / "apps" / "core" / "models" / "region.py"
COUNTRY_OUTPUT = REPO_ROOT / "apps" / "core" / "models" / "country.py"

CODE_RE = re.compile(r"^[A-Z0-9+\-]{4}$")


def read_source(source: str) -> str:
    if source.startswith("http://") or source.startswith("https://"):
        request = urllib.request.Request(source, headers={"User-Agent": "crbirding-sync/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            if response.status != 200:
                raise SystemExit(f"Failed to fetch {source}: HTTP {response.status}")
            return response.read().decode("latin-1")
    path = Path(source)
    if not path.exists():
        raise SystemExit(f"No such file: {path}")
    return path.read_bytes().decode("latin-1")


def parse_rows(text: str) -> list[tuple[str, str, str]]:
    """[(country_name, region_name, place_code), ...] for current rows.

    The place code is found by pattern rather than fixed column
    position, since a handful of region names contain an unquoted "|"
    that shifts every field after it -- see module docstring.
    """
    rows = []
    for line in text.splitlines()[1:]:
        if not line.strip():
            continue
        fields = line.split("|")
        code_index = next(
            (i for i in range(1, len(fields)) if CODE_RE.match(fields[i].strip())), None
        )
        if code_index is None:
            continue
        current = fields[code_index + 1].strip() if len(fields) > code_index + 1 else ""
        if current != "Y":
            continue
        country = fields[0].strip()
        region = ", ".join(f.strip() for f in fields[1:code_index] if f.strip())
        code = fields[code_index].strip()
        rows.append((country, region, code))
    return rows


def build_country_codes(rows: list[tuple[str, str, str]]) -> dict[str, list[str]]:
    """{country_name: [code, ...]}, one code per blank-region row for that
    country, plus a synthesised entry (from that name's own alphabetically
    first code) for any country with no blank-region row of its own.
    """
    codes_by_name: dict[str, list[str]] = {}
    for country, region, code in rows:
        if not region:
            codes_by_name.setdefault(country, []).append(code)

    referenced_names = {country for country, _region, _code in rows}
    for name in sorted(referenced_names - set(codes_by_name)):
        candidate = min(code for country, _region, code in rows if country == name)
        codes_by_name[name] = [candidate]
    return codes_by_name


def country_code_for(name: str, region_code: str, codes_by_name: dict[str, list[str]]) -> str:
    """Which of a country's code(s) a given region belongs to.

    Almost always unambiguous (one code per name). Germany is the one
    current exception -- two codes for two historical entities sharing
    the "Germany" name -- disambiguated by matching the region's own
    2-character code prefix against each candidate's.
    """
    codes = codes_by_name[name]
    if len(codes) == 1:
        return codes[0]
    prefix = region_code[:2]
    return next((code for code in codes if code[:2] == prefix), codes[0])


def to_identifier(name: str, seen: set[str]) -> str:
    ident = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").upper()
    if not ident or ident[0].isdigit():
        ident = f"P_{ident}"
    unique, n = ident, 2
    while unique in seen:
        unique = f"{ident}_{n}"
        n += 1
    seen.add(unique)
    return unique


def render_choices_class(class_name: str, docstring: str, entries: list[tuple[str, str]]) -> str:
    seen: set[str] = set()
    lines = [f'class {class_name}(models.TextChoices):', f'    """{docstring}"""', ""]
    for code, name in sorted(entries):
        escaped = name.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    {to_identifier(name, seen)} = "{code}", _("{escaped}")')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Region and Country TextChoices from EURING's place-code list."
    )
    parser.add_argument("--source", default=SOURCE_URL)
    options = parser.parse_args()

    rows = parse_rows(read_source(options.source))
    codes_by_name = build_country_codes(rows)

    region_entries = [(code, region or country) for country, region, code in rows]

    country_entries: list[tuple[str, str]] = []
    seen_codes: set[str] = set()
    for country, region, code in rows:
        if not region and code not in seen_codes:
            country_entries.append((code, country))
            seen_codes.add(code)
    for name, codes in codes_by_name.items():
        if codes[0] not in seen_codes:
            country_entries.append((codes[0], name))
            seen_codes.add(codes[0])

    place_to_country = {
        code: country_code_for(country, code, codes_by_name) for country, region, code in rows
    }

    region_source = f'''"""EURING place codes -- see scripts/generate_region_choices.py, which
generates this file (and country.py's Country class) wholesale from
EURING's own place-code list. Don't hand-edit; re-run that script when
EURING publishes an update.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


{render_choices_class(
        "Region",
        "Every current EURING place code, country-level and finer sub-regions alike.",
        region_entries,
    )}


PLACE_TO_COUNTRY: dict[str, str] = {{
{chr(10).join(f'    "{code}": "{country_code}",' for code, country_code in sorted(place_to_country.items()))}
}}
'''

    country_source = f'''"""EURING country-level place codes -- see scripts/generate_region_choices.py,
which generates this file (and region.py's Region class and
PLACE_TO_COUNTRY) wholesale from EURING's own place-code list. Don't
hand-edit; re-run that script when EURING publishes an update.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


{render_choices_class(
        "Country",
        "The EURING place code for each country (or other top-level area, "
        "e.g. an area at sea) as a whole.",
        country_entries,
    )}
'''

    REGION_OUTPUT.write_text(region_source, encoding="utf-8")
    COUNTRY_OUTPUT.write_text(country_source, encoding="utf-8")

    print(f"{len(region_entries)} regions written to {REGION_OUTPUT}.")
    print(f"{len(country_entries)} countries written to {COUNTRY_OUTPUT}.")


if __name__ == "__main__":
    sys.exit(main())
