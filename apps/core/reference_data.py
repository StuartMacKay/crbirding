"""Import Country, Place, and Species records from the maintainer-curated
reference CSVs in apps/core/data/.

Deliberately plain functions, not Django management commands: these are
called from the "import from reference data" admin views (see
apps/core/admin/reference_import.py) so an end user can pull in exactly
the records they need without preloading everything, and being ordinary
functions rather than management commands means the same logic could be
reimplemented as a Go handler without dragging Django's command
machinery along with it.

The CSVs themselves are built by scripts/sync_place_reference.py and
scripts/sync_species_reference.py, occasionally, by a maintainer -- not
by anything here.
"""

import csv
from dataclasses import dataclass, field
from pathlib import Path

from django.apps import apps
from django.db.models import Count

from .models import Capture, Country, Place, Resighting, Species, SpeciesName
from .models.script import Script

DATA_DIR = Path(apps.get_app_config("core").path) / "data"
COUNTRIES_CSV = DATA_DIR / "countries_reference.csv"
PLACES_CSV = DATA_DIR / "place_reference.csv"
PLACE_TRANSLATIONS_CSV = DATA_DIR / "place_translations.csv"
SPECIES_CSV = DATA_DIR / "species_reference.csv"

# place_translations.csv column -> Script code. latin_name lives in
# place_reference.csv instead, since that's the one script EURING's own
# data can supply.
PLACE_TRANSLATION_COLUMNS = {
    "greek_name": Script.GREEK,
    "cyrillic_name": Script.CYRILLIC,
    "armenian_name": Script.ARMENIAN,
    "georgian_name": Script.GEORGIAN,
    "arabic_name": Script.ARABIC,
    "hebrew_name": Script.HEBREW,
}


@dataclass
class ImportResult:
    created: int = 0
    updated: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# --- Country ---------------------------------------------------------------


def find_countries(query: str, limit: int = 20) -> list[dict]:
    query = query.strip().lower()
    if not query:
        return []
    matches = [
        row
        for row in _read_csv(COUNTRIES_CSV)
        if query in row["name"].lower() or query in row["code"].lower()
    ]
    return matches[:limit]


def import_country(code: str) -> Country:
    row = next((r for r in _read_csv(COUNTRIES_CSV) if r["code"] == code), None)
    if row is None:
        raise LookupError(f"No country with code {code!r} in the reference file.")
    country, _ = Country.objects.update_or_create(code=row["code"], defaults={"name": row["name"]})
    return country


def import_all_countries() -> ImportResult:
    result = ImportResult()
    for row in _read_csv(COUNTRIES_CSV):
        code, name = row["code"].strip(), row["name"].strip()
        if not code or not name:
            result.skipped += 1
            continue
        _, created = Country.objects.update_or_create(code=code, defaults={"name": name})
        result.created += created
        result.updated += not created
    return result


# --- Place -------------------------------------------------------------


def _place_translations() -> dict[str, dict[str, str]]:
    """{place_code: {script_code: name}}, non-empty columns only."""
    translations = {}
    for row in _read_csv(PLACE_TRANSLATIONS_CSV):
        names = {
            script: row[column].strip()
            for column, script in PLACE_TRANSLATION_COLUMNS.items()
            if row.get(column, "").strip()
        }
        if names:
            translations[row["place_code"].strip()] = names
    return translations


def _active_place_rows() -> list[dict]:
    return [row for row in _read_csv(PLACES_CSV) if row["active"].strip().lower() == "true"]


def find_places(query: str, limit: int = 20) -> list[dict]:
    query = query.strip().lower()
    if not query:
        return []
    matches = [
        row
        for row in _active_place_rows()
        if query in row["latin_name"].lower() or query in row["place_code"].lower()
    ]
    return matches[:limit]


def _upsert_place(row: dict, translations: dict[str, dict[str, str]]) -> tuple[Place, bool]:
    code = row["place_code"].strip()
    try:
        country = Country.objects.get(code=row["country_code"].strip())
    except Country.DoesNotExist as exc:
        raise LookupError(
            f"Place {code}: country {row['country_code']!r} isn't loaded -- import it first."
        ) from exc

    name_updates = {Script.LATIN: row["latin_name"].strip()} | translations.get(code, {})

    place, created = Place.objects.get_or_create(
        code=code, defaults={"country": country, "active": True, "name": name_updates}
    )
    if not created:
        place.country = country
        place.active = True
        place.name = {**place.name, **name_updates}
        place.save()
    return place, created


