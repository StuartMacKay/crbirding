"""Core admin."""

from .bird import BirdAdmin
from .location import LocationAdmin
from .observation import ObservationAdmin
from .project import ProjectAdmin
from .species import SpeciesAdmin

__all__ = [
    "BirdAdmin",
    "LocationAdmin",
    "ObservationAdmin",
    "ProjectAdmin",
    "SpeciesAdmin",
]
