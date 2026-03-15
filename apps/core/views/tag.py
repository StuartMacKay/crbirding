from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View

from ..forms import TagForm


class AddTagRowView(LoginRequiredMixin, View):
    """HTMX endpoint backing the "Add another tag" button: renders one
    more blank TagForm at the next index and, via an out-of-band swap,
    bumps the formset's TOTAL_FORMS count to match -- so the result is
    an ordinary Django formset submission, nothing HTMX-specific to
    unpick server-side.
    """

    def get(self, request):
        index = int(request.GET.get("index", 0))
        form = TagForm(prefix=f"tags-{index}")
        row_html = render_to_string("core/_tag_form_row.html", {"form": form}, request=request)
        total_forms_input = (
            f'<input type="hidden" name="tags-TOTAL_FORMS" id="id_tags-TOTAL_FORMS" '
            f'value="{index + 1}" hx-swap-oob="true">'
        )
        return HttpResponse(row_html + total_forms_input)
