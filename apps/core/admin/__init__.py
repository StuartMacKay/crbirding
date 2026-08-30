"""Core admin."""

from .capture import CaptureAdmin
from .country import CountryAdmin
from .location import LocationAdmin
from .observer import ObserverAdmin
from .place import PlaceAdmin
from .project import ProjectAdmin
from .resighting import ResightingAdmin
from .rule import RuleAdmin
from .species import SpeciesAdmin
from .tag import TagAdmin

__all__ = [
    "CaptureAdmin",
    "CountryAdmin",
    "LocationAdmin",
    "ObserverAdmin",
    "PlaceAdmin",
    "ProjectAdmin",
    "ResightingAdmin",
    "RuleAdmin",
    "SpeciesAdmin",
    "TagAdmin",
]
