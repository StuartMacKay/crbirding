"""Deleting a model's uploaded files once nothing points at them --
Django itself never does: replacing a FileField's file only ever adds
the new one alongside, and deleting the row leaves its file behind, so
without this every re-upload or delete would leave an orphan in
MEDIA_ROOT.

Deletes wait for the surrounding transaction to commit -- if it rolls
back instead, the row still points at the file, so it has to still be
there.
"""

from django.db import models, transaction


def stored_file_name(instance: models.Model, field_name: str) -> str | None:
    """The file name `instance` currently has saved in the database for
    `field_name` -- read before a save() that may replace it.
    """
    if instance.pk is None:
        return None
    return (
        type(instance)
        ._default_manager.filter(pk=instance.pk)
        .values_list(field_name, flat=True)
        .first()
    )


def delete_replaced_file(instance: models.Model, field_name: str, previous: str | None) -> None:
    """After a save(): delete `previous` if `field_name` no longer
    points at it (a new file was uploaded, or it was cleared).
    """
    field_file = getattr(instance, field_name)
    if previous and previous != field_file.name:
        _delete_on_commit(field_file.storage, previous)


def delete_file(field_file) -> None:
    """Delete `field_file` itself -- for when its row is deleted."""
    if field_file:
        _delete_on_commit(field_file.storage, field_file.name)


def _delete_on_commit(storage, name: str) -> None:
    transaction.on_commit(lambda: storage.delete(name))
