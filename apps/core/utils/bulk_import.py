"""Bulk-importing historical Observation records from a CSV file someone
provides -- either their own sightings, or a whole life history for one
bird that a project coordinator has sent back, covering several
observers at once.

Distinct from the "import from reference data" admin views (see
core.admin.country/place), which import from the maintainer-curated
EURING reference file bundled with the app -- this is a one-off personal
data migration, not an ongoing sync. Species is a closed, baked-in list
(see core.models.species) so every EURING code is always resolvable
without any prior setup. Location and Observer, unlike species, aren't
closed lists -- a row naming one that doesn't exist yet creates it (see
_resolve_location and _resolve_observer), which is what makes this usable
directly on a life history a project coordinator hands back: that file
was never going to name *this* database's internal ids for places and
people it doesn't yet know about.

Each row's `owner` is whichever registered user (if any) its resolved
Observer's `user` is -- never whoever is running the import. That's
what keeps a life history's other observers' rows out of the importing
user's My Observations page, without this needing to know anything
about who's asking: a historical or unregistered Observer with no
linked user leaves the row unowned, visible to nobody's My
Observations, only wherever a bird's full history (across every
observer) is eventually shown.

CSV columns: species, age, sex, location, region, country, observer,
date, time, latitude, longitude, accuracy, notes, plus one column per
tag Position -- left_above, left_below, left_wing, nasal_saddle,
neck_collar, right_above, right_below, right_wing. species, location,
region, country, observer, and date are required; the rest, including
every position column, may be blank -- but at least one position column
must have a value somewhere in the file, and the file must include at
least one of them. Each position column holds the code for what's worn
there, top to bottom -- e.g. a neck_collar of "WB(A123)u" and a
right_below of "O,Y" (see core.utils.codes for the notation).
Spreading positions across columns catches a code typed into the wrong
slot at a glance, which a mis-typed position prefix could bury in
mismatched sightings that only surface later, if at all.

species accepts its 5-digit EURING code, its scientific name, or its
common name (in whichever language, since translations are just
gettext catalogs over the same fixed list of labels).

age and sex, like region and country, accept either their EURING code
or their display label -- e.g. an age of "9" or "4CY", a sex of "M" or
"Male". Both are optional and default to "unknown" when blank, since a
field sighting often can't age or sex a bird the way a ringer holding
it in the hand can.

location, region, and country are text, matched the same way the
web submission form's own location picker works: country narrows which
region a name can mean (region names aren't unique across countries --
"region" alone is exactly as ambiguous here as it is in
core.forms.LocationForm's own country-then-region fields), and location
is then matched by name within that region. Both region and country
accept either their EURING code or their display label, the same as
species does. If no existing Location matches all three, a new
one is created from the row's own latitude, longitude, and accuracy --
which must all be given in that case, the same requirement
core.forms.LocationForm makes of a new location described through the
web form. Two rows are free to disagree about a name -- "Old Mill" one
week, "the Mill (locals)" the next -- since each is looked up
independently; what matters is that a life history's rows, taken
together, don't invent a new Location per row for what's really the
same place.

observer is matched by name (case-insensitively) against every existing
Observer -- an Observer can be linked to one specific registered user
(see Observer.user, core.views.observation.SubmitObservationView.
_observer_for), and a self-import naming that user by their own name
needs to find their own Observer record, not create a second,
unlinked one for the same person. A name match must be unambiguous: if
more than one Observer shares the name, the row is rejected rather
than guessed at. If none matches, a new Observer with no linked user
is created -- exactly the "historical observer with no account of
their own" case described above.

Re-running an import (e.g. an original file plus fixes for the rows
that failed, or the same life history a second time) is safe: a row
whose species, date, and tags already match an existing
Observation is recognised as one already imported and skipped, rather
than creating a duplicate -- deliberately not also matching on
location, observer, or time, since those are exactly what two
independently-kept records of the same sighting are likely to disagree
on (see _import_row). The tags are compared with "?" left out
(core.utils.matching.loose_signature): the same file re-read, or a
coordinator's copy of it, may well record uncertainty differently.

A newly imported row whose tags exactly match an already-identified
sighting of the same species is linked to that bird's Origin, the same
as one entered through the web form (see link_to_known_bird).

Since time isn't part of the match, the same bird read twice in one
day -- a real, common occurrence, not a re-run -- is also reported as
a duplicate. That's correct, but indistinguishable from a genuine
already-imported row by count alone, so ImportReport.duplicate_details
carries one line per such row naming which earlier row (and what time)
it matches -- e.g. "Row 82: this bird was already logged earlier that
day, at 15:47." -- so it reads as an intentional, understood outcome
rather than something that looks like a bug. Only a same-day
resighting first introduced *by this same import run* gets a note:
nothing about an Observation records whether some earlier import
already explained a duplicate of it, so re-running a whole file (e.g.
after fixing an unrelated row's error) would otherwise re-explain
every already-imported same-day pair on every single run. See
_import_row for exactly how that's told apart from a genuinely new
same-day resighting. Anyone who does want a same-day resighting kept
as its own record can still add it by hand afterwards.
"""

