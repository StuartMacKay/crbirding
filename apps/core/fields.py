from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .widgets import ScriptTextarea, ScriptTextInput


class ScriptField(forms.MultiValueField):
    def __init__(self, **kwargs):
        # Define one set of messages for all fields.
        kwargs["error_messages"] = {
            "required": "Enter the text for the script",
            "incomplete": "Enter text for every script",
        }
        super().__init__(require_all_fields=True, **kwargs)

    def compress(self, data_list):
        codes = [code for code, language in settings.SCRIPTS]
        values = zip(codes, data_list)
        translations = {code: value for code, value in values if value}
        return translations

    def has_changed(self, initial, data):
        # If the value from the database is an empty string, rather than
        # the string representation of an empty dict, set the value to None,
        # so it decompresses correctly.
        return super().has_changed(initial or None, data)


class ScriptCharField(ScriptField):
    def __init__(self, **kwargs):
        fields = [forms.CharField(label=_(language)) for code, language in settings.SCRIPTS]
        widget = ScriptTextInput
        super().__init__(fields=fields, widget=widget, **kwargs)


class ScriptTextField(ScriptField):
    def __init__(self, **kwargs):
        fields = [forms.CharField(label=_(language)) for code, language in settings.SCRIPTS]
        widget = ScriptTextarea
        super().__init__(fields=fields, widget=widget, **kwargs)
