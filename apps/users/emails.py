"""Sends every account-related notification and confirmation email.

Each function renders a subject/body template pair from
apps/users/templates/account/email/ and sends it with django.core.mail.send_mail.
Plain text, not HTML -- there's no HTML-email scaffolding anywhere else in
the project to build on, and these are short, functional messages.

Callers pass `request` so link-building templates can use
request.build_absolute_uri() -- these functions never guess a domain.
"""

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


def _send(*, subject_template: str, body_template: str, to: str, context: dict) -> None:
    subject = render_to_string(subject_template, context).strip()
    body = render_to_string(body_template, context).strip()
    send_mail(subject, body, None, [to])


def send_verification_email(request, *, email: str, token: str) -> None:
    url = request.build_absolute_uri(reverse("accounts:verify_email", args=[token]))
    _send(
        subject_template="account/email/verify_email_subject.txt",
        body_template="account/email/verify_email_body.txt",
        to=email,
        context={"url": url},
    )


def send_password_changed_email(user) -> None:
    _send(
        subject_template="account/email/password_changed_subject.txt",
        body_template="account/email/password_changed_body.txt",
        to=user.email,
        context={"user": user},
    )


def send_email_change_confirmation(request, *, new_email: str, token: str) -> None:
    url = request.build_absolute_uri(reverse("accounts:email_change_confirm", args=[token]))
    _send(
        subject_template="account/email/email_change_confirm_subject.txt",
        body_template="account/email/email_change_confirm_body.txt",
        to=new_email,
        context={"url": url},
    )


def send_email_changed_notifications(*, user, old_email: str, new_email: str) -> None:
    context = {"user": user, "old_email": old_email, "new_email": new_email}
    _send(
        subject_template="account/email/email_changed_subject.txt",
        body_template="account/email/email_changed_old_body.txt",
        to=old_email,
        context=context,
    )
    _send(
        subject_template="account/email/email_changed_subject.txt",
        body_template="account/email/email_changed_new_body.txt",
        to=new_email,
        context=context,
    )
