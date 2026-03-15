"""
Pytest configuration and shared fixtures for the crbirding test suite.
"""

import os

import django
import pytest

# Ensure test environment settings are applied
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("DJANGO_ENV", "development")


@pytest.fixture(scope="session")
def django_db_setup():
    """Use a test database for the test session."""
    pass


@pytest.fixture
def client(db):
    """Return a Django test client."""
    from django.test import Client

    return Client()


@pytest.fixture
def authenticated_client(client, user):
    """Return a client authenticated as the test user."""
    client.force_login(user)
    return client


@pytest.fixture
def user(db):
    """Create and return a regular test user."""
    from django.contrib.auth import get_user_model

    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="TestPassword123!",
    )


@pytest.fixture
def staff_user(db):
    """Create and return a staff test user."""
    from django.contrib.auth import get_user_model

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
    from django.contrib.auth import get_user_model

    User = get_user_model()
    return User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="AdminPassword123!",
    )
