from django import forms
from django.contrib import admin

from apps.core.fields import ScriptCharField
from apps.core.models import Location


class LocationAdminForm(forms.ModelForm):
    name = ScriptCharField(
        label="Name",
        help_text="The name of the location in each script; at least one is required.",
    )

    class Meta:
        model = Location
        fields = "__all__"
        widgets = {
            "label": forms.TextInput(),
        }


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ("get_name", "label", "place", "latitude", "longitude", "accuracy")
    list_filter = ("place__country", "captures__project__country")
    search_fields = ("name__Latn", "name__Cyrl", "name__Grek")
