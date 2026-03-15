"""Exporting Rules to a CSV file -- the mirror of
core.utils.rule_import, writing the same columns that import reads. A
Rule's project is identified there by coordinator and/or project name
(see core.utils.rule_import._resolve_project), not by its internal id,
so a row here gives both -- not the id -- which is enough to resolve
the same Project unambiguously on the way back in, even where
coordinator or name alone might not be.

species and position are written as their own EURING codes, not their
display label -- unambiguous and locale-independent, unlike a label,
which core.utils.rule_import also accepts on the way back in.
"""

from django.db.models import QuerySet

from ..models import Rule
from .csv_export import write_csv

FIELDNAMES = ["species", "position", "regex", "coordinator", "project"]


def _row(rule: Rule) -> dict:
    return {
        "species": rule.species,
        "position": rule.position,
        "regex": rule.regex,
        "coordinator": rule.project.coordinator,
        "project": rule.project.name,
    }


def export_rules_csv(queryset: QuerySet[Rule] | None = None) -> str:
    queryset = Rule.objects.all() if queryset is None else queryset
    rules = queryset.select_related("project").order_by("project__country", "species", "position")
    return write_csv(FIELDNAMES, [_row(rule) for rule in rules])
