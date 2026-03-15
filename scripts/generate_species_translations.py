#!/usr/bin/env python3
"""Populate common-name translations for every Species label straight
into the project's gettext .po catalogs, from IOC's own multilingual
names spreadsheet -- so a translation exists for every supported
language without a human translator ever typing one in by hand.

Species' English common names (the msgids -- see
scripts/generate_species_choices.py) come from EURING's own species
list; IOC's multilingual file is a separate publication with its own
row order and its own (incompatible) numeric IDs, so the two are joined
here by scientific name instead, which is stable across both.

The source file is IOC's "Multiling IOC" spreadsheet (.xlsx) -- parsed
directly as a zip of OOXML/SpreadsheetML XML via the stdlib rather than
a library like openpyxl, which this project deliberately doesn't
depend on. Only the "List" sheet's header row (language names) and
data rows (scientific name + one column per language) are read.

Language columns are matched to Django locale codes via Django's own
LANGUAGES list (matching by English language name), with a handful of
manual overrides where IOC's column name doesn't match Django's name
exactly (e.g. splitting "Chinese"/"Chinese (Traditional)" into
zh-hans/zh-hant) or Django has no code for it at all (skipped).

For each resulting language: runs `makemessages` to (re)generate that
locale's django.po with every msgid currently in use across the app,
fills in a msgstr for every Species label IOC has a translation for
using polib, then runs `compilemessages`. Existing translations for
anything else (a non-species string) are left exactly as they were.

Run by project maintainers occasionally (when EURING or IOC publish an
update) -- not by individual deployers or end users. Requires GNU
gettext (xgettext/msguniq/msgfmt) to be installed, same as any other
use of Django's makemessages/compilemessages.

Source: https://www.worldbirdnames.org/new/ioc-lists/multilingual/
"""

import argparse
import csv
import io
import os
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

REPO_ROOT = Path(__file__).resolve().parent.parent
SPECIES_SOURCE_URL = "https://euring.org/files/documents/EURING_SpeciesCodes_IOC15_1_2.csv"
LOCALE_DIR = REPO_ROOT / "apps" / "core" / "locale"

INCLUDED_STATUSES = {"sp", "a", "h", "f"}

XLSX_NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

# IOC column name -> Django locale code, for columns Django's own
# LANGUAGES list can't resolve by name alone (see main()).
LANGUAGE_CODE_OVERRIDES = {
    "Chinese": "zh-hans",
    "Chinese (Traditional)": "zh-hant",
    "Norwegian": "nb",
    "Portuguese (Lusophone)": "pt-br",
    "Portuguese (Portuguese)": "pt",
}
# IOC columns with no usable Django locale at all.
LANGUAGE_COLUMNS_SKIPPED = {"French (Gaudin)", "Northern Sami"}


