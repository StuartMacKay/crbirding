"""Formatting helpers for EURING-style origin/observation report lines.

A Observation with a linked Origin gets the full 3-line format: marking
details, observation details, and a computed distance/direction/elapsed
line. Without a linked Origin there's nothing to compare against, so
it's just the 2-line format: identifying details, then the observation
itself.

This app's schema doesn't map onto the classic EURING recovery format
field-for-field, so a few things are substituted with the closest
equivalent available: the colour-mark encoding stands in for a metal ring
number, and the marking project's coordinator stands in for an individual
ringer's name, since neither of those is tracked separately here.
"""

import math
from dataclasses import dataclass

from ..models import SPECIES_SCIENTIFIC_NAME, Position, Species
from .codes import parse_code

EARTH_RADIUS_KM = 6371.0
_COMPASS_POINTS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def format_coordinates(latitude, longitude) -> str | None:
    """Signed decimal degrees, latitude first -- e.g. "57.2500, -0.5000".
    Each value is shown exactly as stored, so a DecimalField's own
    precision (trailing zeros included) carries through unchanged.
    """
    if latitude is None or longitude is None:
        return None
    return f"{latitude}, {longitude}"


def haversine_distance_km(lat1, lon1, lat2, lon2) -> float:
    """Great-circle distance between two points, in kilometres."""
    lat1, lon1, lat2, lon2 = (math.radians(float(v)) for v in (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return EARTH_RADIUS_KM * 2 * math.asin(math.sqrt(a))


def bearing_degrees(lat1, lon1, lat2, lon2) -> float:
    """Initial compass bearing from point 1 to point 2, in degrees (0-360)."""
    lat1, lon1, lat2, lon2 = (math.radians(float(v)) for v in (lat1, lon1, lat2, lon2))
    dlon = lon2 - lon1
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    return (math.degrees(math.atan2(x, y)) + 360) % 360


def compass_point(degrees: float) -> str:
    return _COMPASS_POINTS[round(degrees / 45) % 8]


def effective_coordinates(record):
    """The record's own lat/long if set, else its Location's."""
    lat = record.latitude if record.latitude is not None else record.location.latitude
    lon = record.longitude if record.longitude is not None else record.location.longitude
    return lat, lon


def format_tags(tags) -> str | None:
    """All of an Observation's tags as one line, e.g.
    "LA:R,WN(KY); RA:M,WN(KY)" -- each Position's code, labelled.
    """
    tags = sorted(tags, key=lambda tag: tag.position)
    if not tags:
        return None
    return "; ".join(f"{tag.position}:{tag.code}" for tag in tags)


# Reading order for a compact display of the marks on a bird -- top to
# bottom, left before right: nasal saddle, neck collar, then each
# wing/leg pair with the higher segment (wing, or the leg's "above" --
# i.e. tibia) before the lower one ("below" -- i.e. tarsus).
_COMPACT_POSITION_ORDER = {
    position: index
    for index, position in enumerate(
        [
            Position.NASAL_SADDLE,
            Position.NECK_COLLAR,
            Position.LEFT_WING,
            Position.LEFT_ABOVE,
            Position.LEFT_BELOW,
            Position.RIGHT_WING,
            Position.RIGHT_ABOVE,
            Position.RIGHT_BELOW,
        ]
    )
}


def format_colour_marks(tags) -> str | None:
    """A shortened version of format_tags(), for display where space is
    tight -- e.g. a list column. Drops metal rings (Colour.METAL or
    Colour.OTHER on its own, rather than an actual colour mark) -- not a
    "colour mark" itself, and already in the full display elsewhere.
    Positions are read
    in the same order the marks would be read on the bird -- see
    _COMPACT_POSITION_ORDER -- rather than format_tags()'s alphabetical
    order, and aren't labelled: with the reading order fixed, the
    position is implied by where in the sequence a mark falls.

    e.g. "LB:M; RB:BW(M556)" -> "BW(M556)": the metal ring at LB is
    dropped entirely.
    """
    stacks = []
    for tag in sorted(tags, key=lambda tag: _COMPACT_POSITION_ORDER[tag.position]):
        marks = [mark for mark in parse_code(tag.code) if not mark.is_metal]
        if marks:
            stacks.append(",".join(mark.format() for mark in marks))
    return "; ".join(stacks) or None


def describe_place(location, latitude=None, longitude=None) -> tuple[str, str | None]:
    lat = latitude if latitude is not None else location.latitude
    lon = longitude if longitude is not None else location.longitude
    parts = [location.get_name()]
    # A country-level Location's region is the country's own code --
    # naming it as well would just repeat the country.
    if location.region != location.get_country_code():
        parts.append(str(location.get_region_display()))
    parts.append(str(location.get_country_display()))
    place = ", ".join(parts)
    return place, format_coordinates(lat, lon)


@dataclass
class RecoveryReport:
    lines: list[str]


def format_recovery_report(observation) -> RecoveryReport:
    species_label = (
        f"{Species(observation.species).label} ({SPECIES_SCIENTIFIC_NAME[observation.species]})"
    )
    origin = observation.origin

    marks = format_tags(observation.tags.all()) or "—"

    if origin is not None:
        marking_place, marking_coords = describe_place(
            origin.location, *effective_coordinates(origin)
        )
        ringer = origin.project.coordinator if origin.project_id else ""
        line1 = (
            f"{species_label}  {marks}  {origin.age}{origin.sex}  "
            f"{origin.date:%d-%b-%Y}  {marking_place}: {marking_coords or ''} by {ringer}"
        ).strip()
    else:
        line1 = f"{species_label}  {marks}".strip()

    observer_names = ", ".join(observer.name for observer in observation.observers.all())
    obs_place, obs_coords = describe_place(
        observation.location, *effective_coordinates(observation)
    )
    observed_when = f"{observation.date:%d-%b-%Y}"
    if observation.time is not None:
        observed_when += f" {observation.time:%H:%M}"
    age = observation.get_age_display() or "Unknown"
    sex = observation.get_sex_display() or "Unknown"
    age_and_sex = f"Age: {age}  Sex: {sex}"
    line2 = (
        f"{observed_when}  {age_and_sex}  {obs_place}: {obs_coords or ''} by {observer_names}"
    ).strip()

    lines = [line1, line2]

    if origin is not None:
        lat1, lon1 = effective_coordinates(origin)
        lat2, lon2 = effective_coordinates(observation)
        if None not in (lat1, lon1, lat2, lon2, origin.date):
            distance = haversine_distance_km(lat1, lon1, lat2, lon2)
            bearing = bearing_degrees(lat1, lon1, lat2, lon2)
            days = (observation.date - origin.date).days
            lines.append(
                f"Distance: {distance:.0f} km. Direction: {bearing:.0f}° "
                f"({compass_point(bearing)}). Time elapsed: {days} days."
            )

    return RecoveryReport(lines=lines)


@dataclass
class Sighting:
    """What was seen, and when and where -- the values the
    core/_observation_email.html snippet lays out. Blank age/sex stay
    blank here; how to show "not recorded" is up to each template.
    """

    species: str
    scientific_name: str
    marks: str | None
    date: object
    time: object
    age: str
    sex: str
    place: str
    coordinates: str | None
    observers: str


def describe_sighting(observation) -> Sighting:
    place, coordinates = describe_place(observation.location, *effective_coordinates(observation))
    return Sighting(
        species=str(Species(observation.species).label),
        scientific_name=SPECIES_SCIENTIFIC_NAME[observation.species],
        marks=format_tags(observation.tags.all()),
        date=observation.date,
        time=observation.time,
        age=str(observation.get_age_display()),
        sex=str(observation.get_sex_display()),
        place=place,
        coordinates=coordinates,
        observers=", ".join(observer.name for observer in observation.observers.all()),
    )


@dataclass
class Marking:
    """When, where, and by whom a bird was marked -- the Origin side of
    a Recovery."""

    date: object
    time: object
    age: str
    sex: str
    place: str
    coordinates: str | None
    label: str
    project: object


def describe_marking(origin) -> Marking:
    place, coordinates = describe_place(origin.location, *effective_coordinates(origin))
    return Marking(
        date=origin.date,
        time=origin.time,
        age=str(origin.get_age_display()),
        sex=str(origin.get_sex_display()),
        place=place,
        coordinates=coordinates,
        label=origin.label,
        project=origin.project if origin.project_id else None,
    )


@dataclass
class Recovery:
    """A marked bird seen again -- the values the core/_recovery.html
    snippet lays out. Always has a distance: both sides fall back to
    their Location's own (required) coordinates. `days` is None when the
    ringing date isn't known.
    """

    marking: Marking
    sighting: Sighting
    distance_km: float
    bearing: float
    direction: str
    days: int | None


def describe_recovery(observation) -> Recovery | None:
    """None for an observation not (yet) linked to its Origin."""
    origin = observation.origin
    if origin is None:
        return None

    lat1, lon1 = effective_coordinates(origin)
    lat2, lon2 = effective_coordinates(observation)
    bearing = bearing_degrees(lat1, lon1, lat2, lon2)
    return Recovery(
        marking=describe_marking(origin),
        sighting=describe_sighting(observation),
        distance_km=haversine_distance_km(lat1, lon1, lat2, lon2),
        bearing=bearing,
        direction=compass_point(bearing),
        days=(observation.date - origin.date).days if origin.date else None,
    )


@dataclass
class Journey:
    """The 'ringed here, seen here' story for a observation -- the
    engaging headline for the home page, as opposed to the precise
    RecoveryReport lines above."""

    species_common_name: str
    scientific_name: str
    photo_url: str | None
    date: object
    observed_place: str
    observed_country: str
    ringed_place: str | None
    ringed_country: str | None
    label: str | None
    distance_km: float | None


def describe_journey(observation) -> Journey:
    origin = observation.origin

    observed_place = observation.location.get_name()
    ringed_place = distance_km = None

    if origin is not None:
        ringed_place = origin.location.get_name()
        lat1, lon1 = effective_coordinates(origin)
        lat2, lon2 = effective_coordinates(observation)
        if None not in (lat1, lon1, lat2, lon2):
            distance_km = haversine_distance_km(lat1, lon1, lat2, lon2)

    first_photo = observation.photos.first()

    return Journey(
        species_common_name=str(Species(observation.species).label),
        scientific_name=SPECIES_SCIENTIFIC_NAME[observation.species],
        photo_url=first_photo.image.url if first_photo else None,
        date=observation.date,
        observed_place=observed_place,
        observed_country=observation.location.get_country_display(),
        ringed_place=ringed_place,
        ringed_country=origin.location.get_country_display() if origin else None,
        label=origin.label if origin else None,
        distance_km=distance_km,
    )
