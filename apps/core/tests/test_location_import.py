import io

import pytest

from core.models import Location
from core.utils.location_import import import_locations_csv

from .factories import LocationFactory

# Matches LocationFactory's own default region ("GB--") -- region and
# country have different labels for the same code, which is the more
# interesting case to exercise than a country like France, whose region
# and country labels happen to be identical.
REGION = "Great Britain"
COUNTRY = "United Kingdom"

HEADER = "name,region,country,latitude,longitude,accuracy,notes"


def _csv(text: str) -> io.BytesIO:
    return io.BytesIO(text.encode())


def _rows(*row_overrides: dict) -> str:
    lines = [HEADER]
    for overrides in row_overrides:
        fields = {
            "name": "Test Location",
            "region": REGION,
            "country": COUNTRY,
            "latitude": "51.5074",
            "longitude": "-0.1278",
            "accuracy": "50",
            "notes": "",
        }
        fields.update(overrides)
        lines.append(",".join(str(fields[column]) for column in HEADER.split(",")))
    return "\n".join(lines) + "\n"


def _row(**overrides) -> str:
    return _rows(overrides)


@pytest.mark.django_db
class TestColumnValidation:
    def test_missing_required_columns_reported(self):
        report = import_locations_csv(_csv("name,latitude\nSomewhere,51.5\n"))
        assert report.errors == ["CSV is missing required columns: country, longitude, region"]
        assert report.created == 0

    def test_header_casing_and_whitespace_dont_hide_columns(self):
        csv_text = (
            "Name,Region,Country,Latitude ,Longitude\n"
            f"Test Location,{REGION},{COUNTRY},51.5074,-0.1278\n"
        )
        report = import_locations_csv(_csv(csv_text))
        assert report.errors == []
        assert report.created == 1


@pytest.mark.django_db
class TestLocationCreation:
    def test_creates_a_new_location(self):
        report = import_locations_csv(_csv(_row()))

        assert report.errors == []
        assert report.created == 1
        location = Location.objects.get()
        assert location.get_name() == "Test Location"
        assert location.region == "GB--"
        assert str(location.latitude) == "51.5074"
        assert str(location.longitude) == "-0.1278"
        assert location.accuracy == 50

    def test_notes_and_accuracy_are_optional(self):
        report = import_locations_csv(_csv(_row(notes="", accuracy="")))

        assert report.errors == []
        location = Location.objects.get()
        assert location.notes == ""
        assert location.accuracy is None

    def test_missing_latitude_is_an_error(self):
        report = import_locations_csv(_csv(_row(latitude="")))
        assert report.skipped == 1
        assert "latitude and longitude are required" in report.errors[0]
        assert Location.objects.count() == 0

    def test_bad_coordinate_is_an_error(self):
        report = import_locations_csv(_csv(_row(latitude="notanumber")))
        assert report.skipped == 1
        assert "not a valid coordinate" in report.errors[0]

    def test_blank_name_is_an_error(self):
        report = import_locations_csv(_csv(_row(name="")))
        assert report.skipped == 1
        assert "no name given" in report.errors[0]

    def test_unknown_country_is_an_error(self):
        report = import_locations_csv(_csv(_row(country="Not a real country")))
        assert report.skipped == 1
        assert "no country matching" in report.errors[0]

    def test_unknown_region_is_an_error(self):
        report = import_locations_csv(_csv(_row(region="Not a real region")))
        assert report.skipped == 1
        assert "no region matching" in report.errors[0]


@pytest.mark.django_db
class TestLocationMatching:
    def test_matching_name_and_region_is_a_duplicate(self):
        location = LocationFactory(name={"Latn": "South Park"}, region="GB--")

        report = import_locations_csv(_csv(_row(name="South Park")))

        assert (report.created, report.duplicates) == (0, 1)
        assert Location.objects.get().pk == location.pk

    def test_match_is_case_insensitive(self):
        LocationFactory(name={"Latn": "South Park"}, region="GB--")

        report = import_locations_csv(_csv(_row(name="south park")))

        assert (report.created, report.duplicates) == (0, 1)

    def test_existing_coordinates_are_not_overwritten(self):
        location = LocationFactory(
            name={"Latn": "South Park"},
            region="GB--",
            latitude="51.0000",
            longitude="-1.0000",
            accuracy=100,
        )

        import_locations_csv(
            _csv(_row(name="South Park", latitude="51.2345", longitude="-1.2345", accuracy="25"))
        )

        location.refresh_from_db()
        assert str(location.latitude) == "51.0000"
        assert str(location.longitude) == "-1.0000"
        assert location.accuracy == 100

    def test_same_name_in_a_different_country_does_not_match(self):
        gb_location = LocationFactory(name={"Latn": "Harbour Wall"}, region="GB--")

        report = import_locations_csv(
            _csv(_row(name="Harbour Wall", region="France", country="France"))
        )

        assert report.created == 1
        fr_location = Location.objects.exclude(pk=gb_location.pk).get()
        assert fr_location.region == "FR--"

    def test_same_name_in_a_different_region_of_the_same_country_does_not_match(self):
        LocationFactory(name={"Latn": "The Point"}, region="GB--")

        report = import_locations_csv(_csv(_row(name="The Point", region="Aberdeen")))

        assert report.created == 1
        assert Location.objects.filter(region="GBAB").exists()

    def test_ambiguous_match_is_an_error(self):
        LocationFactory(name={"Latn": "Duplicate"}, region="GB--")
        LocationFactory(name={"Latn": "Duplicate"}, region="GB--")

        report = import_locations_csv(_csv(_row(name="Duplicate")))

        assert report.skipped == 1
        assert "more than one location" in report.errors[0]


@pytest.mark.django_db
class TestIdempotency:
    def test_rerunning_the_same_file_reports_duplicates_not_new_rows(self):
        csv_text = _row(name="Repeatable Place")
        first = import_locations_csv(_csv(csv_text))
        assert (first.created, first.duplicates) == (1, 0)

        second = import_locations_csv(_csv(csv_text))
        assert (second.created, second.duplicates) == (0, 1)
        assert Location.objects.count() == 1
