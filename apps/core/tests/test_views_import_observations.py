import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from core.models import Observation, Species

from .factories import LocationFactory, ObserverFactory, UserFactory

SPECIES_CODE = Species.COMMON_OSTRICH


def _csv_file(text: str) -> SimpleUploadedFile:
    return SimpleUploadedFile("observations.csv", text.encode(), content_type="text/csv")


@pytest.mark.django_db
class TestImportObservationsView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("core:observation-import"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_get_renders_form(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:observation-import"))
        assert response.status_code == 200
        assert "form" in response.context

    def test_post_imports_and_redirects_to_my_observations(self, client: Client):
        client.force_login(UserFactory())
        LocationFactory(name={"Latn": "Test Spot"}, region="GB--")
        ObserverFactory(name="Jo Smith")
        csv_text = (
            "species,location,region,country,observer,date,left_below\n"
            f"{SPECIES_CODE},Test Spot,Great Britain,United Kingdom,Jo Smith,2026-01-01,Y\n"
        )

        response = client.post(
            reverse("core:observation-import"), {"csv_file": _csv_file(csv_text)}
        )

        assert response.status_code == 302
        assert response.url == reverse("core:my-observations")
        assert Observation.objects.count() == 1

    def test_row_owner_is_the_rows_own_observer_not_the_importer(self, client: Client):
        """A life history can span several observers -- the importer
        shouldn't end up owning sightings that weren't theirs.
        """
        importer = UserFactory()
        someone_else = UserFactory()
        LocationFactory(name={"Latn": "Test Spot"}, region="GB--")
        ObserverFactory(name="Someone Else", user=someone_else)
        csv_text = (
            "species,location,region,country,observer,date,left_below\n"
            f"{SPECIES_CODE},Test Spot,Great Britain,United Kingdom,Someone Else,2026-01-01,Y\n"
        )

        client.force_login(importer)
        client.post(reverse("core:observation-import"), {"csv_file": _csv_file(csv_text)})

        observation = Observation.objects.get()
        assert observation.owner == someone_else
        assert observation.owner != importer

    def test_same_day_duplicate_note_is_shown_as_a_message(self, client: Client):
        client.force_login(UserFactory())
        LocationFactory(name={"Latn": "Test Spot"}, region="GB--")
        ObserverFactory(name="Jo Smith")
        csv_text = (
            "species,location,region,country,observer,date,time,left_below\n"
            f"{SPECIES_CODE},Test Spot,Great Britain,United Kingdom,Jo Smith,2026-01-01,"
            "09:15,WB(A123)\n"
            f"{SPECIES_CODE},Test Spot,Great Britain,United Kingdom,Jo Smith,2026-01-01,"
            "14:30,WB(A123)\n"
        )

        response = client.post(
            reverse("core:observation-import"), {"csv_file": _csv_file(csv_text)}, follow=True
        )

        messages = [str(m) for m in response.context["messages"]]
        assert "Row 3: this bird was already logged earlier that day, at 09:15." in messages

    def test_errors_are_reported_without_redirecting(self, client: Client):
        client.force_login(UserFactory())
        csv_text = "species,location,date,left_below\n"  # missing region, country, observer

        response = client.post(
            reverse("core:observation-import"), {"csv_file": _csv_file(csv_text)}
        )

        assert response.status_code == 200
        messages = [str(m) for m in response.context["messages"]]
        assert any("missing required columns" in m for m in messages)
