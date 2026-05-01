"""Admin for Species."""
from django import forms
from django.contrib import admin
from apps.core.models import Species
from apps.core.fields import TranslationCharField


class SpeciesForm(forms.ModelForm):
    common_name = TranslationCharField()

    class Meta:
        fields = "__all__"


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("get_common_name", "scientific_name", "code")
    search_fields = ("common_name", "scientific_name")
    ordering = ("order",)
    form = SpeciesForm
