import io

import pytest

from core.models import Age, Location, Observation, Observer, Sex, Species
from core.utils.bulk_import import import_observations_csv

from .factories import (
    LocationFactory,
    ObservationFactory,
    ObserverFactory,
    OriginFactory,
    TagFactory,
    UserFactory,
)

SPECIES_CODE = Species.COMMON_OSTRICH
SPECIES_NAME = "Struthio camelus"

# Matches LocationFactory's own default region ("GB--") -- region and
# country have different labels for the same code, which is the more
# interesting case to exercise than a country like France, whose region
# and country labels happen to be identical.
REGION = "Great Britain"
COUNTRY = "United Kingdom"

HEADER = "species,location,region,country,observer,date,latitude,longitude,accuracy,left_below"


def _csv(text: str) -> io.BytesIO:
    return io.BytesIO(text.encode())


def _rows(*row_overrides: dict) -> str:
    """A CSV file with HEADER's columns, one line per dict of
    overrides on top of a sensible default row. Coordinates are
    included by default (matching LocationFactory's own) purely so a
    row whose location isn't pre-created still resolves -- as a new
    Location -- rather than every test that doesn't care about location
    resolution having to either pre-create one or pass coordinates
    itself.
    """
    lines = [HEADER]
    for overrides in row_overrides:
        fields = {
            "species": SPECIES_CODE,
            "location": "Test Location",
            "region": REGION,
            "country": COUNTRY,
            "observer": "Jo Smith",
            "date": "2026-01-01",
            "latitude": "51.5074",
            "longitude": "-0.1278",
            "accuracy": "50",
            "left_below": "Y",
        }
        fields.update(overrides)
        lines.append(",".join(str(fields[column]) for column in HEADER.split(",")))
    return "\n".join(lines) + "\n"


def _row(**overrides) -> str:
    return _rows(overrides)


@pytest.mark.django_db
class TestColumnValidation:
    def test_missing_required_columns_reported(self):
        report = import_observations_csv(
            _csv("species,location,date,left_below\n00010,Somewhere,2026-01-01,Y\n")
        )
        assert report.errors == ["CSV is missing required columns: country, observer, region"]
        assert report.created == 0

    def test_no_position_columns_reported(self):
        csv_text = "species,location,region,country,observer,date\n" + (
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01\n"
        )
        report = import_observations_csv(_csv(csv_text))
        assert len(report.errors) == 1
        assert "must include at least one tag position column" in report.errors[0]
        assert report.created == 0


@pytest.mark.django_db
class TestDateParsing:
    def test_non_iso_date_gives_a_user_friendly_error(self):
        """A day-first or month-first date isn't just rejected -- it's
        rejected with a message that says what format is expected,
        rather than surfacing the stdlib's own "Invalid isoformat
        string" wording.
        """
        report = import_observations_csv(_csv(_row(date="07/02/2026")))

        assert report.created == 0
        assert report.skipped == 1
        assert report.errors == ["Row 2: '07/02/2026' is not a valid date -- use YYYY-MM-DD"]


@pytest.mark.django_db
class TestSpeciesResolution:
    def test_resolved_by_euring_code(self):
        report = import_observations_csv(_csv(_row(species=SPECIES_CODE)))
        assert report.errors == []
        assert report.created == 1
        assert Observation.objects.get().species == SPECIES_CODE

    def test_resolved_by_scientific_name(self):
        report = import_observations_csv(_csv(_row(species=SPECIES_NAME)))
        assert report.created == 1
        assert Observation.objects.get().species == SPECIES_CODE

    def test_resolved_by_common_name(self):
        report = import_observations_csv(_csv(_row(species="Common Ostrich")))
        assert report.created == 1
        assert Observation.objects.get().species == SPECIES_CODE

    def test_unknown_name_is_an_error(self):
        report = import_observations_csv(_csv(_row(species="Not a real bird")))
        assert report.created == 0
        assert report.skipped == 1
        assert "no species matching" in report.errors[0]


