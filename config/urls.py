"""
URL configuration for crbirding project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from health_check.views import HealthCheckView

from apps.core.views import handler403, handler404, handler500  # noqa: F401


class CRBirdingHealthCheckView(HealthCheckView):
    """Health check endpoint — checks DB, cache (Redis), and storage."""

    checks = [
        "health_check.checks.Database",
        "health_check.checks.Cache",
        "health_check.checks.Storage",
    ]


health_check_view = CRBirdingHealthCheckView.as_view()

# Custom error handlers
handler403 = "apps.core.views.handler403"
handler404 = "apps.core.views.handler404"
handler500 = "apps.core.views.handler500"

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Health checks (django-health-check v4.x class-based view)
    path("health/", health_check_view, name="health-check"),
]

# Development-only URLs
if settings.DJANGO_ENV == "development":
    urlpatterns += [
        # Browser auto-reload
        path("__reload__/", include("django_browser_reload.urls")),
    ]

    # Debug toolbar
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
