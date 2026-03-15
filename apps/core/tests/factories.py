"""factory_boy factories for every model tests in this package need.

One factory per model, each with just enough default data to save
cleanly on its own -- pass overrides for anything a specific test cares
about. Related objects are built via SubFactory rather than shared
fixtures, so each test gets its own isolated object graph unless it
explicitly reuses one.
"""

import datetime
from decimal import Decimal

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from core.models import (
    Country,
    Location,
    Observation,
    Observer,
    Origin,
    Position,
    Project,
    Rule,
    Species,
    Tag,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_staff = False
    is_superuser = False


class StaffUserFactory(UserFactory):
    is_staff = True


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    # "GB--" is EURING's own code for the UK as a whole (it has no
    # finer-grained code of its own -- see core.models.region) --
    # a real, always-valid Region choice, standing in for "don't care
    # which place, just need a valid one" in most tests.
    region = "GB--"
    name = factory.LazyFunction(lambda: {"Latn": "Test Location"})
    latitude = Decimal("51.5074")
    longitude = Decimal("-0.1278")


class ObserverFactory(DjangoModelFactory):
    class Meta:
        model = Observer

    name = factory.Sequence(lambda n: f"Observer {n}")


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: f"Project {n}")
    coordinator = factory.Sequence(lambda n: f"Coordinator {n}")
    # country is unique per Project; cycle through real Country codes
    # rather than a fixed default so more than one Project can exist.
    country = factory.Sequence(lambda n: Country.choices[n % len(Country.choices)][0])


class OriginFactory(DjangoModelFactory):
    class Meta:
        model = Origin

    # "00010" is EURING's code for Common Ostrich -- a real, always-valid
    # Species choice, standing in for "don't care which species" in most tests.
    species = Species.COMMON_OSTRICH
    label = factory.Sequence(lambda n: f"W({n})")
    age = ""
    sex = ""
    date = datetime.date(2026, 1, 1)
    location = factory.SubFactory(LocationFactory)
    project = factory.SubFactory(ProjectFactory)


class ObservationFactory(DjangoModelFactory):
    class Meta:
        model = Observation

    species = Species.COMMON_OSTRICH
    date = datetime.date(2026, 1, 15)
    location = factory.SubFactory(LocationFactory)

    @factory.post_generation
    def observers(self, create, extracted, **kwargs):
        """`observers` is a ManyToManyField, so it can't be set until
        after the instance is saved -- defaults to one auto-created
        Observer; pass `observers=[...]` to set specific ones instead.
        """
        if not create:
            return
        for observer in extracted if extracted is not None else [ObserverFactory()]:
            self.observers.add(observer)


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    observation = factory.SubFactory(ObservationFactory)
    position = Position.LEFT_BELOW
    code = "W"


class RuleFactory(DjangoModelFactory):
    class Meta:
        model = Rule

    species = Species.COMMON_OSTRICH
    position = Position.LEFT_BELOW
    regex = r"^W\(.*\)$"
    project = factory.SubFactory(ProjectFactory)
