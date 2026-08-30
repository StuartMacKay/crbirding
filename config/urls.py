"""
URL configuration for crbirding project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.core.views import handler403, handler404, handler500  # noqa: F401
from apps.users.urls import auth_urlpatterns

handler403 = "apps.core.views.handler403"
handler404 = "apps.core.views.handler404"
handler500 = "apps.core.views.handler500"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include(auth_urlpatterns)),
    path("accounts/", include("apps.users.urls")),
    path("", include("apps.core.urls")),
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
