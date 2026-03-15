"""Registry mapping a field name to the search function that powers its
autocomplete widget -- see autocomplete.widgets.AutocompleteSelect
and autocomplete.views.AutocompleteView.

A search function takes the current query text plus any parent field
values (as keyword arguments, keyed by the parent's own field name --
see AutocompleteSelect's `depends_on`) and returns an iterable of
(value, label) pairs, already limited to a sensible number of results:
the registry itself doesn't cap or paginate.

Kept as a plain dict rather than a class-based registry since there's
nothing to configure per entry beyond "how do I search this" -- the
whole point is that each entry is a few lines of filtering over an
in-memory list or a queryset, not a new abstraction to learn.
"""

from collections.abc import Callable, Iterable

SearchFunction = Callable[..., Iterable[tuple[str, str]]]

_registry: dict[str, SearchFunction] = {}


def register(field: str, search: SearchFunction) -> None:
    _registry[field] = search


def get_search_function(field: str) -> SearchFunction | None:
    return _registry.get(field)
