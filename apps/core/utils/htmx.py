"""Minimal htmx helpers.

htmx only ever needs plain HTTP headers -- nothing here depends on the
django-htmx package (removed; it was only ever a thin wrapper around
these same headers). Add more here only once a feature actually needs
it (e.g. HX-Trigger, for firing a client-side event after a response),
rather than ahead of time.
"""

from django.http import HttpRequest, HttpResponse


def is_htmx(request: HttpRequest) -> bool:
    """Was this request made by htmx (an hx-get/hx-post/etc. swap),
    rather than an ordinary browser navigation?
    """
    return request.headers.get("HX-Request") == "true"


def htmx_redirect(url: str) -> HttpResponse:
    """Redirect after an htmx-driven request.

    htmx swaps response content into the page rather than navigating,
    so a plain redirect's Location header is followed by htmx's own
    fetch() call, not the browser -- the user never actually moves.
    HX-Redirect tells htmx to do a full client-side navigation instead.
    """
    response = HttpResponse(status=200)
    response["HX-Redirect"] = url
    return response
