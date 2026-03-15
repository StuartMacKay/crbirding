"""A single generic JSON search endpoint shared by every autocomplete
field -- see autocomplete.registry.

Deliberately returns nothing but `{"results": [{"value", "label"}]}` --
no Django-specific response shaping -- so the same contract could be
served by a non-Django backend later without the frontend widget
changing at all.
"""

from django.http import HttpRequest, JsonResponse
from django.views import View

from .registry import get_search_function

_RESULT_LIMIT = 50


class AutocompleteView(View):
    def get(self, request: HttpRequest, field: str) -> JsonResponse:
        search = get_search_function(field)
        if search is None:
            return JsonResponse({"results": []}, status=404)

        query = request.GET.get("q", "")
        parents = {key: value for key, value in request.GET.items() if key != "q"}

        results = [
            {"value": value, "label": label}
            for value, label in search(query, **parents)
        ]
        return JsonResponse({"results": results[:_RESULT_LIMIT]})
