"""Bulk-importing Rules from a CSV file -- typically a batch of colour-
mark patterns a maintainer has already worked out for one or more
projects, letting them be added in bulk rather than one at a time
through the admin.

CSV columns: species, position, regex, coordinator, project. species,
position, and regex are required; coordinator and project are each
optional, but at least one of the two must be given per row, to
identify which Project the rule belongs to -- see _resolve_project.
species and position accept either their EURING code or their display
label, the same as core.utils.bulk_import's own species/position-shaped
columns.

If both coordinator and project are given, the match must satisfy both
-- useful as a check against typos, since a row naming a coordinator
and project that don't actually belong to the same Project is rejected
as no match, rather than silently picking one over the other.

A row matching an existing Rule's species, position, regex, and
project exactly is skipped as a duplicate, so re-running an import (an
original file plus fixes for the rows that failed, say) is safe.
"""

import re

from django.db import transaction

from ..models import Position, Project, Rule
from .csv_import import ImportReport, normalized_dict_reader, resolve_choice, resolve_species

REQUIRED_COLUMNS = {"species", "position", "regex"}


def _resolve_project(row: dict) -> Project:
    """The Project identified by this row's `coordinator` and/or
    `project` column -- at least one must be given; if both are, the
    match must satisfy both.
    """
    coordinator = row.get("coordinator", "").strip()
    name = row.get("project", "").strip()
    if not coordinator and not name:
        raise ValueError("no coordinator or project given")

    filters = {}
    if coordinator:
        filters["coordinator__iexact"] = coordinator
    if name:
        filters["name__iexact"] = name

    described = " and ".join(
        part
        for part in (
            f"coordinator {coordinator!r}" if coordinator else "",
            f"project {name!r}" if name else "",
        )
        if part
    )

    matches = list(Project.objects.filter(**filters))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise ValueError(f"more than one project matches {described}")
    raise ValueError(f"no project matching {described}")


def _resolve_regex(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("no regex given")
    try:
        re.compile(value)
    except re.error as exc:
        raise ValueError(f"{value!r} is not a valid regular expression: {exc}") from None
    return value


def _import_row(row: dict) -> bool:
    """Create the Rule for this row. Returns False, without creating
    anything, if an identical one already exists.
    """
    species = resolve_species(row["species"])
    position = resolve_choice(row["position"], Position, "position")
    regex = _resolve_regex(row["regex"])
    project = _resolve_project(row)

    if Rule.objects.filter(
        species=species, position=position, regex=regex, project=project
    ).exists():
        return False

    Rule.objects.create(species=species, position=position, regex=regex, project=project)
    return True


def import_rules_csv(file) -> ImportReport:
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
