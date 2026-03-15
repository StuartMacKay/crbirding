import datetime
from decimal import Decimal

import pytest

from core.models import Age, Sex, Species
from core.utils.formatting import (
    bearing_degrees,
    compass_point,
    describe_journey,
    describe_place,
    describe_recovery,
    describe_sighting,
    effective_coordinates,
    format_colour_marks,
    format_coordinates,
    format_recovery_report,
    format_tags,
    haversine_distance_km,
)

from .factories import LocationFactory, ObservationFactory, OriginFactory, TagFactory


class TestCoordinateHelpers:
    def test_format_coordinates(self):
        assert format_coordinates(57.25, -0.5) == "57.25, -0.5"

    def test_format_coordinates_keeps_the_stored_precision(self):
        assert format_coordinates(Decimal("57.2500"), Decimal("-0.5000")) == "57.2500, -0.5000"
        assert format_coordinates(Decimal("1.9997"), Decimal("-12.0001")) == "1.9997, -12.0001"

    def test_format_coordinates_none_if_either_missing(self):
        assert format_coordinates(None, -0.5) is None
        assert format_coordinates(57.25, None) is None

    def test_haversine_distance_zero_for_same_point(self):
        assert haversine_distance_km(51.5, -0.1, 51.5, -0.1) == pytest.approx(0.0)

    def test_haversine_distance_known_value(self):
        # London to Paris, roughly 344 km.
        distance = haversine_distance_km(51.5074, -0.1278, 48.8566, 2.3522)
        assert distance == pytest.approx(344, abs=5)

    def test_bearing_degrees_due_east(self):
        bearing = bearing_degrees(0, 0, 0, 10)
        assert bearing == pytest.approx(90, abs=1)

    @pytest.mark.parametrize(
        "degrees,expected",
        [(0, "N"), (44, "NE"), (90, "E"), (180, "S"), (270, "W"), (360, "N")],
    )
    def test_compass_point(self, degrees, expected):
        assert compass_point(degrees) == expected


@pytest.mark.django_db
class TestEffectiveCoordinates:
    def test_uses_own_coordinates_when_set(self):
        observation = ObservationFactory(latitude="1.0000", longitude="2.0000")
        lat, lon = effective_coordinates(observation)
        assert float(lat) == pytest.approx(1.0)
        assert float(lon) == pytest.approx(2.0)

    def test_falls_back_to_location_coordinates(self):
        location = LocationFactory(latitude="51.5074", longitude="-0.1278")
        observation = ObservationFactory(location=location, latitude=None, longitude=None)
        lat, lon = effective_coordinates(observation)
        assert float(lat) == pytest.approx(51.5074)
        assert float(lon) == pytest.approx(-0.1278)


class TestFormatTags:
    def test_none_when_no_tags(self):
        assert format_tags([]) is None

    def test_each_position_labelled_in_order(self):
        tags = [
            TagFactory.build(position="RB", code="M"),
            TagFactory.build(position="LB", code="O,Y"),
        ]
        assert format_tags(tags) == "LB:O,Y; RB:M"


class TestFormatColourMarks:
    def test_none_when_no_tags(self):
        assert format_colour_marks([]) is None

    def test_drops_metal_rings(self):
        assert format_colour_marks([TagFactory.build(position="LB", code="M,A")]) is None

    def test_drops_direction_but_keeps_inscription(self):
        """ "LB:M; RB:BW(M:556)" displays as "BW(M:556)" -- the metal
        ring is dropped entirely, and the other's direction too.
        """
        tags = [
            TagFactory.build(position="LB", code="M"),
            TagFactory.build(position="RB", code="BW(M:556)"),
        ]
        assert format_colour_marks(tags) == "BW(M:556)"

    def test_keeps_uncertainty(self):
        assert format_colour_marks([TagFactory.build(position="LB", code="Y?")]) == "Y?"

    def test_orders_anatomically_not_alphabetically(self):
        """format_tags() would put "C" (neck collar) before "LW" (left
        wing) alphabetically; the compact display instead reads
        top-to-bottom, left-to-right on the bird.
        """
        tags = [
            TagFactory.build(position="RW", code="Y"),
            TagFactory.build(position="C", code="O"),
            TagFactory.build(position="S", code="G"),
        ]
        assert format_colour_marks(tags) == "G; O; Y"

    def test_keeps_a_stack_together_dropping_only_its_metal(self):
        tags = [TagFactory.build(position="LA", code="R,M,WN(KY)")]
        assert format_colour_marks(tags) == "R,WN(KY)"


@pytest.mark.django_db
class TestDescribePlace:
    def test_includes_country_name(self):
        location = LocationFactory(name={"Latn": "Somewhere"})
        place, coords = describe_place(location)
        assert "Somewhere" in place
        assert coords is not None

    def test_includes_region_between_name_and_country(self):
        location = LocationFactory(name={"Latn": "Somewhere"}, region="GBAB")
        place, _coords = describe_place(location)
        assert place == "Somewhere, Aberdeen, United Kingdom"

    def test_omits_region_for_a_country_level_location(self):
        location = LocationFactory(name={"Latn": "Somewhere"}, region="FR--")
        place, _coords = describe_place(location)
        assert place == "Somewhere, France"


