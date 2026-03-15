import csv
import io

import pytest

from core.models import Rule
from core.utils.rule_export import export_rules_csv
from core.utils.rule_import import import_rules_csv

from .factories import ProjectFactory, RuleFactory


def _parse(csv_text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(csv_text)))


@pytest.mark.django_db
class TestRuleExport:
    def test_header_matches_the_importer(self):
        csv_text = export_rules_csv()
        header = csv_text.splitlines()[0]
        assert header == "species,position,regex,coordinator,project"

    def test_exports_a_rule(self):
        project = ProjectFactory(name="Gull Watch", coordinator="Jo Smith")
        RuleFactory(project=project, species="00010", position="LB", regex=r"^W\(.*\)$")

        rows = _parse(export_rules_csv())

        assert len(rows) == 1
        row = rows[0]
        assert row["species"] == "00010"
        assert row["position"] == "LB"
        assert row["regex"] == r"^W\(.*\)$"
        assert row["coordinator"] == "Jo Smith"
        assert row["project"] == "Gull Watch"

    def test_only_the_given_queryset_is_exported(self):
        included = RuleFactory(regex="^A$")
        RuleFactory(regex="^B$")

        rows = _parse(export_rules_csv(Rule.objects.filter(pk=included.pk)))

        assert [row["regex"] for row in rows] == ["^A$"]

    def test_round_trips_through_the_importer(self):
        RuleFactory()
        csv_text = export_rules_csv()

        report = import_rules_csv(io.BytesIO(csv_text.encode()))

        assert report.errors == []
        assert (report.created, report.duplicates) == (0, 1)
