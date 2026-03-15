from pathlib import Path

import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError, transaction

from core.models import (
    PLACE_TO_COUNTRY,
    SPECIES_SCIENTIFIC_NAME,
    Country,
    Photo,
    Region,
    Species,
)

from .factories import (
    LocationFactory,
    ObservationFactory,
    OriginFactory,
    ProjectFactory,
    RuleFactory,
    TagFactory,
)


class TestRegionAndCountryChoices:
    """Region and Country are generated, static TextChoices (see
    scripts/generate_region_choices.py) rather than database models --
    these just check the generated data's own internal consistency.
    """

    def test_every_region_code_has_a_country(self):
        for code, _label in Region.choices:
            assert code in PLACE_TO_COUNTRY

    def test_every_place_to_country_value_is_a_real_country(self):
        country_codes = {code for code, _label in Country.choices}
        for country_code in PLACE_TO_COUNTRY.values():
            assert country_code in country_codes

    def test_a_country_level_code_maps_to_itself(self):
        assert PLACE_TO_COUNTRY["GB--"] == "GB--"


class TestSpeciesChoices:
    """Species is also a generated, static TextChoices (see
    scripts/generate_species_choices.py) rather than a database model.
    """

    def test_every_species_has_a_scientific_name(self):
        for code, _label in Species.choices:
            assert code in SPECIES_SCIENTIFIC_NAME

    def test_common_ostrich_code_is_stable(self):
        assert Species.COMMON_OSTRICH == "00010"
        assert SPECIES_SCIENTIFIC_NAME["00010"] == "Struthio camelus"


@pytest.mark.django_db
class TestLocation:
    def test_get_name_falls_back_to_latin(self):
        location = LocationFactory(name={"Latn": "Somewhere"})
        assert location.get_name("Cyrl") == "Somewhere"

    def test_get_country_code_is_derived_from_region(self):
        location = LocationFactory(region="GB--")
        assert location.get_country_code() == "GB--"

    def test_get_country_display_is_the_country_label(self):
        location = LocationFactory(region="GB--")
        assert location.get_country_display() == Country("GB--").label


@pytest.mark.django_db
class TestTag:
    def test_code_is_standardised_on_save(self):
        tag = TagFactory(code=" r , wn(ky) ")
        assert tag.code == "R,WN(KY)"

    def test_a_badly_formed_code_is_not_saved(self):
        with pytest.raises(ValueError, match="missing closing bracket"):
            TagFactory(code="BW(A1")

    def test_clean_reports_a_badly_formed_code_on_the_field(self):
        tag = TagFactory.build(observation=ObservationFactory(), code="Z")
        with pytest.raises(ValidationError) as excinfo:
            tag.full_clean()
        assert "code" in excinfo.value.message_dict

    def test_one_per_position_per_observation(self):
        observation = ObservationFactory()
        TagFactory(observation=observation, position="LA", code="Y")
        with pytest.raises(IntegrityError):
            TagFactory(observation=observation, position="LA", code="R")

    def test_str(self):
        assert str(TagFactory.build(position="LA", code="R,WN(KY)")) == "LA:R,WN(KY)"


@pytest.mark.django_db
class TestObservation:
    def test_tags_are_optional(self):
        observation = ObservationFactory()
        assert observation.tags.count() == 0

    def test_observers_defaults_to_one_auto_created_observer(self):
        observation = ObservationFactory()
        assert observation.observers.count() == 1

    def test_age_and_sex_can_be_blank(self):
        observation = ObservationFactory(age="", sex="")
        observation.full_clean()
        observation.refresh_from_db()
        assert observation.age == ""
        assert observation.sex == ""

    def test_age_and_sex_default_to_blank(self):
        observation = ObservationFactory()
        assert observation.age == ""
        assert observation.sex == ""


@pytest.mark.django_db
class TestOrigin:
    def test_str_is_the_species_and_label(self):
        assert str(OriginFactory(label="BW(123)")) == "Common Ostrich (BW(123))"

    def test_age_and_sex_can_be_blank(self):
        origin = OriginFactory(age="", sex="")
        origin.full_clean()
        origin.refresh_from_db()
        assert origin.age == ""
        assert origin.sex == ""


