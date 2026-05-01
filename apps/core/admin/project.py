"""Admin for Project."""

from django.contrib import admin

from apps.core.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "coordinator", "country")
    list_filter = ("country", "species")
    search_fields = ("name", "coordinator")
