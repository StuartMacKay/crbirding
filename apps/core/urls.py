"""
URL patterns for the core app.
"""

from django.conf import settings
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]

# Development-only URL patterns for testing error pages and Sentry
if settings.DJANGO_ENV == "development":
    urlpatterns += [
        path("403/", views.test_403, name="test-403"),
        path("404/", views.test_404, name="test-404"),
        path("500/", views.test_500, name="test-500"),
        path("sentry-test/", views.test_sentry, name="sentry-test"),
    ]