def read_bytes(source: str) -> bytes:
    if source.startswith("http://") or source.startswith("https://"):
        import urllib.request

        request = urllib.request.Request(source, headers={"User-Agent": "crbirding-sync/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            if response.status != 200:
                raise SystemExit(f"Failed to fetch {source}: HTTP {response.status}")
            return response.read()
    path = Path(source)
    if not path.exists():
        raise SystemExit(f"No such file: {path}")
    return path.read_bytes()


def species_common_names(species_csv_source: str) -> dict[str, tuple[str, str]]:
    """{scientific_name: (euring_code, english_label)} for every
    species with a real EURING-supplied English common name -- the
    msgid these translations must match.
    """
    text = read_bytes(species_csv_source).decode("utf-8-sig")
    result = {}
    for row in csv.DictReader(io.StringIO(text)):
        if row["Status"] not in INCLUDED_STATUSES:
            continue
        english_name = row["English_Name"]
        if english_name and english_name != "NA":
            result[row["Current_Name"]] = (row["EURING_Code"], english_name)
    return result


def read_ioc_sheet(xlsx_source: str) -> tuple[list[str], dict[str, list[str]]]:
    """(header row, {scientific_name: row cells}) from the xlsx's "List" sheet."""
    with zipfile.ZipFile(io.BytesIO(read_bytes(xlsx_source))) as archive:
        shared_root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
        shared_strings = [
            "".join(t.text or "" for t in si.findall(".//m:t", XLSX_NS))
            for si in shared_root.findall("m:si", XLSX_NS)
        ]
        sheet_root = ElementTree.fromstring(archive.read("xl/worksheets/sheet1.xml"))

    def cell_value(cell) -> str:
        value = cell.find("m:v", XLSX_NS)
        if value is None:
            return ""
        if cell.get("t") == "s":
            return shared_strings[int(value.text)]
        return value.text or ""

    rows = sheet_root.findall(".//m:sheetData/m:row", XLSX_NS)
    header = [cell_value(c) for c in rows[0].findall("m:c", XLSX_NS)]
    sci_index = header.index("IOC_15.2")

    by_scientific_name = {}
    for row in rows[1:]:
        values = [cell_value(c) for c in row.findall("m:c", XLSX_NS)]
        if len(values) <= sci_index:
            continue
        by_scientific_name[values[sci_index]] = values

    return header, by_scientific_name


def language_codes_for_columns(header: list[str]) -> dict[str, str]:
    """{column_name: django_locale_code} for every language column IOC
    provides that Django also has a locale code for.
    """
    from django.conf import global_settings

    names_to_codes = {name.lower(): code for code, name in global_settings.LANGUAGES}

    codes = {}
    non_language_columns = {"seq", "Order", "Family", "IOC_15.2", "English"}
    for column in header:
        if column in non_language_columns or column in LANGUAGE_COLUMNS_SKIPPED:
            continue
        code = LANGUAGE_CODE_OVERRIDES.get(column) or names_to_codes.get(column.lower())
        if code:
            codes[column] = code
        else:
            print(f"warning: no Django locale for IOC column {column!r}; skipping", file=sys.stderr)
    return codes


def run_django_admin(*args: str) -> None:
    """Runs manage.py from apps/core, not the repo root -- core is the
    only app with its own locale/ directory, and makemessages refuses
    to run over source files it can't find one for (apps/autocomplete,
    apps/users).
    """
    env = {**os.environ, "DJANGO_SETTINGS_MODULE": "config.settings"}
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "manage.py"), *args],
        cwd=REPO_ROOT / "apps" / "core",
        env=env,
        check=True,
    )


def update_locale(code: str, translations: dict[str, str]) -> int:
    """(Re)generate `code`'s django.po (picking up any new/changed
    msgids across the app) and fill in a msgstr for every Species label
    in `translations`, leaving every other entry untouched. Returns how
    many entries were filled in.
    """
    import polib
    from django.utils.translation import to_locale

    # makemessages/compilemessages and the locale/ directory itself use
    # Unix locale naming (e.g. "pt_BR"), not the hyphenated form Django's
    # LANGUAGES/translation.override use ("pt-br") -- to_locale() converts.
    locale_name = to_locale(code)

    run_django_admin("makemessages", "--locale", locale_name, "--no-obsolete")

    po_path = LOCALE_DIR / locale_name / "LC_MESSAGES" / "django.po"
    catalog = polib.pofile(str(po_path))

    filled = 0
    for entry in catalog:
        translation = translations.get(entry.msgid)
        if translation:
            entry.msgstr = translation
            filled += 1
    catalog.save()

    run_django_admin("compilemessages", "--locale", locale_name)
    return filled


def main():
    parser = argparse.ArgumentParser(
        description="Fill in Species label translations from IOC's multilingual names file."
    )
    parser.add_argument("--species-source", default=SPECIES_SOURCE_URL)
    parser.add_argument("ioc_xlsx", help="Path (or URL) to IOC's 'Multiling IOC' .xlsx file")
    options = parser.parse_args()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    sys.path.insert(0, str(REPO_ROOT))
    sys.path.insert(0, str(REPO_ROOT / "apps"))
    import django

    django.setup()

    common_names = species_common_names(options.species_source)
    header, ioc_rows = read_ioc_sheet(options.ioc_xlsx)
    language_codes = language_codes_for_columns(header)

    for column, code in sorted(language_codes.items(), key=lambda pair: pair[1]):
        column_index = header.index(column)
        translations = {}
        for scientific_name, (_euring_code, english_label) in common_names.items():
            ioc_row = ioc_rows.get(scientific_name)
            if ioc_row is None or len(ioc_row) <= column_index:
                continue
            translated = ioc_row[column_index]
            if translated:
                translations[english_label] = translated

        filled = update_locale(code, translations)
        print(f"{code} ({column}): {filled} species translations filled in.")


if __name__ == "__main__":
    sys.exit(main())
