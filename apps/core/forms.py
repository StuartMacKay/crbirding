"""Forms for the public-facing resighting submission page.

Structured input is primary here (dropdowns for position/kind/colour,
not a free-text encoded string) -- see apps.core.models.Tag and
apps.core.formatting.format_tags, which derives the interchange notation
from these fields rather than the other way round.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Capture, Resighting, Tag

_INPUT_CLASSES = (
    "mt-1 block w-full rounded-md border-gray-300 text-sm shadow-sm "
    "focus:border-brand-500 focus:ring-brand-500"
)
_CHECKBOX_CLASSES = "rounded border-gray-300 text-brand-600 focus:ring-brand-500"


def _style_widgets(form: forms.BaseForm) -> None:
    """Apply the site's shared Tailwind input styling to every field,
    so individual forms don't have to repeat it per widget.
    """
    for field in form.fields.values():
        if isinstance(field.widget, forms.CheckboxInput):
            field.widget.attrs.setdefault("class", _CHECKBOX_CLASSES)
        else:
            field.widget.attrs.setdefault("class", _INPUT_CLASSES)


class ResightingForm(forms.ModelForm):
    class Meta:
        model = Resighting
        fields = [
            "species",
            "location",
            "date",
            "time",
            "photo",
            "notes",
            "latitude",
            "longitude",
            "accuracy",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class TagForm(forms.ModelForm):
    """`order` is deliberately not a field here -- it's derived from the
    order rows are entered in (see assign_tag_order), since asking a
    birder to number a ring stack manually is friction for a case
    (multiple tags at one position) that's the exception, not the rule.
    """

    class Meta:
        model = Tag
        fields = [
            "position",
            "kind",
            "colour",
            "second_colour",
            "inscription",
            "inscription_colour",
            "inscription_direction",
            "uncertain",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)

    def has_data(self) -> bool:
        """Whether this form's fields were actually filled in -- an
        untouched extra row shouldn't count as "no tags provided".
        """
        return bool(self.cleaned_data.get("colour"))


class BaseTagFormSet(BaseInlineFormSet):
    """Requires at least one real Tag: a Resighting with none isn't
    meaningful for an app whose whole purpose is colour-mark sightings.
    """

    def clean(self):
        super().clean()
        if any(self.errors):
            return
        real_forms = [
            form
            for form in self.forms
            if form.has_data() and not form.cleaned_data.get("DELETE", False)
        ]
        if not real_forms:
            raise ValidationError(_("Describe at least one colour ring, flag, or other tag."))


TagFormSet = inlineformset_factory(
    Resighting,
    Tag,
    form=TagForm,
    formset=BaseTagFormSet,
    extra=2,
    can_delete=True,
)

CaptureTagFormSet = inlineformset_factory(
    Capture,
    Tag,
    form=TagForm,
    formset=BaseTagFormSet,
    extra=2,
    can_delete=True,
)


class CaptureForm(forms.ModelForm):
    class Meta:
        model = Capture
        fields = [
            "species",
            "age",
            "sex",
            "location",
            "date",
            "time",
            "resolution",
            "project",
            "notes",
            "latitude",
            "longitude",
            "accuracy",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


def assign_tag_order(tags: list[Tag]) -> None:
    """Number each Tag's stacking position by how many earlier tags in
    the list already share its Position -- the order the birder typed
    them in, not something they had to specify themselves.
    """
    seen: dict[str, int] = {}
    for tag in tags:
        tag.order = seen.get(tag.position, 0)
        seen[tag.position] = tag.order + 1
