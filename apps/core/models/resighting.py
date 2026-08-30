from django.db import models
from django.utils.translation import gettext_lazy as _


class Resighting(models.Model):
    """A record of where and when a colour-marked bird was seen in the field.

    The details recorded in a Resighting focus on the species, the colour marks,
    date/time and location. Other information such as age, sex, condition of the
    bird, etc. are of secondary importance, and these can be recorded in the notes.
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
    submitted = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("submitted"),
        help_text=_("When was the record submitted to the project coordinator."),
    )
    species = models.ForeignKey(
        "core.Species",
        on_delete=models.PROTECT,
        related_name="resightings",
        verbose_name=_("species"),
        help_text=_("The species observed."),
    )
    date = models.DateField(
        verbose_name=_("date"),
        help_text=_("The date the resighting was made."),
    )
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_("time"),
        help_text=_("The time the resighting was made."),
    )
    location = models.ForeignKey(
        "core.Location",
        on_delete=models.PROTECT,
        related_name="resightings",
        verbose_name=_("location"),
        help_text=_("The location where the resighting was made."),
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
    photo = models.ImageField(
        upload_to="resightings/%Y/%m/%d/",
        blank=True,
        verbose_name=_("photo"),
        help_text=_(
            "A photo of the bird at the time of the resighting. "
            "Used to verify that the tags were read correctly."
        ),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("notes"),
        help_text=_("Any additional notes about the resighting."),
    )
    observer = models.ForeignKey(
        "core.Observer",
        on_delete=models.PROTECT,
        related_name="resightings",
        verbose_name=_("observer"),
        help_text=_("The person who made this resighting."),
    )
    capture = models.ForeignKey(
        "core.Capture",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="resightings",
        verbose_name=_("capture"),
        help_text=_("The details of where the bird was marked."),
    )

    class Meta:
        verbose_name = _("resighting")
        verbose_name_plural = _("resightings")

    def __str__(self) -> str:
        return f"{self.species.get_common_name()}"
