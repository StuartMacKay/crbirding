"""Admin list filters that only offer choices actually used by at least
one record, rather than every value in an exhaustive TextChoices class.

Region and Country (see core.models.region) are deliberately
exhaustive -- every current EURING place, baked in, so nothing needs
importing or initialising before a Location can be recorded. That's
also exactly what would clutter a small deployment's admin sidebar with
hundreds of places nobody's ever used; these filters are what keeps the
two properties -- exhaustive choices, an uncluttered admin -- from
being in tension.
"""

from django.contrib import admin

from core.models import PLACE_TO_COUNTRY, Country


class ChoicesDropdownFilter(admin.ChoicesFieldListFilter):
    """Renders a choices list_filter as a <select> instead of a link
    list, for a choices field (or a `__`-separated lookup to one on a
    related model, e.g. "tags__colour") with enough options to make
    the default sidebar list unwieldy. Use directly in list_filter,
    e.g. `("colour", ChoicesDropdownFilter)`.
    """

    template = "admin/filter_dropdown.html"


def choice_list_filter(field_path: str, choices_class, *, title: str, parameter_name: str):
    """A SimpleListFilter over a TextChoices-backed field, listing only
    the codes actually present on `field_path` (a model field name, or
    a `__`-separated lookup for a related field).
    """

    class ChoiceListFilter(admin.SimpleListFilter):
        def lookups(self, request, model_admin):
            codes = model_admin.get_queryset(request).values_list(field_path, flat=True).distinct()
            # A reverse or optional relation can produce None via the
            # LEFT JOIN even where .exclude(field="") lets the row through.
            codes = {code for code in codes if code}
            return sorted(
                ((code, choices_class(code).label) for code in codes),
                key=lambda pair: pair[1],
            )

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(**{field_path: self.value()})
            return queryset

    ChoiceListFilter.title = title
    ChoiceListFilter.parameter_name = parameter_name
    return ChoiceListFilter


def is_set_list_filter(field_path: str, *, title: str, parameter_name: str):
    """A SimpleListFilter offering "Yes"/"No" for whether `field_path` (a
    nullable model field, or a `__`-separated lookup) is set.

    Same idea as admin.EmptyFieldListFilter, but with plain Yes/No
    choices and a caller-chosen title, instead of "Empty"/"Not empty"
    and the field's own verbose_name.
    """

    class IsSetListFilter(admin.SimpleListFilter):
        def lookups(self, request, model_admin):
            return (("yes", "Yes"), ("no", "No"))

        def queryset(self, request, queryset):
            if self.value() == "yes":
                return queryset.filter(**{f"{field_path}__isnull": False})
            if self.value() == "no":
                return queryset.filter(**{f"{field_path}__isnull": True})
            return queryset

    IsSetListFilter.title = title
    IsSetListFilter.parameter_name = parameter_name
    return IsSetListFilter


def country_list_filter(region_field_path: str, *, title: str, parameter_name: str):
    """A SimpleListFilter grouping by the country each used *region*
    belongs to (via PLACE_TO_COUNTRY) -- for use where only a Region
    field is available to filter on, e.g. "location__region".
    """

    class CountryListFilter(admin.SimpleListFilter):
        def lookups(self, request, model_admin):
            region_codes = (
                model_admin.get_queryset(request)
                .values_list(region_field_path, flat=True)
                .distinct()
            )
            country_codes = {PLACE_TO_COUNTRY[code] for code in region_codes if code}
            return sorted(
                ((code, Country(code).label) for code in country_codes),
                key=lambda pair: pair[1],
            )

        def queryset(self, request, queryset):
            if self.value():
                matching_regions = [
                    code
                    for code, country_code in PLACE_TO_COUNTRY.items()
                    if country_code == self.value()
                ]
                return queryset.filter(**{f"{region_field_path}__in": matching_regions})
            return queryset

    CountryListFilter.title = title
    CountryListFilter.parameter_name = parameter_name
    return CountryListFilter
