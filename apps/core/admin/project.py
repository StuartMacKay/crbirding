from autocomplete.widgets import AutocompleteSelect
from django import forms
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from core.forms import ProjectImportForm
from core.models import Country, Project, Rule
from core.utils.csv_export import csv_download_response
from core.utils.project_export import export_projects_csv
from core.utils.project_import import import_projects_csv

from .filters import choice_list_filter
from .rule import RuleAdminForm


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "vTextField"}),
            "coordinator": forms.TextInput(attrs={"class": "vTextField"}),
            "country": AutocompleteSelect(
                "country", get_label=lambda code: Country(code).label if code else ""
            ),
        }


class RuleInline(admin.TabularInline):
    model = Rule
    form = RuleAdminForm
    extra = 1
    fields = ("species", "position", "regex")
    ordering = ("species", "position")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "coordinator", "country")
    list_filter = (
        choice_list_filter("country", Country, title="country", parameter_name="country"),
    )
    search_fields = ("coordinator", "description")
    change_list_template = "admin/core/change_list_with_csv_import.html"
    fields = (
        "name",
        "coordinator",
        "contact",
        "submit",
        "site",
        "country",
        "description",
        "created",
        "modified",
    )
    form = ProjectAdminForm
    readonly_fields = ("created", "modified")
    inlines = [RuleInline]
    actions = ["export_csv"]

    @admin.action(description="Export selected to CSV")
    def export_csv(self, request, queryset):
        return csv_download_response(export_projects_csv(queryset), "projects.csv")

    def get_urls(self):
        import_url = path(
            "import-csv/",
            self.admin_site.admin_view(self.import_csv_view),
            name="core_project_import_csv",
        )
        return [import_url, *super().get_urls()]

    def import_csv_view(self, request):
        if request.method == "POST":
            form = ProjectImportForm(request.POST, request.FILES)
            if form.is_valid():
                report = import_projects_csv(form.cleaned_data["csv_file"])
                if report.created:
                    messages.success(request, f"Imported {report.created} project(s).")
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
                    return redirect("admin:core_project_changelist")
        else:
            form = ProjectImportForm()

        context = {
            **self.admin_site.each_context(request),
            "title": "Import projects from CSV",
            "opts": self.model._meta,
            "form": form,
        }
        return render(request, "admin/core/project_import.html", context)
