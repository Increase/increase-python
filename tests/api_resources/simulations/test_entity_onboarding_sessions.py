# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import EntityOnboardingSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntityOnboardingSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        entity_onboarding_session = client.simulations.entity_onboarding_sessions.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.entity_onboarding_sessions.with_raw_response.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.entity_onboarding_sessions.with_streaming_response.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            client.simulations.entity_onboarding_sessions.with_raw_response.submit(
                "",
            )


class TestAsyncEntityOnboardingSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.simulations.entity_onboarding_sessions.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.entity_onboarding_sessions.with_raw_response.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = await response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.entity_onboarding_sessions.with_streaming_response.submit(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = await response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            await async_client.simulations.entity_onboarding_sessions.with_raw_response.submit(
                "",
            )
