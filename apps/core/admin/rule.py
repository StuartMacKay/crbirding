from django.contrib import admin

from apps.core.models import Rule


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("species", "position", "regex", "project")
    list_filter = ("species", "position", "project")
    search_fields = ("regex", "species__scientific_name", "project__coordinator")
    autocomplete_fields = ("species", "project")
    ordering = ("species", "position")
