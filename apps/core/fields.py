from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .widgets import AlphabetTextInput


class AlphabetField(forms.MultiValueField):
    def __init__(self, **kwargs):
        # Define one set of messages for all fields.
        kwargs["error_messages"] = {
            "required": "Enter the text for the alphabet",
            "incomplete": "Enter text for every alphabet",
        }
        super().__init__(require_all_fields=True, **kwargs)

    def compress(self, data_list):
        codes = [code for code, language in settings.ALPHABETS]
        values = zip(codes, data_list)
        translations = {code: value for code, value in values if value}
        return translations

    def has_changed(self, initial, data):
        # If the value from the database is an empty string, rather than
        # the string representation of an empty dict, set the value to None,
        # so it decompresses correctly.
        return super().has_changed(initial or None, data)


class AlphabetCharField(AlphabetField):
    def __init__(self, **kwargs):
        fields = [forms.CharField(label=_(language)) for code, language in settings.ALPHABETS]
        widget = AlphabetTextInput
        super().__init__(fields=fields, widget=widget, **kwargs)
