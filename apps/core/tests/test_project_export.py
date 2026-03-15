import csv
import io

import pytest

from core.models import Project
from core.utils.project_export import export_projects_csv
from core.utils.project_import import import_projects_csv

from .factories import ProjectFactory


def _parse(csv_text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(csv_text)))


@pytest.mark.django_db
class TestProjectExport:
    def test_header_matches_the_importer(self):
        csv_text = export_projects_csv()
        header = csv_text.splitlines()[0]
        assert header == "name,coordinator,country,contact,submit,site,description"

    def test_exports_a_project(self):
        ProjectFactory(
            name="Gull Watch",
            coordinator="Jo Smith",
            country="GB--",
            contact="coordinator@example.com",
            submit="https://example.com/submit",
            site="https://example.com",
            description="A description.",
        )

        rows = _parse(export_projects_csv())

        assert len(rows) == 1
        row = rows[0]
        assert row["name"] == "Gull Watch"
        assert row["coordinator"] == "Jo Smith"
        assert row["country"] == "GB--"
        assert row["contact"] == "coordinator@example.com"
        assert row["submit"] == "https://example.com/submit"
        assert row["site"] == "https://example.com"
        assert row["description"] == "A description."

    def test_only_the_given_queryset_is_exported(self):
        ProjectFactory(name="Included", country="GB--")
        ProjectFactory(name="Excluded", country="FR--")

        rows = _parse(export_projects_csv(Project.objects.filter(name="Included")))

        assert [row["name"] for row in rows] == ["Included"]

    def test_round_trips_through_the_importer(self):
        ProjectFactory(name="Gull Watch", coordinator="Jo Smith", country="GB--")
        csv_text = export_projects_csv()

        report = import_projects_csv(io.BytesIO(csv_text.encode()))

        assert report.errors == []
        assert (report.created, report.duplicates) == (0, 1)
