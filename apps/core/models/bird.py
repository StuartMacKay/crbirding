"""Bird model."""

from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.db.models.expressions import RawSQL
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class Bird(BaseModel):
    """Bird represents a bird tagged with colour rings, leg flags, wing tags,
    a nasal saddle, or a neck collar.
    """
    species = models.ForeignKey(
        "core.Species",
        on_delete=models.PROTECT,
        related_name="origins",
        verbose_name=_("species"),
        help_text=_("The species recorded at the time of capture."),
    )
    project = models.ForeignKey(
        "core.Project",
        on_delete=models.PROTECT,
        related_name="origins",
        verbose_name=_("project"),
        help_text=_("The project that tagged this bird."),
    )
    tags = models.JSONField(
        default=dict,
        verbose_name=_("tags"),
        help_text=_(
            "A dictionary of all tags and their positions. "
            'For example: {"LA": "WN(ABC)", "RA": "M"}.'
        ),
    )
    search = models.JSONField(
        default=dict,
        verbose_name=_("search"),
        help_text=_(
            "A dictionary of key-value pairs which are used to search the tags."
        ),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("comments"),
        help_text=_("Any additional notes about the bird."),
    )

    class Meta:
        verbose_name = _("bird")
        verbose_name_plural = _("birds")
        indexes = [
            GinIndex(fields=["search"]),
            models.Index(
                RawSQL("((search->>'code'))", []),
                name="idx_bird_search_code",
            ),
        ]