@pytest.mark.django_db
class TestAgeAndSexResolution:
    def _csv_with(self, age: str = "", sex: str = "") -> io.BytesIO:
        csv_text = (
            "species,age,sex,location,region,country,observer,date,"
            "latitude,longitude,accuracy,left_below\n"
            f"{SPECIES_CODE},{age},{sex},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,"
            "51.5074,-0.1278,50,Y\n"
        )
        return _csv(csv_text)

    def test_blank_is_left_blank(self):
        report = import_observations_csv(self._csv_with())
        assert report.errors == []
        observation = Observation.objects.get()
        assert observation.age == ""
        assert observation.sex == ""

    def test_resolved_by_euring_code(self):
        report = import_observations_csv(self._csv_with(age="9", sex="M"))
        assert report.errors == []
        observation = Observation.objects.get()
        assert observation.age == Age.FOURTH_YEAR
        assert observation.sex == Sex.MALE

    def test_resolved_by_display_label(self):
        report = import_observations_csv(self._csv_with(age="4CY", sex="Male"))
        assert report.errors == []
        observation = Observation.objects.get()
        assert observation.age == Age.FOURTH_YEAR
        assert observation.sex == Sex.MALE

    def test_label_match_is_case_insensitive(self):
        report = import_observations_csv(self._csv_with(age="4cy", sex="male"))
        assert report.errors == []
        observation = Observation.objects.get()
        assert observation.age == Age.FOURTH_YEAR
        assert observation.sex == Sex.MALE

    def test_unknown_age_is_an_error(self):
        report = import_observations_csv(self._csv_with(age="not a real age"))
        assert report.created == 0
        assert report.skipped == 1
        assert "no age matching" in report.errors[0]

    def test_unknown_sex_is_an_error(self):
        report = import_observations_csv(self._csv_with(sex="not a real sex"))
        assert report.created == 0
        assert report.skipped == 1
        assert "no sex matching" in report.errors[0]

    def test_columns_are_optional(self):
        """A file with no age/sex columns at all -- the common case for
        an older export -- still imports, leaving both blank.
        """
        LocationFactory(name={"Latn": "Test Location"}, region="GB--")
        report = import_observations_csv(_csv(_row()))
        assert report.errors == []
        observation = Observation.objects.get()
        assert observation.age == ""
        assert observation.sex == ""


@pytest.mark.django_db
class TestLocationResolution:
    def test_matches_an_existing_location_by_name_region_and_country(self):
        location = LocationFactory(name={"Latn": "South Park"}, region="GB--")

        report = import_observations_csv(_csv(_row(location="South Park")))

        assert report.created == 1
        assert Observation.objects.get().location_id == location.pk

    def test_match_is_case_insensitive(self):
        location = LocationFactory(name={"Latn": "South Park"}, region="GB--")

        report = import_observations_csv(_csv(_row(location="south park")))

        assert report.created == 1
        assert Observation.objects.get().location_id == location.pk

    def test_same_name_in_a_different_country_does_not_match(self):
        """Region and country are part of the match key precisely so a
        name shared by two real places (a common occurrence) doesn't
        collide -- see core.utils.bulk_import's module docstring.
        """
        gb_location = LocationFactory(name={"Latn": "Harbour Wall"}, region="GB--")
        fr_location = LocationFactory(name={"Latn": "Harbour Wall"}, region="FR--")

        report = import_observations_csv(
            _csv(_row(location="Harbour Wall", region="France", country="France"))
        )

        assert report.created == 1
        observation = Observation.objects.get()
        assert observation.location_id == fr_location.pk
        assert observation.location_id != gb_location.pk

    def test_ambiguous_location_name_is_an_error(self):
        LocationFactory(name={"Latn": "Duplicate"}, region="GB--")
        LocationFactory(name={"Latn": "Duplicate"}, region="GB--")

        report = import_observations_csv(_csv(_row(location="Duplicate")))

        assert report.skipped == 1
        assert "more than one location" in report.errors[0]

    def test_unknown_country_is_an_error(self):
        report = import_observations_csv(_csv(_row(country="Not a real country")))
        assert report.skipped == 1
        assert "no country matching" in report.errors[0]

    def test_unknown_region_is_an_error(self):
        report = import_observations_csv(_csv(_row(region="Not a real region")))
        assert report.skipped == 1
        assert "no region matching" in report.errors[0]

    def test_creates_a_new_location_when_none_matches(self):
        report = import_observations_csv(
            _csv(
                _row(
                    location="Brand New Site",
                    latitude="51.5074",
                    longitude="-0.1278",
                    accuracy="50",
                )
            )
        )

        assert report.errors == []
        assert report.created == 1
        location = Observation.objects.get().location
        assert location.get_name() == "Brand New Site"
        assert location.region == "GB--"
        assert str(location.latitude) == "51.5074"
        assert str(location.longitude) == "-0.1278"
        assert location.accuracy == 50

    def test_new_location_without_coordinates_is_an_error(self):
        report = import_observations_csv(
            _csv(_row(location="No Coordinates Given", latitude="", longitude="", accuracy=""))
        )

        assert report.skipped == 1
        assert "latitude, longitude, and accuracy are required" in report.errors[0]
        assert Location.objects.filter(name__Latn="No Coordinates Given").exists() is False

    def test_new_locations_own_coordinates_are_not_also_saved_as_an_override(self):
        """The coordinates given for a new Location are its own base
        coordinates -- they don't also become a redundant per-sighting
        override on top of themselves (compare
        test_views_resighting.py's identical rule for the web form).
        """
        report = import_observations_csv(
            _csv(
                _row(
                    location="Brand New Site",
                    latitude="51.5074",
                    longitude="-0.1278",
                    accuracy="50",
                )
            )
        )
        assert report.created == 1
        observation = Observation.objects.get()
        assert observation.latitude is None
        assert observation.longitude is None
        assert observation.accuracy is None

    def test_existing_locations_coordinates_become_an_observation_override(self):
        location = LocationFactory(
            name={"Latn": "South Park"},
            region="GB--",
            latitude="51.0000",
            longitude="-1.0000",
            accuracy=100,
        )

        report = import_observations_csv(
            _csv(
                _row(
                    location="South Park",
                    latitude="51.2345",
                    longitude="-1.2345",
                    accuracy="25",
                )
            )
        )

        assert report.created == 1
        observation = Observation.objects.get()
        assert str(observation.latitude) == "51.2345"
        assert str(observation.longitude) == "-1.2345"
        assert observation.accuracy == 25
        location.refresh_from_db()
        assert str(location.latitude) == "51.0000"
        assert location.accuracy == 100


