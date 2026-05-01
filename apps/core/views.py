"""
Views for the core app.
"""

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view."""

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_name"] = "CRBirding"
        context["project_description"] = (
            "A website for managing observations of colour-ringed birds. "
            "Record and track individual birds identified by their unique colour ring combinations."
        )
        return context


def handler403(request: HttpRequest, exception=None) -> HttpResponse:
    """Custom 403 Forbidden handler."""
    return render(request, "403.html", status=403)


def handler404(request: HttpRequest, exception=None) -> HttpResponse:
    """Custom 404 Not Found handler."""
    return render(request, "404.html", status=404)


def handler500(request: HttpRequest) -> HttpResponse:
    """Custom 500 Internal Server Error handler."""
    return render(request, "500.html", status=500)


# Development-only views for testing error pages and Sentry
if settings.DJANGO_ENV == "development":

    def test_403(request: HttpRequest) -> HttpResponse:
        """Test view for 403 page (development only)."""
        return render(request, "403.html", status=403)

    def test_404(request: HttpRequest) -> HttpResponse:
        """Test view for 404 page (development only)."""
        return render(request, "404.html", status=404)

    def test_500(request: HttpRequest) -> HttpResponse:
        """Test view for 500 page (development only)."""
        return render(request, "500.html", status=500)

    def test_sentry(request: HttpRequest) -> HttpResponse:
        """Test view to trigger a Sentry error (development only)."""
        raise ValueError(
            "This is a test error to verify Sentry is configured correctly."
        )
