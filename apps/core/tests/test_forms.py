import pytest

from core.forms import TagForm, TagFormSet
from core.models import Observation, Position
from core.models.tag import DUPLICATE_POSITION_MESSAGE

from .factories import ObservationFactory, TagFactory


def _formset_data(*rows, initial=0):
    """TagFormSet POST data -- one (position, code[, id[, delete]]) per row."""
    data = {
        "tags-TOTAL_FORMS": str(len(rows)),
        "tags-INITIAL_FORMS": str(initial),
        "tags-MIN_NUM_FORMS": "0",
        "tags-MAX_NUM_FORMS": "1000",
    }
    for index, (position, code, *rest) in enumerate(rows):
        data[f"tags-{index}-position"] = position
        data[f"tags-{index}-code"] = code
        if rest:
            data[f"tags-{index}-id"] = rest[0]
        if len(rest) > 1 and rest[1]:
            data[f"tags-{index}-DELETE"] = "on"
    return data


class TestTagForm:
    def test_code_is_standardised(self):
        form = TagForm(data={"position": Position.LEFT_ABOVE, "code": " r , wn(ky) "})
        assert form.is_valid(), form.errors
        assert form.instance.code == "R,WN(KY)"

    def test_a_bad_code_is_an_error_on_the_code(self):
        form = TagForm(data={"position": Position.LEFT_ABOVE, "code": "BW(A1"})
        assert not form.is_valid()
        assert form.errors == {"code": ["'BW(A1': missing closing bracket"]}

    def test_a_direction_after_the_inscription_is_an_error(self):
        form = TagForm(data={"position": Position.LEFT_ABOVE, "code": "BW(A1)d"})
        assert not form.is_valid()
        assert "after the inscription" in form.errors["code"][0]


@pytest.mark.django_db
class TestTagFormSet:
    def test_saves_a_tag_per_row(self):
        observation = ObservationFactory()
        formset = TagFormSet(_formset_data(("LA", "r,wn(ky)"), ("RA", "m")), instance=observation)
        assert formset.is_valid(), formset.errors
        formset.save()

        assert {tag.position: tag.code for tag in observation.tags.all()} == {
            "LA": "R,WN(KY)",
            "RA": "M",
        }

    def test_a_blank_extra_row_is_ignored(self):
        observation = ObservationFactory()
        formset = TagFormSet(_formset_data(("LA", "Y"), ("", "")), instance=observation)
        assert formset.is_valid(), formset.errors
        formset.save()
        assert observation.tags.count() == 1

    def test_two_rows_for_the_same_position_is_an_error(self):
        formset = TagFormSet(_formset_data(("LA", "Y"), ("LA", "R")), instance=ObservationFactory())
        assert not formset.is_valid()
        assert formset.non_form_errors() == [DUPLICATE_POSITION_MESSAGE]

    def test_a_row_repeating_a_saved_tags_position_is_an_error_on_that_row(self):
        observation = ObservationFactory()
        saved = TagFactory(observation=observation, position="LA", code="Y")

        formset = TagFormSet(
            _formset_data(("LA", "Y", saved.pk), ("LA", "R"), initial=1), instance=observation
        )

        assert not formset.is_valid()
        assert formset.forms[1].non_field_errors() == [DUPLICATE_POSITION_MESSAGE]

    def test_rows_can_be_changed_and_deleted(self):
        observation = ObservationFactory()
        kept = TagFactory(observation=observation, position="LA", code="Y")
        gone = TagFactory(observation=observation, position="RA", code="M")

        formset = TagFormSet(
            _formset_data(("LA", "Y,R", kept.pk), ("RA", "M", gone.pk, True), initial=2),
            instance=observation,
        )
        assert formset.is_valid(), formset.errors
        formset.save()

        assert [(tag.position, tag.code) for tag in observation.tags.all()] == [("LA", "Y,R")]

    def test_starts_with_one_blank_row(self):
        formset = TagFormSet(instance=Observation())
        assert len(formset.forms) == 1
