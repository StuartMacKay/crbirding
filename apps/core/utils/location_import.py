"""Bulk-importing Locations from a CSV file -- typically a spreadsheet
of established sites a project coordinator already tracks, letting them
be added in bulk rather than one at a time through the admin.

CSV columns: name, region, country, latitude, longitude, accuracy,
notes. name, region, country, latitude, and longitude are required;
accuracy and notes may be blank. region and country accept either
their EURING code or their display label, the same as
core.utils.bulk_import's Observation import -- country narrows which
region a name can mean, since region labels aren't unique across
countries (see core.utils.csv_import.resolve_region).

A row is matched against existing Locations the same way
core.utils.bulk_import resolves an Observation's location: by name
(case-insensitive, in the Latin alphabet) and region. A row matching
one already on file is skipped as a duplicate rather than creating a
second record for the same place; its coordinates are left untouched,
since re-running an import (an original file plus fixes, say)
shouldn't silently overwrite whatever accuracy is already on file. A
row matching more than one is rejected, the same as an ambiguous name
is for Observation import. A row matching none creates a new Location
from its own name, region, latitude, longitude, and accuracy.
"""

from django.conf import settings
from django.db import transaction

from ..models import Location
from .csv_import import (
    ImportReport,
    normalized_dict_reader,
    parse_decimal,
    parse_int,
    resolve_country,
    resolve_region,
)

REQUIRED_COLUMNS = {"name", "region", "country", "latitude", "longitude"}


def _import_row(row: dict) -> bool:
    """Create the Location for this row. Returns False, without
    creating anything, if a Location with the same name and region
    already exists.
    """
    name = row["name"].strip()
    if not name:
        raise ValueError("no name given")

    country_code = resolve_country(row["country"])
    region_code = resolve_region(row["region"], country_code)

    matches = list(Location.objects.filter(name__Latn__iexact=name, region=region_code))
    if len(matches) == 1:
        return False
    if len(matches) > 1:
        raise ValueError(f"{name!r} matches more than one location in that region")

    latitude = parse_decimal(row["latitude"].strip())
    longitude = parse_decimal(row["longitude"].strip())
    if latitude is None or longitude is None:
        raise ValueError("latitude and longitude are required")
    accuracy = parse_int(row.get("accuracy", "").strip())

    primary_alphabet = settings.ALPHABETS[0][0]
    Location.objects.create(
        name={primary_alphabet: name},
        region=region_code,
        latitude=latitude,
        longitude=longitude,
        accuracy=accuracy,
        notes=row.get("notes", "").strip(),
    )
    return True


def import_locations_csv(file) -> ImportReport:
    report = ImportReport()
    reader = normalized_dict_reader(file)

    missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
    if missing:
        report.errors.append(f"CSV is missing required columns: {', '.join(sorted(missing))}")
        return report

    for row_number, row in enumerate(reader, start=2):  # header is row 1
        try:
            with transaction.atomic():
                created = _import_row(row)
        except (ValueError, KeyError) as exc:
            report.errors.append(f"Row {row_number}: {exc}")
            report.skipped += 1
            continue
        if created:
            report.created += 1
        else:
            report.duplicates += 1

    return report
