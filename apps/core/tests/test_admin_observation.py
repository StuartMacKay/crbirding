import pytest
from django.test import Client
from django.urls import reverse

from .factories import ObservationFactory, OriginFactory, SuperUserFactory


@pytest.mark.django_db
class TestObservationAdminOriginEvent:
    def _post(self, client, observation, origin):
        data = {
            "species": observation.species,
            "age": "",
            "sex": "",
            "date": observation.date.isoformat(),
            "time": "",
            "location": observation.location.pk,
            "latitude": "",
            "longitude": "",
            "accuracy": "",
            "notes": "",
            "owner": observation.owner_id or "",
            "origin": origin.pk if origin else "",
            "observers": [o.pk for o in observation.observers.all()],
        }
        for prefix in ("tags", "photos"):
            data.update(
                {
                    f"{prefix}-TOTAL_FORMS": "0",
                    f"{prefix}-INITIAL_FORMS": "0",
                    f"{prefix}-MIN_NUM_FORMS": "0",
                    f"{prefix}-MAX_NUM_FORMS": "1000",
                }
            )
        return client.post(reverse("admin:core_observation_change", args=[observation.pk]), data)

    def test_setting_origin_records_an_event(self, client: Client):
        observation = ObservationFactory(origin=None)
        origin = OriginFactory()

        client.force_login(SuperUserFactory())
        response = self._post(client, observation, origin)

        assert response.status_code == 302, response.context["errors"]
        assert observation.events.get().description.startswith("Ringing details added")

    def test_saving_without_changing_origin_records_nothing(self, client: Client):
        observation = ObservationFactory(origin=OriginFactory())

        client.force_login(SuperUserFactory())
        response = self._post(client, observation, observation.origin)

        assert response.status_code == 302, response.context["errors"]
        assert not observation.events.exists()
