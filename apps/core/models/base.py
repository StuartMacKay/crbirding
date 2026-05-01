"""Abstract base model providing timestamps, soft-deletion, and history."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Abstract base class providing timestamps, soft-deletion, and history for all models."""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
        help_text=_("The date and time when this record was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at"),
        help_text=_("The date and time when this record was last updated."),
    )

    class Meta:
        abstract = True
