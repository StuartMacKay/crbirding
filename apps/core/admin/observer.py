"""Admin for Observer."""

from django.contrib import admin

from apps.core.models import Observer


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at"]
    search_fields = ["name", "user__email"]
    ordering = ["name"]
