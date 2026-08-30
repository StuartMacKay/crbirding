from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """A country, dependent territory, or other named area (e.g. an area
    at sea) that a Place or Project can be located in.

    This is a database table, not a fixed choices list, so a new entry
    -- a historical political entity needed for an old ringing record,
    say -- can be added by an administrator without a new application
    release. Rows are never deleted automatically; that decision is left
    to an administrator, who can check the admin list for how many
    Places and Projects reference a row before removing it.
    """

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
    code = models.TextField(
        db_index=True,
        unique=True,
        verbose_name=_("code"),
        help_text=_(
            "The ISO 3166-1 alpha-3 code, or a user-assigned alpha-3 code "
            "for a non-ISO entity such as an area at sea."
        ),
    )
    name = models.TextField(
        verbose_name=_("name"),
        help_text=_("The name of the country or area."),
    )

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")
        ordering = ["name"]

    def __repr__(self) -> str:
        return str(self.code)

    def __str__(self):
        return self.name