def import_place(place_code: str) -> Place:
    row = next((r for r in _active_place_rows() if r["place_code"] == place_code), None)
    if row is None:
        raise LookupError(f"No active place with code {place_code!r} in the reference file.")
    place, _ = _upsert_place(row, _place_translations())
    return place


def import_all_places() -> ImportResult:
    result = ImportResult()
    translations = _place_translations()
    for row in _active_place_rows():
        if not row["place_code"].strip() or not row["country_code"].strip():
            result.skipped += 1
            continue
        try:
            _, created = _upsert_place(row, translations)
        except LookupError as exc:
            result.errors.append(str(exc))
            result.skipped += 1
            continue
        result.created += created
        result.updated += not created
    return result


# --- Species -------------------------------------------------------------


def _species_index() -> tuple[dict[str, list[dict]], dict[str, set[str]]]:
    rows_by_code: dict[str, list[dict]] = {}
    codes_by_name: dict[str, set[str]] = {}
    for row in _read_csv(SPECIES_CSV):
        code = row["euring_code"]
        rows_by_code.setdefault(code, []).append(row)
        codes_by_name.setdefault(row["scientific_name"].strip().lower(), set()).add(code)
        codes_by_name.setdefault(row["common_name"].strip().lower(), set()).add(code)
    return rows_by_code, codes_by_name


def find_species(query: str, limit: int = 20) -> list[dict]:
    """One representative row (English name, if available) per matching species."""
    query = query.strip().lower()
    if not query:
        return []
    rows_by_code, _ = _species_index()
    matches = []
    for code, rows in rows_by_code.items():
        english_row = next((r for r in rows if r["language_code"] == "en"), rows[0])
        if query in code.lower() or query in rows[0]["scientific_name"].lower() or any(
            query in r["common_name"].lower() for r in rows
        ):
            matches.append(english_row)
        if len(matches) >= limit:
            break
    return matches


def import_species(identifier: str) -> Species:
    rows_by_code, codes_by_name = _species_index()
    key = identifier.strip()
    codes = {key} if key in rows_by_code else codes_by_name.get(key.lower(), set())

    if not codes:
        raise LookupError(f"No match for {identifier!r}.")
    if len(codes) > 1:
        raise LookupError(f"{identifier!r} matches more than one species; use the EURING code.")

    code = codes.pop()
    return _upsert_species(code, rows_by_code[code])


def _upsert_species(code: str, rows: list[dict]) -> Species:
    scientific_name = rows[0]["scientific_name"]
    species, _ = Species.objects.update_or_create(
        code=code, defaults={"scientific_name": scientific_name}
    )
    for row in rows:
        SpeciesName.objects.update_or_create(
            species=species,
            language_code=row["language_code"],
            defaults={"common_name": row["common_name"]},
        )
    return species


def import_all_species() -> ImportResult:
    result = ImportResult()
    rows_by_code, _ = _species_index()
    for code, rows in rows_by_code.items():
        if not code or not rows[0]["scientific_name"].strip():
            result.skipped += 1
            continue
        species = Species.objects.filter(code=code).first()
        _upsert_species(code, rows)
        result.created += species is None
        result.updated += species is not None
    return result


def backfill_missing_species_names() -> ImportResult:
    """Species already referenced by a Capture/Resighting but with no
    SpeciesName rows yet -- e.g. one created by hand via the admin.
    """
    result = ImportResult()
    used_ids = set(Capture.objects.values_list("species_id", flat=True)) | set(
        Resighting.objects.values_list("species_id", flat=True)
    )
    missing_codes = (
        Species.objects.filter(id__in=used_ids)
        .annotate(name_count=Count("names"))
        .filter(name_count=0)
        .values_list("code", flat=True)
    )
    rows_by_code, _ = _species_index()
    for code in missing_codes:
        rows = rows_by_code.get(code)
        if rows is None:
            result.errors.append(f"{code}: not found in reference file.")
            result.skipped += 1
            continue
        _upsert_species(code, rows)
        result.updated += 1
    return result
