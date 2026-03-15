"""Browser-driven tests for core/static/core/location_form.js -- the
behaviour a Django test client can't exercise at all, since it never
runs JavaScript. Slow relative to the rest of the suite (a real,
if headless, browser per test) -- see the `e2e` marker, excluded from
the default `pytest` run (see pyproject.toml); run explicitly with
`pytest -m e2e`.

These found a real bug on first use: the "Use default coordinates"
button lived inside a collapsed <details>, so unhiding it left it
still invisible -- exactly the class of thing this file exists to
catch, since apps/core/tests/test_views_resighting.py et al. only ever
see the pre-JS HTML.
"""

import pytest

from .factories import LocationFactory, UserFactory

pytestmark = [pytest.mark.e2e, pytest.mark.django_db]


def _login(page, live_server, user):
    page.goto(f"{live_server.url}/accounts/login/")
    page.fill("#id_username", user.email)
    page.fill("#id_password", "password")
    page.click("button[type=submit]")
    page.wait_for_url("**/accounts/settings/")


def _search_and_pick(page, live_server, query):
    page.goto(f"{live_server.url}/observations/new/")
    page.click("#id_location-search-ts-control")
    page.fill("#id_location-search-ts-control", query)
    page.wait_for_selector("#id_location-search-ts-dropdown .option")
    page.click("#id_location-search-ts-dropdown .option")


class TestLocationFormJS:
    def test_selecting_a_match_fills_and_locks_region_and_country(self, page, live_server):
        LocationFactory(name={"Latn": "Riverside Meadow"}, region="FR--")
        _login(page, live_server, UserFactory())

        _search_and_pick(page, live_server, "Riverside Meadow")

        page.wait_for_function("document.querySelector('#id_location-region').value === 'FR--'")
        assert page.eval_on_selector("#id_location-region", "el => el.disabled") is True
        assert page.eval_on_selector("#id_location-country", "el => el.disabled") is True
        assert page.eval_on_selector("#id_location-country", "el => el.value") == "FR--"
        assert page.is_visible("#location-matched-hint")

    def test_selecting_a_match_shows_its_notes_read_only_and_hides_the_textarea(
        self, page, live_server
    ):
        """LocationForm never saves typed notes against an existing
        Location (see LocationForm.resolve()) -- editing them would be
        misleading busywork, so a match's own notes are shown as
        read-only text instead of a now-pointless editable textarea.
        """
        LocationFactory(
            name={"Latn": "Quarry Pool"},
            region="GB--",
            notes="Access via the north gate only.",
        )
        _login(page, live_server, UserFactory())

        _search_and_pick(page, live_server, "Quarry Pool")

        page.wait_for_selector("#location-notes-readonly:not([hidden])")
        assert (
            page.text_content("#location-notes-readonly").strip()
            == "Access via the north gate only."
        )
        assert page.is_hidden("#id_location-notes")

    def test_use_default_coordinates_fills_the_coordinate_fields(self, page, live_server):
        LocationFactory(
            name={"Latn": "Harbour View"},
            region="GB--",
            latitude="51.5074",
            longitude="-0.1278",
            accuracy=50,
        )
        _login(page, live_server, UserFactory())

        _search_and_pick(page, live_server, "Harbour View")
        page.click("#use-default-coordinates")

        page.wait_for_function("document.querySelector('#id_location-latitude').value !== ''")
        assert page.eval_on_selector("#id_location-latitude", "el => el.value") == "51.5074"
        assert page.eval_on_selector("#id_location-longitude", "el => el.value") == "-0.1278"
        assert page.eval_on_selector("#id_location-accuracy", "el => el.value") == "50"

    def test_coordinate_fields_are_not_prefilled_before_use_default_is_clicked(
        self, page, live_server
    ):
        """These are an optional override, not a copy of the location's
        own coordinates -- they must stay blank until the user asks
        for the default, or types their own.
        """
        LocationFactory(name={"Latn": "Quiet Cove"}, region="GB--", latitude="50.0")
        _login(page, live_server, UserFactory())

        _search_and_pick(page, live_server, "Quiet Cove")
        page.wait_for_selector("#location-matched-hint:not([hidden])")

        assert page.eval_on_selector("#id_location-latitude", "el => el.value") == ""

    def test_clearing_the_selection_unlocks_region_and_country(self, page, live_server):
        LocationFactory(name={"Latn": "Windy Point"}, region="GB--")
        _login(page, live_server, UserFactory())

        _search_and_pick(page, live_server, "Windy Point")
        page.wait_for_function("document.querySelector('#id_location-region').disabled === true")

        # No visible "clear" control on a single-select TomSelect
        # (the clear_button plugin isn't enabled) -- this is what a
        # user re-opening and deleting their search does under the
        # hood.
        page.evaluate(
            "document.querySelector('#id_location-search').tomselect.clear(true);"
            "document.querySelector('#id_location-search')"
            ".dispatchEvent(new Event('change'));"
        )

        page.wait_for_function("document.querySelector('#id_location-region').disabled === false")
        assert page.is_hidden("#use-default-coordinates")

    def test_typing_an_unmatched_name_offers_to_add_it(self, page, live_server):
        """The merged search/create field's whole point: no separate
        "add a new location" section to find -- typing a name with no
        match offers "Add ..." right there in the same dropdown.
        """
        _login(page, live_server, UserFactory())
        page.goto(f"{live_server.url}/observations/new/")

        page.click("#id_location-search-ts-control")
        page.fill("#id_location-search-ts-control", "Somewhere New")
        page.wait_for_selector("#id_location-search-ts-dropdown .create")
        page.click("#id_location-search-ts-dropdown .create")

        page.wait_for_selector("#location-new-hint:not([hidden])")
        assert page.text_content("#location-new-hint-name").strip() == "Somewhere New"
        assert page.eval_on_selector("#id_location-region", "el => el.disabled") is False
        assert page.eval_on_selector("#id_location-country", "el => el.disabled") is False
        assert page.is_visible("#id_location-notes")
        assert page.is_hidden("#location-notes-readonly")
        assert page.is_hidden("#location-matched-hint")
