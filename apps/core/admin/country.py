from django.contrib import admin
from django.db.models import Count

from apps.core import reference_data
from apps.core.models import Country

from .reference_import import ReferenceImportMixin


@admin.register(Country)
class CountryAdmin(ReferenceImportMixin, admin.ModelAdmin):
    list_display = ("name", "code", "used_count")
    search_fields = ("code", "name")
    ordering = ("name",)

    reference_find = staticmethod(reference_data.find_countries)
    reference_import_one = staticmethod(reference_data.import_country)
    reference_import_all = staticmethod(reference_data.import_all_countries)
    reference_format_match = staticmethod(lambda row: (row["code"], row["name"], row["code"]))

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _place_count=Count("places", distinct=True),
            _project_count=Count("project", distinct=True),
        )

    @admin.display(description="In use", ordering="_place_count")
    def used_count(self, obj):
        return obj._place_count + obj._project_count
