"""Admin for Location."""

from django.contrib import admin

from apps.core.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "country", "latitude", "longitude")
    list_filter = ("country",)
    search_fields = ("name",)
