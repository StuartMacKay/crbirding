from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

# Flat, unnamespaced -- matches the URL names templates already reference
# (account_login, account_logout, account_signup), so no template changes
# are needed to switch between this and a future auth backend using the
# same names.
auth_urlpatterns = [
    path("login/", LoginView.as_view(template_name="account/login.html"), name="account_login"),
    path("logout/", LogoutView.as_view(), name="account_logout"),
    path("signup/", views.SignupView.as_view(), name="account_signup"),
]

app_name = "accounts"

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
]