import datetime
from decimal import Decimal

from django.conf import settings
from django.db import transaction

from ..models import Age, Location, Observation, Observer, Position, Sex, Tag
from .codes import normalise_code
from .csv_import import (
    ImportReport,
    normalized_dict_reader,
    parse_decimal,
    parse_int,
    resolve_choice,
    resolve_country,
    resolve_region,
    resolve_species,
)
from .matching import link_to_known_bird, loose_signature

REQUIRED_COLUMNS = {"species", "location", "region", "country", "observer", "date"}
POSITION_COLUMNS = {position.name.lower(): position.value for position in Position}


def _parse_date(value: str) -> datetime.date:
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"{value!r} is not a valid date -- use YYYY-MM-DD") from None


def _parse_time(value: str) -> datetime.time | None:
    return datetime.time.fromisoformat(value) if value else None


def _resolve_age(value: str) -> str:
    """The EURING age code matching `value` -- by code, or by its
    display label. Blank leaves it blank (not recorded), since a field
    sighting often can't age a bird at all.
    """
    return resolve_choice(value, Age, "age", default="")


def _resolve_sex(value: str) -> str:
    """The EURING sex code matching `value` -- by code, or by its
    display label. Blank leaves it blank (not recorded).
    """
    return resolve_choice(value, Sex, "sex", default="")


def _resolve_location(
    name: str,
    region_value: str,
    country_value: str,
    latitude: Decimal | None,
    longitude: Decimal | None,
    accuracy: int | None,
) -> tuple[Location, bool]:
    """The Location named `name` in that region/country, or a newly
    created one if none matches. Returns (location, created) -- callers
    need to know which, since a freshly created Location's own
    coordinates (just set from this same row) shouldn't also become a
    redundant per-observation override (see _import_row).
    """
    name = name.strip()
    if not name:
        raise ValueError("no location given")

    country_code = resolve_country(country_value)
    region_code = resolve_region(region_value, country_code)

    matches = list(Location.objects.filter(name__Latn__iexact=name, region=region_code))
    if len(matches) == 1:
        return matches[0], False
    if len(matches) > 1:
        raise ValueError(f"{name!r} matches more than one location in that region")

    if latitude is None or longitude is None or accuracy is None:
        raise ValueError(
            f"no location matching {name!r} -- latitude, longitude, and accuracy "
            "are required to add it as a new one"
        )
    primary_alphabet = settings.ALPHABETS[0][0]
    location = Location.objects.create(
        name={primary_alphabet: name},
        region=region_code,
        latitude=latitude,
        longitude=longitude,
        accuracy=accuracy,
    )
    return location, True


def _resolve_observer(value: str) -> Observer:
    value = value.strip()
    if not value:
        raise ValueError("no observer given")

    matches = list(Observer.objects.filter(name__iexact=value))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise ValueError(f"{value!r} matches more than one observer")

    return Observer.objects.create(name=value)


def _parse_position_tags(row: dict) -> list[Tag]:
    """A (not yet saved) Tag for each of the row's filled-in position
    columns, its code written the standard way -- e.g. left_below="y"
    and right_below="O, Y" give Tags "Y" at LB and "O,Y" at RB.
    """
    tags = []
    for column, position in POSITION_COLUMNS.items():
        code = row.get(column, "").strip()
        if not code:
            continue
        try:
            tags.append(Tag(position=position, code=normalise_code(code)))
        except ValueError as exc:
            raise ValueError(f"{column}: {exc}") from None
    return tags


