"""
URL patterns for the core app.
"""

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("observations/mine/", views.MyObservationsView.as_view(), name="my-observations"),
    path("observations/new/", views.SubmitObservationView.as_view(), name="observation-submit"),
    path(
        "observations/import/",
        views.ImportObservationsView.as_view(),
        name="observation-import",
    ),
    path(
        "observations/<int:pk>/",
        views.ObservationDetailView.as_view(),
        name="observation-detail",
    ),
    path(
        "observations/<int:pk>/events/",
        views.ObservationEventsView.as_view(),
        name="observation-events",
    ),
    path(
        "observations/<int:pk>/link/",
        views.LinkObservationView.as_view(),
        name="observation-link",
    ),
    path(
        "observations/<int:pk>/edit/",
        views.EditObservationView.as_view(),
        name="observation-edit",
    ),
    path(
        "observations/<int:pk>/send/",
        views.SendToProjectView.as_view(),
        name="observation-send",
    ),
    path("origins/new/", views.SubmitOriginView.as_view(), name="origin-submit"),
    path(
        "origins/<int:pk>/history/",
        views.LifeHistoryView.as_view(),
        name="origin-history",
    ),
    path("tags/add-row/", views.AddTagRowView.as_view(), name="add-tag-row"),
    path("photos/add-row/", views.AddPhotoRowView.as_view(), name="add-photo-row"),
    path(
        "locations/<int:pk>/detail/",
        views.LocationDetailView.as_view(),
        name="location-detail",
    ),
]
