"""
URL configuration for crbirding project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from users.urls import auth_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include(auth_urlpatterns)),
    path("accounts/", include("users.urls")),
    path("autocomplete/", include("autocomplete.urls")),
    path("", include("core.urls")),
]

if "django_browser_reload" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