@pytest.mark.django_db
class TestObserverResolution:
    def test_matches_an_existing_observer_by_name(self):
        observer = ObserverFactory(name="Jo Smith")

        report = import_observations_csv(_csv(_row(observer="Jo Smith")))

        assert report.created == 1
        assert list(Observation.objects.get().observers.all()) == [observer]

    def test_match_is_case_insensitive(self):
        observer = ObserverFactory(name="Jo Smith")

        report = import_observations_csv(_csv(_row(observer="jo smith")))

        assert report.created == 1
        assert list(Observation.objects.get().observers.all()) == [observer]

    def test_matches_the_importing_users_own_observer(self):
        """An Observer can be linked to a specific registered user -- a
        self-import naming that user by their own name needs to find
        their own Observer record, not create a second, unlinked one
        for the same person.
        """
        user = UserFactory()
        observer = ObserverFactory(name="Jo Smith", user=user)

        report = import_observations_csv(_csv(_row(observer="Jo Smith")))

        assert report.created == 1
        assert list(Observation.objects.get().observers.all()) == [observer]
        assert Observation.objects.get().owner == user

    def test_ambiguous_observer_name_is_an_error(self):
        ObserverFactory(name="Jo Smith")
        ObserverFactory(name="Jo Smith")

        report = import_observations_csv(_csv(_row(observer="Jo Smith")))

        assert report.skipped == 1
        assert "more than one observer" in report.errors[0]

    def test_creates_a_new_observer_when_none_matches(self):
        report = import_observations_csv(_csv(_row(observer="A New Person")))

        assert report.errors == []
        assert report.created == 1
        observer = Observer.objects.get()
        assert observer.name == "A New Person"
        assert observer.user is None

    def test_observation_owner_follows_the_observers_own_account(self):
        """A life history spans several observers at once -- each row's
        owner must be whichever site account (if any) *that* row's
        observer is linked to, not whoever ran the import, so someone
        else's sightings never end up on the importer's My Observations.
        """
        user = UserFactory()
        ObserverFactory(name="Registered Person", user=user)
        csv_text = _rows(
            {"observer": "Registered Person", "date": "2026-01-01"},
            {"observer": "Unregistered Person", "date": "2026-01-02"},
        )

        report = import_observations_csv(_csv(csv_text))

        assert report.created == 2
        assert Observation.objects.get(date="2026-01-01").owner == user
        assert Observation.objects.get(date="2026-01-02").owner is None