def _import_row(
    row: dict, created_this_run: dict[tuple[str, datetime.date, str], list[datetime.time | None]]
) -> tuple[bool, str | None]:
    """Create the Observation for this row. Returns (False, note),
    without creating anything, if one with the same identity already
    exists (species + date + tags, matched regardless of
    time -- see the module docstring). `note` explains which earlier
    row *in this same import run* it matches, so a genuine same-day
    resighting reads as an intentional, expected outcome rather than a
    silent count someone might mistake for a bug -- and `note` is None
    for a duplicate of data from an *earlier* run, since there's
    nothing this run itself is telling the caller that they haven't
    already been told (see created_this_run below, and the module
    docstring). Returns (True, None) for a newly created Observation.

    created_this_run records the (species, date, signature) -> times
    of every Observation this same call to import_observations_csv has
    itself created so far, so a duplicate can be explained against
    *this run's own* earlier rows without querying, from stored data
    alone, something no Observation actually records: whether an
    earlier reading it matches was already explained in some previous
    import. Only a row that was itself newly created this run gets
    added -- a duplicate row contributes nothing new to explain later
    rows against, so a full re-run (every row a duplicate of
    pre-existing data) naturally stays silent throughout.
    """
    species = resolve_species(row["species"])
    age = _resolve_age(row.get("age", "").strip())
    sex = _resolve_sex(row.get("sex", "").strip())
    date = _parse_date(row["date"].strip())
    time = _parse_time(row.get("time", "").strip())
    latitude = parse_decimal(row.get("latitude", "").strip())
    longitude = parse_decimal(row.get("longitude", "").strip())
    accuracy = parse_int(row.get("accuracy", "").strip())

    location, location_created = _resolve_location(
        row["location"], row["region"], row["country"], latitude, longitude, accuracy
    )
    observer = _resolve_observer(row["observer"])

    tags = _parse_position_tags(row)
    if not tags:
        raise ValueError("no tags given")
    signature = loose_signature(tags)

    # Matched on species, date, and the tags alone -- not
    # location, observer, or time. Those are exactly the fields two
    # independently-kept records of the same real sighting are likely
    # to disagree on (a project's life history won't necessarily name
    # the site or observer the way this row's own submitter did), while
    # species + date + a uniquely colour-marked individual's full tag
    # set is already about as strong an identity signal as a sighting
    # has. The tradeoff: two genuinely different sightings of the same
    # bird on the same day at different places would also collide here
    # -- rare enough, for an individually marked bird, to accept.
    existing = Observation.objects.filter(species=species, date=date).prefetch_related("tags")
    is_duplicate = any(
        loose_signature(observation.tags.all()) == signature for observation in existing
    )
    if is_duplicate:
        key = (species, date, signature)
        earlier_this_run = [
            earlier_time
            for earlier_time in created_this_run.get(key, [])
            if earlier_time is not None and time is not None and earlier_time < time
        ]
        if earlier_this_run:
            note = (
                f"this bird was already logged earlier that day, at {max(earlier_this_run):%H:%M}."
            )
        else:
            note = None
        return False, note

    observation = Observation.objects.create(
        species=species,
        age=age,
        sex=sex,
        location=location,
        date=date,
        time=time,
        # A newly created Location's own coordinates -- just set above,
        # from this same row -- are already the precise ones, so no
        # separate override applies on top of themselves (the same rule
        # LocationForm.resolve() follows for a location added through
        # the web form). For an existing Location, the row's own
        # reading, if given, becomes this Observation's own override.
        latitude=None if location_created else latitude,
        longitude=None if location_created else longitude,
        accuracy=None if location_created else accuracy,
        notes=row.get("notes", "").strip(),
        # Whichever registered user (if any) that row's Observer is
        # linked to -- not whoever is running this import. A life
        # history a project sends back covers many observers at once;
        # each row should land in *that* person's My Observations, not
        # the importer's, and a historical/unregistered observer's row
        # should show up in neither.
        owner=observer.user,
    )
    observation.observers.add(observer)
    for tag in tags:
        tag.observation = observation
    Tag.objects.bulk_create(tags)
    link_to_known_bird(observation)
    created_this_run.setdefault((species, date, signature), []).append(time)
    return True, None


def import_observations_csv(file) -> ImportReport:
    report = ImportReport()
    reader = normalized_dict_reader(file)

    missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
    if missing:
        report.errors.append(f"CSV is missing required columns: {', '.join(sorted(missing))}")
        return report

    if not set(reader.fieldnames or []) & set(POSITION_COLUMNS):
        report.errors.append(
            "CSV must include at least one tag position column: "
            f"{', '.join(sorted(POSITION_COLUMNS))}"
        )
        return report

    created_this_run: dict[tuple[str, datetime.date, str], list[datetime.time | None]] = {}
    for row_number, row in enumerate(reader, start=2):  # header is row 1
        try:
            with transaction.atomic():
                created, note = _import_row(row, created_this_run)
        except (ValueError, KeyError) as exc:
            report.errors.append(f"Row {row_number}: {exc}")
            report.skipped += 1
            continue
        if created:
            report.created += 1
        else:
            report.duplicates += 1
            if note:
                report.duplicate_details.append(f"Row {row_number}: {note}")

    return report
