from django import forms
from django.contrib import admin

from core.models import Country, Observer

from .filters import choice_list_filter, country_list_filter


class ObserverAdminForm(forms.ModelForm):
    class Meta:
        model = Observer
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "vTextField"}),
        }


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    list_filter = [
        country_list_filter(
            "observations__location__region", title="country", parameter_name="country"
        ),
        choice_list_filter(
            "observations__origin__project__country",
            Country,
            title="origin project country",
            parameter_name="project_country",
        ),
    ]
    search_fields = [
        "name",
    ]
    autocomplete_fields = ["user"]
    ordering = ["name"]
    fields = ("name", "user", "created", "modified")
    readonly_fields = ("created", "modified")
    form = ObserverAdminForm
