"""Exporting Projects to a CSV file -- the mirror of
core.utils.project_import, writing the same columns that import reads.
Project.country is unique, and is what import matches an existing
Project by (see core.utils.project_import), so it -- not the internal
id -- is what a row identifies a Project by here too.

country is written as its own EURING code, not its display label --
unambiguous and locale-independent, unlike a label, which
core.utils.project_import also accepts on the way back in.
"""

from django.db.models import QuerySet

from ..models import Project
from .csv_export import write_csv

FIELDNAMES = ["name", "coordinator", "country", "contact", "submit", "site", "description"]


def _row(project: Project) -> dict:
    return {
        "name": project.name,
        "coordinator": project.coordinator,
        "country": project.country,
        "contact": project.contact,
        "submit": project.submit,
        "site": project.site,
        "description": project.description,
    }


def export_projects_csv(queryset: QuerySet[Project] | None = None) -> str:
    queryset = Project.objects.all() if queryset is None else queryset
    projects = queryset.order_by("country")
    return write_csv(FIELDNAMES, [_row(project) for project in projects])
