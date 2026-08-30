from django.utils import translation

from . import scripts


class ScriptMiddleware:
    """Activate the script (writing system) for the duration of the request.

    Must run after LocaleMiddleware (needs the active language) and
    after AuthenticationMiddleware (needs request.user for an explicit
    preference).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        script = scripts.default_script_for_language(translation.get_language())

        user = getattr(request, "user", None)
        if user is not None and getattr(user, "is_authenticated", False) and user.script:
            script = user.script

        scripts.activate(script)
        try:
            response = self.get_response(request)
        finally:
            scripts.deactivate()
        return response
