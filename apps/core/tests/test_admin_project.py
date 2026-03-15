import pytest
from django.test import Client
from django.urls import reverse

from core.models import Position, Rule, Species

from .factories import ProjectFactory, RuleFactory, SuperUserFactory


def _management_form(total, initial):
    return {
        "patterns-TOTAL_FORMS": str(total),
        "patterns-INITIAL_FORMS": str(initial),
        "patterns-MIN_NUM_FORMS": "0",
        "patterns-MAX_NUM_FORMS": "1000",
    }


def _project_fields(project):
    return {
        "name": project.name,
        "coordinator": project.coordinator,
        "contact": project.contact,
        "submit": project.submit,
        "site": project.site,
        "country": project.country,
        "description": project.description,
    }


@pytest.mark.django_db
class TestProjectAdminRuleInline:
    def test_change_page_lists_the_projects_rules(self, client: Client):
        project = ProjectFactory()
        RuleFactory(project=project, regex=r"^B\(A\d{3}\)$")
        RuleFactory(regex=r"^R\(X\d{3}\)$")

        client.force_login(SuperUserFactory())
        response = client.get(reverse("admin:core_project_change", args=[project.pk]))

        content = response.content.decode()
        assert response.status_code == 200
        assert r"^B\(A\d{3}\)$" in content
        assert r"^R\(X\d{3}\)$" not in content

    def test_adds_a_rule_from_the_project_page(self, client: Client):
        project = ProjectFactory()

        client.force_login(SuperUserFactory())
        response = client.post(
            reverse("admin:core_project_change", args=[project.pk]),
            {
                **_project_fields(project),
                **_management_form(total=1, initial=0),
                "patterns-0-species": Species.COMMON_OSTRICH,
                "patterns-0-position": Position.LEFT_BELOW,
                "patterns-0-regex": r"^W\(.*\)$",
            },
        )

        assert response.status_code == 302
        rule = Rule.objects.get(project=project)
        assert rule.species == Species.COMMON_OSTRICH
        assert rule.regex == r"^W\(.*\)$"

    def test_deletes_a_rule_from_the_project_page(self, client: Client):
        project = ProjectFactory()
        rule = RuleFactory(project=project)

        client.force_login(SuperUserFactory())
        response = client.post(
            reverse("admin:core_project_change", args=[project.pk]),
            {
                **_project_fields(project),
                **_management_form(total=1, initial=1),
                "patterns-0-id": rule.pk,
                "patterns-0-project": project.pk,
                "patterns-0-species": rule.species,
                "patterns-0-position": rule.position,
                "patterns-0-regex": rule.regex,
                "patterns-0-DELETE": "on",
            },
        )

        assert response.status_code == 302
        assert not Rule.objects.filter(pk=rule.pk).exists()
