import datetime

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from core.models import Event, Species

from .factories import (
    ObservationFactory,
    OriginFactory,
    ProjectFactory,
    RuleFactory,
    StaffUserFactory,
    TagFactory,
    UserFactory,
)


def _detail_url(observation):
    return reverse("core:observation-detail", args=[observation.pk])


def _events_url(observation):
    return reverse("core:observation-events", args=[observation.pk])


@pytest.mark.django_db
class TestObservationDetailView:
    def test_requires_login(self):
        observation = ObservationFactory()
        response = Client().get(_detail_url(observation))
        assert response.status_code == 302
        assert "login" in response.url

    def test_other_users_cannot_view(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(UserFactory())
        response = client.get(_detail_url(observation))
        assert response.status_code == 403

    def test_staff_can_view_anyones(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(StaffUserFactory())
        response = client.get(_detail_url(observation))
        assert response.status_code == 200

    def test_shows_report_with_copy_and_edit_links(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = response.content.decode()
        sighting = response.context["sighting"]
        assert "core/_observation_email.html" in [t.name for t in response.templates]
        assert sighting.scientific_name in content
        assert "<textarea" not in content
        assert 'id="copy-report"' in content
        assert reverse("core:observation-edit", args=[observation.pk]) in content

    def test_lists_events_in_date_order_with_edit_link(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        Event.objects.create(
            observation=observation, date=datetime.date(2026, 3, 1), description="Heard back"
        )
        Event.objects.create(
            observation=observation, date=datetime.date(2026, 1, 1), description="Emailed"
        )

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = response.content.decode()
        assert [e.description for e in response.context["events"]] == ["Emailed", "Heard back"]
        assert "1 Jan. 2026" in content
        assert _events_url(observation) in content

    def test_back_link_goes_to_the_list_as_last_filtered(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user, origin=None)
        list_url = reverse("core:my-observations")

        client.force_login(user)
        client.get(list_url, {"status": "open", "q": "A1", "page": "1"})
        response = client.get(_detail_url(observation))

        assert response.context["back_url"] == f"{list_url}?status=open&q=A1&page=1"
        assert f'href="{list_url}?status=open&amp;q=A1&amp;page=1"' in response.content.decode()

    def test_back_link_is_the_plain_list_without_filters(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        assert response.context["back_url"] == reverse("core:my-observations")

    def test_clearing_the_filters_is_remembered_too(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        list_url = reverse("core:my-observations")

        client.force_login(user)
        client.get(list_url, {"status": "open"})
        client.get(list_url)
        response = client.get(_detail_url(observation))

        assert response.context["back_url"] == list_url

    def test_back_link_survives_a_trip_to_the_events_page(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        list_url = reverse("core:my-observations")

        client.force_login(user)
        client.get(list_url, {"status": "closed"})
        client.get(_events_url(observation))
        response = client.get(_detail_url(observation))

        assert response.context["back_url"] == f"{list_url}?status=closed"

    def test_back_link_encodes_the_remembered_query(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        list_url = reverse("core:my-observations")

        client.force_login(user)
        client.get(list_url, {"q": 'W(A1) "x"&y'})
        response = client.get(_detail_url(observation))

        assert response.context["back_url"] == f"{list_url}?q=W%28A1%29+%22x%22%26y"

    def test_report_is_the_email_layout_even_when_closed(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(_detail_url(observation))

        report = response.content.decode().split('id="report"')[1].split("</section>")[0]
        assert "Observers" in report
        assert "Ringed" not in report

    def test_open_observation_has_no_recovery(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        assert response.context["recovery"] is None
        assert "core/_recovery.html" not in [t.name for t in response.templates]

    def test_open_observation_lists_matching_projects(self, client: Client):
        user = UserFactory()
        rule = RuleFactory(project=ProjectFactory(name="Gulls of Norway"))
        observation = ObservationFactory(owner=user, species=rule.species, origin=None)
        TagFactory(observation=observation, position=rule.position, code="W(A1)")

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = response.content.decode()
        assert response.context["matches"] == [rule.project]
        assert "Matching projects" in content
        assert "Gulls of Norway" in content
        assert ">Open<" in content

    def test_project_contact_rows_show_the_address_and_url_with_actions(self, client: Client):
        user = UserFactory()
        project = ProjectFactory(
            name="Gulls of Norway",
            contact="ringer@example.org",
            submit="https://example.org/submit",
        )
        rule = RuleFactory(project=project)
        observation = ObservationFactory(owner=user, species=rule.species, origin=None)
        TagFactory(observation=observation, position=rule.position, code="W(A1)")

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = " ".join(response.content.decode().split())
        assert 'href="mailto:ringer@example.org?' in content
        assert ">Send email</a>" in content
        assert 'href="https://example.org/submit"' in content
        assert ">Submit online</a>" in content
        assert "Email ringer@example.org" not in content
        assert "Open submission page" not in content

    def test_closed_observation_shows_ringing_details_and_life_history(
        self, client: Client, settings, tmp_path
    ):
        settings.MEDIA_ROOT = tmp_path
        user = UserFactory()
        origin = OriginFactory(
            date=datetime.date(2024, 6, 1),
            project=ProjectFactory(name="Gulls of Norway", contact="ringer@example.org"),
            history_url="https://example.org/history/123",
            history_file=SimpleUploadedFile("history.pdf", b"%PDF-1.4"),
        )
        observation = ObservationFactory(owner=user, origin=origin)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = response.content.decode()
        assert ">Closed<" in content
        assert "core/_recovery.html" in [t.name for t in response.templates]
        assert ">Recovery<" in content
        assert "Matching projects" not in content
        assert "1 June 2024" in content
        assert "Gulls of Norway" in content
        assert "mailto:ringer@example.org" in content
        assert "https://example.org/history/123" in content
        assert origin.history_file.url in content
        assert reverse("core:origin-history", args=[origin.pk]) in content

    def test_staff_see_add_ringing_details_on_an_open_observation(self, client: Client):
        user = StaffUserFactory()
        observation = ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        content = response.content.decode()
        assert "Add ringing details" in content
        assert f"{reverse('core:origin-submit')}?observation={observation.pk}&next=" in content

    def test_non_staff_do_not_see_add_ringing_details(self, client: Client):
        user = UserFactory(is_staff=False)
        observation = ObservationFactory(owner=user, origin=None)

        client.force_login(user)
        response = client.get(_detail_url(observation))

        assert b"Add ringing details" not in response.content

    def test_no_add_ringing_details_once_closed(self, client: Client):
        user = StaffUserFactory()
        observation = ObservationFactory(owner=user, origin=OriginFactory())

        client.force_login(user)
        response = client.get(_detail_url(observation))

        assert b"Add ringing details" not in response.content


@pytest.mark.django_db
class TestObservationEventsView:
    def _management_form(self, total, initial):
        return {
            "events-TOTAL_FORMS": str(total),
            "events-INITIAL_FORMS": str(initial),
            "events-MIN_NUM_FORMS": "0",
            "events-MAX_NUM_FORMS": "1000",
        }

    def test_other_users_cannot_edit(self, client: Client):
        observation = ObservationFactory(owner=UserFactory())
        client.force_login(UserFactory())
        assert client.get(_events_url(observation)).status_code == 403

    def test_get_shows_a_date_picker_defaulting_to_today(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.get(_events_url(observation))

        content = response.content.decode()
        assert 'type="date"' in content
        assert f'value="{datetime.date.today():%Y-%m-%d}"' in content

    def test_adds_an_event(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        response = client.post(
            _events_url(observation),
            {
                **self._management_form(total=1, initial=0),
                "events-0-date": "2026-09-01",
                "events-0-description": "Emailed the coordinator",
            },
        )

        assert response.status_code == 302
        assert response.url == _detail_url(observation)
        event = observation.events.get()
        assert event.date == datetime.date(2026, 9, 1)
        assert event.description == "Emailed the coordinator"

    def test_blank_extra_row_adds_nothing(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)

        client.force_login(user)
        client.post(
            _events_url(observation),
            {
                **self._management_form(total=1, initial=0),
                "events-0-date": f"{datetime.date.today():%Y-%m-%d}",
                "initial-events-0-date": f"{datetime.date.today():%Y-%m-%d}",
                "events-0-description": "",
            },
        )

        assert not observation.events.exists()

    def test_edits_and_deletes_events(self, client: Client):
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        kept = Event.objects.create(observation=observation, description="Emailed")
        removed = Event.objects.create(observation=observation, description="Mistake")

        client.force_login(user)
        response = client.post(
            _events_url(observation),
            {
                **self._management_form(total=2, initial=2),
                "events-0-id": kept.pk,
                "events-0-observation": observation.pk,
                "events-0-date": "2026-08-15",
                "events-0-description": "Emailed the coordinator",
                "events-1-id": removed.pk,
                "events-1-observation": observation.pk,
                "events-1-date": "2026-08-16",
                "events-1-description": "Mistake",
                "events-1-DELETE": "on",
            },
        )

        assert response.status_code == 302
        kept.refresh_from_db()
        assert kept.date == datetime.date(2026, 8, 15)
        assert kept.description == "Emailed the coordinator"
        assert not Event.objects.filter(pk=removed.pk).exists()


@pytest.mark.django_db
class TestPossibleSightingsReview:
    def _bird(self):
        """A Closed sighting, and an Open one of the same bird whose
        observer wasn't sure of one ring."""
        origin = OriginFactory()
        linked = ObservationFactory(origin=origin)
        TagFactory(observation=linked, position="LA", code="R,WN(KY)")
        candidate = ObservationFactory(species=linked.species, origin=None)
        TagFactory(observation=candidate, position="LA", code="R?,WN(KY)")
        return origin, linked, candidate

    def test_staff_see_possible_sightings_with_their_differences(self, client: Client):
        _origin, linked, candidate = self._bird()

        client.force_login(StaffUserFactory())
        response = client.get(_detail_url(linked))

        content = response.content.decode()
        assert "Possible sightings of this bird" in content
        assert reverse("core:observation-link", args=[candidate.pk]) in content
        assert "R?,WN(KY)" in content
        assert "R,WN(KY)" in content

    def test_owners_who_are_not_staff_do_not(self, client: Client):
        user = UserFactory()
        _origin, linked, _candidate = self._bird()
        linked.owner = user
        linked.save()

        client.force_login(user)
        response = client.get(_detail_url(linked))

        assert response.context["possible_sightings"] == []
        assert "Possible sightings of this bird" not in response.content.decode()

    def test_linking_after_review(self, client: Client):
        origin, linked, candidate = self._bird()

        client.force_login(StaffUserFactory())
        response = client.post(
            reverse("core:observation-link", args=[candidate.pk]),
            {"origin": origin.pk, "next": _detail_url(linked)},
        )

        assert response.status_code == 302
        assert response.url == _detail_url(linked)
        candidate.refresh_from_db()
        assert candidate.origin == origin
        assert candidate.events.get().description.startswith("Linked after review")

    def test_linking_is_staff_only(self, client: Client):
        origin, _linked, candidate = self._bird()

        client.force_login(UserFactory())
        response = client.post(
            reverse("core:observation-link", args=[candidate.pk]), {"origin": origin.pk}
        )

        assert response.status_code == 403
        candidate.refresh_from_db()
        assert candidate.origin is None

    def test_will_not_link_a_different_species(self, client: Client):
        origin = OriginFactory(species=Species.COMMON_OSTRICH)
        candidate = ObservationFactory(species=Species.RED_THROATED_LOON, origin=None)

        client.force_login(StaffUserFactory())
        client.post(reverse("core:observation-link", args=[candidate.pk]), {"origin": origin.pk})

        candidate.refresh_from_db()
        assert candidate.origin is None

    def test_will_not_relink_a_closed_observation(self, client: Client):
        origin, linked, _candidate = self._bird()

        client.force_login(StaffUserFactory())
        response = client.post(
            reverse("core:observation-link", args=[linked.pk]), {"origin": OriginFactory().pk}
        )

        assert response.status_code == 404
        linked.refresh_from_db()
        assert linked.origin == origin

    def test_ignores_an_unsafe_next(self, client: Client):
        origin, _linked, candidate = self._bird()

        client.force_login(StaffUserFactory())
        response = client.post(
            reverse("core:observation-link", args=[candidate.pk]),
            {"origin": origin.pk, "next": "https://evil.example/"},
        )

        assert response.url == _detail_url(candidate)
