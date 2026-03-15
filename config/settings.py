"""
Django settings for crbirding project.

"""

import os
import sys
from pathlib import Path

from django.conf import global_settings
from django.utils.translation import gettext_lazy as _

# ---------------------------------------------------------------------------
# Base paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR / "apps"))

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
# Plain os.environ reads -- direnv (see .envrc) loads .env into the shell
# environment before Python even starts.


def _env_list(name: str) -> list[str]:
    value = os.environ.get(name, "")
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_bool(name: str) -> bool:
    value = os.environ.get(name, "")
    return value.strip().lower() in {"true", "1", "yes", "on"}


def _env_int(name: str) -> int:
    return int(os.environ.get(name, ""))


DEBUG = _env_bool("DEBUG")

# ---------------------------------------------------------------------------
# Installed Apps
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "core",
    "autocomplete",
]

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.AlphabetMiddleware",
]

# ---------------------------------------------------------------------------
# URLs & WSGI
# ---------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "assets" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "assets" / "static",
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# ---------------------------------------------------------------------------
# Media files
# ---------------------------------------------------------------------------
STORAGES["default"] = {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
}
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "crbirding.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "accounts:settings"
LOGOUT_REDIRECT_URL = "core:home"

# ---------------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------------

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = _env_list("ALLOWED_HOSTS")

SESSION_COOKIE_SECURE = _env_bool("SESSION_COOKIE_SECURE")

CSRF_COOKIE_SECURE = _env_bool("CSRF_COOKIE_SECURE")
CSRF_TRUSTED_ORIGINS = _env_list("CSRF_TRUSTED_ORIGINS")

SECURE_SSL_REDIRECT = _env_bool("SECURE_SSL_REDIRECT")
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = _env_int("SECURE_HSTS_SECONDS")

# ---------------------------------------------------------------------------
# Email
# ---------------------------------------------------------------------------

if _env_bool("EMAIL_ENABLED"):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = _env_int("EMAIL_PORT")
    EMAIL_USE_TLS = _env_bool("EMAIL_USE_TLS")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    DEFAULT_FROM_EMAIL = os.environ.get("FROM_EMAIL")
    SERVER_EMAIL = os.environ.get("SERVER_EMAIL")
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ---------------------------------------------------------------------------
# Internationalisation
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Build the list of language names using all the languages supported by Django.
# The the LANGUAGES setting can be set at runtim using a comma-separated list
# of language code in an environment variable.

_all_language_names = dict(global_settings.LANGUAGES)

LANGUAGES = [(code, _all_language_names.get(code, code)) for code in _env_list("LANGUAGES")]

# The list of writing systems (scripts) that can be used for Location and Region names.
# Similarly to the LANGUAGES setting the list of alphabets supported in the application
# can be set from a comma-separated list of ISO 15924 codes, e.g. "Arab,Cyrl,Latn".
_all_alphabet_names = {
    "Arab": _("Arabic"),
    "Armn": _("Armenian"),
    "Cyrl": _("Cyrillic"),
    "Geor": _("Georgian"),
    "Grek": _("Greek"),
    "Hebr": _("Hebrew"),
    "Latn": _("Latin"),
}
ALPHABETS = [(code, _all_alphabet_names.get(code, code)) for code in _env_list("ALPHABETS")]

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": os.environ.get("LOGGING_FORMATTER"),
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "apps": {
            "handlers": ["console"],
            "level": os.environ.get("LOGGING_LEVEL"),
            "propagate": False,
        },
    },
}

# ---------------------------------------------------------------------------
# Sentry
# ---------------------------------------------------------------------------

if _env_bool("SENTRY_ENABLED"):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        environment=os.environ.get("SENTRY_ENVIRONMENT"),
        send_default_pii=False,
    )

# ---------------------------------------------------------------------------
# Django Debug Toolbar
# ---------------------------------------------------------------------------

if _env_bool("DEBUG_TOOLBAR_ENABLED"):
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INSTALLED_APPS.append("debug_toolbar")
    INTERNAL_IPS = ["127.0.0.1", "localhost"]

# ---------------------------------------------------------------------------
# Django Browser Reload
# ---------------------------------------------------------------------------

if _env_bool("BROWSER_RELOAD_ENABLED"):
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
    INSTALLED_APPS.append("django_browser_reload")
