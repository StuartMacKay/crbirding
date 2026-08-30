"""Bulk-importing a user's own historical Resighting records from a CSV
file they provide.

Distinct from apps.core.reference_data, which imports from the
maintainer-curated EURING/IOC reference files bundled with the app --
this is a one-off personal data migration, not an ongoing sync. Species
and Location are assumed to already exist (see apps.core.reference_data
and the admin for creating them); this never creates either.

CSV columns: species (EURING code), location (numeric id), date,
time, latitude, longitude, accuracy, notes, tags. Only species,
location, date, and tags are required; the rest may be blank. tags
uses the same compact notation Tag display uses (see
apps.core.formatting.parse_tags) -- e.g. "LB:WB(A123)u;RB:O,Y".
"""

import csv
import datetime
import io
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation

from django.db import transaction

from .formatting import parse_tags
from .models import Location, Observer, Resighting, Species, Tag

REQUIRED_COLUMNS = {"species", "location", "date", "tags"}


@dataclass
class ImportReport:
    created: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


def _parse_date(value: str) -> datetime.date:
    return datetime.date.fromisoformat(value)


def _parse_time(value: str) -> datetime.time | None:
    return datetime.time.fromisoformat(value) if value else None


def _parse_decimal(value: str) -> Decimal | None:
    if not value:
        return None
    try:
        return Decimal(value)
    except InvalidOperation:
        raise ValueError(f"{value!r} is not a valid coordinate") from None


def _parse_int(value: str) -> int | None:
    return int(value) if value else None


def _import_row(row: dict, observer: Observer) -> None:
    species_code = row["species"].strip()
    try:
        species = Species.objects.get(code=species_code)
    except Species.DoesNotExist:
        raise ValueError(f"no species with code {species_code!r}") from None

    location_id = row["location"].strip()
    try:
        location = Location.objects.get(pk=int(location_id))
    except (Location.DoesNotExist, ValueError):
        raise ValueError(f"no location with id {location_id!r}") from None

    tag_specs = parse_tags(row["tags"])
    if not tag_specs:
        raise ValueError("no tags given")

    resighting = Resighting.objects.create(
        species=species,
        location=location,
        date=_parse_date(row["date"].strip()),
        time=_parse_time(row.get("time", "").strip()),
        latitude=_parse_decimal(row.get("latitude", "").strip()),
        longitude=_parse_decimal(row.get("longitude", "").strip()),
        accuracy=_parse_int(row.get("accuracy", "").strip()),
        notes=row.get("notes", "").strip(),
        observer=observer,
    )
    Tag.objects.bulk_create(Tag(resighting=resighting, **spec) for spec in tag_specs)


def import_resightings_csv(file, observer: Observer) -> ImportReport:
    report = ImportReport()
    text = file.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))

    missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
    if missing:
        report.errors.append(f"CSV is missing required columns: {', '.join(sorted(missing))}")
        return report

    for row_number, row in enumerate(reader, start=2):  # header is row 1
        try:
            with transaction.atomic():
                _import_row(row, observer)
        except (ValueError, KeyError) as exc:
            report.errors.append(f"Row {row_number}: {exc}")
            report.skipped += 1
            continue
        report.created += 1

    return report
