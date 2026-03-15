from django.test import RequestFactory

from core.utils.htmx import htmx_redirect, is_htmx


class TestIsHtmx:
    def test_true_with_header(self):
        request = RequestFactory().get("/", HTTP_HX_REQUEST="true")
        assert is_htmx(request) is True

    def test_false_without_header(self):
        request = RequestFactory().get("/")
        assert is_htmx(request) is False

    def test_false_with_other_header_value(self):
        request = RequestFactory().get("/", HTTP_HX_REQUEST="false")
        assert is_htmx(request) is False


class TestHtmxRedirect:
    def test_sets_hx_redirect_header(self):
        response = htmx_redirect("/somewhere/")
        assert response["HX-Redirect"] == "/somewhere/"

    def test_status_is_200_not_a_normal_redirect(self):
        response = htmx_redirect("/somewhere/")
        assert response.status_code == 200

    def test_no_location_header(self):
        response = htmx_redirect("/somewhere/")
        assert "Location" not in response
