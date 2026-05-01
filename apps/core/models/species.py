"""Species model."""
import json
import logging

from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from .base import BaseModel

log = logging.getLogger(__name__)


class Species(BaseModel):
    """The species of bird tagged or observed."""

    order = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("taxonomy order"),
        help_text=_("The position in the eBird/Clements taxonomic order."),
    )
    code = models.TextField(
        unique=True,
        verbose_name=_("code"),
        help_text=_("The eBird species code used to uniquely identify this species."),
    )
    common_name = models.JSONField(
        default=dict,
        verbose_name=_("common name"),
        help_text=_(
            "The standardised common name for the species in each supported language, "
            "stored as a JSON object with language codes as keys. "
            'For example: {"en": "Mallard", "de": "Stockente", "fr": "colvert"}.'
        ),
    )
    scientific_name = models.TextField(
        verbose_name=_("scientific name"),
        help_text=_("The scientific (Latin) name for the species."),
    )

    class Meta:
        verbose_name = _("species")
        verbose_name_plural = _("species")

    def __repr__(self) -> str:
        return str(self.code)

    def __str__(self) -> str:
        return self.get_common_name()

    def get_common_name(self) -> str:
        try:
            data = json.loads(self.common_name)
            common_name = data.get(get_language(), "")
            if not common_name:
                common_name = data.get(next(iter(data)), "")
        except json.JSONDecodeError:
            log.error("Incorrect JSON for Species common_name: %s", self.id)
            common_name = ""
        return common_name
