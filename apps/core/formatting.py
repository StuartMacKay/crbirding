"""Formatting helpers for EURING-style ringing/resighting report lines.

A Resighting with a linked Capture gets the full 3-line format: marking
details, resighting details, and a computed distance/direction/elapsed
line. Without a linked Capture there's nothing to compare against, so
it's just the 2-line format: identifying details, then the resighting
itself.

This app's schema doesn't map onto the classic EURING recovery format
field-for-field, so a few things are substituted with the closest
equivalent available: the colour-mark encoding stands in for a metal ring
number, and the marking project's coordinator stands in for an individual
ringer's name, since neither of those is tracked separately here.
"""

import math
from dataclasses import dataclass
from itertools import groupby

from .models import Age, Sex, TagType

EARTH_RADIUS_KM = 6371.0
_COMPASS_POINTS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def decimal_to_dms(value, positive_suffix: str, negative_suffix: str) -> str:
    """57.25 -> "57°15'N" (given suffixes "N", "S")."""
    value = float(value)
    suffix = positive_suffix if value >= 0 else negative_suffix
    value = abs(value)
    degrees = int(value)
    minutes = round((value - degrees) * 60)
    if minutes == 60:
        minutes = 0
        degrees += 1
    return f"{degrees}°{minutes:02d}'{suffix}"


def format_coordinates(latitude, longitude) -> str | None:
    if latitude is None or longitude is None:
        return None
    return f"{decimal_to_dms(latitude, 'N', 'S')} {decimal_to_dms(longitude, 'E', 'W')}"


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


def format_tag(tag) -> str:
    """One physical tag's own notation, e.g. "BW(A123)d" or "PC" or "Y".

    The direction, if any, is the lowercase of its stored code (d/h/u),
    right after the inscription's closing bracket -- unambiguous, since
    a colour code only ever appears before the opening bracket. See
    apps.core.models.Direction for why this replaced arrow symbols.

    Doesn't include its Position -- that's added by format_tags when
    assembling the full stack, since a single tag's position only
    matters relative to the others on the same bird.
    """
    code = tag.colour + tag.second_colour
    if tag.kind == TagType.FLAG:
        code += "F"

    if tag.inscription:
        code += f"{tag.inscription_colour}({tag.inscription})"
        if tag.inscription_direction:
            code += tag.inscription_direction.lower()

    if tag.uncertain:
        code += "?"

    return code


def format_tags(tags) -> str | None:
    """The full colour-mark notation for a Resighting: tags sharing a
    Position are joined top-to-bottom with ",", and different Positions
    are joined with ";" -- e.g. "LA:O,Y; RB:BW(A123)d".
    """
    tags = sorted(tags, key=lambda tag: (tag.position, tag.order))
    if not tags:
        return None
    groups = groupby(tags, key=lambda tag: tag.position)
    return "; ".join(
        f"{position}:" + ",".join(format_tag(tag) for tag in group) for position, group in groups
    )


def describe_place(location, latitude=None, longitude=None) -> tuple[str, str | None]:
    lat = latitude if latitude is not None else location.latitude
    lon = longitude if longitude is not None else location.longitude
    place = f"{location.get_name()}, {location.place.country.name}"
    return place, format_coordinates(lat, lon)


def _code_or_blank(value: str, unknown_value: str) -> str:
    return value if value and value != unknown_value else ""


@dataclass
class RecoveryReport:
    lines: list[str]


def format_recovery_report(resighting) -> RecoveryReport:
    species = resighting.species
    species_label = f"{species.get_common_name()} ({species.scientific_name})"
    capture = resighting.capture

    # resighting.age is free text (the observer's own words), so it reads
    # oddly next to a bare EURING sex code -- use the display label
    # ("Male"/"Female") instead of the raw stored value here.
    resighting_age_sex = " ".join(filter(None, [resighting.age, resighting.get_sex_display()]))
    marks = format_tags(resighting.tags.all()) or "—"

    if capture is not None:
        capture_age = _code_or_blank(capture.age, Age.UNKNOWN)
        capture_sex = _code_or_blank(capture.sex, Sex.UNKNOWN)
        marking_place, marking_coords = describe_place(
            capture.location, *effective_coordinates(capture)
        )
        ringer = capture.project.coordinator if capture.project_id else ""
        line1 = (
            f"{species_label}  {marks}  {capture_age}{capture_sex}  "
            f"{capture.date:%d-%b-%Y}  {marking_place}: {marking_coords or ''} by {ringer}"
        ).strip()
    else:
        line1 = f"{species_label}  {marks}  {resighting_age_sex}".strip()

    obs_place, obs_coords = describe_place(resighting.location, *effective_coordinates(resighting))
    line2 = (
        f"{resighting.date:%d-%b-%Y}  {obs_place}: {obs_coords or ''} by {resighting.observer.name}"
    ).strip()

    lines = [line1, line2]

    if capture is not None:
        lat1, lon1 = effective_coordinates(capture)
        lat2, lon2 = effective_coordinates(resighting)
        if None not in (lat1, lon1, lat2, lon2):
            distance = haversine_distance_km(lat1, lon1, lat2, lon2)
            bearing = bearing_degrees(lat1, lon1, lat2, lon2)
            days = (resighting.date - capture.date).days
            lines.append(
                f"Distance: {distance:.0f} km. Direction: {bearing:.0f}° "
                f"({compass_point(bearing)}). Time elapsed: {days} days."
            )

    return RecoveryReport(lines=lines)


@dataclass
class Journey:
    """The 'ringed here, seen here' story for a resighting -- the
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
    distance_km: float | None


def describe_journey(resighting) -> Journey:
    species = resighting.species
    capture = resighting.capture

    observed_place = resighting.location.get_name()
    ringed_place = distance_km = None

    if capture is not None:
        ringed_place = capture.location.get_name()
        lat1, lon1 = effective_coordinates(capture)
        lat2, lon2 = effective_coordinates(resighting)
        if None not in (lat1, lon1, lat2, lon2):
            distance_km = haversine_distance_km(lat1, lon1, lat2, lon2)

    return Journey(
        species_common_name=species.get_common_name(),
        scientific_name=species.scientific_name,
        photo_url=resighting.photo.url if resighting.photo else None,
        date=resighting.date,
        observed_place=observed_place,
        observed_country=resighting.location.place.country.name,
        ringed_place=ringed_place,
        ringed_country=capture.location.place.country.name if capture else None,
        distance_km=distance_km,
    )
