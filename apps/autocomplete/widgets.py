"""A <select> that progressively enhances into a Tom Select search box
backed by /autocomplete/<field>/ (see autocomplete.views) -- used
instead of Django admin's `autocomplete_fields` so the same widget
works in the public submission forms too, and doesn't require the
field to be a real ModelAdmin-backed queryset (Country, Region and
Species are all in-memory TextChoices, not database tables).

Only the currently selected option is ever rendered server-side --
matches, including the widget's own current value, are otherwise
fetched on demand -- so a field with thousands of possible values
doesn't dump them all into the page.
"""

from collections.abc import Callable

from django import forms


class AutocompleteSelect(forms.Select):
    class Media:
        css = {
            "all": (
                "autocomplete/vendor/tom-select.default.min.css",
                "autocomplete/autocomplete.css",
            )
        }
        js = (
            "autocomplete/vendor/tom-select.complete.min.js",
            "autocomplete/autocomplete.js",
        )

    def __init__(
        self,
        field: str,
        *,
        depends_on: str | None = None,
        get_label: Callable[[str], str] | None = None,
        allow_create: bool = False,
        attrs: dict | None = None,
    ) -> None:
        """
        field: the registry key -- also the URL segment queried for matches.
        depends_on: the HTML id of a parent AutocompleteSelect whose
            current value narrows this field's results (e.g. picking a
            country narrows the regions on offer). The parent's own
            registry key is used as the query parameter name.
        get_label: given a stored value, returns the text to show for
            it when the field already has a value (an existing record
            being edited) -- e.g. `lambda code: Region(code).label`.
        allow_create: whether typing something with no match offers
            "Add <text>" as a choice, submitted as "__new__:<text>" (see
            autocomplete.js) rather than a real match's own value --
            only meaningful for a field backed by open-ended data (e.g.
            Location); never set this for a closed set like Country or
            Region, which have nothing sensible to "create".
        """
        super().__init__(attrs)
        self.field = field
        self.depends_on = depends_on
        self.get_label = get_label or (lambda value: value)
        self.allow_create = allow_create

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["attrs"]["data-autocomplete-field"] = self.field
        if self.depends_on:
            context["widget"]["attrs"]["data-autocomplete-depends-on"] = self.depends_on
        if self.allow_create:
            context["widget"]["attrs"]["data-autocomplete-allow-create"] = "true"
        return context

    def optgroups(self, name, value, attrs=None):
        values = value if isinstance(value, (list, tuple)) else [value]
        groups = []
        index = 0
        for v in values:
            if not v:
                continue
            option = self.create_option(name, v, self.get_label(v), True, index)
            groups.append((None, [option], index))
            index += 1
        return groups
