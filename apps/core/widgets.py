from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ScriptTextInput(forms.MultiWidget):
    template_name = "core/widgets/script_field.html"

    def __init__(self, *args, **kwargs):
        widgets = [
            forms.TextInput(attrs={"locale": _(language), "class": "vTextField"})
            for code, language in settings.SCRIPTS
        ]
        super().__init__(widgets, **kwargs)

    def decompress(self, value):
        if value:
            return [value.get(code, "") for code, language in settings.SCRIPTS]
        return []


class ScriptTextarea(forms.MultiWidget):
    template_name = "core/widgets/script_field.html"

    def __init__(self, *args, **kwargs):
        if "widgets" not in kwargs:
            kwargs["widgets"] = [
                forms.Textarea(
                    attrs={
                        "locale": _(language),
                        "rows": 10,
                        "class": "vLargeTextField",
                    }
                )
                for code, language in settings.SCRIPTS
            ]
        super().__init__(**kwargs)

    def decompress(self, value):
        if value:
            return [value.get(code, "") for code, language in settings.SCRIPTS]
        return []