@pytest.mark.django_db
class TestFormatRecoveryReport:
    def test_without_origin_is_two_lines(self):
        observation = ObservationFactory()
        TagFactory(observation=observation, code="Y")
        report = format_recovery_report(observation)
        assert len(report.lines) == 2

    def test_with_linked_origin_adds_distance_line(self):
        origin = OriginFactory(
            location=LocationFactory(latitude="51.5074", longitude="-0.1278"),
            date=datetime.date(2020, 1, 1),
        )
        observation = ObservationFactory(
            origin=origin,
            species=origin.species,
            location=LocationFactory(latitude="48.8566", longitude="2.3522"),
            date=datetime.date(2020, 6, 1),
        )
        TagFactory(observation=observation, code="Y")
        report = format_recovery_report(observation)
        assert len(report.lines) == 3
        assert "Distance" in report.lines[2]

    def test_observation_line_includes_date_time_and_decimal_coordinates(self):
        observation = ObservationFactory(
            location=LocationFactory(latitude="43.2500", longitude="-2.9200"),
            date=datetime.date(2026, 9, 23),
            time=datetime.time(14, 35),
        )
        report = format_recovery_report(observation)
        assert report.lines[1].startswith("23-Sep-2026 14:35  ")
        assert ": 43.2500, -2.9200 by" in report.lines[1]

    def test_observation_line_includes_age_and_sex(self):
        observation = ObservationFactory(age=Age.SECOND_YEAR, sex=Sex.MALE)
        report = format_recovery_report(observation)
        assert "  Age: 2CY  Sex: Male  " in report.lines[1]

    def test_observation_line_shows_blank_age_and_sex_as_unknown(self):
        observation = ObservationFactory(age="", sex="")
        report = format_recovery_report(observation)
        assert "  Age: Unknown  Sex: Unknown  " in report.lines[1]

    def test_observation_line_omits_time_when_not_recorded(self):
        observation = ObservationFactory(date=datetime.date(2026, 9, 23), time=None)
        report = format_recovery_report(observation)
        assert report.lines[1].startswith("23-Sep-2026  ")


@pytest.mark.django_db
class TestDescribeSighting:
    def test_describes_the_observation(self):
        observation = ObservationFactory(
            species=Species.COMMON_OSTRICH,
            date=datetime.date(2026, 9, 20),
            time=datetime.time(9, 15),
            age=Age.SECOND_YEAR,
            sex=Sex.MALE,
            location=LocationFactory(
                name={"Latn": "Somewhere"},
                region="GBAB",
                latitude=Decimal("57.1497"),
                longitude=Decimal("-2.0943"),
            ),
        )
        TagFactory(observation=observation, code="WN(A123)")

        sighting = describe_sighting(observation)

        assert sighting.species == "Common Ostrich"
        assert sighting.scientific_name == "Struthio camelus"
        assert sighting.marks == "LB:WN(A123)"
        assert sighting.date == datetime.date(2026, 9, 20)
        assert sighting.time == datetime.time(9, 15)
        assert (sighting.age, sighting.sex) == ("2CY", "Male")
        assert sighting.place == "Somewhere, Aberdeen, United Kingdom"
        assert sighting.coordinates == "57.1497, -2.0943"
        assert sighting.observers == ", ".join(o.name for o in observation.observers.all())

    def test_blank_age_and_sex_stay_blank(self):
        sighting = describe_sighting(ObservationFactory(age="", sex=""))
        assert (sighting.age, sighting.sex) == ("", "")

    def test_no_tags(self):
        assert describe_sighting(ObservationFactory()).marks is None


@pytest.mark.django_db
class TestDescribeRecovery:
    def test_none_without_an_origin(self):
        assert describe_recovery(ObservationFactory(origin=None)) is None

    def test_describes_both_sides_and_the_journey(self):
        origin = OriginFactory(
            location=LocationFactory(latitude="51.5074", longitude="-0.1278"),
            date=datetime.date(2020, 1, 1),
            age=Age.NESTLING,
            label="BW(123)",
        )
        observation = ObservationFactory(
            origin=origin,
            location=LocationFactory(latitude="48.8566", longitude="2.3522"),
            date=datetime.date(2020, 6, 1),
        )

        recovery = describe_recovery(observation)

        assert recovery.marking.date == datetime.date(2020, 1, 1)
        assert recovery.marking.age == "Nestling"
        assert recovery.marking.label == "BW(123)"
        assert recovery.marking.project == origin.project
        assert recovery.sighting.date == datetime.date(2020, 6, 1)
        assert recovery.distance_km == pytest.approx(343.5, abs=1)
        assert recovery.direction == "SE"
        assert recovery.days == 152

    def test_no_days_without_a_ringing_date(self):
        recovery = describe_recovery(ObservationFactory(origin=OriginFactory(date=None)))
        assert recovery.days is None
        assert recovery.distance_km is not None


@pytest.mark.django_db
class TestDescribeJourney:
    def test_basic_fields(self):
        observation = ObservationFactory()
        journey = describe_journey(observation)
        assert journey.species_common_name == Species(observation.species).label
        assert journey.observed_place == observation.location.get_name()
        assert journey.ringed_place is None
        assert journey.distance_km is None

    def test_with_origin_computes_distance(self):
        origin = OriginFactory(location=LocationFactory(latitude="51.5074", longitude="-0.1278"))
        observation = ObservationFactory(
            origin=origin,
            species=origin.species,
            location=LocationFactory(latitude="48.8566", longitude="2.3522"),
        )
        journey = describe_journey(observation)
        assert journey.ringed_place == origin.location.get_name()
        assert journey.distance_km is not None
