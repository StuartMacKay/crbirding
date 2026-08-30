from django.contrib import admin

from apps.core.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("coordinator", "country")
    list_filter = ("country",)
    search_fields = ("coordinator", "description")
    autocomplete_fields = ("country",)
