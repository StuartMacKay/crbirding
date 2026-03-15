"""Forms for the public-facing observation and origin pages.

Tags are typed in as colour-mark codes, one row per Position (see
TagForm and core.utils.codes), checked and written the standard way as
they're saved.
"""

from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.conf import settings
from django.forms import BaseInlineFormSet, inlineformset_factory

from .models import (
    Country,
    Event,
    Location,
    Observation,
    Origin,
    Photo,
    Region,
    Species,
    Tag,
)
from .models.tag import DUPLICATE_POSITION_MESSAGE

# Must match autocomplete.js's own NEW_ITEM_PREFIX -- marks a
# LocationForm.search value as free-typed text with no matching
# Location, rather than a real match's own pk.
NEW_LOCATION_PREFIX = "__new__:"


def _species_widget() -> AutocompleteSelect:
    return AutocompleteSelect("species", get_label=lambda code: Species(code).label if code else "")


def _country_widget() -> AutocompleteSelect:
    return AutocompleteSelect("country", get_label=lambda code: Country(code).label if code else "")


_INPUT_CLASSES = (
    "mt-1 block w-full rounded-md border-gray-300 text-sm shadow-sm "
    "focus:border-accent-500 focus:ring-accent-500"
)
_CHECKBOX_CLASSES = "rounded border-gray-300 text-accent-600 focus:ring-accent-500"


def _style_widgets(form: forms.BaseForm) -> None:
    """Apply the site's shared Tailwind input styling to every field,
    so individual forms don't have to repeat it per widget.
    """
    for field in form.fields.values():
        if isinstance(field.widget, forms.CheckboxInput):
            field.widget.attrs.setdefault("class", _CHECKBOX_CLASSES)
        else:
            field.widget.attrs.setdefault("class", _INPUT_CLASSES)


