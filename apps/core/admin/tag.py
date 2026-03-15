from django import forms
from django.contrib import admin
from django.db import models

from core.models import Tag

from .filters import ChoicesDropdownFilter


class TagInline(admin.TabularInline):
    """An Observation's Tags -- one row per Position, its colour-mark
    code (see core.utils.codes), checked and standardised on save.
    """

    model = Tag
    extra = 1
    fields = ("position", "code")
    formfield_overrides = {
        models.TextField: {"widget": forms.TextInput},
    }


class TagAdminForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        widgets = {
            "code": forms.TextInput(),
        }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("code", "position", "observation")
    list_filter = (("position", ChoicesDropdownFilter),)
    search_fields = ("code",)
    list_select_related = ("observation",)
    fields = ("observation", "position", "code", "created", "modified")
    readonly_fields = ("created", "modified")
    raw_id_fields = ("observation",)
    form = TagAdminForm
