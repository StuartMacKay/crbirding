import pytest
from django.test import Client
from django.urls import reverse

from core.models import Location, Observation, Position, Species

from .factories import (
    LocationFactory,
    ObservationFactory,
    OriginFactory,
    RuleFactory,
    StaffUserFactory,
    TagFactory,
    UserFactory,
)


def _tag_formset_data(observation=None, **codes):
    """TagFormSet POST data, by position name like the CSV columns --
    e.g. _tag_formset_data(observation, left_below="Y"). Every tag `observation`
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
class TestSubmitObservationView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("core:observation-submit"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_get_renders_form(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:observation-submit"))
        assert response.status_code == 200
        assert "form" in response.context
        assert "formset" in response.context
        assert "photo_formset" in response.context

    def test_post_creates_observation_with_tags(self, client: Client):
        user = UserFactory()
        client.force_login(user)
        species = Species.COMMON_OSTRICH
        location = LocationFactory()

        data = {
            "species": species,
            "age": "",
            "sex": "",
            "location-search": location.pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 302
        observation = Observation.objects.get()
        assert observation.species == species
        assert [(tag.position, tag.code) for tag in observation.tags.all()] == [("LB", "Y")]
        # Recording a sighting in the app isn't the same as sending it to
        # a project coordinator -- nothing's happened to it yet.
        assert not observation.events.exists()
        assert observation.origin is None

    def test_post_creates_a_new_location_when_provided_instead_of_selecting_one(
        self, client: Client
    ):
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "location-search": "__new__:Harbour Wall",
            "location-region": "GB--",
            "location-latitude": "51.5",
            "location-longitude": "-0.1",
            "location-accuracy": "50",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 302
        observation = Observation.objects.get()
        assert observation.location.get_name() == "Harbour Wall"
        assert observation.location.region == "GB--"

    def test_post_without_a_location_or_a_new_one_is_invalid(self, client: Client):
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 200
        assert Observation.objects.count() == 0
        location_form = response.context["location_form"]
        assert "Select an existing location, or type a new name to add one." in list(
            location_form.non_field_errors()
        )

    def test_post_with_partial_new_location_is_invalid(self, client: Client):
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "location-search": "__new__:Half Described Place",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 200
        assert Observation.objects.count() == 0
        assert Location.objects.filter(name__Latn="Half Described Place").exists() is False
        location_form = response.context["location_form"]
        assert "region" in location_form.errors
        assert "latitude" in location_form.errors
        assert "longitude" in location_form.errors
        assert "accuracy" in location_form.errors

    def test_post_with_existing_location_and_override_coordinates(self, client: Client):
        """Selecting an existing location, but entering coordinates
        anyway, records them as this observation's own override --
        never on the shared Location itself.
        """
        location = LocationFactory(latitude="51.0000", longitude="-1.0000", accuracy=100)
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "location-search": location.pk,
            "location-latitude": "51.2345",
            "location-longitude": "-1.2345",
            "location-accuracy": "25",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 302
        observation = Observation.objects.get()
        assert str(observation.latitude) == "51.2345"
        assert str(observation.longitude) == "-1.2345"
        assert observation.accuracy == 25
        location.refresh_from_db()
        assert str(location.latitude) == "51.0000"
        assert str(location.longitude) == "-1.0000"
        assert location.accuracy == 100

    def test_post_with_a_new_location_leaves_no_separate_override(self, client: Client):
        """The coordinates entered for a new Location are its own base
        coordinates -- they don't also become a redundant per-sighting
        override on top of themselves.
        """
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "date": "2026-01-01",
            "location-search": "__new__:Fresh Site",
            "location-region": "GB--",
            "location-latitude": "51.5",
            "location-longitude": "-0.1",
            "location-accuracy": "50",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 302
        observation = Observation.objects.get()
        assert observation.latitude is None
        assert observation.longitude is None
        assert observation.accuracy is None
        assert str(observation.location.latitude) == "51.5000"

    def test_post_sets_owner_to_the_submitting_user(self, client: Client):
        user = UserFactory()
        client.force_login(user)
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-submit"), data)

        assert Observation.objects.get().owner == user

    def test_post_creates_observer_from_user_if_none_linked(self, client: Client):
        from core.models import Observer

        user = UserFactory(first_name="Jo", last_name="Smith")
        client.force_login(user)
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-submit"), data)

        observer = Observer.objects.get(user=user)
        assert observer.name == "Jo Smith"

    def test_post_reuses_existing_linked_observer(self, client: Client):
        from .factories import ObserverFactory

        user = UserFactory()
        observer = ObserverFactory(name="Existing Observer", user=user)
        client.force_login(user)
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-submit"), data)

        assert list(Observation.objects.get().observers.all()) == [observer]

    def test_post_claims_a_matching_unclaimed_observer_rather_than_duplicating(
        self, client: Client
    ):
        """A user who skips accounts.ObserverSetupView and submits an
        observation directly still gets linked to an existing, unclaimed
        Observer of the same name (e.g. from imported historical data)
        instead of _observer_for silently creating a duplicate.
        """
        from .factories import ObserverFactory

        historical = ObserverFactory(name="Jo Smith", user=None)
        user = UserFactory(first_name="Jo", last_name="Smith")
        client.force_login(user)
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-submit"), data)

        historical.refresh_from_db()
        assert historical.user == user
        assert list(Observation.objects.get().observers.all()) == [historical]

    def test_post_without_any_tag_data_is_valid(self, client: Client):
        """Tags are optional on a Observation -- only load-bearing while
        its origin is still being worked out (see core.models.Tag)
        -- so a submission naming no tags at all still succeeds.
        """
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 302
        assert Observation.objects.count() == 1
        assert Observation.objects.get().tags.count() == 0

    def test_post_with_a_bad_code_shows_the_error_on_its_box(self, client: Client):
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_above="Z"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 200
        assert response.context["formset"].errors == [
            {"code": ["'Z': 'Z' is not a known colour code"]}
        ]
        assert not Observation.objects.exists()

    def test_post_matching_an_identified_bird_is_linked_to_it(self, client: Client):
        known = ObservationFactory(species=Species.COMMON_OSTRICH, origin=OriginFactory())
        TagFactory(observation=known, position="LA", code="R,WN(KY)")
        client.force_login(UserFactory())
        data = {
            "species": Species.COMMON_OSTRICH,
            "age": "",
            "sex": "",
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_above="r,wn(ky)"),
            **_photo_formset_data(),
        }
        client.post(reverse("core:observation-submit"), data)

        new = Observation.objects.exclude(pk=known.pk).get()
        assert new.origin == known.origin
        assert new.events.get().description.startswith("Linked: same tags")

    def test_post_missing_required_field_is_invalid(self, client: Client):
        client.force_login(UserFactory())
        data = {
            "location-search": LocationFactory().pk,
            "date": "2026-01-01",
            **_tag_formset_data(left_below="Y"),
            **_photo_formset_data(),
        }
        response = client.post(reverse("core:observation-submit"), data)

        assert response.status_code == 200
        assert Observation.objects.count() == 0


@pytest.mark.django_db
class TestSendToProjectView:
    def test_requires_login(self):
        observation = ObservationFactory()
        client = Client()
        response = client.get(reverse("core:observation-send", args=[observation.pk]))
        assert response.status_code == 302
        assert "login" in response.url

    def test_owner_can_view(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        client.force_login(user)

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        assert response.status_code == 200

    def test_other_user_is_forbidden(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(UserFactory())

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        assert response.status_code == 403

    def test_staff_can_view_any_observation(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(StaffUserFactory())

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        assert response.status_code == 200

    def test_shows_the_definite_project_from_a_linked_origin(self, client: Client):
        user = UserFactory()
        origin = OriginFactory()
        observation = ObservationFactory(owner=user, origin=origin, species=origin.species)
        client.force_login(user)

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        assert response.context["matches"] == [(origin.project, True)]

    def test_shows_candidate_projects_from_matching_rules_when_unlinked(self, client: Client):
        user = UserFactory()
        rule = RuleFactory()
        observation = ObservationFactory(owner=user, origin=None, species=rule.species)
        TagFactory(observation=observation, position=rule.position, code="W(A123)")
        client.force_login(user)

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        assert response.context["matches"] == [(rule.project, False)]

    def test_has_no_mark_as_submitted_button(self, client: Client):
        """Replaced by Events -- see ObservationEventsView."""
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        client.force_login(user)

        response = client.get(reverse("core:observation-send", args=[observation.pk]))

        content = response.content.decode()
        assert "Mark as submitted" not in content
        assert "Marked as submitted" not in content

    def test_post_is_not_allowed(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        client.force_login(user)

        response = client.post(reverse("core:observation-send", args=[observation.pk]))

        assert response.status_code == 405
