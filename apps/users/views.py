from core.models import Observer
from core.utils.matching import find_claimable_observer
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeDoneView, PasswordChangeView
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, UpdateView

from .emails import (
    send_email_change_confirmation,
    send_email_changed_notifications,
    send_password_changed_email,
    send_verification_email,
)
from .forms import (
    ChangeEmailForm,
    ObserverNameForm,
    ProfileForm,
    SignupForm,
    StyledPasswordChangeForm,
)
from .models import User
from .ratelimit import is_rate_limited
from .tokens import sign_email_change, sign_signup, unsign_email_change, unsign_signup

# (limit, window in seconds) per anonymous, abuse-prone endpoint. See
# ratelimit.is_rate_limited -- keyed by IP alone, one shared 15-minute
# window for everything except login, which is more generous since
# legitimate users on a shared/NAT'd IP hit it far more often than a
# signup or password-reset form.
RATE_LIMIT_WINDOW_SECONDS = 60 * 15
SIGNUP_RATE_LIMIT = 5
RESEND_VERIFICATION_RATE_LIMIT = 3
LOGIN_RATE_LIMIT = 15
PASSWORD_RESET_RATE_LIMIT = 5

# Session key SignupView stashes its token under, so SignupSentView can
# offer a "resend" button without needing anything persisted server-side
# (see SignupView's own docstring for why nothing is persisted at all).
PENDING_SIGNUP_SESSION_KEY = "pending_signup_token"


class SignupView(FormView):
    """Doesn't create a User at all -- see tokens.sign_signup. The form
    data (including the already-hashed password) is signed into the
    verification link instead, so an account only ever exists once its
    email has been proven reachable, and an abandoned signup never
    squats on an email address.
    """

    form_class = SignupForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("accounts:signup_sent")

    def post(self, request, *args, **kwargs):
        if is_rate_limited(
            action="signup",
            request=request,
            limit=SIGNUP_RATE_LIMIT,
            window_seconds=RATE_LIMIT_WINDOW_SECONDS,
        ):
            messages.error(request, "Too many signup attempts -- please try again later.")
            return redirect("account_signup")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.cleaned_data["website"]:
            # Honeypot tripped -- still show the normal success page so a
            # bot doesn't learn it was caught, but don't send anything.
            return super().form_valid(form)

        user = form.save(commit=False)  # hashes the password; never saved
        token = sign_signup(
            email=user.email,
            password_hash=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            alphabet=user.alphabet,
        )
        send_verification_email(self.request, email=user.email, token=token)
        self.request.session[PENDING_SIGNUP_SESSION_KEY] = token
        return super().form_valid(form)


class SignupSentView(TemplateView):
    template_name = "account/signup_sent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_resend"] = PENDING_SIGNUP_SESSION_KEY in self.request.session
        return context


