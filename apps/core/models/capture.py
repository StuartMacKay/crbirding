from django.db import models
from django.utils.translation import gettext_lazy as _

from .age import Age
from .sex import Sex


class Capture(models.Model):
    """The details of when and where a bird was first caught and marked
    with colour rings, leg flags, wing tags, a nasal saddle, or a neck
    collar.

    A bird is only ever captured (in this sense) once -- every subsequent
    resighting, however it happened (seen in the field, caught again,
    found dead), is a Resighting pointing back to this record.
    """

    class Resolution(models.TextChoices):
        """The accuracy of the given date.

        If an incomplete code is recored it still might be possible to narrow
        down when and where the bird was marked. For example, if a given colour
        combination was used in a given year, or month.
        """

        DAY = "d", _("Day")
        MONTH = "m", _("Month")
        YEAR = "y", _("Year")

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
    species = models.ForeignKey(
        "core.Species",
        on_delete=models.PROTECT,
        related_name="captures",
        verbose_name=_("species"),
        help_text=_("The species recorded at the time of capture."),
    )
    age = models.TextField(
        choices=Age.choices,
        default=Age.UNKNOWN,
        verbose_name=_("age"),
        help_text=_("The age of the bird when it was marked, using the EURING age code."),
    )
    sex = models.TextField(
        choices=Sex.choices,
        default=Sex.UNKNOWN,
        verbose_name=_("sex"),
        help_text=_("The sex of the bird, using the EURING sex code."),
    )
    date = models.DateField(
        verbose_name=_("date"),
        help_text=_("The date the bird was marked."),
    )
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_("time"),
        help_text=_("The time the bird was marked."),
    )
    resolution = models.TextField(
        choices=Resolution.choices,
        default=Resolution.DAY,
        verbose_name=_("resolution"),
        help_text=_("The units the date is accurate to."),
    )
    location = models.ForeignKey(
        "core.Location",
        on_delete=models.PROTECT,
        related_name="captures",
        verbose_name=_("location"),
        help_text=_("The location where the bird was marked."),
    )
    latitude = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name=_("latitude"),
        help_text=_("The precise latitude of the bird, overriding the location coordinates."),
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name=_("longitude"),
        help_text=_("The precise longitude of the bird, overriding the location coordinates."),
    )
    accuracy = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("accuracy"),
        help_text=_(
            "The estimated distance in metres, from the coordinates, "
            "to the actual position of the bird."
        ),
    )
    project = models.ForeignKey(
        "core.Project",
        on_delete=models.PROTECT,
        related_name="captures",
        verbose_name=_("project"),
        help_text=_("The project that tagged this bird."),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("comments"),
        help_text=_("Any additional notes about the bird."),
    )

    class Meta:
        verbose_name = _("capture")
        verbose_name_plural = _("captures")
