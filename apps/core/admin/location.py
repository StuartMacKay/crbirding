from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from core.fields import AlphabetCharField
from core.forms import LocationImportForm
from core.models import PLACE_TO_COUNTRY, Country, Location, Region
from core.utils.csv_export import csv_download_response
from core.utils.location_export import export_locations_csv
from core.utils.location_import import import_locations_csv

from .filters import choice_list_filter, country_list_filter


class LocationAdminForm(forms.ModelForm):
    name = AlphabetCharField(
        label="Name",
        help_text="The name of the location in each alphabet; at least one is required.",
    )
    # Not a model field -- narrows the region autocomplete below to one
    # country's regions. The region alone is what's actually stored,
    # since it always implies exactly one country (see Location.region).
    country = forms.CharField(
        label="Country",
        required=False,
        widget=AutocompleteSelect(
            "country", get_label=lambda code: Country(code).label if code else ""
        ),
    )

    class Meta:
        model = Location
        fields = "__all__"
        widgets = {
            "region": AutocompleteSelect(
                "region",
                depends_on="id_country",
                get_label=lambda code: Region(code).label if code else "",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        region = self.initial.get("region") or getattr(self.instance, "region", "")
        if region:
            self.initial["country"] = PLACE_TO_COUNTRY[region]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "region",
        "latitude",
        "longitude",
        "accuracy",
    )
    list_filter = (
        country_list_filter("region", title="country", parameter_name="country"),
        choice_list_filter(
            "origins__project__country",
            Country,
            title="origin project country",
            parameter_name="project_country",
        ),
    )
    search_fields = ("name__Latn", "name__Cyrl", "name__Grek")
    change_list_template = "admin/core/change_list_with_csv_import.html"
    fields = (
        "name",
        "region",
        "country",
        "latitude",
        "longitude",
        "accuracy",
        "notes",
        "created",
        "modified",
    )
    readonly_fields = ("created", "modified")
    form = LocationAdminForm
    actions = ["export_csv"]

    @admin.action(description="Export selected to CSV")
    def export_csv(self, request, queryset):
        return csv_download_response(export_locations_csv(queryset), "locations.csv")

    def get_urls(self):
        import_url = path(
            "import-csv/",
            self.admin_site.admin_view(self.import_csv_view),
            name="core_location_import_csv",
        )
        return [import_url, *super().get_urls()]

    def import_csv_view(self, request):
        if request.method == "POST":
            form = LocationImportForm(request.POST, request.FILES)
            if form.is_valid():
                report = import_locations_csv(form.cleaned_data["csv_file"])
                if report.created:
                    messages.success(request, f"Imported {report.created} location(s).")
                if report.duplicates:
                    messages.info(
                        request,
                        f"Skipped {report.duplicates} row(s) already on file.",
                    )
                if report.skipped:
                    messages.warning(request, f"Skipped {report.skipped} row(s); see below.")
                for error in report.errors[:50]:
                    messages.error(request, error)
                if not report.errors:
                    return redirect("admin:core_location_changelist")
        else:
            form = LocationImportForm()

        context = {
            **self.admin_site.each_context(request),
            "title": "Import locations from CSV",
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "admin/core/location_import.html", context)
