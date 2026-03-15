import datetime

import pytest
from django.test import Client
from django.urls import reverse

from .factories import (
    ObservationFactory,
    ObserverFactory,
    OriginFactory,
    ProjectFactory,
    TagFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestLifeHistoryView:
    def test_public_access_returns_200(self):
        origin = OriginFactory()
        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))
        assert response.status_code == 200

    def test_uses_correct_template(self):
        origin = OriginFactory()
        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))
        assert "core/origin_history.html" in [t.name for t in response.templates]

    def test_404_for_unknown_origin(self):
        client = Client()
        response = client.get(reverse("core:origin-history", args=[999999]))
        assert response.status_code == 404

    def test_shows_observations_from_every_owner(self):
        origin = OriginFactory()
        mine = ObservationFactory(origin=origin, owner=UserFactory())
        someone_elses = ObservationFactory(origin=origin, owner=UserFactory())
        unowned = ObservationFactory(origin=origin, owner=None)

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        observations = [row["observation"] for row in response.context["rows"]]
        assert mine in observations
        assert someone_elses in observations
        assert unowned in observations

    def test_shows_observer_names(self):
        origin = OriginFactory()
        observer = ObserverFactory(name="Jo Smith")
        ObservationFactory(origin=origin, observers=[observer])

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        assert b"Jo Smith" in response.content

    def test_edit_link_shown_only_for_the_viewers_own_observation(self, client: Client):
        origin = OriginFactory()
        user = UserFactory()
        mine = ObservationFactory(origin=origin, owner=user)
        someone_elses = ObservationFactory(origin=origin, owner=UserFactory())

        client.force_login(user)
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        rows_by_pk = {row["observation"].pk: row for row in response.context["rows"]}
        assert rows_by_pk[mine.pk]["is_mine"] is True
        assert rows_by_pk[someone_elses.pk]["is_mine"] is False
        content = response.content.decode()
        assert content.count(reverse("core:observation-edit", args=[mine.pk])) == 1
        assert reverse("core:observation-edit", args=[someone_elses.pk]) not in content

    def test_anonymous_visitor_sees_no_edit_links_even_for_unowned_observations(self):
        """A regression guard: an unowned observation's owner_id is None,
        and an anonymous request.user.id is also None -- is_mine must
        not compare those two Nones and call it a match.
        """
        origin = OriginFactory()
        ObservationFactory(origin=origin, owner=None)

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        assert response.context["rows"][0]["is_mine"] is False
        assert "Edit" not in response.content.decode()

    def test_observations_ordered_chronologically(self):
        origin = OriginFactory()
        later = ObservationFactory(origin=origin, date=datetime.date(2026, 3, 1))
        earlier = ObservationFactory(origin=origin, date=datetime.date(2026, 1, 1))

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        observations = [row["observation"] for row in response.context["rows"]]
        assert observations.index(earlier) < observations.index(later)

    def test_project_contact_and_submit_links_shown(self):
        project = ProjectFactory(
            contact="coordinator@example.com", submit="https://example.com/submit"
        )
        origin = OriginFactory(project=project)

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        content = response.content.decode()
        assert "mailto:coordinator@example.com" in content
        assert "https://example.com/submit" in content

    def test_shows_the_label_and_each_sightings_colour_marks(self):
        origin = OriginFactory(label="BW(123)")
        observation = ObservationFactory(origin=origin)
        TagFactory(observation=observation, position="RB", code="O,M")

        client = Client()
        response = client.get(reverse("core:origin-history", args=[origin.pk]))

        assert "BW(123)" in response.content.decode()
        assert response.context["rows"][0]["colour_marks"] == "O"
