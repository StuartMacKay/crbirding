"""Stateless, signed tokens for the two account flows that need to prove
someone controls an email address before anything is written to the
database: signup (see SignupView) and changing an existing account's email
(see ChangeEmailView).

Both use django.core.signing.dumps/loads rather than a stored token model
-- there's nothing to clean up if a link is never clicked, and nothing to
race against if it's clicked twice. Distinct `salt` values per purpose mean
a token minted for one endpoint can't be replayed against the other, even
though the payloads are otherwise easy to tell apart.
"""

from django.core import signing

SIGNUP_SALT = "users.signup"
SIGNUP_MAX_AGE = 60 * 60 * 24 * 3  # 3 days

EMAIL_CHANGE_SALT = "users.email-change"
EMAIL_CHANGE_MAX_AGE = 60 * 60 * 24  # 1 day


def sign_signup(
    *, email: str, password_hash: str, first_name: str, last_name: str, alphabet: str
) -> str:
    return signing.dumps(
        {
            "email": email,
            "password_hash": password_hash,
            "first_name": first_name,
            "last_name": last_name,
            "alphabet": alphabet,
        },
        salt=SIGNUP_SALT,
        compress=True,
    )


def unsign_signup(token: str) -> dict | None:
    try:
        return signing.loads(token, salt=SIGNUP_SALT, max_age=SIGNUP_MAX_AGE)
    except signing.BadSignature:
        return None


def sign_email_change(*, user_id: int, new_email: str) -> str:
    return signing.dumps(
        {"user_id": user_id, "new_email": new_email},
        salt=EMAIL_CHANGE_SALT,
        compress=True,
    )


def unsign_email_change(token: str) -> dict | None:
    try:
        return signing.loads(token, salt=EMAIL_CHANGE_SALT, max_age=EMAIL_CHANGE_MAX_AGE)
    except signing.BadSignature:
        return None
