from django import forms
from django.contrib import admin
from django.db import models

from apps.core import reference_data
from apps.core.models import Species, SpeciesName

from .reference_import import ReferenceImportMixin


class SpeciesNameInline(admin.TabularInline):
    model = SpeciesName
    extra = 1
    ordering = ("language_code",)
    formfield_overrides = {
        models.TextField: {"widget": forms.TextInput},
    }


@admin.register(Species)
class SpeciesAdmin(ReferenceImportMixin, admin.ModelAdmin):
    list_display = ("get_common_name", "scientific_name", "code", "name_count")
    search_fields = ("scientific_name", "code", "names__common_name")
    ordering = ("code",)
    inlines = [SpeciesNameInline]
    formfield_overrides = {
        models.TextField: {"widget": forms.TextInput},
    }

    reference_find = staticmethod(reference_data.find_species)
    reference_import_one = staticmethod(reference_data.import_species)
    reference_import_all = staticmethod(reference_data.import_all_species)
    reference_format_match = staticmethod(
        lambda row: (
            row["euring_code"],
            row["common_name"],
            f"{row['scientific_name']} ({row['euring_code']})",
        )
    )
    reference_extra_actions = (
        (
            "backfill_missing",
            "Backfill names for species already in use",
            reference_data.backfill_missing_species_names,
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("names")

    @admin.display(description="languages")
    def name_count(self, species: Species) -> int:
        return len(species.names.all())


@admin.register(SpeciesName)
class SpeciesNameAdmin(admin.ModelAdmin):
    list_display = ("species", "language_code", "common_name")
    list_filter = ("language_code",)
    search_fields = ("common_name", "species__scientific_name", "species__code")
    autocomplete_fields = ("species",)
    ordering = ("species__code", "language_code")
