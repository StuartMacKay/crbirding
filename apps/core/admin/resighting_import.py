"""A changelist-attached view for bulk-importing a user's own historical
Resighting records from a CSV file -- see apps.core.bulk_import.
"""

from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import path

from apps.core.bulk_import import import_resightings_csv
from apps.core.models import Observer


class ResightingImportForm(forms.Form):
    csv_file = forms.FileField(label="CSV file")
    observer = forms.ModelChoiceField(
        queryset=Observer.objects.all(),
        help_text="Every imported resighting is attributed to this observer.",
    )


class ResightingImportMixin:
    change_list_template = "admin/core/change_list_with_csv_import.html"

    def get_urls(self):
        import_url = path(
            "import-csv/",
            self.admin_site.admin_view(self.import_csv_view),
            name="core_resighting_import_csv",
        )
        return [import_url, *super().get_urls()]

    def import_csv_view(self, request):
        if request.method == "POST":
            form = ResightingImportForm(request.POST, request.FILES)
            if form.is_valid():
                report = import_resightings_csv(
                    form.cleaned_data["csv_file"], form.cleaned_data["observer"]
                )
                if report.created:
                    messages.success(request, f"Imported {report.created} resighting(s).")
                if report.skipped:
                    messages.warning(request, f"Skipped {report.skipped} row(s); see below.")
                for error in report.errors[:50]:
                    messages.error(request, error)
                if not report.errors:
                    return redirect("admin:core_resighting_changelist")
        else:
            form = ResightingImportForm()

        context = {
            **self.admin_site.each_context(request),
            "title": "Import resightings from CSV",
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "admin/core/resighting_import.html", context)
