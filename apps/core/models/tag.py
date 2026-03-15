from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .position import Position

DUPLICATE_POSITION_MESSAGE = _(
    "There's already a row for this position -- put everything worn there in one "
    "code, top to bottom, separated by commas."
)


class Tag(models.Model):
    """Everything worn at one Position on an observed bird, as its
    colour-mark code -- e.g. "R,WN(KY)d" for a red ring above a white
    one inscribed "KY" -- see core.utils.codes for the notation.

    One per Position per Observation: a bird is identified by, and a
    project's Rules are matched against, the whole stack at a position,
    not its individual rings, so that's the unit stored. The code is
    checked and written one standard way on save (normalise_code), so
    the same marks always give the same text to match and compare.

    Only Observations have Tags. An Origin is the bird once it's been
    identified -- it carries a display `label` instead, and nothing
    about it needs to be matched.
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
    observation = models.ForeignKey(
        "core.Observation",
        on_delete=models.CASCADE,
        related_name="tags",
        verbose_name=_("observation"),
        help_text=_("The observation the tags were read on."),
    )
    position = models.TextField(
        choices=Position.choices,
        verbose_name=_("position"),
        help_text=_("Where on the bird the tags are worn."),
    )
    code = models.TextField(
        verbose_name=_("code"),
        help_text=_('The rings, flags, etc. at this position, top to bottom, e.g. "R,WN(KY)d".'),
    )

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(
                fields=["observation", "position"],
                name="one_tag_per_position",
                violation_error_message=DUPLICATE_POSITION_MESSAGE,
            ),
        ]

    def __str__(self) -> str:
        return f"{self.position}:{self.code}"

    def save(self, *args, **kwargs):
        from core.utils.codes import normalise_code

        self.code = normalise_code(self.code)
        super().save(*args, **kwargs)

    def clean(self):
        from core.utils.codes import normalise_code

        try:
            self.code = normalise_code(self.code)
        except ValueError as exc:
            raise ValidationError({"code": str(exc)}) from exc
