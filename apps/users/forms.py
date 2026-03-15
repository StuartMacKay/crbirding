from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
)

from .models import User

INPUT_CLASSES = (
    "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
    "focus:border-accent-500 focus:ring-accent-500 sm:text-sm"
)


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", INPUT_CLASSES)


class SignupForm(StyledFormMixin, UserCreationForm):
    # Honeypot -- real visitors never see this (see signup.html, which
    # renders hidden fields without a visible label) so it should always
    # be blank. A filled-in value means a bot; SignupView quietly no-ops
    # rather than telling it so.
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "alphabet")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False


class ProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "alphabet")


class ChangeEmailForm(StyledFormMixin, forms.Form):
    """Doesn't touch User.email itself -- see ChangeEmailView, which signs
    the new address into a token and only applies it once the confirmation
    link sent there is clicked.
    """

    new_email = forms.EmailField(label="New email address")
    current_password = forms.CharField(label="Current password", widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        password = self.cleaned_data["current_password"]
        if not self.user.check_password(password):
            raise forms.ValidationError("That's not your current password.")
        return password

    def clean_new_email(self):
        email = User.objects.normalize_email(self.cleaned_data["new_email"])
        if User.objects.exclude(pk=self.user.pk).filter(email__iexact=email).exists():
            raise forms.ValidationError("That email address is already in use.")
        return email


class ObserverNameForm(StyledFormMixin, forms.Form):
    name = forms.CharField(label="Your name")


# Tailwind-styled versions of Django's own auth forms, so password
# change/reset match the rest of the site instead of rendering unstyled.
class StyledPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    pass


class StyledPasswordResetForm(StyledFormMixin, PasswordResetForm):
    pass


class StyledSetPasswordForm(StyledFormMixin, SetPasswordForm):
    pass
