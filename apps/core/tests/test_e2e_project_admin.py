"""Browser-driven tests for the Rule inline on ProjectAdmin -- in
particular that the species AutocompleteSelect (autocomplete.js) is
enhanced in rows added with "Add another Rule", which only exist once
Django admin's inlines.js has cloned the hidden template row. See
test_e2e_location_form.py for how the `e2e` marker is run.
"""

import pytest

from core.models import Rule, Species

from .factories import ProjectFactory, SuperUserFactory

pytestmark = [pytest.mark.e2e, pytest.mark.django_db]


def _login(page, live_server, user):
    page.goto(f"{live_server.url}/admin/login/")
    page.fill("#id_username", user.email)
    page.fill("#id_password", "password")
    page.click("input[type=submit]")
    page.wait_for_url(f"{live_server.url}/admin/")


class TestProjectAdminRuleInlineJS:
    def test_template_row_is_not_enhanced(self, page, live_server):
        project = ProjectFactory()
        _login(page, live_server, SuperUserFactory())

        page.goto(f"{live_server.url}/admin/core/project/{project.pk}/change/")

        assert page.query_selector("#id_patterns-0-species-ts-control")
        assert not page.query_selector("#id_patterns-__prefix__-species-ts-control")

    def test_added_row_gets_a_working_species_autocomplete(self, page, live_server):
        project = ProjectFactory()
        _login(page, live_server, SuperUserFactory())
        page.goto(f"{live_server.url}/admin/core/project/{project.pk}/change/")

        page.click("#patterns-group .add-row a")
        page.click("#id_patterns-1-species-ts-control")
        page.fill("#id_patterns-1-species-ts-control", "Common Ostrich")
        page.wait_for_selector("#id_patterns-1-species-ts-dropdown .option")
        page.click("#id_patterns-1-species-ts-dropdown .option")
        page.select_option("#id_patterns-1-position", index=1)
        page.fill("#id_patterns-1-regex", r"^W\(.*\)$")
        page.click("input[name=_save]")
        page.wait_for_url(f"{live_server.url}/admin/core/project/")

        rule = Rule.objects.get(project=project)
        assert rule.species == Species.COMMON_OSTRICH
        assert rule.regex == r"^W\(.*\)$"
