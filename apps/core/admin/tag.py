from django import forms
from django.contrib import admin
from django.db import models

from apps.core.models import Tag


class BaseTagInline(admin.TabularInline):
    """Shared by ResightingAdmin and CaptureAdmin -- Django infers which
    FK ties a Tag to its parent from whichever of Tag.capture/resighting
    points at that parent model, so no fk_name is needed on either use.
    """

    model = Tag
    extra = 1
    fields = (
        "position",
        "order",
        "kind",
        "colour",
        "second_colour",
        "inscription",
        "inscription_colour",
        "inscription_direction",
        "uncertain",
    )
    ordering = ("position", "order")
    formfield_overrides = {
        models.TextField: {"widget": forms.TextInput},
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "capture",
        "resighting",
        "position",
        "kind",
        "colour",
        "second_colour",
        "inscription",
    )
    list_filter = ("position", "kind", "colour")
    search_fields = ("inscription", "resighting__notes", "capture__notes")
    autocomplete_fields = ("capture", "resighting")
    ordering = ("resighting", "capture", "position", "order")
