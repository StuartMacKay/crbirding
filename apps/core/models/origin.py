from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .age import Age
from .files import delete_file, delete_replaced_file, stored_file_name
from .sex import Sex
from .species import Species


class Origin(models.Model):
    """The details of when and where a bird was first caught and marked.

    A bird is only ever marked (in this sense) once -- every subsequent
    observation, however it happened (seen in the field, caught again,
    found dead), is a Observation pointing back to this record.

    Has no Tags of its own: Observations are what get matched (see
    core.utils.matching), and linking one to its Origin is what
    identifies the bird. `label` is only how the bird is shown to
    people -- nothing relies on it.
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
    species = models.CharField(
        max_length=5,
        choices=Species.choices,
        verbose_name=_("species"),
        help_text=_("The species recorded at the time of marking."),
    )
    label = models.TextField(
        verbose_name=_("label"),
        help_text=_(
            'The bird\'s colour marks written short, e.g. "BW(123)" -- just enough '
            "to recognise it by. Only for display."
        ),
    )
    age = models.TextField(
        blank=True,
        choices=Age.choices,
        verbose_name=_("age"),
        help_text=_("The age of the bird, using the EURING age code."),
    )
    sex = models.TextField(
        blank=True,
        choices=Sex.choices,
        verbose_name=_("sex"),
        help_text=_("The sex of the bird, using the EURING sex code."),
    )
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("date"),
        help_text=_("The date the bird was marked."),
    )
    time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_("time"),
        help_text=_("The time the bird was marked."),
    )
    location = models.ForeignKey(
        "core.Location",
        on_delete=models.PROTECT,
        related_name="origins",
        verbose_name=_("location"),
        help_text=_("The location where the bird(s) was marked."),
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
    project = models.ForeignKey(
        "core.Project",
        on_delete=models.PROTECT,
        related_name="origins",
        verbose_name=_("project"),
        help_text=_("The project that tagged this bird."),
    )
    history_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_("life history URL"),
        help_text=_("The link to the life history of the bird."),
    )
    history_file = models.FileField(
        blank=True,
        null=True,
        upload_to="histories/%Y/%m/%d/",
        verbose_name=_("life history file"),
        help_text=_("The file containing the life history of the bird."),
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("notes"),
        help_text=_("Any additional notes."),
    )

    class Meta:
        verbose_name = _("origin")
        verbose_name_plural = _("origins")

    def __str__(self) -> str:
        return f"{Species(self.species).label} ({self.label})"

    def save(self, *args, **kwargs):
        """Replacing or clearing `history_file` deletes the file it
        replaced -- see core.models.files.
        """
        previous = stored_file_name(self, "history_file")
        super().save(*args, **kwargs)
        delete_replaced_file(self, "history_file", previous)


@receiver(post_delete, sender=Origin)
def _delete_history_file(sender, instance, **kwargs):
    """Deleting an Origin (directly, or by cascade) deletes its life
    history file too.
    """
    delete_file(instance.history_file)
