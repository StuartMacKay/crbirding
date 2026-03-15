"""Every admin list page renders with data in it -- which is what runs
each ModelAdmin's own list columns (e.g. ObservationAdmin.observer_names)
-- plus the columns, filters, and "Export selected to CSV" actions that
are this project's own rather than Django's.
"""

import csv
import io

import pytest
from django.test import Client
from django.urls import reverse

from core.models import Location, Project, Rule, Species

from .factories import (
    LocationFactory,
    ObservationFactory,
    ObserverFactory,
    OriginFactory,
    ProjectFactory,
    RuleFactory,
    SuperUserFactory,
    TagFactory,
)


@pytest.fixture
def admin_client(db) -> Client:
    client = Client()
    client.force_login(SuperUserFactory())
    return client


@pytest.fixture
def one_of_everything(db):
    origin = OriginFactory(label="W(A123)")
    observation = ObservationFactory(origin=origin)
    TagFactory(observation=observation, code="W(A123)")
    RuleFactory(project=origin.project)
    ObserverFactory()
    return observation


@pytest.mark.parametrize(
    "model",
    [
        "core.location",
        "core.observation",
        "core.observer",
        "core.origin",
        "core.project",
        "core.rule",
        "core.tag",
        "users.user",
    ],
)
class TestChangelistsRender:
    def test_lists_its_records(self, admin_client, one_of_everything, model):
        app_label, model_name = model.split(".")
        response = admin_client.get(reverse(f"admin:{app_label}_{model_name}_changelist"))
        assert response.status_code == 200
        assert response.context["cl"].result_count >= 1

    def test_search_works(self, admin_client, one_of_everything, model):
        app_label, model_name = model.split(".")
        response = admin_client.get(
            reverse(f"admin:{app_label}_{model_name}_changelist"), {"q": "a"}
        )
        assert response.status_code == 200


@pytest.mark.django_db
class TestObservationChangelist:
    def test_shows_location_observers_and_whether_found(self, admin_client):
        found = ObservationFactory(
            origin=OriginFactory(), location=LocationFactory(name={"Latn": "Riverside"})
        )
        observer_names = ", ".join(o.name for o in found.observers.all())

        response = admin_client.get(reverse("admin:core_observation_changelist"))

        content = response.content.decode()
        assert "Riverside" in content
        assert observer_names in content
        assert 'alt="True"' in content  # the "found" boolean icon

    @pytest.mark.parametrize("value, expected", [("yes", "found"), ("no", "not_found")])
    def test_found_filter(self, admin_client, value, expected):
        records = {
            "found": ObservationFactory(origin=OriginFactory()),
            "not_found": ObservationFactory(origin=None),
        }

        response = admin_client.get(reverse("admin:core_observation_changelist"), {"found": value})

        assert list(response.context["cl"].result_list) == [records[expected]]

    def test_species_filter(self, admin_client):
        wanted = ObservationFactory(species=Species.COMMON_OSTRICH)
        ObservationFactory(species=Species.RED_THROATED_LOON)

        response = admin_client.get(
            reverse("admin:core_observation_changelist"),
            {"species": Species.COMMON_OSTRICH},
        )

        assert list(response.context["cl"].result_list) == [wanted]


@pytest.mark.django_db
class TestOriginChangelist:
    def test_shows_the_country(self, admin_client):
        OriginFactory(location=LocationFactory(region="FR--"))
        response = admin_client.get(reverse("admin:core_origin_changelist"))
        assert "France" in response.content.decode()


@pytest.mark.django_db
class TestExportCsvActions:
    @pytest.mark.parametrize(
        "model, factory, filename",
        [
            (Location, LocationFactory, "locations.csv"),
            (Project, ProjectFactory, "projects.csv"),
            (Rule, RuleFactory, "rules.csv"),
        ],
        ids=["location", "project", "rule"],
    )
    def test_exports_only_the_selected_records(self, admin_client, model, factory, filename):
        selected = factory()
        factory()  # not selected

        response = admin_client.post(
            reverse(f"admin:core_{model._meta.model_name}_changelist"),
            {"action": "export_csv", "_selected_action": [selected.pk]},
        )

        assert response.status_code == 200
        assert response["Content-Type"].startswith("text/csv")
        assert response["Content-Disposition"] == f'attachment; filename="{filename}"'
        rows = list(csv.DictReader(io.StringIO(response.content.decode())))
        assert len(rows) == 1


@pytest.mark.django_db
class TestLocationAdminForm:
    def test_country_is_filled_in_from_the_saved_region(self, admin_client):
        location = LocationFactory(region="FR01")

        response = admin_client.get(reverse("admin:core_location_change", args=[location.pk]))

        assert response.context["adminform"].form.initial["country"] == "FR--"
