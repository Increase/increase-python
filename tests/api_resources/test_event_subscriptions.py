# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    EventSubscription,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.create(
            url="https://website.com/webhooks",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.create(
            url="https://website.com/webhooks",
            oauth_connection_id="x",
            selected_event_category="account.created",
            shared_secret="x",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.event_subscriptions.with_raw_response.create(
            url="https://website.com/webhooks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.event_subscriptions.with_streaming_response.create(
            url="https://website.com/webhooks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.retrieve(
            "event_subscription_id",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.event_subscriptions.with_raw_response.retrieve(
            "event_subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.event_subscriptions.with_streaming_response.retrieve(
            "event_subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_subscription_id` but received ''"):
            client.event_subscriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            status="active",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.event_subscriptions.with_raw_response.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.event_subscriptions.with_streaming_response.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_subscription_id` but received ''"):
            client.event_subscriptions.with_raw_response.update(
                event_subscription_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.list()
        assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.event_subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.event_subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = response.parse()
            assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEventSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.create(
            url="https://website.com/webhooks",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.create(
            url="https://website.com/webhooks",
            oauth_connection_id="x",
            selected_event_category="account.created",
            shared_secret="x",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.event_subscriptions.with_raw_response.create(
            url="https://website.com/webhooks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = await response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.event_subscriptions.with_streaming_response.create(
            url="https://website.com/webhooks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = await response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.retrieve(
            "event_subscription_id",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.event_subscriptions.with_raw_response.retrieve(
            "event_subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = await response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.event_subscriptions.with_streaming_response.retrieve(
            "event_subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = await response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_subscription_id` but received ''"):
            await async_client.event_subscriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            status="active",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.event_subscriptions.with_raw_response.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = await response.parse()
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.event_subscriptions.with_streaming_response.update(
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = await response.parse()
            assert_matches_type(EventSubscription, event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_subscription_id` but received ''"):
            await async_client.event_subscriptions.with_raw_response.update(
                event_subscription_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.list()
        assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        event_subscription = await async_client.event_subscriptions.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.event_subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = await response.parse()
        assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.event_subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = await response.parse()
            assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
