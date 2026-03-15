import pytest

from core.utils.codes import Mark, match_code, normalise_code, parse_code, parse_mark


class TestParseMark:
    def test_plain_colour(self):
        assert parse_mark("Y") == Mark(colour="Y")

    def test_striped_ring(self):
        assert parse_mark("OY") == Mark(colour="O", second_colour="Y")

    def test_flag(self):
        assert parse_mark("RF") == Mark(colour="R", flag=True)

    def test_inscription_colour_is_the_last_letter(self):
        """ "BW(A123)" is a blue ring with *white* letters, not a
        blue-and-white striped ring."""
        mark = parse_mark("BW(A123)")
        assert (mark.colour, mark.second_colour, mark.inscription_colour) == ("B", "", "W")
        assert mark.inscription == "A123"

    def test_striped_ring_with_inscription(self):
        mark = parse_mark("OYW(A123)")
        assert (mark.colour, mark.second_colour, mark.inscription_colour) == ("O", "Y", "W")

    def test_uncertain(self):
        assert parse_mark("BW(A123)?").uncertain is True

    @pytest.mark.parametrize("code", ["BW(A123)d", "BW(A123)u", "BW(A123)h?", "BW(A123)x"])
    def test_nothing_may_follow_the_inscription(self, code):
        """Which way the letters read isn't part of the code -- they're
        always written top to bottom, anything more goes in the notes."""
        with pytest.raises(ValueError, match="after the inscription"):
            parse_mark(code)

    def test_inscription_may_contain_punctuation(self):
        assert parse_mark("BW(M:556)").inscription == "M:556"
        assert parse_mark("RW(8.H)").inscription == "8.H"

    def test_metal(self):
        assert parse_mark("M").is_metal
        assert parse_mark("A").is_metal
        assert not parse_mark("MY").is_metal  # a striped ring, not a metal one

    @pytest.mark.parametrize(
        "code, message",
        [
            ("", "empty mark"),
            ("?", "empty mark"),
            ("Z", "'Z' is not a known colour code"),
            ("BW(A123", "missing closing bracket"),
            ("BW A123)", "missing opening bracket"),
            ("BW()", "empty inscription"),
            ("(A123)", "missing colour"),
            ("F", "missing colour"),
            ("RWY", "too many colour letters"),
            ("RWYB(A1)", "too many colour letters"),
        ],
    )
    def test_rejects(self, code, message):
        with pytest.raises(ValueError, match=message.replace("(", r"\(").replace(")", r"\)")):
            parse_mark(code)


class TestParseCode:
    def test_splits_the_stack_top_to_bottom(self):
        assert [mark.colour for mark in parse_code("R,WN(KY)")] == ["R", "W"]

    @pytest.mark.parametrize("code", ["", "  ", "R,", ",R", "R,,W"])
    def test_rejects_empty_codes_and_marks(self, code):
        with pytest.raises(ValueError):
            parse_code(code)


class TestNormaliseCode:
    @pytest.mark.parametrize(
        "code, normalised",
        [
            ("r,wn(ky)", "R,WN(KY)"),
            (" R , WN(KY) ", "R,WN(KY)"),
            ("fr", "RF"),
            ("OYW(a123)?", "OYW(A123)?"),
            ("M", "M"),
        ],
    )
    def test_writes_codes_one_standard_way(self, code, normalised):
        assert normalise_code(code) == normalised

    def test_is_stable(self):
        assert normalise_code(normalise_code("r,wn(ky)?")) == "R,WN(KY)?"


class TestMatchCode:
    def test_leaves_out_uncertainty(self):
        assert match_code("R?,WN(KY)?") == "R,WN(KY)"

    def test_otherwise_the_same_as_normalised(self):
        assert match_code("r,bw(a1)") == normalise_code("r,bw(a1)")
