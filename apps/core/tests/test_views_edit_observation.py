import pytest
from django.test import Client
from django.urls import reverse

from core.models import Observation, Position, Species

from .factories import (
    LocationFactory,
    ObservationFactory,
    ObserverFactory,
    OriginFactory,
    StaffUserFactory,
    TagFactory,
    UserFactory,
)


def _tags(observation=None, **codes):
    """TagFormSet POST data, by position name like the CSV columns --
    e.g. _tags(observation, left_below="Y"). Every tag `observation`
    already has gets its own row (changed if named here; a code of ""
    deletes it), followed by a new row for each other position named.
    """
    positions = {position.name.lower(): position.value for position in Position}
    wanted = {positions[name]: code for name, code in codes.items()}
    rows = []
    if observation is not None:
        for tag in observation.tags.all():
            code = wanted.pop(tag.position, tag.code)
            rows.append((tag.position, code or tag.code, tag.pk, code == ""))
    rows += [(position, code, "", False) for position, code in wanted.items()]

    data = {
        "tags-TOTAL_FORMS": str(len(rows)),
        "tags-INITIAL_FORMS": str(sum(1 for row in rows if row[2])),
        "tags-MIN_NUM_FORMS": "0",
        "tags-MAX_NUM_FORMS": "1000",
    }
    for index, (position, code, pk, delete) in enumerate(rows):
        data[f"tags-{index}-position"] = position
        data[f"tags-{index}-code"] = code
        data[f"tags-{index}-id"] = pk
        if delete:
            data[f"tags-{index}-DELETE"] = "on"
    return data


def _photo_formset_data(**overrides):
    data = {
        "photos-TOTAL_FORMS": "0",
        "photos-INITIAL_FORMS": "0",
        "photos-MIN_NUM_FORMS": "0",
        "photos-MAX_NUM_FORMS": "1000",
    }
    data.update(overrides)
    return data


@pytest.mark.django_db
class TestEditObservationView:
    def test_requires_login(self):
        observation = ObservationFactory()
        client = Client()
        response = client.get(reverse("core:observation-edit", args=[observation.pk]))
        assert response.status_code == 302
        assert "login" in response.url

    def test_owner_can_get_form_prefilled(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user, species=Species.COMMON_OSTRICH)
        client.force_login(user)

        response = client.get(reverse("core:observation-edit", args=[observation.pk]))

        assert response.status_code == 200
        assert response.context["form"].instance == observation
        assert response.context["editing"] is True

    def test_get_prefills_location_country_and_region(self, client: Client):
        """A regression check: the location field itself was already
        being prefilled, but its country/region narrowing fields
        weren't, leaving them blank even though a location was
        correctly pre-selected.
        """
        user = UserFactory()
        location = LocationFactory(region="FR--")
        observation = ObservationFactory(owner=user, location=location)
        client.force_login(user)

        response = client.get(reverse("core:observation-edit", args=[observation.pk]))

        location_form = response.context["location_form"]
        assert location_form.initial["search"] == str(location.pk)
        assert location_form.initial["region"] == "FR--"
        assert location_form.initial["country"] == "FR--"

    def test_non_owner_non_staff_forbidden(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(UserFactory())

        response = client.get(reverse("core:observation-edit", args=[observation.pk]))

        assert response.status_code == 403

    def test_staff_can_edit_someone_elses_observation(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(StaffUserFactory())

        response = client.get(reverse("core:observation-edit", args=[observation.pk]))

        assert response.status_code == 200

    def test_post_updates_fields_and_redirects_to_the_observation(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user, species=Species.COMMON_OSTRICH)
        TagFactory(observation=observation, position="LB", code="Y")

        client.force_login(user)
        data = {
            "species": Species.RED_THROATED_LOON,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": "2026-02-02",
            "notes": "updated notes",
            **_tags(observation, left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert response.status_code == 302
        assert response.url == reverse("core:observation-detail", args=[observation.pk])
        observation.refresh_from_db()
        assert observation.species == Species.RED_THROATED_LOON
        assert observation.date.isoformat() == "2026-02-02"
        assert observation.notes == "updated notes"

    def test_post_can_switch_to_a_newly_added_location(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LB", code="Y")

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "date": observation.date.isoformat(),
            "location-search": "__new__:New Spot",
            "location-region": "GB--",
            "location-latitude": "51.5",
            "location-longitude": "-0.1",
            "location-accuracy": "50",
            **_tags(observation, left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert response.status_code == 302
        observation.refresh_from_db()
        assert observation.location.get_name() == "New Spot"

    def test_post_can_add_a_tag(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LB", code="Y")

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": observation.date.isoformat(),
            **_tags(observation, left_below="Y", right_below="o"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert response.status_code == 302
        assert {tag.position: tag.code for tag in observation.tags.all()} == {"LB": "Y", "RB": "O"}

    def test_post_can_delete_a_tag(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LB", code="Y")
        TagFactory(observation=observation, position="RB", code="O")

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": observation.date.isoformat(),
            **_tags(observation, left_below="Y", right_below=""),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert [tag.position for tag in observation.tags.all()] == ["LB"]

    def test_post_with_a_bad_code_shows_the_error(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LB", code="Y")

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": observation.date.isoformat(),
            **_tags(observation, left_below="BW(A1"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert response.status_code == 200
        assert "missing closing bracket" in response.content.decode()
        assert observation.tags.get().code == "Y"

    def test_get_shows_the_current_codes(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LA", code="R,WN(KY)")

        client.force_login(user)
        response = client.get(reverse("core:observation-edit", args=[observation.pk]))

        assert 'name="tags-0-code" value="R,WN(KY)"' in response.content.decode()

    def test_saving_links_to_an_identified_bird_with_the_same_tags(self, client: Client):
        known = ObservationFactory(origin=OriginFactory())
        TagFactory(observation=known, position="LB", code="W(A1)")
        user = UserFactory()
        observation = ObservationFactory(owner=user, species=known.species, origin=None)

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": observation.date.isoformat(),
            **_tags(observation, left_below="w(a1)"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        observation.refresh_from_db()
        assert observation.origin == known.origin

    def test_edit_does_not_change_observers(self, client: Client):
        user = UserFactory()
        observer = ObserverFactory(user=user)
        observation = ObservationFactory(owner=user, observers=[observer])
        TagFactory(observation=observation, position="LB", code="Y")

        client.force_login(user)
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "location-search": observation.location.pk,
            "date": observation.date.isoformat(),
            **_tags(observation, left_below="Y"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-edit", args=[observation.pk]), data)

        assert list(Observation.objects.get(pk=observation.pk).observers.all()) == [observer]
