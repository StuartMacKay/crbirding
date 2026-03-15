from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AlphabetTextInput(forms.MultiWidget):
    template_name = "core/widgets/alphabet_field.html"

    def __init__(self, *args, **kwargs):
        widgets = [
            forms.TextInput(attrs={"locale": _(language), "class": "vTextField"})
            for code, language in settings.ALPHABETS
        ]
        super().__init__(widgets, **kwargs)

    def decompress(self, value):
        if value:
            return [value.get(code, "") for code, language in settings.ALPHABETS]
        return []
