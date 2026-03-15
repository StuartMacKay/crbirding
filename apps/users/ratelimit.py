"""A minimal fixed-window rate limiter for the handful of anonymous
account endpoints a bot or attacker might hammer: signup, resending a
verification email, login, and requesting a password reset.

Built on Django's own cache framework (an atomic incr() with expiry is
exactly what a rate limiter needs) rather than a third-party package --
this project doesn't otherwise use one for anything account-related (see
apps.users.tokens, apps.users.emails), and the cache framework already
does the job. Per-process (Django's default LocMemCache, unless the
deployment configures something shared) -- good enough to deter casual
abuse for a small trusted-community app; not a defence against a
determined, distributed attacker, which isn't this app's threat model
(see the account-features plan this followed).

Keyed by IP address alone, not IP+username/email -- simpler, and avoids
the rate limit itself leaking whether a given email/username exists by
behaving differently for known vs. unknown accounts.
"""

from django.core.cache import cache


def is_rate_limited(*, action: str, request, limit: int, window_seconds: int) -> bool:
    """True if this IP has already used `action` `limit` or more times
    within the last `window_seconds` -- callers should reject the
    request without doing anything else. Counts toward the limit
    otherwise, so checking is itself the increment; call it once per
    attempt, not speculatively.
    """
    ip = request.META.get("REMOTE_ADDR", "unknown")
    cache_key = f"ratelimit:{action}:{ip}"

    count = cache.get(cache_key)
    if count is None:
        cache.set(cache_key, 1, timeout=window_seconds)
        return False
    if count >= limit:
        return True
    try:
        cache.incr(cache_key)
    except ValueError:
        # Expired between get() and incr() -- treat as a fresh window.
        cache.set(cache_key, 1, timeout=window_seconds)
    return False