class ObservationForm(forms.ModelForm):
    """Doesn't include `location`, `latitude`, `longitude`, or
    `accuracy` -- see LocationForm, which resolves the location (an
    existing one searched by name, or a newly described one) and
    those same coordinate fields, shared with it rather than
    duplicated here. See LocationForm.observation_coordinate_overrides().
    """

    class Meta:
        model = Observation
        fields = ["species", "age", "sex", "date", "time", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
            "species": _species_widget(),
            "label": forms.TextInput(attrs={"spellcheck": "false"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


def _location_search_label(value: str) -> str:
    """The text to show for `search`'s current value -- either an
    existing Location's own display text, or (a page re-rendered after
    a validation error, say) whatever new name was typed, read back out
    of the NEW_LOCATION_PREFIX marker rather than treated as a pk.
    """
    if not value:
        return ""
    if value.startswith(NEW_LOCATION_PREFIX):
        return value[len(NEW_LOCATION_PREFIX) :]
    if not value.isdigit():
        return ""
    location = Location.objects.filter(pk=value).first()
    return str(location) if location else ""


class LocationForm(forms.ModelForm):
    """Resolves which Location an Observation or Origin belongs to --
    either an existing one, searched by name with no region/country
    filter (region and country are shown per choice only to tell
    same-named places apart), or, if nothing matches, a newly
    described one, named after whatever was typed -- see resolve().
    One field handles both: `search` is a Tom Select "search, or create
    what you typed" box (see autocomplete.js's `create` option), not a
    separate "pick existing" field plus a separate "name" field for a
    new one.

    Country and region are only needed for the *new* location: country
    narrows the region search, and region is required, the same way it
    always was. (A brand new Location made this way only ever gets a
    name in the deployment's first configured alphabet -- see
    resolve() -- unlike the admin's own LocationAdminForm, which asks
    for every alphabet; a quick add from the public site doesn't need
    that rigour, and can always be filled in properly later.)

    latitude/longitude/accuracy are dual-purpose, matching the parent
    form's (Observation's or Origin's) own coordinate fields, which
    this replaces rather than duplicates:

    - An existing Location selected: optional, and never touch that
      Location's own stored coordinates (editing them here would
      corrupt the shared record for everyone else who's picked it) --
      they become the *parent record's own override* instead, e.g.
      for a sighting at a slightly different spot than a named site's
      other sub-locations. See observation_coordinate_overrides().
    - No existing Location selected (describing a new one): required
      together with region -- they become that new Location's own
      base coordinates.

    Every field below is optional at the form level (so leaving the
    whole "describe a new location" section blank doesn't fail
    validation when an existing Location was picked instead), but
    required together once `search` doesn't name an existing Location
    -- see clean().
    """

    search = forms.CharField(
        required=False,
        label="Location",
        help_text='Search by name. Not there? Type the new name and choose "Add" to add it.',
        widget=AutocompleteSelect(
            "location",
            get_label=_location_search_label,
            allow_create=True,
        ),
    )
    # Not a model field -- narrows the region autocomplete below to one
    # country's regions, same as core.admin.location.LocationAdminForm.
    country = forms.CharField(label="Country", required=False, widget=_country_widget())

    class Meta:
        model = Location
        fields = ["region", "latitude", "longitude", "accuracy", "notes"]
        widgets = {
            "region": AutocompleteSelect(
                "region",
                depends_on="id_location-country",
                get_label=lambda code: Region(code).label if code else "",
            ),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("prefix", "location")
        super().__init__(*args, **kwargs)
        for name in ("region", "latitude", "longitude"):
            self.fields[name].required = False
        _style_widgets(self)

    def clean(self):
        cleaned_data = super().clean()
        search = cleaned_data.get("search", "")

        if search.startswith(NEW_LOCATION_PREFIX):
            cleaned_data["existing_location"] = None
            cleaned_data["new_name"] = search[len(NEW_LOCATION_PREFIX) :].strip()
        elif search:
            existing = Location.objects.filter(pk=search).first() if search.isdigit() else None
            if existing is None:
                self.add_error("search", "Select a location from the list, or type a new name.")
                return cleaned_data
            cleaned_data["existing_location"] = existing
            cleaned_data["new_name"] = ""
        else:
            cleaned_data["existing_location"] = None
            cleaned_data["new_name"] = ""

        if cleaned_data["existing_location"] is not None:
            return cleaned_data

        if not cleaned_data["new_name"]:
            self.add_error(None, "Select an existing location, or type a new name to add one.")
            return cleaned_data
        if not cleaned_data.get("region"):
            self.add_error("region", "Required to add a new location.")
        if cleaned_data.get("latitude") is None:
            self.add_error("latitude", "Required to add a new location.")
        if cleaned_data.get("longitude") is None:
            self.add_error("longitude", "Required to add a new location.")
        if cleaned_data.get("accuracy") is None:
            self.add_error("accuracy", "Required to add a new location.")
        return cleaned_data

    def resolve(self) -> Location:
        """The Location to use -- call only once this form is valid."""
        existing = self.cleaned_data.get("existing_location")
        if existing is not None:
            return existing
        primary_alphabet = settings.ALPHABETS[0][0]
        self.instance.name = {primary_alphabet: self.cleaned_data["new_name"]}
        return self.save()

    def observation_coordinate_overrides(self) -> dict:
        """The parent record's own latitude/longitude/accuracy override
        values -- only meaningful when an existing Location was
        selected (a brand new Location's own coordinates, just entered
        above, are already the precise ones -- no separate override
        applies). Call only once this form is valid.

        Callers should apply whichever keys they have a matching field
        for (Origin has no `accuracy` of its own, for instance).
        """
        if self.cleaned_data.get("existing_location") is None:
            return {}
        return {
            "latitude": self.cleaned_data.get("latitude"),
            "longitude": self.cleaned_data.get("longitude"),
            "accuracy": self.cleaned_data.get("accuracy"),
        }


class ObservationImportForm(forms.Form):
    """Shared by the admin's own CSV import and the public My
    Observations one -- see core.utils.bulk_import for the format.
    """

    csv_file = forms.FileField(
        label="CSV file",
        help_text="Each row identifies its own species, location and observer.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class LocationImportForm(forms.Form):
    """Admin-only CSV import for Location -- see
    core.utils.location_import for the format.
    """

    csv_file = forms.FileField(
        label="CSV file",
        help_text="Each row identifies its own name, region, and country.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class ProjectImportForm(forms.Form):
    """Admin-only CSV import for Project -- see
    core.utils.project_import for the format.
    """

    csv_file = forms.FileField(
        label="CSV file",
        help_text="Each row identifies its own name, coordinator, and country.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class RuleImportForm(forms.Form):
    """Admin-only CSV import for Rule -- see core.utils.rule_import for
    the format.
    """

    csv_file = forms.FileField(
        label="CSV file",
        help_text=(
            "Each row identifies its own species, position, regex, and "
            "project (by coordinator and/or project name)."
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class TagForm(forms.ModelForm):
    """One row of an Observation's tags: a Position, and the colour-mark
    code for what's worn there (see core.utils.codes). The code is
    checked and written the standard way by Tag.clean(), so a badly
    formed one is reported against this row's own code box.
    """

    class Meta:
        model = Tag
        fields = ["position", "code"]
        widgets = {
            # Tag.code is a TextField, which ModelForm would otherwise
            # render as a multi-line Textarea -- it's a short code.
            "code": forms.TextInput(attrs={"autocomplete": "off", "spellcheck": "false"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


class BaseTagFormSet(BaseInlineFormSet):
    """One Tag per Position: two rows naming the same Position are
    reported by the formset's own validate_unique() (from Tag's
    UniqueConstraint) -- with the same message as a row clashing with an
    already-saved Tag gets, rather than Django's generic one.
    """

    def get_unique_error_message(self, unique_check):
        return DUPLICATE_POSITION_MESSAGE


TagFormSet = inlineformset_factory(
    Observation,
    Tag,
    form=TagForm,
    formset=BaseTagFormSet,
    extra=1,
    can_delete=True,
)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


PhotoFormSet = inlineformset_factory(
    Observation,
    Photo,
    form=PhotoForm,
    extra=1,
    can_delete=True,
)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["date", "description"]
        widgets = {
            # The browser's own calendar picker -- an event only ever
            # needs a day, not a time (see Event.date).
            "date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "description": forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)


EventFormSet = inlineformset_factory(
    Observation,
    Event,
    form=EventForm,
    extra=1,
    can_delete=True,
)


class OriginForm(forms.ModelForm):
    """Doesn't include `location`, `latitude`, or `longitude` -- see
    LocationForm, which resolves the location and those same
    coordinate fields, shared with it rather than duplicated here.
    """

    class Meta:
        model = Origin
        fields = [
            "species",
            "label",
            "age",
            "sex",
            "date",
            "time",
            "project",
            "notes",
            "history_url",
            "history_file",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
            "species": _species_widget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_widgets(self)
