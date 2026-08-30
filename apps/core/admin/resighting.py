from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.models import Resighting

from .resighting_import import ResightingImportMixin
from .tag import BaseTagInline


@admin.register(Resighting)
class ResightingAdmin(ResightingImportMixin, admin.ModelAdmin):
    list_display = (
        "species",
        "location",
        "date",
        "observer",
        "origin",
    )
    list_filter = ("species",)
    search_fields = ("notes", "observer__name")
    ordering = ("-date",)
    inlines = [BaseTagInline]
    autocomplete_fields = ["location", "species"]
    readonly_fields = ["created", "modified", "submitted"]

    @admin.display(description=_("origin"))
    def origin(self, obj):
        return f"{obj.capture.location.place}" if obj.capture else ""
