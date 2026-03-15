from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .files import delete_file, delete_replaced_file, stored_file_name


class Photo(models.Model):
    """A photo attached to a Observation -- a Observation can have
    several, e.g. separate shots of each tag or angle.
    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    observation = models.ForeignKey(
        "core.Observation",
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name=_("observation"),
        help_text=_("The observation this photo was taken for."),
    )
    image = models.ImageField(
        upload_to="observations/%Y/%m/%d/",
        verbose_name=_("photo"),
        help_text=_(
            "A photo of the bird at the time of the observation. "
            "Used to verify that the tags were read correctly."
        ),
    )

    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")

    def __str__(self) -> str:
        return self.image.name

    def save(self, *args, **kwargs):
        """Replacing `image` deletes the file it replaced -- see
        core.models.files.
        """
        previous = stored_file_name(self, "image")
        super().save(*args, **kwargs)
        delete_replaced_file(self, "image", previous)


@receiver(post_delete, sender=Photo)
def _delete_image_file(sender, instance, **kwargs):
    """Deleting a Photo -- directly, removed from its Observation's
    photo formset, or by cascade when the Observation is deleted --
    deletes its image file too.
    """
    delete_file(instance.image)
