import io

import pytest

from core.models import Rule, Species
from core.utils.rule_import import import_rules_csv

from .factories import ProjectFactory

SPECIES_CODE = Species.COMMON_OSTRICH
SPECIES_NAME = "Struthio camelus"

HEADER = "species,position,regex,coordinator,project"


def _csv(text: str) -> io.BytesIO:
    return io.BytesIO(text.encode())


def _rows(default_project, *row_overrides: dict) -> str:
    lines = [HEADER]
    for overrides in row_overrides:
        fields = {
            "species": SPECIES_CODE,
            "position": "Left Below",
            "regex": r"^W\(.*\)$",
            "coordinator": default_project.coordinator,
            "project": "",
        }
        fields.update(overrides)
        lines.append(",".join(str(fields[column]) for column in HEADER.split(",")))
    return "\n".join(lines) + "\n"


def _row(default_project, **overrides) -> str:
    return _rows(default_project, overrides)


@pytest.mark.django_db
class TestColumnValidation:
    def test_missing_required_columns_reported(self):
        report = import_rules_csv(_csv("species,position\n00010,LB\n"))
        assert report.errors == ["CSV is missing required columns: regex"]
        assert report.created == 0

    def test_header_casing_and_whitespace_dont_hide_columns(self):
        project = ProjectFactory()
        csv_text = (
            f"Species,Position ,Regex,Coordinator\n"
            f"{SPECIES_CODE},LB,^W\\(.*\\)$,{project.coordinator}\n"
        )
        report = import_rules_csv(_csv(csv_text))
        assert report.errors == []
        assert report.created == 1


@pytest.mark.django_db
class TestRuleCreation:
    def test_creates_a_new_rule(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project)))

        assert report.errors == []
        assert report.created == 1
        rule = Rule.objects.get()
        assert rule.species == SPECIES_CODE
        assert rule.position == "LB"
        assert rule.regex == r"^W\(.*\)$"
        assert rule.project == project

    def test_species_resolved_by_scientific_name(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, species=SPECIES_NAME)))
        assert report.created == 1
        assert Rule.objects.get().species == SPECIES_CODE

    def test_position_resolved_by_euring_code(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, position="RW")))
        assert report.created == 1
        assert Rule.objects.get().position == "RW"

    def test_unknown_species_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, species="Not a real bird")))
        assert report.skipped == 1
        assert "no species matching" in report.errors[0]

    def test_unknown_position_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, position="Not a real position")))
        assert report.skipped == 1
        assert "no position matching" in report.errors[0]

    def test_blank_regex_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, regex="")))
        assert report.skipped == 1
        assert "no regex given" in report.errors[0]

    def test_invalid_regex_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, regex="^W(unclosed")))
        assert report.skipped == 1
        assert "not a valid regular expression" in report.errors[0]


@pytest.mark.django_db
class TestProjectResolution:
    def test_resolved_by_coordinator(self):
        project = ProjectFactory(coordinator="Jo Smith")
        report = import_rules_csv(_csv(_row(project, coordinator="Jo Smith", project="")))
        assert report.created == 1
        assert Rule.objects.get().project == project

    def test_resolved_by_project_name(self):
        project = ProjectFactory(name="Gull Watch")
        report = import_rules_csv(_csv(_row(project, coordinator="", project="Gull Watch")))
        assert report.created == 1
        assert Rule.objects.get().project == project

    def test_resolved_by_both_when_consistent(self):
        project = ProjectFactory(coordinator="Jo Smith", name="Gull Watch")
        report = import_rules_csv(_csv(_row(project, coordinator="Jo Smith", project="Gull Watch")))
        assert report.created == 1
        assert Rule.objects.get().project == project

    def test_mismatched_coordinator_and_project_is_an_error(self):
        ProjectFactory(coordinator="Jo Smith", name="Gull Watch")
        other_project = ProjectFactory(coordinator="Other Person", name="Tern Watch")
        report = import_rules_csv(
            _csv(_row(other_project, coordinator="Jo Smith", project="Tern Watch"))
        )
        assert report.skipped == 1
        assert "no project matching" in report.errors[0]

    def test_neither_coordinator_nor_project_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, coordinator="", project="")))
        assert report.skipped == 1
        assert "no coordinator or project given" in report.errors[0]

    def test_unknown_coordinator_is_an_error(self):
        project = ProjectFactory()
        report = import_rules_csv(_csv(_row(project, coordinator="Nobody Real", project="")))
        assert report.skipped == 1
        assert "no project matching" in report.errors[0]

    def test_ambiguous_coordinator_is_an_error(self):
        """Unlike country, coordinator isn't unique on Project -- two
        projects (in different countries) can share a coordinator name.
        """
        project = ProjectFactory(coordinator="Jo Smith")
        ProjectFactory(coordinator="Jo Smith")

        report = import_rules_csv(_csv(_row(project, coordinator="Jo Smith", project="")))

        assert report.skipped == 1
        assert "more than one project matches" in report.errors[0]


@pytest.mark.django_db
class TestIdempotency:
    def test_rerunning_the_same_file_reports_duplicates_not_new_rows(self):
        project = ProjectFactory()
        csv_text = _row(project)
        first = import_rules_csv(_csv(csv_text))
        assert (first.created, first.duplicates) == (1, 0)

        second = import_rules_csv(_csv(csv_text))
        assert (second.created, second.duplicates) == (0, 1)
        assert Rule.objects.count() == 1

    def test_same_project_different_regex_is_a_new_rule(self):
        project = ProjectFactory()
        import_rules_csv(_csv(_row(project, regex=r"^A$")))
        report = import_rules_csv(_csv(_row(project, regex=r"^B$")))
        assert (report.created, report.duplicates) == (1, 0)
        assert Rule.objects.count() == 2