@pytest.mark.django_db
class TestRowParsing:
    def test_missing_tags_is_an_error(self):
        report = import_observations_csv(_csv(_row(left_below="")))
        assert report.skipped == 1
        assert "no tags given" in report.errors[0]

    def test_tags_split_across_position_columns(self):
        LocationFactory(name={"Latn": "Test Location"}, region="GB--")
        csv_text = (
            "species,location,region,country,observer,date,left_below,right_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,"
            'WB(A123),"O,Y"\n'
        )
        report = import_observations_csv(_csv(csv_text))
        assert report.errors == []
        assert report.created == 1
        observation = Observation.objects.get()
        assert {tag.position: tag.code for tag in observation.tags.all()} == {
            "LB": "WB(A123)",
            "RB": "O,Y",
        }

    def test_codes_are_standardised_on_bulk_created_tags(self):
        """Tag.save() normally standardises `code`, but bulk_create() --
        used here for performance -- never calls save(), so the import
        itself has to.
        """
        report = import_observations_csv(_csv(_row(left_below=" wb(a123) ")))
        assert report.created == 1
        tag = Observation.objects.get().tags.get()
        assert tag.code == "WB(A123)"

    def test_a_bad_code_names_its_column(self):
        report = import_observations_csv(_csv(_row(left_below="WB(A123")))
        assert report.created == 0
        assert report.errors == ["Row 2: left_below: 'WB(A123': missing closing bracket"]

    def test_a_row_matching_an_identified_bird_is_linked_to_it(self):
        elsewhere = LocationFactory(name={"Latn": "Elsewhere"})
        origin = OriginFactory(location=elsewhere)
        known = ObservationFactory(species=SPECIES_CODE, origin=origin, location=elsewhere)
        TagFactory(observation=known, position="LB", code="WB(A123)")

        report = import_observations_csv(_csv(_row(left_below="WB(A123)", date="2026-02-01")))

        assert report.created == 1
        assert Observation.objects.exclude(pk=known.pk).get().origin == origin

    def test_optional_fields_saved_when_present(self):
        LocationFactory(name={"Latn": "Test Location"}, region="GB--")
        csv_text = (
            "species,location,region,country,observer,date,time,latitude,longitude,"
            "accuracy,notes,left_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,14:30,"
            "51.5074,-0.1278,50,Nice bird,Y\n"
        )
        report = import_observations_csv(_csv(csv_text))
        assert report.created == 1
        observation = Observation.objects.get()
        assert str(observation.time) == "14:30:00"
        assert observation.accuracy == 50
        assert observation.notes == "Nice bird"

    def test_header_casing_and_whitespace_dont_hide_columns(self):
        """A column header like "Time" or "time " (easy to end up with
        from a spreadsheet export) must still be recognised -- not
        silently treated as absent, leaving the field unset.
        """
        LocationFactory(name={"Latn": "Test Location"}, region="GB--")
        csv_text = (
            "Species,Location,Region,Country,Observer,Date,Time ,Left_Below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,14:30,Y\n"
        )
        report = import_observations_csv(_csv(csv_text))
        assert report.errors == []
        assert report.created == 1
        assert str(Observation.objects.get().time) == "14:30:00"

    def test_bad_coordinate_is_an_error(self):
        LocationFactory(name={"Latn": "Test Location"}, region="GB--")
        csv_text = (
            "species,location,region,country,observer,date,latitude,left_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,"
            "notanumber,Y\n"
        )
        report = import_observations_csv(_csv(csv_text))
        assert report.skipped == 1
        assert "not a valid coordinate" in report.errors[0]


