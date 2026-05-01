"""Project model."""
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.db.models.expressions import RawSQL
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

from .base import BaseModel


class Project(BaseModel):
    """A research project responsible for marking birds with colour tags."""

    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The name of the project."),
    )
    species = models.ForeignKey(
        "core.Species",
        on_delete=models.PROTECT,
        related_name="projects",
        verbose_name=_("species"),
        help_text=_("The primary species of bird being marked by this project."),
    )
    search = models.JSONField(
        default=dict,
        verbose_name=_("search"),
        help_text=_(
            "A dictionary of key-value pairs which are used to search "
            "for the combinations used by the project."
        ),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("description"),
        help_text=_("A description of the project."),
    )
    country = CountryField()
    coordinator = models.TextField(
        verbose_name=_("coordinator"),
        help_text=_("The name of the project coordinator."),
    )
    email = models.EmailField(
        blank=True,
        verbose_name=_("email"),
        help_text=_("The email address where observations should be sent."),
    )
    submit = models.URLField(
        blank=True,
        verbose_name=_("submission URL"),
        help_text=_("The URL of a website where observations may be submitted."),
    )
    url = models.URLField(
        blank=True,
        verbose_name=_("website URL"),
        help_text=_("The URL of the website describing this project."),
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        indexes = [
            GinIndex(fields=["search"]),
            models.Index(
                RawSQL("((search->>'code'))", []),
                name="idx_project_search_code",
            ),
        ]

    def __str__(self):
        return self.name
