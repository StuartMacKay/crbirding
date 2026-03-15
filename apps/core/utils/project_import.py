"""Bulk-importing Projects from a CSV file -- typically a short list of
ringing/colour-marking projects a maintainer already has on hand,
letting them be added in bulk rather than one at a time through the
admin.

CSV columns: name, coordinator, country, contact, submit, site,
description. name, coordinator, and country are required; the rest may
be blank. country accepts either its EURING code or its display label,
the same as core.utils.bulk_import's and core.utils.location_import's
own country columns.

Project.country is unique -- there's only ever one Project per country
on file -- so a row naming a country that already has one is skipped as
a duplicate rather than attempted, which would otherwise fail at the
database level. Re-running an import (an original file plus fixes for
the rows that failed, say) is therefore safe: rows for countries
already on file are simply skipped, and only genuinely new ones are
added.
"""

from django.db import transaction

from ..models import Project
from .csv_import import ImportReport, normalized_dict_reader, resolve_country

REQUIRED_COLUMNS = {"name", "coordinator", "country"}


def _import_row(row: dict) -> bool:
    """Create the Project for this row. Returns False, without creating
    anything, if a Project for the same country already exists.
    """
    name = row["name"].strip()
    if not name:
        raise ValueError("no name given")

    coordinator = row["coordinator"].strip()
    if not coordinator:
        raise ValueError("no coordinator given")

    country_code = resolve_country(row["country"])

    if Project.objects.filter(country=country_code).exists():
        return False

    Project.objects.create(
        name=name,
        coordinator=coordinator,
        country=country_code,
        contact=row.get("contact", "").strip(),
        submit=row.get("submit", "").strip(),
        site=row.get("site", "").strip(),
        description=row.get("description", "").strip(),
    )
    return True


def import_projects_csv(file) -> ImportReport:
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
