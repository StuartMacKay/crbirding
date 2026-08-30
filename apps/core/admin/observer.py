from django import forms
from django.contrib import admin
from django.db import models

from apps.core.models import Observer


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = [
        "resightings__location__place__country",
        "resightings__capture__project__country",
    ]
    search_fields = ["name", "user__email"]
    ordering = ["name"]
    formfield_overrides = {
        models.TextField: {"widget": forms.TextInput},
    }
