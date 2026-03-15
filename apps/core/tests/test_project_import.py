import io

import pytest

from core.models import Project
from core.utils.project_import import import_projects_csv

from .factories import ProjectFactory

COUNTRY = "United Kingdom"

HEADER = "name,coordinator,country,contact,submit,site,description"


def _csv(text: str) -> io.BytesIO:
    return io.BytesIO(text.encode())


def _rows(*row_overrides: dict) -> str:
    lines = [HEADER]
    for overrides in row_overrides:
        fields = {
            "name": "Test Project",
            "coordinator": "Jo Smith",
            "country": COUNTRY,
            "contact": "",
            "submit": "",
            "site": "",
            "description": "",
        }
        fields.update(overrides)
        lines.append(",".join(str(fields[column]) for column in HEADER.split(",")))
    return "\n".join(lines) + "\n"


def _row(**overrides) -> str:
    return _rows(overrides)


@pytest.mark.django_db
class TestColumnValidation:
    def test_missing_required_columns_reported(self):
        report = import_projects_csv(_csv("name,country\nSomewhere,GB--\n"))
        assert report.errors == ["CSV is missing required columns: coordinator"]
        assert report.created == 0

    def test_header_casing_and_whitespace_dont_hide_columns(self):
        csv_text = f"Name,Coordinator,Country \nTest Project,Jo Smith,{COUNTRY}\n"
        report = import_projects_csv(_csv(csv_text))
        assert report.errors == []
        assert report.created == 1


@pytest.mark.django_db
class TestProjectCreation:
    def test_creates_a_new_project(self):
        report = import_projects_csv(_csv(_row()))

        assert report.errors == []
        assert report.created == 1
        project = Project.objects.get()
        assert project.name == "Test Project"
        assert project.coordinator == "Jo Smith"
        assert project.country == "GB--"

    def test_resolved_by_euring_code(self):
        report = import_projects_csv(_csv(_row(country="GB--")))
        assert report.created == 1
        assert Project.objects.get().country == "GB--"

    def test_optional_fields_saved_when_present(self):
        report = import_projects_csv(
            _csv(
                _row(
                    contact="coordinator@example.com",
                    submit="https://example.com/submit",
                    site="https://example.com",
                    description="A description.",
                )
            )
        )

        assert report.errors == []
        project = Project.objects.get()
        assert project.contact == "coordinator@example.com"
        assert project.submit == "https://example.com/submit"
        assert project.site == "https://example.com"
        assert project.description == "A description."

    def test_blank_name_is_an_error(self):
        report = import_projects_csv(_csv(_row(name="")))
        assert report.skipped == 1
        assert "no name given" in report.errors[0]
        assert Project.objects.count() == 0

    def test_blank_coordinator_is_an_error(self):
        report = import_projects_csv(_csv(_row(coordinator="")))
        assert report.skipped == 1
        assert "no coordinator given" in report.errors[0]
        assert Project.objects.count() == 0

    def test_unknown_country_is_an_error(self):
        report = import_projects_csv(_csv(_row(country="Not a real country")))
        assert report.skipped == 1
        assert "no country matching" in report.errors[0]


@pytest.mark.django_db
class TestProjectMatching:
    def test_matching_country_is_a_duplicate(self):
        """Project.country is unique -- there's only ever one Project
        per country -- so a row for a country already on file is
        skipped rather than attempted, which would otherwise fail at
        the database level.
        """
        project = ProjectFactory(country="GB--")

        report = import_projects_csv(_csv(_row(country=COUNTRY)))

        assert (report.created, report.duplicates) == (0, 1)
        assert Project.objects.get().pk == project.pk

    def test_different_countries_both_import(self):
        report = import_projects_csv(
            _csv(_rows({"country": COUNTRY}, {"country": "France", "name": "Projet Test"}))
        )

        assert (report.created, report.duplicates) == (2, 0)
        assert set(Project.objects.values_list("country", flat=True)) == {"GB--", "FR--"}


@pytest.mark.django_db
class TestIdempotency:
    def test_rerunning_the_same_file_reports_duplicates_not_new_rows(self):
        csv_text = _row(country=COUNTRY)
        first = import_projects_csv(_csv(csv_text))
        assert (first.created, first.duplicates) == (1, 0)

        second = import_projects_csv(_csv(csv_text))
        assert (second.created, second.duplicates) == (0, 1)
        assert Project.objects.count() == 1
