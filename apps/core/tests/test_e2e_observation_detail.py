"""Browser-driven test for the "Copy" link on ObservationDetailView's
report panel -- Alpine.js copying the report text to the clipboard,
which the Django test client can't run. Copied as HTML and plain text. See test_e2e_location_form.py
for how the `e2e` marker is run.
"""

from urllib.parse import parse_qs, urlsplit

import pytest

from .factories import ObservationFactory, OriginFactory, ProjectFactory, UserFactory

pytestmark = [pytest.mark.e2e, pytest.mark.django_db]


def _login(page, live_server, user):
    page.goto(f"{live_server.url}/accounts/login/")
    page.fill("#id_username", user.email)
    page.fill("#id_password", "password")
    page.click("button[type=submit]")
    page.wait_for_url("**/accounts/settings/")


class TestObservationDetailJS:
    def test_copy_puts_the_report_on_the_clipboard(self, page, live_server):
        page.context.grant_permissions(["clipboard-read", "clipboard-write"])
        user = UserFactory()
        observation = ObservationFactory(owner=user)
        _login(page, live_server, user)

        page.goto(f"{live_server.url}/observations/{observation.pk}/")
        page.click("#copy-report")

        page.wait_for_selector("#copy-report:text('Copied')")
        copied = page.evaluate("navigator.clipboard.readText()")
        assert "Colour marks: " in copied
        assert copied == page.evaluate("elementText(document.querySelector('#report'))")

    def test_email_link_body_is_the_report_panel_text(self, page, live_server):
        user = UserFactory()
        origin = OriginFactory(project=ProjectFactory(contact="ringer@example.org"))
        observation = ObservationFactory(owner=user, origin=origin)
        _login(page, live_server, user)
        page.goto(f"{live_server.url}/observations/{observation.pk}/")

        # Run the link's click handler without following the mailto: link.
        href = page.eval_on_selector(
            "a[href^='mailto:ringer@example.org']", "el => { el.onclick(); return el.href; }"
        )

        query = parse_qs(urlsplit(href).query)
        report = page.evaluate("elementText(document.querySelector('#report'))")
        assert query["body"] == [report]
        location = observation.location
        assert query["subject"] == [
            f"{observation.get_species_display()}, {location.get_region_display()}, "
            f"{location.get_country_display()}"
        ]
        assert "Species: " in report
        assert "+" not in href
