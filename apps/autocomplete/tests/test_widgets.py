from autocomplete.widgets import AutocompleteSelect


class TestAutocompleteSelect:
    def test_renders_data_attributes(self):
        widget = AutocompleteSelect("species")
        html = widget.render("species", None)
        assert 'data-autocomplete-field="species"' in html

    def test_renders_depends_on_attribute(self):
        widget = AutocompleteSelect("region", depends_on="id_country")
        html = widget.render("region", None)
        assert 'data-autocomplete-depends-on="id_country"' in html

    def test_no_value_renders_no_options(self):
        widget = AutocompleteSelect("species")
        html = widget.render("species", None)
        assert "<option" not in html

    def test_current_value_renders_as_the_only_option_using_get_label(self):
        widget = AutocompleteSelect("species", get_label=lambda code: f"Species {code}")
        html = widget.render("species", "00020")
        assert html.count("<option") == 1
        assert "Species 00020" in html
        assert 'value="00020"' in html
        assert "selected" in html

    def test_get_label_defaults_to_identity(self):
        widget = AutocompleteSelect("species")
        html = widget.render("species", "00020")
        assert ">00020<" in html
