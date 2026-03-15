import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from core.models import Origin, Species

from .factories import (
    LocationFactory,
    ObservationFactory,
    OriginFactory,
    ProjectFactory,
    StaffUserFactory,
    TagFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestSubmitOriginView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("core:origin-submit"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_non_staff_forbidden(self, client: Client):
        client.force_login(UserFactory(is_staff=False))
        response = client.get(reverse("core:origin-submit"))
        assert response.status_code == 403

    def test_staff_can_get_form(self, client: Client):
        client.force_login(StaffUserFactory())
        response = client.get(reverse("core:origin-submit"))
        assert response.status_code == 200

    def test_post_creates_origin_with_its_label(self, client: Client):
        client.force_login(StaffUserFactory())
        species = Species.COMMON_OSTRICH
        location = LocationFactory()
        project = ProjectFactory()

        data = {
            "species": species,
            "age": "",
            "sex": "",
            "location-search": location.pk,
            "date": "2026-01-01",
            "project": project.pk,
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)

        assert response.status_code == 302
        origin = Origin.objects.get()
        assert origin.species == species
        assert origin.label == "BW(123)"

    def test_post_saves_life_history_url_and_file(self, client: Client, settings, tmp_path):
        settings.MEDIA_ROOT = tmp_path
        client.force_login(StaffUserFactory())
        location = LocationFactory()

        data = {
            "species": Species.COMMON_OSTRICH,
            "location-search": location.pk,
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "history_url": "https://example.org/history/1",
            "history_file": SimpleUploadedFile("history.pdf", b"%PDF-1.4"),
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)

        assert response.status_code == 302
        origin = Origin.objects.get()
        assert origin.history_url == "https://example.org/history/1"
        assert origin.history_file.read() == b"%PDF-1.4"

    def test_form_accepts_file_uploads(self, client: Client):
        client.force_login(StaffUserFactory())
        response = client.get(reverse("core:origin-submit"))
        content = response.content.decode()
        assert 'enctype="multipart/form-data"' in content
        assert 'name="history_file"' in content
        assert 'name="history_url"' in content

    def _data(self, observation=None, **extra):
        data = {
            "species": Species.COMMON_OSTRICH,
            "label": "BW(123)",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            **extra,
        }
        if observation is not None:
            data["observation"] = observation.pk
        return data

    def test_get_from_an_observation_starts_with_its_species_and_marks(self, client: Client):
        observation = ObservationFactory(species=Species.RED_THROATED_LOON, origin=None)
        TagFactory(observation=observation, position="LA", code="M,BW(A1)")

        client.force_login(StaffUserFactory())
        response = client.get(reverse("core:origin-submit"), {"observation": observation.pk})

        form = response.context["form"]
        assert form.initial == {"species": Species.RED_THROATED_LOON, "label": "BW(A1)"}
        assert "LA:M,BW(A1)" in response.content.decode()
        assert f'name="observation" value="{observation.pk}"' in response.content.decode()

    def test_post_links_the_observation_it_was_added_from(self, client: Client):
        observation = ObservationFactory(species=Species.COMMON_OSTRICH, origin=None)
        TagFactory(observation=observation, position="LA", code="BW(A1)")

        client.force_login(StaffUserFactory())
        response = client.post(reverse("core:origin-submit"), self._data(observation))

        assert response.status_code == 302
        observation.refresh_from_db()
        assert observation.origin == Origin.objects.get()
        assert observation.events.get().description.startswith("Ringing details added")

    def test_post_also_links_sightings_with_exactly_the_same_tags(self, client: Client):
        observation = ObservationFactory(species=Species.COMMON_OSTRICH, origin=None)
        TagFactory(observation=observation, position="LA", code="BW(A1)")
        same = ObservationFactory(species=Species.COMMON_OSTRICH, origin=None)
        TagFactory(observation=same, position="LA", code="BW(A1)")
        near = ObservationFactory(species=Species.COMMON_OSTRICH, origin=None)
        TagFactory(observation=near, position="LA", code="BW(A1)?")

        client.force_login(StaffUserFactory())
        response = client.post(reverse("core:origin-submit"), self._data(observation), follow=True)

        origin = Origin.objects.get()
        same.refresh_from_db()
        near.refresh_from_db()
        assert same.origin == origin
        assert near.origin is None
        assert "1 other sighting(s) with exactly the same tags were linked too." in (
            response.content.decode()
        )

    def test_an_already_linked_observation_is_not_found(self, client: Client):
        observation = ObservationFactory(origin=OriginFactory())

        client.force_login(StaffUserFactory())
        response = client.get(reverse("core:origin-submit"), {"observation": observation.pk})

        assert response.status_code == 404

    def test_post_without_a_label_is_invalid(self, client: Client):
        client.force_login(StaffUserFactory())
        response = client.post(reverse("core:origin-submit"), self._data(label=""))

        assert response.status_code == 200
        assert "label" in response.context["form"].errors
        assert not Origin.objects.exists()

    def test_post_creates_a_new_location_when_provided_instead_of_selecting_one(
        self, client: Client
    ):
        client.force_login(StaffUserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "location-search": "__new__:Ringing Station",
            "location-region": "GB--",
            "location-latitude": "51.5",
            "location-longitude": "-0.1",
            "location-accuracy": "50",
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)

        assert response.status_code == 302
        origin = Origin.objects.get()
        assert origin.location.get_name() == "Ringing Station"

    def test_post_without_a_location_or_a_new_one_is_invalid(self, client: Client):
        client.force_login(StaffUserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)

        assert response.status_code == 200
        assert Origin.objects.count() == 0
        location_form = response.context["location_form"]
        assert "Select an existing location, or type a new name to add one." in list(
            location_form.non_field_errors()
        )

    def test_post_redirects_to_next_when_given(self, client: Client):
        client.force_login(StaffUserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "next": "/observations/mine/",
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)
        assert response.status_code == 302
        assert response.url == "/observations/mine/"

    def test_post_ignores_an_unsafe_next(self, client: Client):
        client.force_login(StaffUserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "next": "https://evil.example/",
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)
        assert response.status_code == 302
        assert response.url == reverse("core:home")

    def test_post_missing_required_field_is_invalid(self, client: Client):
        client.force_login(StaffUserFactory())
        data = {
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            "project": ProjectFactory().pk,
            "label": "BW(123)",
        }
        response = client.post(reverse("core:origin-submit"), data)

        assert response.status_code == 200
        assert Origin.objects.count() == 0
