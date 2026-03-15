import pytest
from core.models import Observer
from core.tests.factories import ObserverFactory, UserFactory
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestObserverSetupView:
    def test_requires_login(self):
        client = Client()
        response = client.get(reverse("accounts:observer_setup"))
        assert response.status_code == 302
        assert "login" in response.url

    def test_already_linked_redirects_to_settings(self, client: Client):
        user = UserFactory()
        ObserverFactory(user=user)
        client.force_login(user)

        response = client.get(reverse("accounts:observer_setup"))

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")

    def test_get_prefills_name_from_full_name(self, client: Client):
        user = UserFactory(first_name="Jo", last_name="Smith")
        client.force_login(user)

        response = client.get(reverse("accounts:observer_setup"))

        assert response.context["form"].initial["name"] == "Jo Smith"

    def test_no_match_creates_and_links_immediately(self, client: Client):
        user = UserFactory()
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": "Brand New Observer"})

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        observer = Observer.objects.get(name="Brand New Observer")
        assert observer.user == user

    def test_single_unclaimed_match_requires_confirmation_before_linking(self, client: Client):
        existing = ObserverFactory(name="Jo Smith", user=None)
        user = UserFactory()
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": "Jo Smith"})

        assert response.status_code == 200
        assert response.context["candidate"] == existing
        existing.refresh_from_db()
        assert existing.user is None  # not linked yet -- still needs confirming

    def test_confirming_links_the_existing_observer(self, client: Client):
        existing = ObserverFactory(name="Jo Smith", user=None)
        user = UserFactory()
        client.force_login(user)

        response = client.post(
            reverse("accounts:observer_setup"),
            {"name": "Jo Smith", "action": "confirm", "observer_id": existing.pk},
        )

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        existing.refresh_from_db()
        assert existing.user == user
        assert Observer.objects.filter(name="Jo Smith").count() == 1

    def test_declining_creates_a_separate_observer(self, client: Client):
        existing = ObserverFactory(name="Jo Smith", user=None)
        user = UserFactory()
        client.force_login(user)

        response = client.post(
            reverse("accounts:observer_setup"),
            {"name": "Jo Smith", "action": "create_new"},
        )

        assert response.status_code == 302
        existing.refresh_from_db()
        assert existing.user is None
        new_observer = Observer.objects.exclude(pk=existing.pk).get(name="Jo Smith")
        assert new_observer.user == user

    def test_ambiguous_match_creates_new_rather_than_offering_to_claim(self, client: Client):
        ObserverFactory(name="Jo Smith", user=None)
        ObserverFactory(name="Jo Smith", user=None)
        user = UserFactory()
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": "Jo Smith"})

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        linked = Observer.objects.get(user=user)
        assert linked.name == "Jo Smith"
        assert Observer.objects.filter(name="Jo Smith").count() == 3

    def test_name_matching_someone_elses_claimed_observer_creates_a_new_one(self, client: Client):
        other_user = UserFactory()
        ObserverFactory(name="Jo Smith", user=other_user)
        user = UserFactory()
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": "Jo Smith"})

        assert response.status_code == 302
        linked = Observer.objects.get(user=user)
        assert linked.name == "Jo Smith"
        assert Observer.objects.filter(name="Jo Smith").count() == 2

    def test_already_linked_post_redirects_to_settings(self, client: Client):
        """Guards against a user re-submitting the form (e.g. double-click,
        or two tabs) after they already have an Observer linked."""
        user = UserFactory()
        ObserverFactory(user=user)
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": "Someone Else"})

        assert response.status_code == 302
        assert response.url == reverse("accounts:settings")
        assert Observer.objects.filter(user=user).count() == 1

    def test_blank_name_reshows_the_form_with_errors(self, client: Client):
        user = UserFactory()
        client.force_login(user)

        response = client.post(reverse("accounts:observer_setup"), {"name": ""})

        assert response.status_code == 200
        assert "name" in response.context["form"].errors

    def test_confirming_a_since_claimed_observer_shows_an_error(self, client: Client):
        """A race: the candidate Observer was claimed by someone else
        between being offered up and this confirmation being submitted.
        """
        existing = ObserverFactory(name="Jo Smith", user=UserFactory())
        user = UserFactory()
        client.force_login(user)

        response = client.post(
            reverse("accounts:observer_setup"),
            {"name": "Jo Smith", "action": "confirm", "observer_id": existing.pk},
        )

        assert response.status_code == 302
        assert response.url == reverse("accounts:observer_setup")
        assert Observer.objects.filter(user=user).exists() is False
