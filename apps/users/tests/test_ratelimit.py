import pytest
from django.test import RequestFactory

from users.ratelimit import is_rate_limited

# conftest.py's clear_ratelimit_cache fixture (autouse) keeps these tests
# isolated from each other and from every other test in this package.


@pytest.fixture
def request_(rf: RequestFactory):
    return rf.post("/", REMOTE_ADDR="203.0.113.1")


class TestIsRateLimited:
    def test_allows_up_to_the_limit(self, request_):
        for _ in range(3):
            assert (
                is_rate_limited(action="test", request=request_, limit=3, window_seconds=60)
                is False
            )

    def test_blocks_once_the_limit_is_reached(self, request_):
        for _ in range(3):
            is_rate_limited(action="test", request=request_, limit=3, window_seconds=60)

        assert is_rate_limited(action="test", request=request_, limit=3, window_seconds=60) is True

    def test_different_actions_have_independent_limits(self, request_):
        for _ in range(3):
            is_rate_limited(action="action-a", request=request_, limit=3, window_seconds=60)

        assert (
            is_rate_limited(action="action-b", request=request_, limit=3, window_seconds=60)
            is False
        )

    def test_different_ips_have_independent_limits(self, rf: RequestFactory):
        request_a = rf.post("/", REMOTE_ADDR="203.0.113.1")
        request_b = rf.post("/", REMOTE_ADDR="203.0.113.2")

        for _ in range(3):
            is_rate_limited(action="test", request=request_a, limit=3, window_seconds=60)

        assert (
            is_rate_limited(action="test", request=request_b, limit=3, window_seconds=60) is False
        )
