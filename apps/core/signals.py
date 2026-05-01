"""Signal handlers for the accounts app."""

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender="users.User")
def create_observer_for_user(sender, instance, created, **kwargs):
    """Automatically create an Observer record when a new User registers."""
    if created:
        from .models import Observer

        Observer.objects.create(
            name=instance.get_full_name() or instance.email,
            user=instance,
        )
