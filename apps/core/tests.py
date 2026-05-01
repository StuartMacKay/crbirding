"""
Tests for the core app.
"""

import pytest
from django.test import Client, override_settings
from django.urls import reverse


@pytest.mark.django_db
class TestHomeView:
    """Tests for the home page view."""

    def test_home_page_returns_200(self, client: Client):
        """Home page should return HTTP 200."""
        url = reverse("core:home")
        response = client.get(url)
        assert response.status_code == 200

    def test_home_page_uses_correct_template(self, client: Client):
        """Home page should use the correct template."""
        url = reverse("core:home")
        response = client.get(url)
        assert "core/home.html" in [t.name for t in response.templates]

    def test_home_page_contains_project_name(self, client: Client):
        """Home page should display the project name."""
        url = reverse("core:home")
        response = client.get(url)
        assert b"CRBirding" in response.content

    def test_home_page_contains_project_description(self, client: Client):
        """Home page should display the project description."""
        url = reverse("core:home")
        response = client.get(url)
        assert b"colour-ringed birds" in response.content

    def test_home_page_context_has_project_name(self, client: Client):
        """Home page context should include project_name."""
        url = reverse("core:home")
        response = client.get(url)
        assert response.context["project_name"] == "CRBirding"

    def test_home_page_context_has_project_description(self, client: Client):
        """Home page context should include project_description."""
        url = reverse("core:home")
        response = client.get(url)
        assert "project_description" in response.context
        assert len(response.context["project_description"]) > 0


@pytest.mark.django_db
@override_settings(DJANGO_ENV="development")
class TestErrorPageViews:
    """Tests for development error page views."""

    def test_403_page_returns_403(self, client: Client):
        """Test 403 page returns correct status code."""
        # The development test endpoint returns a 403 response
        response = client.get("/403/")
        assert response.status_code == 403

    def test_404_page_returns_404(self, client: Client):
        """Test 404 page returns correct status code."""
        response = client.get("/404/")
        assert response.status_code == 404

    def test_500_page_returns_500(self, client: Client):
        """Test 500 page returns correct status code."""
        response = client.get("/500/")
        assert response.status_code == 500

    def test_404_on_missing_page(self, client: Client):
        """Requesting a non-existent URL should return 404."""
        response = client.get("/this-page-does-not-exist-at-all/")
        assert response.status_code == 404


@pytest.mark.django_db
class TestErrorHandlers:
    """Tests for custom error handler functions."""

    def test_handler_404_uses_correct_template(self, client: Client):
        """404 handler should use the 404 template."""
        response = client.get("/nonexistent-url-that-does-not-exist/")
        assert response.status_code == 404
        assert "404.html" in [t.name for t in response.templates]

    def test_handler_403_uses_correct_template(self, client: Client):
        """403 handler should use the 403 template."""
        response = client.get("/403/")
        assert response.status_code == 403
        assert "403.html" in [t.name for t in response.templates]

    def test_handler_500_uses_correct_template(self, client: Client):
        """500 handler should use the 500 template."""
        response = client.get("/500/")
        assert response.status_code == 500
        assert "500.html" in [t.name for t in response.templates]
