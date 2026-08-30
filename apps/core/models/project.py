from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """The project responsible for marking the birds."""

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
        help_text=_("When was the record last updated."),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("description"),
        help_text=_("A description of the project."),
    )
    country = models.OneToOneField(
        "core.Country",
        on_delete=models.PROTECT,
        related_name="project",
        verbose_name=_("country"),
        help_text=_("The country where the project is based."),
    )
    coordinator = models.TextField(
        verbose_name=_("coordinator"),
        help_text=_("The name of the project coordinator."),
    )
    contact = models.EmailField(
        blank=True,
        verbose_name=_("contact"),
        help_text=_("The email address where observations should be sent."),
    )
    submit = models.URLField(
        blank=True,
        verbose_name=_("submit"),
        help_text=_("The website where observations should be submitted."),
    )
    site = models.URLField(
        blank=True,
        verbose_name=_("website"),
        help_text=_("The website describing the project."),
    )

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
