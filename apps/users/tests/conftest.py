import pytest
from django.core.cache import cache


@pytest.fixture(autouse=True)
def locmem_email_backend(settings):
    """The project's real EMAIL_BACKEND is console/SMTP, never locmem, so
    nothing normally populates django.core.mail.outbox -- override it just
    for this package's tests, which need to inspect what was sent.
    """
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


@pytest.fixture(autouse=True)
def clear_ratelimit_cache():
    """users.ratelimit.is_rate_limited's counters live in the cache, which
    -- unlike the database -- pytest-django doesn't reset between tests.
    Every test in this package hits the same default REMOTE_ADDR
    (Django's test Client always uses 127.0.0.1 unless told otherwise),
    so without this, an earlier test's signup/login/etc. attempts would
    count toward a later, unrelated test's rate limit.
    """
    cache.clear()
