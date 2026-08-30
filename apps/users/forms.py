from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

INPUT_CLASSES = (
    "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-brand-500 focus:ring-brand-500 sm:text-sm"
)


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", INPUT_CLASSES)


class SignupForm(StyledFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "script")


class ProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("script",)