@pytest.mark.django_db
class TestOriginHistoryFileCleanup:
    """Origin.save() / its post_delete handler remove a life history
    file once nothing points at it -- deferred until commit, hence
    django_capture_on_commit_callbacks (tests never really commit).
    """

    @pytest.fixture(autouse=True)
    def _media_root(self, settings, tmp_path):
        settings.MEDIA_ROOT = tmp_path

    def _origin_with_file(self, content=b"first"):
        return OriginFactory(history_file=SimpleUploadedFile("history.pdf", content))

    def test_replacing_the_file_deletes_the_old_one(self, django_capture_on_commit_callbacks):
        origin = self._origin_with_file()
        old_path = Path(origin.history_file.path)

        with django_capture_on_commit_callbacks(execute=True):
            origin.history_file = SimpleUploadedFile("history.pdf", b"second")
            origin.save()

        assert not old_path.exists()
        assert Path(origin.history_file.path).read_bytes() == b"second"

    def test_clearing_the_file_deletes_it(self, django_capture_on_commit_callbacks):
        origin = self._origin_with_file()
        old_path = Path(origin.history_file.path)

        with django_capture_on_commit_callbacks(execute=True):
            origin.history_file = None
            origin.save()

        assert not old_path.exists()

    def test_saving_other_fields_keeps_the_file(self, django_capture_on_commit_callbacks):
        origin = self._origin_with_file()

        with django_capture_on_commit_callbacks(execute=True) as callbacks:
            origin.notes = "Edited"
            origin.save()

        assert callbacks == []
        assert Path(origin.history_file.path).exists()

    def test_deleting_the_origin_deletes_its_file(self, django_capture_on_commit_callbacks):
        origin = self._origin_with_file()
        old_path = Path(origin.history_file.path)

        with django_capture_on_commit_callbacks(execute=True):
            origin.delete()

        assert not old_path.exists()

    def test_nothing_is_deleted_if_the_save_rolls_back(self, django_capture_on_commit_callbacks):
        origin = self._origin_with_file()
        old_path = Path(origin.history_file.path)

        with django_capture_on_commit_callbacks(execute=True):
            with pytest.raises(RuntimeError), transaction.atomic():
                origin.history_file = SimpleUploadedFile("history.pdf", b"second")
                origin.save()
                raise RuntimeError("roll back")

        assert old_path.exists()
        origin.refresh_from_db()
        assert Path(origin.history_file.path) == old_path


@pytest.mark.django_db
class TestRule:
    def test_str_is_the_regex(self):
        rule = RuleFactory(regex=r"^W\(J")
        assert str(rule) == r"^W\(J"


@pytest.mark.django_db
class TestProject:
    def test_str_is_name(self):
        project = ProjectFactory(name="My Project")
        assert str(project) == "My Project"


# The smallest valid GIF -- a 1x1 transparent pixel.
_GIF = (
    b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01"
    b"\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
)


@pytest.mark.django_db
class TestPhotoImageCleanup:
    """The same cleanup as TestOriginHistoryFileCleanup, for Photo.image."""

    @pytest.fixture(autouse=True)
    def _media_root(self, settings, tmp_path):
        settings.MEDIA_ROOT = tmp_path

    def _photo(self, observation=None):
        return Photo.objects.create(
            observation=observation or ObservationFactory(),
            image=SimpleUploadedFile("bird.gif", _GIF, content_type="image/gif"),
        )

    def test_replacing_the_image_deletes_the_old_one(self, django_capture_on_commit_callbacks):
        photo = self._photo()
        old_path = Path(photo.image.path)

        with django_capture_on_commit_callbacks(execute=True):
            photo.image = SimpleUploadedFile("other.gif", _GIF, content_type="image/gif")
            photo.save()

        assert not old_path.exists()
        assert Path(photo.image.path).exists()

    def test_saving_without_a_new_image_keeps_it(self, django_capture_on_commit_callbacks):
        photo = self._photo()

        with django_capture_on_commit_callbacks(execute=True) as callbacks:
            photo.save()

        assert callbacks == []
        assert Path(photo.image.path).exists()

    def test_deleting_the_photo_deletes_its_image(self, django_capture_on_commit_callbacks):
        photo = self._photo()
        old_path = Path(photo.image.path)

        with django_capture_on_commit_callbacks(execute=True):
            photo.delete()

        assert not old_path.exists()

    def test_deleting_the_observation_deletes_its_photos_images(
        self, django_capture_on_commit_callbacks
    ):
        observation = ObservationFactory()
        paths = [Path(self._photo(observation).image.path) for _ in range(2)]

        with django_capture_on_commit_callbacks(execute=True):
            observation.delete()

        assert not any(path.exists() for path in paths)
