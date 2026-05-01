"""Admin for Observation."""

from django.contrib import admin

from apps.core.models import Observation


@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ("observer", "location", "date", "status")
    list_filter = ("status", "location__country")
    search_fields = ("notes", "observer__name")
    ordering = ("-date",)
