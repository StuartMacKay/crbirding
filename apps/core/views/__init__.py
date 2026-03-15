"""Core views."""

from .home import HomeView
from .location import LocationDetailView
from .observation import (
    EditObservationView,
    ImportObservationsView,
    LinkObservationView,
    MyObservationsView,
    ObservationDetailView,
    ObservationEventsView,
    SendToProjectView,
    SubmitObservationView,
)
from .origin import LifeHistoryView, SubmitOriginView
from .photo import AddPhotoRowView
from .tag import AddTagRowView

__all__ = [
    "AddPhotoRowView",
    "AddTagRowView",
    "EditObservationView",
    "HomeView",
    "ImportObservationsView",
    "LifeHistoryView",
    "LinkObservationView",
    "LocationDetailView",
    "MyObservationsView",
    "ObservationDetailView",
    "ObservationEventsView",
    "SendToProjectView",
    "SubmitObservationView",
    "SubmitOriginView",
]
