"""Admin for User."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Admin for the custom email-based User model."""

    ordering = ["email"]
    list_display = ["email", "language", "is_staff", "is_active", "created"]
    list_filter = ["is_staff", "is_active"]
    search_fields = ["email"]
    readonly_fields = ["created", "modified"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Preferences"), {"fields": ("language", "script")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Timestamps"),
            {"fields": ("created", "modified"), "classes": ("collapse",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
