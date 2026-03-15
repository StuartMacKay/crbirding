"""Exporting Locations to a CSV file -- the mirror of
core.utils.location_import, writing the same columns that import
reads. A Location is identified there by name, region, and country
(see core.utils.location_import), not by its internal id, so those --
not the id -- are what a row identifies it by here too, which is what
makes the file re-importable, and shareable between two databases that
have never exchanged a primary key.

region and country are written as their own EURING codes, not their
display label -- unambiguous and locale-independent, unlike a label,
which core.utils.location_import also accepts on the way back in.
"""

from django.conf import settings
from django.db.models import QuerySet

from ..models import Location
from .csv_export import write_csv

FIELDNAMES = ["name", "region", "country", "latitude", "longitude", "accuracy", "notes"]


def _row(location: Location) -> dict:
    primary_alphabet = settings.ALPHABETS[0][0]
    return {
        "name": location.name.get(primary_alphabet) or location.get_name(),
        "region": location.region,
        "country": location.get_country_code(),
        "latitude": location.latitude,
        "longitude": location.longitude,
        "accuracy": location.accuracy if location.accuracy is not None else "",
        "notes": location.notes,
    }


def export_locations_csv(queryset: QuerySet[Location] | None = None) -> str:
    queryset = Location.objects.all() if queryset is None else queryset
    locations = queryset.order_by("region", "name__Latn")
    return write_csv(FIELDNAMES, [_row(location) for location in locations])
