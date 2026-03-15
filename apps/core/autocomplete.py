"""Registers this app's autocomplete search functions -- see
autocomplete.registry. Imported from CoreConfig.ready() so the
registrations exist regardless of which admin/forms module happens to
get imported first.
"""

from autocomplete.registry import register
from django.conf import settings
from django.db.models import Q

from .models import PLACE_TO_COUNTRY, Country, Location, Region, Species


def _matches(choices, query: str) -> list[tuple[str, str]]:
    query = query.lower()
    matches = [(code, str(label)) for code, label in choices if query in str(label).lower()]
    matches.sort(key=lambda pair: pair[1])
    return matches


def search_country(query: str, **_parents) -> list[tuple[str, str]]:
    return _matches(Country.choices, query)


def search_region(query: str, country: str = "", **_parents) -> list[tuple[str, str]]:
    choices = Region.choices
    if country:
        choices = [(code, label) for code, label in choices if PLACE_TO_COUNTRY[code] == country]
    return _matches(choices, query)


def search_species(query: str, **_parents) -> list[tuple[str, str]]:
    return _matches(Species.choices, query)


def search_location(query: str, region: str = "", **_parents) -> list[tuple[str, str]]:
    """Existing Locations, shared by everyone using the site."""
    qs = Location.objects.all()
    if region:
        qs = qs.filter(region=region)
    if query:
        name_matches = Q()
        for code, _label in settings.ALPHABETS:
            name_matches |= Q(**{f"name__{code}__icontains": query})
        qs = qs.filter(name_matches)
    locations = list(qs[:200])
    matches = [(str(location.pk), str(location)) for location in locations]
    matches.sort(key=lambda pair: pair[1])
    return matches


def register_autocompletes() -> None:
    register("country", search_country)
    register("region", search_region)
    register("species", search_species)
    register("location", search_location)
