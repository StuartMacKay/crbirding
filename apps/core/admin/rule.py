from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from core.forms import RuleImportForm
from core.models import Rule, Species
from core.utils.csv_export import csv_download_response
from core.utils.rule_export import export_rules_csv
from core.utils.rule_import import import_rules_csv

from .filters import choice_list_filter


class RuleAdminForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = "__all__"
        widgets = {
            "regex": forms.TextInput(attrs={"class": "vTextField"}),
            "species": AutocompleteSelect(
                "species", get_label=lambda code: Species(code).label if code else ""
            ),
        }


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("species", "position", "regex", "project")
    list_filter = (
        choice_list_filter("species", Species, title="species", parameter_name="species"),
        "position",
        "project",
    )
    search_fields = ("regex", "project__coordinator")
    autocomplete_fields = ("project",)
    ordering = ("species", "position")
    change_list_template = "admin/core/change_list_with_csv_import.html"
    fields = (
        "species",
        "position",
        "regex",
        "description",
        "project",
        "created",
        "modified",
    )
    readonly_fields = ("created", "modified")
    form = RuleAdminForm
    actions = ["export_csv"]

    @admin.action(description="Export selected to CSV")
    def export_csv(self, request, queryset):
        return csv_download_response(export_rules_csv(queryset), "rules.csv")

    def get_urls(self):
        import_url = path(
            "import-csv/",
            self.admin_site.admin_view(self.import_csv_view),
            name="core_rule_import_csv",
        )
        return [import_url, *super().get_urls()]

    def import_csv_view(self, request):
        if request.method == "POST":
            form = RuleImportForm(request.POST, request.FILES)
            if form.is_valid():
                report = import_rules_csv(form.cleaned_data["csv_file"])
                if report.created:
                    messages.success(request, f"Imported {report.created} rule(s).")
                if report.duplicates:
                    messages.info(
                        request,
                        f"Skipped {report.duplicates} row(s) already on file.",
                    )
                if report.skipped:
                    messages.warning(request, f"Skipped {report.skipped} row(s); see below.")
                for error in report.errors[:50]:
                    messages.error(request, error)
                if not report.errors:
                    return redirect("admin:core_rule_changelist")
        else:
            form = RuleImportForm()

        context = {
            **self.admin_site.each_context(request),
            "title": "Import rules from CSV",
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "admin/core/rule_import.html", context)
