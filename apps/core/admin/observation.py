from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.forms import ObservationImportForm
from core.models import Observation, Photo, Species
from core.utils.bulk_import import import_observations_csv
from core.utils.events import record_origin_linked
from core.utils.formatting import format_colour_marks

from .filters import choice_list_filter, is_set_list_filter
from .tag import TagInline


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ("image",)


class ObservationAdminForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = "__all__"
        widgets = {
            "species": AutocompleteSelect(
                "species", get_label=lambda code: Species(code).label if code else ""
            ),
        }


@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = (
        "species",
        "colour_marks",
        "date",
        "time",
        "location_name",
        "observer_names",
        "found",
    )
    list_filter = (
        choice_list_filter("species", Species, title="species", parameter_name="species"),
        is_set_list_filter("origin", title=_("Found"), parameter_name="found"),
    )
    search_fields = ("tags__code",)
    ordering = ("-date",)
    autocomplete_fields = ["location", "owner", "observers"]
    change_list_template = "admin/core/change_list_with_csv_import.html"
    fields = (
        "species",
        "age",
        "sex",
        "date",
        "time",
        "location",
        "latitude",
        "longitude",
        "accuracy",
        "notes",
        "owner",
        "origin",
        "created",
        "modified",
    )
    readonly_fields = ["created", "modified"]
    form = ObservationAdminForm
    inlines = [TagInline, PhotoInline]

    @admin.display(description=_("location"))
    def location_name(self, obj):
        return obj.location.get_name()

    @admin.display(description=_("observers"))
    def observer_names(self, obj):
        return ", ".join(observer.name for observer in obj.observers.all())

    @admin.display(description=_("colour marks"))
    def colour_marks(self, obj):
        return format_colour_marks(obj.tags.all())

    @admin.display(description=_("found"), boolean=True)
    def found(self, obj):
        return obj.origin_id is not None

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if "origin" in form.changed_data and obj.origin_id:
            record_origin_linked(obj)

    @admin.display(description=_("origin"))
    def origin(self, obj):
        return obj.origin.location.get_country_display() if obj.origin else ""

    def get_urls(self):
        import_url = path(
            "import-csv/",
            self.admin_site.admin_view(self.import_csv_view),
            name="core_observation_import_csv",
        )
        return [import_url, *super().get_urls()]

    def import_csv_view(self, request):
        if request.method == "POST":
            form = ObservationImportForm(request.POST, request.FILES)
            if form.is_valid():
                report = import_observations_csv(form.cleaned_data["csv_file"])
                if report.created:
                    messages.success(request, f"Imported {report.created} observation(s).")
                if report.duplicates:
                    messages.info(
                        request,
                        f"Skipped {report.duplicates} row(s) already imported previously.",
                    )
                    for detail in report.duplicate_details:
                        messages.info(request, detail)
                if report.skipped:
                    messages.warning(request, f"Skipped {report.skipped} row(s); see below.")
                for error in report.errors[:50]:
                    messages.error(request, error)
                if not report.errors:
                    return redirect("admin:core_observation_changelist")
        else:
            form = ObservationImportForm()

        context = {
            **self.admin_site.each_context(request),
            "title": "Import observations from CSV",
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "admin/core/observation_import.html", context)
