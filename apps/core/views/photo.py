from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View

from ..forms import PhotoForm


class AddPhotoRowView(LoginRequiredMixin, View):
    """HTMX endpoint backing the "Add another photo" button: render one
    more blank PhotoForm at the next index and, via an out-of-band swap,
    bump the formset's TOTAL_FORMS count to match -- so the result is an
    ordinary Django formset submission, nothing HTMX-specific to unpick
    server-side.
    """

    def get(self, request):
        index = int(request.GET.get("index", 0))
        form = PhotoForm(prefix=f"photos-{index}")
        row_html = render_to_string("core/_photo_form_row.html", {"form": form}, request=request)
        total_forms_input = (
            f'<input type="hidden" name="photos-TOTAL_FORMS" id="id_photos-TOTAL_FORMS" '
            f'value="{index + 1}" hx-swap-oob="true">'
        )
        return HttpResponse(row_html + total_forms_input)
