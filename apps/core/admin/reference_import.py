"""A changelist-attached view for pulling individual records, or
everything, out of the reference CSVs -- see apps/core/reference_data.py.

Personal-use deployments don't want every EURING place or every IOC
species common name preloaded (it would swamp every autocomplete and
list_filter with things nobody ever ringed or resighted); this lets a
user pull in just the Country/Place/Species they actually need, searched
by name, without leaving the admin to go find and type in a code by
hand.
"""

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import path


class ReferenceImportMixin:
    """Mix into a ModelAdmin to add an "import/" view, linked from the
    changelist's object-tools. Subclasses set:

    reference_find: callable(query: str) -> list[dict]
    reference_import_one: callable(code: str) -> model instance
    reference_import_all: callable() -> reference_data.ImportResult
    reference_format_match: callable(row: dict) -> (code, label, detail)
    reference_extra_actions: [(slug, label, callable() -> ImportResult), ...]
    """

    change_list_template = "admin/core/change_list_with_import.html"

    reference_find = None
    reference_import_one = None
    reference_import_all = None
    reference_format_match = None
    reference_extra_actions = ()

    def get_urls(self):
        import_url = path(
            "import/", self.admin_site.admin_view(self.import_view), name=self._import_url_name
        )
        return [import_url, *super().get_urls()]

    @property
    def _import_url_name(self):
        opts = self.model._meta
        return f"{opts.app_label}_{opts.model_name}_import"

    def import_view(self, request):
        if request.method == "POST":
            return self._handle_post(request)

        query = request.GET.get("q", "").strip()
        raw_matches = self.reference_find(query) if query else []
        matches = [self.reference_format_match(row) for row in raw_matches]

        context = {
            **self.admin_site.each_context(request),
            "title": f"Import {self.model._meta.verbose_name_plural} from reference data",
            "opts": self.model._meta,
            "query": query,
            "matches": matches,
            "extra_actions": self.reference_extra_actions,
        }
        return render(request, "admin/core/reference_import.html", context)

    def _report_result(self, request, result):
        summary = f"{result.created} created, {result.updated} updated, {result.skipped} skipped."
        messages.success(request, summary)
        for error in result.errors[:10]:
            messages.warning(request, error)

    def _handle_post(self, request):
        action = request.POST.get("action")

        if action == "import_one":
            code = request.POST.get("code", "")
            try:
                obj = self.reference_import_one(code)
                messages.success(request, f"Imported {obj}.")
            except LookupError as exc:
                messages.error(request, str(exc))
            query = request.POST.get("query", "")
            return redirect(f"{request.path}?q={query}")

        if action == "import_all":
            self._report_result(request, self.reference_import_all())
            return redirect(request.path)

        for slug, _label, func in self.reference_extra_actions:
            if action == slug:
                self._report_result(request, func())
                return redirect(request.path)

        return redirect(request.path)