class ResendVerificationView(View):
    """Re-sends the signup verification email -- reachable from
    SignupSentView's "resend" button. Mints a fresh token (rather than
    re-sending the original) so a slow-to-check inbox also gets a fresh
    3-day window, and re-signs it from the token already in the session
    rather than asking the user to retype anything: SignupView never
    persisted their details anywhere else to look them up from.
    """

    def post(self, request):
        if is_rate_limited(
            action="resend-verification",
            request=request,
            limit=RESEND_VERIFICATION_RATE_LIMIT,
            window_seconds=RATE_LIMIT_WINDOW_SECONDS,
        ):
            messages.error(request, "Too many attempts -- please try again later.")
            return redirect("accounts:signup_sent")

        token = request.session.get(PENDING_SIGNUP_SESSION_KEY)
        payload = unsign_signup(token) if token else None
        if payload is None:
            request.session.pop(PENDING_SIGNUP_SESSION_KEY, None)
            messages.error(request, "That signup has expired -- please sign up again.")
            return redirect("account_signup")

        if User.objects.filter(email__iexact=payload["email"]).exists():
            request.session.pop(PENDING_SIGNUP_SESSION_KEY, None)
            messages.info(request, "That email is already verified -- sign in below.")
            return redirect("account_login")

        new_token = sign_signup(
            email=payload["email"],
            password_hash=payload["password_hash"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            alphabet=payload["alphabet"],
        )
        send_verification_email(request, email=payload["email"], token=new_token)
        request.session[PENDING_SIGNUP_SESSION_KEY] = new_token
        messages.success(request, "Sent -- check your email for the new link.")
        return redirect("accounts:signup_sent")


class VerifyEmailView(View):
    """Creates the User the signup token describes -- the first point at
    which a signup actually becomes an account (see SignupView).
    """

    def get(self, request, token):
        payload = unsign_signup(token)
        if payload is None:
            return render(request, "account/verify_email_invalid.html", status=400)

        if User.objects.filter(email__iexact=payload["email"]).exists():
            messages.info(request, "That email is already verified -- sign in below.")
            return redirect("account_login")

        user = User(
            email=payload["email"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            alphabet=payload["alphabet"],
        )
        user.password = payload["password_hash"]
        user.save()

        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("accounts:observer_setup")


class ObserverSetupView(LoginRequiredMixin, View):
    """Link the signed-in user to their Observer identity -- the "credited
    sighting observer" record, distinct from the account itself (see
    core.models.Observer). Reachable right after signup, and again later
    from the account settings if skipped.

    A name matching exactly one existing, unclaimed Observer (likely from
    imported historical data) is offered up for confirmation rather than
    silently linked or silently duplicated -- fraud isn't the concern here,
    just catching the "oh, that's already me" case (see
    core.utils.matching.find_claimable_observer).
    """

    template_name = "account/observer_setup.html"

    def get(self, request):
        if Observer.objects.filter(user=request.user).exists():
            return redirect("accounts:settings")
        form = ObserverNameForm(
            initial={"name": request.user.get_full_name() or request.user.email}
        )
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if Observer.objects.filter(user=request.user).exists():
            return redirect("accounts:settings")

        action = request.POST.get("action", "submit")

        if action == "confirm":
            observer = Observer.objects.filter(
                pk=request.POST.get("observer_id"), user__isnull=True
            ).first()
            if observer is None:
                messages.error(
                    request, "That observer has since been claimed by someone else -- try again."
                )
                return redirect("accounts:observer_setup")
            observer.user = request.user
            observer.save(update_fields=["user"])
            messages.success(request, f'Linked to the existing observer "{observer.name}".')
            return redirect("accounts:settings")

        form = ObserverNameForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        name = form.cleaned_data["name"]

        if action == "submit":
            candidate = find_claimable_observer(name)
            if candidate is not None:
                return render(request, self.template_name, {"form": form, "candidate": candidate})

        Observer.objects.create(name=name, user=request.user)
        messages.success(request, f'Created your observer identity, "{name}".')
        return redirect("accounts:settings")


class ChangeEmailView(LoginRequiredMixin, FormView):
    """Doesn't touch User.email -- see tokens.sign_email_change, which
    signs the new address into the confirmation link sent there instead.
    """

    form_class = ChangeEmailForm
    template_name = "account/change_email.html"
    success_url = reverse_lazy("accounts:settings")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        new_email = form.cleaned_data["new_email"]
        token = sign_email_change(user_id=self.request.user.pk, new_email=new_email)
        send_email_change_confirmation(self.request, new_email=new_email, token=token)
        messages.success(
            self.request,
            f"We've sent a confirmation link to {new_email}. "
            "Click it to finish changing your email.",
        )
        return super().form_valid(form)


class ConfirmEmailChangeView(LoginRequiredMixin, View):
    def get(self, request, token):
        payload = unsign_email_change(token)
        if payload is None or payload["user_id"] != request.user.pk:
            messages.error(request, "That confirmation link is invalid or has expired.")
            return redirect("accounts:settings")

        new_email = payload["new_email"]
        if User.objects.exclude(pk=request.user.pk).filter(email__iexact=new_email).exists():
            messages.error(request, "That email address is already in use.")
            return redirect("accounts:settings")

        old_email = request.user.email
        request.user.email = new_email
        request.user.save(update_fields=["email"])
        send_email_changed_notifications(
            user=request.user, old_email=old_email, new_email=new_email
        )
        messages.success(request, "Your email address has been updated.")
        return redirect("accounts:settings")


class AccountLoginView(LoginView):
    template_name = "account/login.html"

    def post(self, request, *args, **kwargs):
        if is_rate_limited(
            action="login",
            request=request,
            limit=LOGIN_RATE_LIMIT,
            window_seconds=RATE_LIMIT_WINDOW_SECONDS,
        ):
            messages.error(request, "Too many attempts -- please try again later.")
            return redirect("account_login")
        return super().post(request, *args, **kwargs)


class AccountPasswordResetView(BasePasswordResetView):
    def post(self, request, *args, **kwargs):
        if is_rate_limited(
            action="password-reset",
            request=request,
            limit=PASSWORD_RESET_RATE_LIMIT,
            window_seconds=RATE_LIMIT_WINDOW_SECONDS,
        ):
            messages.error(request, "Too many attempts -- please try again later.")
            return redirect("password_reset")
        return super().post(request, *args, **kwargs)


class AccountPasswordChangeView(PasswordChangeView):
    form_class = StyledPasswordChangeForm
    template_name = "account/password_change.html"
    success_url = reverse_lazy("password_change_done")

    def form_valid(self, form):
        response = super().form_valid(form)
        send_password_changed_email(self.request.user)
        return response


class AccountPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "account/password_change_done.html"


class SettingsView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "account/settings.html"
    success_url = reverse_lazy("accounts:settings")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your details were updated successfully.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["observer"] = Observer.objects.filter(user=self.request.user).first()
        return context
