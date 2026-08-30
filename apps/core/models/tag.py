from django.db import models
from django.utils.translation import gettext_lazy as _

from .colour import Colour
from .direction import Direction
from .position import Position
from .tag_kind import TagType


class Tag(models.Model):
    """One physical colour tag (a ring, flag, nasal saddle, wing tag, or
    neck collar) worn at a given Position on a bird.

    Several Tags can share a Position -- rings are commonly worn
    stacked on one leg segment, read top to bottom -- so `order` records
    where in that stack this one sits; it's meaningless across different
    Positions.

    This is a deliberately structured decomposition of the colour-mark
    notation used to exchange sightings between ringing groups (e.g.
    "BW(A123)" for a blue ring with a white inscription "A123", or "O,Y"
    for an orange ring above a yellow one) rather than storing that
    notation directly: structured fields are what makes "find every
    Lesser Black-backed Gull with a blue ring inscribed starting with
    M" a plain query instead of a regex against an opaque string. See
    apps.core.formatting.format_tags for reconstructing the notation
    from these fields for display.

    Belongs to either a Capture (the tags attached when the bird was
    marked) or a Resighting (the tags read on a later sighting) -- never
    both, and never neither, per the constraint below. Keeping one Tag
    model for both, rather than a second near-identical model for
    Captures, is what makes apps.core.matching.link_matching_resightings
    a plain set-equality comparison between the two.
    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated"),
        help_text=_("When was the record last updated."),
    )
    capture = models.ForeignKey(
        "core.Capture",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="tags",
        verbose_name=_("capture"),
        help_text=_("The Capture that the tag belongs to, if attached when the bird was marked."),
    )
    resighting = models.ForeignKey(
        "core.Resighting",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="tags",
        verbose_name=_("resighting"),
        help_text=_("The Resighting that the tag belongs to, if read on a later sighting."),
    )
    position = models.TextField(
        choices=Position.choices,
        verbose_name=_("position"),
        help_text=_("The position of the tag on the bird."),
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("order"),
        help_text=_("Stacking order (top to bottom) among tags sharing the same position."),
    )
    kind = models.TextField(
        choices=TagType.choices,
        default=TagType.RING,
        verbose_name=_("kind"),
        help_text=_("The physical type of tag."),
    )
    colour = models.TextField(
        choices=Colour.choices,
        verbose_name=_("colour"),
        help_text=_("The colour of the tag."),
    )
    second_colour = models.TextField(
        choices=Colour.choices,
        blank=True,
        verbose_name=_("second colour"),
        help_text=_("The second colour, for a two-colour striped ring."),
    )
    inscription = models.TextField(
        blank=True,
        verbose_name=_("inscription"),
        help_text=_("The engraved text on the tag, if any."),
    )
    inscription_colour = models.TextField(
        choices=Colour.choices,
        blank=True,
        verbose_name=_("inscription colour"),
        help_text=_("The colour of the inscription, if different from the tag itself."),
    )
    inscription_direction = models.TextField(
        choices=Direction.choices,
        blank=True,
        verbose_name=_("inscription direction"),
        help_text=_("The direction the inscription reads in, if it could be ambiguous."),
    )
    uncertain = models.BooleanField(
        default=False,
        verbose_name=_("uncertain"),
        help_text=_("Was some part of this tag not clearly seen or read?"),
    )

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        ordering = ["position", "order"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(capture__isnull=False, resighting__isnull=True)
                    | models.Q(capture__isnull=True, resighting__isnull=False)
                ),
                name="tag_belongs_to_exactly_one_owner",
            ),
        ]

    def __str__(self) -> str:
        from apps.core.formatting import format_tag

        return f"{format_tag(self)} ({self.get_position_display()})"
