from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.contrib import admin

from core.models import Origin, Species

from .filters import choice_list_filter, country_list_filter


class OriginAdminForm(forms.ModelForm):
    class Meta:
        model = Origin
        fields = "__all__"
        widgets = {
            "species": AutocompleteSelect(
                "species", get_label=lambda code: Species(code).label if code else ""
            ),
            "label": forms.TextInput(attrs={"class": "vTextField"}),
        }


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = (
        "species",
        "label",
        "age",
        "sex",
        "location",
        "country",
        "project",
    )
    list_filter = (
        choice_list_filter("species", Species, title="species", parameter_name="species"),
        "project",
        country_list_filter("location__region", title="country", parameter_name="country"),
    )
    search_fields = ("label", "notes")
    ordering = ("project",)
    list_select_related = ("project", "location")
    autocomplete_fields = ("project", "location")
    fields = (
        "species",
        "label",
        "age",
        "sex",
        "date",
        "time",
        "location",
        "latitude",
        "longitude",
        "notes",
        "project",
        "history_url",
        "history_file",
        "created",
        "modified",
    )
    readonly_fields = ("created", "modified")
    form = OriginAdminForm

    @admin.display(description="country")
    def country(self, obj):
        return obj.location.get_country_display()
