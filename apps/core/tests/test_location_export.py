import csv
import io

import pytest

from core.models import Location
from core.utils.location_export import export_locations_csv
from core.utils.location_import import import_locations_csv

from .factories import LocationFactory


def _parse(csv_text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(csv_text)))


@pytest.mark.django_db
class TestLocationExport:
    def test_header_matches_the_importer(self):
        csv_text = export_locations_csv()
        header = csv_text.splitlines()[0]
        assert header == "name,region,country,latitude,longitude,accuracy,notes"

    def test_exports_a_location(self):
        LocationFactory(
            name={"Latn": "South Park"},
            region="GB--",
            latitude="51.5074",
            longitude="-0.1278",
            accuracy=50,
            notes="A nice spot.",
        )

        rows = _parse(export_locations_csv())

        assert len(rows) == 1
        row = rows[0]
        assert row["name"] == "South Park"
        assert row["region"] == "GB--"
        assert row["country"] == "GB--"
        assert row["latitude"] == "51.5074"
        assert row["longitude"] == "-0.1278"
        assert row["accuracy"] == "50"
        assert row["notes"] == "A nice spot."

    def test_blank_accuracy_is_an_empty_field(self):
        LocationFactory(accuracy=None)

        row = _parse(export_locations_csv())[0]

        assert row["accuracy"] == ""

    def test_only_the_given_queryset_is_exported(self):
        LocationFactory(name={"Latn": "Included"}, region="GB--")
        LocationFactory(name={"Latn": "Excluded"}, region="GB--")

        rows = _parse(export_locations_csv(Location.objects.filter(name__Latn="Included")))

        assert [row["name"] for row in rows] == ["Included"]

    def test_round_trips_through_the_importer(self):
        LocationFactory(
            name={"Latn": "South Park"},
            region="GB--",
            latitude="51.5074",
            longitude="-0.1278",
            accuracy=50,
        )
        csv_text = export_locations_csv()

        report = import_locations_csv(io.BytesIO(csv_text.encode()))

        assert report.errors == []
        assert (report.created, report.duplicates) == (0, 1)
