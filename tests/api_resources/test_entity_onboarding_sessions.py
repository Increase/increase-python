# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    EntityOnboardingSession,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntityOnboardingSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
            entity_id="entity_id",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entity_onboarding_sessions.with_raw_response.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entity_onboarding_sessions.with_streaming_response.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.entity_onboarding_sessions.with_raw_response.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.entity_onboarding_sessions.with_streaming_response.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            client.entity_onboarding_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.list()
        assert_matches_type(SyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(SyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.entity_onboarding_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = response.parse()
        assert_matches_type(SyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.entity_onboarding_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = response.parse()
            assert_matches_type(SyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_expire(self, client: Increase) -> None:
        entity_onboarding_session = client.entity_onboarding_sessions.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_raw_response_expire(self, client: Increase) -> None:
        response = client.entity_onboarding_sessions.with_raw_response.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    def test_streaming_response_expire(self, client: Increase) -> None:
        with client.entity_onboarding_sessions.with_streaming_response.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_expire(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            client.entity_onboarding_sessions.with_raw_response.expire(
                "",
            )


class TestAsyncEntityOnboardingSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
            entity_id="entity_id",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entity_onboarding_sessions.with_raw_response.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = await response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.entity_onboarding_sessions.with_streaming_response.create(
            program_id="program_i2v2os4mwza1oetokh9i",
            redirect_url="https://example.com/onboarding/session",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = await response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entity_onboarding_sessions.with_raw_response.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = await response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.entity_onboarding_sessions.with_streaming_response.retrieve(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = await response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            await async_client.entity_onboarding_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.list()
        assert_matches_type(AsyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entity_onboarding_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = await response.parse()
        assert_matches_type(AsyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.entity_onboarding_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = await response.parse()
            assert_matches_type(AsyncPage[EntityOnboardingSession], entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_expire(self, async_client: AsyncIncrease) -> None:
        entity_onboarding_session = await async_client.entity_onboarding_sessions.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_raw_response_expire(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entity_onboarding_sessions.with_raw_response.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_onboarding_session = await response.parse()
        assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

    @parametrize
    async def test_streaming_response_expire(self, async_client: AsyncIncrease) -> None:
        async with async_client.entity_onboarding_sessions.with_streaming_response.expire(
            "entity_onboarding_session_wid2ug11fsmvh3k9hymd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_onboarding_session = await response.parse()
            assert_matches_type(EntityOnboardingSession, entity_onboarding_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_expire(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_onboarding_session_id` but received ''"
        ):
            await async_client.entity_onboarding_sessions.with_raw_response.expire(
                "",
            )
