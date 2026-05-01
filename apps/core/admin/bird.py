"""Admin for Bird."""

from django.contrib import admin

from apps.core.models import Bird


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ("species", "project",)
    list_filter = ("species", "project",)
    search_fields = ("notes",)
    ordering = ("project",)
    list_select_related = ("speciees", "project")
    autocomplete_fields = ("species", "project",)
