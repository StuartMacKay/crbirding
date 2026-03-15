"""
Pytest configuration and shared fixtures for the crbirding test suite.
"""

import os

import pytest
from django.contrib.auth import get_user_model
from django.test import Client

# Ensure test environment settings are applied
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("DJANGO_ENV", "development")

# pytest-playwright's sync API runs its own event loop in a background
# thread even for "sync" tests, which trips Django's guard against ORM
# access from an async context (it can't tell that guard is pointless
# here -- our tests are still plain, single-threaded sync code). This
# is the documented escape valve for exactly that false positive --
# see django.utils.asyncio.async_unsafe -- and only matters for tests.
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture
def client(db):
    """Return a Django test client."""

    return Client()


@pytest.fixture
def authenticated_client(client, user):
    """Return a client authenticated as the test user."""
    client.force_login(user)
    return client


@pytest.fixture
def user(db):
    """Create and return a regular test user."""
    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="TestPassword123!",
    )


@pytest.fixture
def staff_user(db):
    """Create and return a staff test user."""
    User = get_user_model()
    return User.objects.create_user(
        username="staffuser",
        email="staff@example.com",
        password="StaffPassword123!",
        is_staff=True,
    )


@pytest.fixture
def superuser(db):
    """Create and return a superuser."""
    User = get_user_model()
    return User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="AdminPassword123!",
    )