@pytest.mark.django_db
class TestIdempotency:
    def test_rerunning_the_same_file_reports_duplicates_not_new_rows(self):
        csv_text = _row(left_below="WB(A123)")
        first = import_observations_csv(_csv(csv_text))
        assert (first.created, first.duplicates) == (1, 0)

        second = import_observations_csv(_csv(csv_text))
        assert (second.created, second.duplicates) == (0, 1)
        assert Observation.objects.count() == 1

    def test_same_slot_different_tags_is_a_new_observation(self):
        import_observations_csv(_csv(_row(left_below="WB(A1)")))
        report = import_observations_csv(_csv(_row(left_below="WB(A2)")))
        assert (report.created, report.duplicates) == (1, 0)
        assert Observation.objects.count() == 2

    def test_matching_species_date_and_tags_is_a_duplicate_despite_different_location_and_observer(
        self,
    ):
        """The whole point of loosening the match: a life history from
        the project coordinator won't necessarily name the site or
        observer the way this row's own submitter did, but the same
        bird, same day, same exact tag set is still the same sighting.
        """
        import_observations_csv(
            _csv(_row(location="Site One", observer="First Observer", left_below="WB(A123)"))
        )
        report = import_observations_csv(
            _csv(_row(location="Site Two", observer="Second Observer", left_below="WB(A123)"))
        )
        assert (report.created, report.duplicates) == (0, 1)
        assert Observation.objects.count() == 1

    def test_same_tags_on_a_different_date_is_a_new_observation(self):
        import_observations_csv(_csv(_row(left_below="WB(A123)", date="2026-01-01")))
        report = import_observations_csv(_csv(_row(left_below="WB(A123)", date="2026-01-02")))
        assert (report.created, report.duplicates) == (1, 0)
        assert Observation.objects.count() == 2

    def test_same_day_resighting_explains_which_earlier_row_and_time_it_matches(self):
        """A same-day resighting is still reported as a duplicate (time
        isn't part of the match -- see the module docstring), but with
        a per-row explanation so it doesn't read as a bug.
        """
        csv_text = (
            "species,location,region,country,observer,date,time,latitude,longitude,"
            "accuracy,left_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,09:15,"
            "51.5074,-0.1278,50,WB(A123)\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,14:30,"
            "51.5074,-0.1278,50,WB(A123)\n"
        )
        report = import_observations_csv(_csv(csv_text))

        assert (report.created, report.duplicates) == (1, 1)
        assert report.duplicate_details == [
            "Row 3: this bird was already logged earlier that day, at 09:15."
        ]

    def test_same_day_repeat_with_no_time_on_either_side_has_no_note(self):
        """Without a time to compare, a repeat can't be told apart from
        re-importing the same row, so no note is worth guessing at --
        it's still counted as a plain duplicate.
        """
        import_observations_csv(_csv(_row(left_below="WB(A123)")))
        report = import_observations_csv(_csv(_row(left_below="WB(A123)")))

        assert report.duplicates == 1
        assert report.duplicate_details == []

    def test_rerunning_a_file_with_a_same_day_resighting_does_not_repeat_the_note(self):
        """Re-importing a file after fixing an unrelated row's error
        shouldn't re-explain every row it already explained the first
        time around -- each row is, on the second run, a match at its
        *own* time (a re-run), not a later one (a new sighting).
        """
        csv_text = (
            "species,location,region,country,observer,date,time,latitude,longitude,"
            "accuracy,left_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,09:15,"
            "51.5074,-0.1278,50,WB(A123)\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,14:30,"
            "51.5074,-0.1278,50,WB(A123)\n"
        )
        import_observations_csv(_csv(csv_text))

        report = import_observations_csv(_csv(csv_text))

        assert (report.created, report.duplicates) == (0, 2)
        assert report.duplicate_details == []

    def test_no_note_when_the_earlier_matching_row_has_no_time_but_this_row_does(self):
        """A blank time on the earlier side means there's nothing to
        compare against, even though this row's own time is known.
        """
        import_observations_csv(_csv(_row(left_below="WB(A123)")))
        csv_text = (
            "species,location,region,country,observer,date,time,latitude,longitude,"
            "accuracy,left_below\n"
            f"{SPECIES_CODE},Test Location,{REGION},{COUNTRY},Jo Smith,2026-01-01,14:30,"
            "51.5074,-0.1278,50,WB(A123)\n"
        )

        report = import_observations_csv(_csv(csv_text))

        assert report.duplicates == 1
        assert report.duplicate_details == []
