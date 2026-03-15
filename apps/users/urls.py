from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
)
from django.urls import path, reverse_lazy

from . import views
from .forms import StyledPasswordResetForm, StyledSetPasswordForm

# Flat, unnamespaced -- matches the URL names templates already reference
# (account_login, account_logout, account_signup), so no template changes
# are needed to switch between this and a future auth backend using the
# same names. Password change/reset use Django's own conventional flat
# names for the same reason.
auth_urlpatterns = [
    path(
        "login/",
        views.AccountLoginView.as_view(template_name="account/login.html"),
        name="account_login",
    ),
    path("logout/", LogoutView.as_view(), name="account_logout"),
    path("signup/", views.SignupView.as_view(), name="account_signup"),
    path(
        "password/change/",
        views.AccountPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password/change/done/",
        views.AccountPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password/reset/",
        views.AccountPasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name="account/password_reset.html",
            email_template_name="account/email/password_reset_email.txt",
            subject_template_name="account/email/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password/reset/done/",
        PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            form_class=StyledSetPasswordForm,
            template_name="account/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]

app_name = "accounts"

urlpatterns = [
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("signup/sent/", views.SignupSentView.as_view(), name="signup_sent"),
    path(
        "signup/sent/resend/",
        views.ResendVerificationView.as_view(),
        name="resend_verification",
    ),
    path("verify/<str:token>/", views.VerifyEmailView.as_view(), name="verify_email"),
    path("observer/", views.ObserverSetupView.as_view(), name="observer_setup"),
    path("email/change/", views.ChangeEmailView.as_view(), name="email_change"),
    path(
        "email/change/confirm/<str:token>/",
        views.ConfirmEmailChangeView.as_view(),
        name="email_change_confirm",
    ),
]
