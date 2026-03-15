from pathlib import Path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from .factories import OriginFactory, SuperUserFactory


@pytest.mark.django_db
class TestOriginAdminHistoryFile:
    def _data(self, origin, **overrides):
        data = {
            "species": origin.species,
            "label": origin.label,
            "age": "",
            "sex": "",
            "date": origin.date.isoformat(),
            "time": "",
            "location": origin.location.pk,
            "latitude": "",
            "longitude": "",
            "notes": "",
            "project": origin.project.pk,
            "history_url": "",
        }
        data.update(overrides)
        return data

    def test_change_page_offers_the_life_history_fields(self, client: Client):
        origin = OriginFactory()
        client.force_login(SuperUserFactory())
        response = client.get(reverse("admin:core_origin_change", args=[origin.pk]))
        content = response.content.decode()
        assert 'name="history_file"' in content
        assert 'name="history_url"' in content

    def test_uploading_a_new_file_replaces_the_old_one(
        self, client: Client, settings, tmp_path, django_capture_on_commit_callbacks
    ):
        settings.MEDIA_ROOT = tmp_path
        origin = OriginFactory(history_file=SimpleUploadedFile("history.pdf", b"first"))
        old_path = Path(origin.history_file.path)

        client.force_login(SuperUserFactory())
        with django_capture_on_commit_callbacks(execute=True):
            response = client.post(
                reverse("admin:core_origin_change", args=[origin.pk]),
                self._data(origin, history_file=SimpleUploadedFile("history.pdf", b"second")),
            )

        assert response.status_code == 302, response.context["errors"]
        origin.refresh_from_db()
        assert origin.history_file.read() == b"second"
        assert not old_path.exists()
