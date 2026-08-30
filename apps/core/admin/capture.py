from django.contrib import admin, messages

from apps.core.matching import link_matching_resightings
from apps.core.models import Capture

from .tag import BaseTagInline


@admin.register(Capture)
class CaptureAdmin(admin.ModelAdmin):
    list_display = (
        "species",
        "age",
        "sex",
        "location",
        "country",
        "project",
    )
    list_filter = (
        "species",
        "project",
        "location__place__country",
    )
    search_fields = ("notes",)
    ordering = ("project",)
    list_select_related = ("species", "project", "location", "location__place__country")
    autocomplete_fields = (
        "species",
        "project",
        "location",
    )
    inlines = [BaseTagInline]

    @admin.display(description="country")
    def country(self, obj):
        return obj.location.place.country

    def save_related(self, request, form, formsets, change):
        """After the inline Tag rows are saved (this runs after them,
        unlike save_model), link any existing Resighting whose tags
        exactly match -- see apps.core.matching.
        """
        super().save_related(request, form, formsets, change)
        linked = link_matching_resightings(form.instance)
        if linked:
            messages.info(request, f"Linked {linked} existing resighting(s) with matching tags.")
