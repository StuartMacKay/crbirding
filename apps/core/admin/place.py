from django import forms
from django.contrib import admin
from django.db.models import Count

from apps.core import reference_data
from apps.core.fields import ScriptCharField
from apps.core.models import Place

from .reference_import import ReferenceImportMixin


class PlaceAdminForm(forms.ModelForm):
    name = ScriptCharField(
        label="Name",
        help_text="The name of the place in each script; at least one is required.",
    )

    class Meta:
        model = Place
        fields = ["name", "code", "country", "active"]


@admin.register(Place)
class PlaceAdmin(ReferenceImportMixin, admin.ModelAdmin):
    form = PlaceAdminForm
    list_display = ("get_name", "code", "country", "active", "used_count")
    list_filter = ("country", "active")
    search_fields = ("code",)
    ordering = ("country", "code")
    autocomplete_fields = ("country",)

    reference_find = staticmethod(reference_data.find_places)
    reference_import_one = staticmethod(reference_data.import_place)
    reference_import_all = staticmethod(reference_data.import_all_places)
    reference_format_match = staticmethod(
        lambda row: (
            row["place_code"],
            row["latin_name"],
            f"{row['place_code']} / {row['country_code']}",
        )
    )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_used_count=Count("locations", distinct=True))

    @admin.display(description="In use", ordering="_used_count")
    def used_count(self, obj):
        return obj._used_count
