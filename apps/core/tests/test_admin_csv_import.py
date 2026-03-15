"""The admin's "Import from CSV" pages -- one per model, all the same
shape (see e.g. LocationAdmin.import_csv_view). The parsing behind each
has its own tests (test_location_import.py et al.); these cover the
admin pages themselves: the form, the messages summarising the
ImportReport, and where each outcome leaves the user.
"""

from collections.abc import Callable
from dataclasses import dataclass

import pytest
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from core.models import Location, Observation, Project, Rule

from .factories import ProjectFactory, SuperUserFactory


@dataclass
class ImportCase:
    name: str
    model: type
    template: str
    plural: str
    # Both take the Project a Rule row points at (ignored by the others).
    good_csv: Callable[[Project], str]
    bad_csv: Callable[[Project], str]

    @property
    def url(self):
        return reverse(f"admin:core_{self.name}_import_csv")

    @property
    def changelist(self):
        return reverse(f"admin:core_{self.name}_changelist")

    def __str__(self):
        return self.name


CASES = [
    ImportCase(
        name="location",
        model=Location,
        template="admin/core/location_import.html",
        plural="location(s)",
        good_csv=lambda _p: (
            "name,region,country,latitude,longitude\n"
            "Riverside,Great Britain,United Kingdom,51.5,-0.12\n"
        ),
        bad_csv=lambda _p: (
            "name,region,country,latitude,longitude\nRiverside,Nowhere,United Kingdom,51.5,-0.12\n"
        ),
    ),
    ImportCase(
        name="project",
        model=Project,
        template="admin/core/project_import.html",
        plural="project(s)",
        good_csv=lambda _p: "name,coordinator,country\nGulls,Jo Smith,France\n",
        bad_csv=lambda _p: "name,coordinator,country\nGulls,Jo Smith,Atlantis\n",
    ),
    ImportCase(
        name="rule",
        model=Rule,
        template="admin/core/rule_import.html",
        plural="rule(s)",
        good_csv=lambda p: (
            f"species,position,regex,coordinator\n00010,Left Below,^W,{p.coordinator}\n"
        ),
        bad_csv=lambda p: f"species,position,regex,coordinator\n00010,Nowhere,^W,{p.coordinator}\n",
    ),
    ImportCase(
        name="observation",
        model=Observation,
        template="admin/core/observation_import.html",
        plural="observation(s)",
        good_csv=lambda _p: (
            "species,location,region,country,observer,date,latitude,longitude,accuracy,left_below\n"
            "00010,Riverside,Great Britain,United Kingdom,Jo Smith,2026-01-01,51.5,-0.12,50,Y\n"
        ),
        bad_csv=lambda _p: (
            "species,location,region,country,observer,date,latitude,longitude,accuracy,left_below\n"
            "nobird,Riverside,Great Britain,United Kingdom,Jo Smith,2026-01-01,51.5,-0.12,50,Y\n"
        ),
    ),
]


def _upload(text: str) -> SimpleUploadedFile:
    return SimpleUploadedFile("import.csv", text.encode(), content_type="text/csv")


def _messages(response) -> list[tuple[str, str]]:
    return [(m.level_tag, str(m)) for m in get_messages(response.wsgi_request)]


@pytest.fixture
def admin_client(client: Client) -> Client:
    client.force_login(SuperUserFactory())
    return client


@pytest.fixture
def project():
    """The Project a Rule row names by its coordinator -- created for
    every case so the other models' counts are unaffected either way
    (a Project import names a different country).
    """
    return ProjectFactory(country="GB--")


@pytest.mark.django_db
@pytest.mark.parametrize("case", CASES, ids=str)
class TestAdminCsvImport:
    def test_get_shows_the_upload_form(self, admin_client, case):
        response = admin_client.get(case.url)

        assert response.status_code == 200
        assert case.template in [t.name for t in response.templates]
        assert 'name="csv_file"' in response.content.decode()

    def test_non_staff_are_sent_to_the_admin_login(self, client, case):
        response = client.get(case.url)
        assert response.status_code == 302
        assert reverse("admin:login") in response.url

    def test_changelist_links_to_the_import_page(self, admin_client, case):
        """A relative link -- "import-csv/" from the changelist is case.url."""
        response = admin_client.get(case.changelist)
        assert case.changelist + "import-csv/" == case.url
        assert 'href="import-csv/"' in response.content.decode()

    def test_good_file_imports_and_returns_to_the_changelist(self, admin_client, case, project):
        before = case.model.objects.count()

        response = admin_client.post(case.url, {"csv_file": _upload(case.good_csv(project))})

        assert response.status_code == 302
        assert response.url == case.changelist
        assert case.model.objects.count() == before + 1
        assert ("success", f"Imported 1 {case.plural}.") in _messages(response)

    def test_reimporting_reports_duplicates(self, admin_client, case, project):
        # Followed, so its own messages are shown (and consumed) first.
        admin_client.post(case.url, {"csv_file": _upload(case.good_csv(project))}, follow=True)
        before = case.model.objects.count()

        response = admin_client.post(case.url, {"csv_file": _upload(case.good_csv(project))})

        assert response.status_code == 302
        assert case.model.objects.count() == before
        messages = _messages(response)
        assert not any(level == "success" for level, _ in messages)
        assert any(level == "info" and "Skipped 1 row(s)" in text for level, text in messages)

    def test_bad_row_stays_on_the_page_with_the_errors(self, admin_client, case, project):
        before = case.model.objects.count()

        response = admin_client.post(case.url, {"csv_file": _upload(case.bad_csv(project))})

        assert response.status_code == 200
        assert case.template in [t.name for t in response.templates]
        assert case.model.objects.count() == before
        messages = _messages(response)
        assert ("warning", "Skipped 1 row(s); see below.") in messages
        assert any(level == "error" and "Row 2" in text for level, text in messages)

    def test_missing_file_redisplays_the_form(self, admin_client, case):
        response = admin_client.post(case.url, {})

        assert response.status_code == 200
        assert response.context["form"].errors["csv_file"]
