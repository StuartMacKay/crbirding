import pytest
from django.test import Client
from django.urls import reverse

from core.models import Species

from .factories import (
    LocationFactory,
    ObservationFactory,
    OriginFactory,
    StaffUserFactory,
    TagFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestMyObservationsView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("core:my-observations"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_uses_correct_template(self, client: Client):
        client.force_login(UserFactory())
        response = client.get(reverse("core:my-observations"))
        assert response.status_code == 200
        assert "core/my_observations.html" in [t.name for t in response.templates]

    def test_lists_only_the_users_own_observations(self, client: Client):
        user = UserFactory()
        mine = ObservationFactory(owner=user)
        someone_elses = ObservationFactory(owner=UserFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        results = list(response.context["observations"])
        assert mine in results
        assert someone_elses not in results

    def test_includes_observations_without_an_identified_origin(self, client: Client):
        user = UserFactory()
        unidentified = ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        assert unidentified in response.context["observations"]

    def test_includes_observations_with_an_identified_origin(self, client: Client):
        user = UserFactory()
        identified = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        assert identified in response.context["observations"]

    def test_does_not_show_add_ringing_details_link(self, client: Client):
        """Moved to the observation's own page (ObservationDetailView)."""
        user = StaffUserFactory()
        ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        assert b"Add ringing details" not in response.content

    def test_has_no_origin_column(self, client: Client):
        """The Status column already says whether the origin is known."""
        user = UserFactory()
        ObservationFactory(owner=user, origin=OriginFactory())
        ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        content = response.content.decode()
        assert ">Origin<" not in content
        assert "Ringed in" not in content
        assert "Not yet identified" not in content

    def test_pagination(self, client: Client):
        user = UserFactory()
        for _ in range(21):
            ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        assert response.context["is_paginated"] is True
        assert len(response.context["observations"]) == 20

    def test_filters_by_species(self, client: Client):
        user = UserFactory()
        wanted = ObservationFactory(owner=user, species=Species.COMMON_OSTRICH)
        other = ObservationFactory(owner=user, species=Species.RED_THROATED_LOON)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"species": wanted.species})

        results = list(response.context["observations"])
        assert wanted in results
        assert other not in results

    def test_filters_by_place_matching_either_side(self, client: Client):
        user = UserFactory()
        location = LocationFactory()
        matching_by_location = ObservationFactory(owner=user, location=location)
        matching_by_origin = ObservationFactory(
            owner=user, origin=OriginFactory(location=location)
        )
        elsewhere = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"place": location.pk})

        results = list(response.context["observations"])
        assert matching_by_location in results
        assert matching_by_origin in results
        assert elsewhere not in results

    def test_filters_by_country(self, client: Client):
        user = UserFactory()
        wanted = ObservationFactory(owner=user, location=LocationFactory(region="FR--"))
        elsewhere = ObservationFactory(owner=user, location=LocationFactory(region="GB--"))

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"country": "FR--"})

        results = list(response.context["observations"])
        assert wanted in results
        assert elsewhere not in results

    def test_filter_options_only_include_the_users_own_observations(self, client: Client):
        user = UserFactory()
        ObservationFactory(owner=user, species=Species.COMMON_OSTRICH)
        ObservationFactory(owner=UserFactory(), species=Species.RED_THROATED_LOON)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        codes = [code for code, _ in response.context["species_options"]]
        assert Species.COMMON_OSTRICH in codes
        assert Species.RED_THROATED_LOON not in codes

    def test_row_links_only_to_view(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        content = response.content.decode()
        assert reverse("core:observation-detail", args=[observation.pk]) in content
        assert reverse("core:observation-edit", args=[observation.pk]) not in content
        assert reverse("core:observation-send", args=[observation.pk]) not in content

    def test_searches_by_tag_code(self, client: Client):
        user = UserFactory()
        wanted = ObservationFactory(owner=user)
        TagFactory(observation=wanted, code="W(A123)")
        other = ObservationFactory(owner=user)
        TagFactory(observation=other, code="W(B456)")

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"q": "a12"})

        results = list(response.context["observations"])
        assert wanted in results
        assert other not in results

    def test_search_requires_every_term_to_match(self, client: Client):
        user = UserFactory()
        both = ObservationFactory(owner=user)
        TagFactory(observation=both, position="LB", code="W(A123)")
        TagFactory(observation=both, position="RB", code="W(B456)")
        one = ObservationFactory(owner=user)
        TagFactory(observation=one, code="W(A123)")

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"q": "A123 B456"})

        results = list(response.context["observations"])
        assert results == [both]

    def test_search_lists_an_observation_once_when_several_tags_match(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        TagFactory(observation=observation, position="LB", code="W(A123)")
        TagFactory(observation=observation, position="RB", code="W(A124)")

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"q": "A12"})

        assert list(response.context["observations"]) == [observation]

    def test_search_only_includes_the_users_own_observations(self, client: Client):
        user = UserFactory()
        someone_elses = ObservationFactory(owner=UserFactory())
        TagFactory(observation=someone_elses, code="W(A123)")

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"q": "A123"})

        assert list(response.context["observations"]) == []

    def test_search_term_is_kept_in_the_form_and_pagination(self, client: Client):
        user = UserFactory()
        for _ in range(21):
            TagFactory(observation=ObservationFactory(owner=user), code="W(A123)")

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"q": "A123"})

        assert response.context["search"] == "A123"
        assert 'value="A123"' in response.content.decode()
        assert "q=A123" in response.context["querystring"]

    def test_status_is_open_without_an_origin(self, client: Client):
        user = UserFactory()
        ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        content = response.content.decode()
        assert ">Open</span>" in content
        assert ">Closed</span>" not in content

    def test_status_is_closed_with_an_origin(self, client: Client):
        user = UserFactory()
        ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"))

        content = response.content.decode()
        assert ">Closed</span>" in content
        assert ">Open</span>" not in content

    def test_filters_by_open_status(self, client: Client):
        user = UserFactory()
        open_ = ObservationFactory(owner=user, origin=None)
        closed = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"status": "open"})

        results = list(response.context["observations"])
        assert open_ in results
        assert closed not in results
        assert response.context["selected_status"] == "open"

    def test_filters_by_closed_status(self, client: Client):
        user = UserFactory()
        open_ = ObservationFactory(owner=user, origin=None)
        closed = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"status": "closed"})

        results = list(response.context["observations"])
        assert closed in results
        assert open_ not in results

    def test_unrecognised_status_shows_everything(self, client: Client):
        user = UserFactory()
        open_ = ObservationFactory(owner=user, origin=None)
        closed = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"status": "bogus"})

        results = list(response.context["observations"])
        assert open_ in results
        assert closed in results

    def test_status_filter_is_kept_in_the_form_and_offers_clear(self, client: Client):
        user = UserFactory()
        ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(reverse("core:my-observations"), {"status": "open"})

        content = response.content.decode()
        assert '<option value="open" selected>' in content
        assert "Clear" in content
        assert "status=open" in response.context["querystring"]
