#!/usr/bin/env python3
"""Build the maintainer-curated place reference file.

Cleans up EURING's place-code file (pipe-delimited, encoding varies --
see --encoding below -- with real data-quality problems: ragged rows,
duplicate codes reused for different regions after boundary changes, the
occasional name already lost to a "?" upstream) into a tidy UTF-8 CSV:
place_code, country_code, active, latin_name. Scoped to the Country rows
already in the database; everything else (other continents, historical
political entities like "Soviet Union") is written to a separate
unmatched-countries report rather than silently dropped.

This is the auto-generated half of the place reference data -- entirely
disposable, safe to overwrite wholesale on every run. Per-script names in
other alphabets (Greek, Cyrillic, ...) live in the separate, hand-curated
apps/core/data/place_translations.csv, which this script never touches:
EURING's file only ever gives one name per place, so there's no source to
regenerate those columns from.

Run by project maintainers occasionally, as part of preparing a release
-- not by individual deployers or end users. Needs the database (to scope
against Country), so, unlike sync_species_reference.py, it does bootstrap
Django -- but only for that one read-only lookup.

Source: https://www.euring.org/files/documents/ECPlacePipeDelimited_0.csv
"""

import argparse
import csv
import io
import os
import re
import sys
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django  # noqa: E402

django.setup()

from apps.core.models import Country  # noqa: E402

SOURCE_URL = "https://www.euring.org/files/documents/ECPlacePipeDelimited_0.csv"
DEFAULT_OUTPUT = REPO_ROOT / "apps" / "core" / "data" / "place_reference.csv"

CODE_RE = re.compile(r"^[A-Z0-9+\-]{4}$")

# EURING's country names don't match our ISO-code labels 1:1.
COUNTRY_NAME_ALIASES = {
    "czech republic": "CZE",
    "russian federation": "RUS",
    "united kingdom": "GBR",
    "macedonia": "MKD",
    "north macedonia": "MKD",
    "svalbard": "SJM",
    "jan mayen": "SJM",
    "the netherlands": "NLD",
    "republic of serbia": "SRB",
}


def read_source(source: str) -> bytes:
    if source.startswith("http://") or source.startswith("https://"):
        response = requests.get(source, timeout=60, headers={"User-Agent": "crbirding-sync/1.0"})
        if response.status_code != 200:
            raise SystemExit(f"Failed to fetch {source}: HTTP {response.status_code}")
        return response.content
    path = Path(source)
    if not path.exists():
        raise SystemExit(f"No such file: {path}")
    return path.read_bytes()


def parse_pipe_delimited(content: bytes, encoding: str) -> list[list[str]]:
    text = content.decode(encoding)
    reader = csv.reader(io.StringIO(text), delimiter="|")
    next(reader)  # header
    return [[field.strip() for field in row] for row in reader if any(f.strip() for f in row)]


def parse_row(fields: list[str]):
    """Find the place-code field by pattern rather than fixed position,
    since some rows have an extra embedded sub-region field that shifts
    everything after it (e.g. the Portuguese islands rows: Country,
    Region, "Azores", Code, Current, ...).
    """
    code_index = next((i for i, f in enumerate(fields) if i > 0 and CODE_RE.match(f)), None)
    if code_index is None or code_index == 0:
        return None

    country_name = fields[0]
    region = ", ".join(f for f in fields[1:code_index] if f)
    code = fields[code_index]

    remainder = fields[code_index + 1 :]
    current = next((f for f in remainder if f in ("Y", "N")), "")
    date_re = re.compile(r"^\d{1,2}/\d{1,2}/\d{2,4}$")
    notes = ", ".join(f for f in remainder if f not in ("Y", "N") and not date_re.match(f))

    return country_name, region, code, current, notes


def main():
    parser = argparse.ArgumentParser(description="Sync the place reference file from EURING.")
    parser.add_argument("--source", default=SOURCE_URL)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument(
        "--encoding",
        default="iso-8859-1",
        help=(
            "Encoding of the source file (default: iso-8859-1). EURING doesn't document "
            "one; iso-8859-1 never raises on any byte, which cp1252 can. Override here if "
            "a future EURING file needs something else."
        ),
    )
    options = parser.parse_args()

    content = read_source(options.source)
    raw_rows = parse_pipe_delimited(content, options.encoding)

    countries = list(Country.objects.all())
    country_names = {country.name.lower(): country.code for country in countries}
    country_names.update(COUNTRY_NAME_ALIASES)
    country_labels = {country.code: country.name for country in countries}

    by_code = {}
    dropped_duplicates = []
    unmatched_countries = []
    unparseable = []

    for row in raw_rows:
        parsed = parse_row(row)
        if parsed is None:
            unparseable.append(row)
            continue
        country_name, region, code, current, notes = parsed

        country_code = country_names.get(country_name.lower())
        if country_code is None:
            unmatched_countries.append((country_name, region, code))
            continue

        active = current == "Y"
        name = region or country_labels[country_code]

        existing = by_code.get(code)
        if existing is not None:
            # Same code reused for a different region after a boundary
            # change (e.g. CZ10). Keep whichever is Current=Y; if
            # both/neither are, keep the first seen and drop the rest.
            if active and not existing["active"]:
                dropped_duplicates.append((code, existing["name"], existing["notes"]))
                by_code[code] = {
                    "country_code": country_code, "active": active,
                    "name": name, "notes": notes,
                }
            else:
                dropped_duplicates.append((code, name, notes))
            continue

        by_code[code] = {
            "country_code": country_code, "active": active,
            "name": name, "notes": notes,
        }

    output_path = Path(options.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["place_code", "country_code", "active", "latin_name"])
        for code, data in sorted(by_code.items()):
            writer.writerow(
                [code, data["country_code"], "true" if data["active"] else "false", data["name"]]
            )

    print(
        f"{len(raw_rows)} source rows -> {len(by_code)} places written to {output_path}. "
        f"{len(unmatched_countries)} rows outside our Country list, "
        f"{len(dropped_duplicates)} duplicate-code rows dropped, "
        f"{len(unparseable)} rows couldn't be parsed."
    )

    if unmatched_countries or dropped_duplicates or unparseable:
        review_path = output_path.with_name(output_path.stem + "_review.csv")
        with review_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["reason", "detail"])
            for name, region, code in unmatched_countries:
                writer.writerow(["country not in Country list", f"{name} / {region} / {code}"])
            for code, name, notes in dropped_duplicates:
                writer.writerow(["duplicate place_code dropped", f"{code}: {name} ({notes})"])
            for row in unparseable:
                writer.writerow(["could not parse row", "|".join(row)])
        print(f"Details written to {review_path} for review.")


if __name__ == "__main__":
    sys.exit(main())
