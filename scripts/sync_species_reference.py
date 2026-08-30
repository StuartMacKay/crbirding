#!/usr/bin/env python3
"""Build the maintainer-curated species reference file.

Cross-references the EURING species code list with the IOC World Bird
List's multilingual names file, by scientific name, and writes a single
tidy CSV (euring_code, scientific_name, language_code, common_name) to
apps/core/data/species_reference.csv. Run by project maintainers
occasionally (e.g. when EURING or IOC publish an update) -- part of the
release process, not something an end user or deployer runs. Doesn't
touch the database, so it's a plain script rather than a Django
management command: nothing here needs the app registry or the ORM, and
the release-prep step doesn't need to survive a port to another
language.

Sources:
    EURING species codes: https://euring.org/files/documents/EURING_SpeciesCodes_IOC15_1_2.csv
    IOC multilingual names: https://worldbirdnames.org/Multiling%20IOC%2015.2.xlsx
        (IOC World Bird List, CC BY 3.0 -- cite as "IOC World Bird List
        v15.2 by Frank Gill, David Donsker & Pamela Rasmussen (Eds)"
        when redistributing data derived from it.)
"""

import argparse
import csv
import io
import sys
from pathlib import Path

import openpyxl
import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
EURING_URL = "https://euring.org/files/documents/EURING_SpeciesCodes_IOC15_1_2.csv"
IOC_URL = "https://worldbirdnames.org/Multiling%20IOC%2015.2.xlsx"
DEFAULT_OUTPUT = REPO_ROOT / "apps" / "core" / "data" / "species_reference.csv"

# IOC column name -> ISO 639-1 code, restricted to languages relevant to
# the countries in apps.core.data.countries_reference.csv. A handful of
# national languages (Albanian, Bosnian, Maltese, Irish, Welsh,
# Luxembourgish, Faroese) aren't in the IOC file and are simply absent
# here.
IOC_LANGUAGE_COLUMNS = {
    "English": "en",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Italian": "it",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Norwegian": "no",
    "Polish": "pl",
    "Portuguese (Portuguese)": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swedish": "sv",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Belarusian": "be",
    "Bulgarian": "bg",
    "Macedonian": "mk",
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


def parse_euring(content: bytes) -> dict[str, tuple[str, str]]:
    """Return {scientific_name: (euring_code, english_name)} for current species."""
    text = content.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    required = {"Status", "EURING_Code", "Current_Name", "English_Name"}
    missing = required - set(reader.fieldnames or [])
    if missing:
        raise SystemExit(f"EURING CSV is missing expected columns: {', '.join(sorted(missing))}")

    result = {}
    for row in reader:
        if (row.get("Status") or "").strip() != "sp":
            continue
        code = (row.get("EURING_Code") or "").strip()
        scientific_name = (row.get("Current_Name") or "").strip()
        english_name = (row.get("English_Name") or "").strip()
        if english_name == "NA":
            english_name = ""
        if not code or not scientific_name:
            continue
        result[scientific_name] = (code, english_name)
    return result


def parse_ioc(content: bytes) -> dict[str, dict[str, str]]:
    """Return {scientific_name: {language_code: common_name}}."""
    workbook = openpyxl.load_workbook(io.BytesIO(content), read_only=True, data_only=True)
    worksheet = workbook["List"]
    rows = worksheet.iter_rows(values_only=True)
    header = next(rows)
    column_index = {name: index for index, name in enumerate(header)}

    if "IOC_15.2" not in column_index:
        raise SystemExit("IOC file is missing the expected 'IOC_15.2' scientific name column.")

    scientific_name_index = column_index["IOC_15.2"]
    language_indices = {
        language_code: column_index[column_name]
        for column_name, language_code in IOC_LANGUAGE_COLUMNS.items()
        if column_name in column_index
    }

    result = {}
    for row in rows:
        scientific_name = row[scientific_name_index]
        if not scientific_name:
            continue
        names = {}
        for language_code, index in language_indices.items():
            value = row[index]
            if value:
                names[language_code] = str(value).strip()
        if names:
            result[str(scientific_name).strip()] = names
    return result


def main():
    parser = argparse.ArgumentParser(description="Sync the species reference file from EURING/IOC.")
    parser.add_argument("--euring-source", default=EURING_URL)
    parser.add_argument("--ioc-source", default=IOC_URL)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    options = parser.parse_args()

    euring = parse_euring(read_source(options.euring_source))
    ioc = parse_ioc(read_source(options.ioc_source))

    rows_out = []
    unmatched = []
    matched = 0

    for scientific_name, (code, english_name) in euring.items():
        names = ioc.get(scientific_name)
        if names is None:
            unmatched.append((code, scientific_name))
            if english_name:
                rows_out.append((code, scientific_name, "en", english_name))
            continue
        matched += 1
        for language_code, common_name in names.items():
            rows_out.append((code, scientific_name, language_code, common_name))

    rows_out.sort(key=lambda row: (row[0], row[2]))

    output_path = Path(options.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["euring_code", "scientific_name", "language_code", "common_name"])
        writer.writerows(rows_out)

    print(
        f"{len(euring)} EURING species considered; {matched} matched an IOC entry, "
        f"{len(unmatched)} did not. {len(rows_out)} name rows written to {output_path}."
    )

    if unmatched:
        unmatched_path = output_path.with_name(output_path.stem + "_unmatched.csv")
        with unmatched_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["euring_code", "scientific_name"])
            writer.writerows(unmatched)
        print(
            f"{len(unmatched)} EURING species had no IOC name match (only EURING's own "
            f"English name, if any, was used) -- see {unmatched_path} for review."
        )


if __name__ == "__main__":
    sys.exit(main())
