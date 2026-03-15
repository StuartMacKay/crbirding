from core.models import Alphabet
from core.utils import alphabets


class TestDefaultAlphabetForLanguage:
    def test_defaults_to_latin(self):
        assert alphabets.default_alphabet_for_language("en") == Alphabet.LATIN
        assert alphabets.default_alphabet_for_language("fr") == Alphabet.LATIN

    def test_known_languages_map_to_cyrillic(self):
        assert alphabets.default_alphabet_for_language("ru") == Alphabet.CYRILLIC
        assert alphabets.default_alphabet_for_language("bg") == Alphabet.CYRILLIC

    def test_greek(self):
        assert alphabets.default_alphabet_for_language("el") == Alphabet.GREEK

    def test_strips_region_subtag(self):
        assert alphabets.default_alphabet_for_language("sr-latn") == Alphabet.CYRILLIC

    def test_case_insensitive(self):
        assert alphabets.default_alphabet_for_language("RU") == Alphabet.CYRILLIC

    def test_empty_or_none_defaults_to_latin(self):
        assert alphabets.default_alphabet_for_language("") == Alphabet.LATIN
        assert alphabets.default_alphabet_for_language(None) == Alphabet.LATIN


class TestActiveAlphabet:
    def teardown_method(self):
        alphabets.deactivate()

    def test_get_alphabet_defaults_to_latin_when_none_active(self):
        assert alphabets.get_alphabet() == Alphabet.LATIN

    def test_activate_sets_the_active_alphabet(self):
        alphabets.activate(Alphabet.CYRILLIC)
        assert alphabets.get_alphabet() == Alphabet.CYRILLIC

    def test_deactivate_clears_it(self):
        alphabets.activate(Alphabet.GREEK)
        alphabets.deactivate()
        assert alphabets.get_alphabet() == Alphabet.LATIN

    def test_deactivate_is_safe_when_nothing_active(self):
        alphabets.deactivate()
        alphabets.deactivate()
