from django.utils import translation

from .utils import alphabets


class AlphabetMiddleware:
    """Activate the alphabet (writing system) for the duration of the request.

    Must run after LocaleMiddleware (needs the active language) and
    after AuthenticationMiddleware (needs request.user for an explicit
    preference).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        alphabet = alphabets.default_alphabet_for_language(translation.get_language())

        user = getattr(request, "user", None)
        if user is not None and getattr(user, "is_authenticated", False) and user.alphabet:
            alphabet = user.alphabet

        alphabets.activate(alphabet)
        try:
            response = self.get_response(request)
        finally:
            alphabets.deactivate()
        return response
