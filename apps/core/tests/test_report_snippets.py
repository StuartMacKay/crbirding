"""core/_observation_email.html and core/_recovery.html rendered on
their own -- each is meant to be included anywhere with just its one
context variable, not only on ObservationDetailView's page.
"""

import datetime

import pytest
from django.template.loader import render_to_string

from core.models import Age, Sex
from core.utils.formatting import describe_recovery, describe_sighting

from .factories import LocationFactory, ObservationFactory, OriginFactory, ProjectFactory


@pytest.mark.django_db
class TestObservationEmailSnippet:
    def _render(self, observation):
        return render_to_string(
            "core/_observation_email.html", {"sighting": describe_sighting(observation)}
        )

    def test_lays_out_every_detail(self):
        observation = ObservationFactory(
            date=datetime.date(2026, 9, 20),
            time=datetime.time(9, 15),
            age=Age.SECOND_YEAR,
            sex=Sex.MALE,
        )

        html = self._render(observation)

        assert "Common Ostrich (<i>Struthio camelus</i>)" in html
        assert "20-Sep-2026 09:15" in html
        assert "2CY" in html
        assert "Male" in html
        assert "51.5074, -0.1278" in html

    def test_unrecorded_values_have_placeholders(self):
        html = self._render(ObservationFactory(time=None, age="", sex=""))

        assert html.count(">Unknown<") == 2  # age and sex
        assert ">—<" in html  # no colour marks

    def test_is_styled_inline_for_pasting_into_email(self):
        html = self._render(ObservationFactory())
        assert 'class="' not in html
        assert 'style="' in html


@pytest.mark.django_db
class TestRecoverySnippet:
    def _render(self, observation):
        return render_to_string("core/_recovery.html", {"recovery": describe_recovery(observation)})

    def test_shows_both_sides_and_the_journey(self):
        origin = OriginFactory(
            location=LocationFactory(latitude="51.5074", longitude="-0.1278"),
            date=datetime.date(2020, 1, 1),
            project=ProjectFactory(name="Gulls of Norway"),
        )
        observation = ObservationFactory(
            origin=origin,
            location=LocationFactory(latitude="48.8566", longitude="2.3522"),
            date=datetime.date(2020, 6, 1),
        )

        html = self._render(observation)

        assert ">Ringed<" in html
        assert ">Seen<" in html
        assert "1 Jan. 2020" in html
        assert "1 June 2020" in html
        assert "Gulls of Norway" in html
        assert "344 km SE (148°), 152 days after ringing." in " ".join(html.split())

    def test_without_a_ringing_date_leaves_out_the_days(self):
        observation = ObservationFactory(origin=OriginFactory(date=None))

        html = " ".join(self._render(observation).split())

        assert "after ringing" not in html
        assert "km" in html
