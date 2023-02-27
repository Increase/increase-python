# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import EventSubscription
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEventSubscriptions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.create(
            url="string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.create(
            url="string",
            shared_secret="x",
            selected_event_category="account.created",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.update(
            "string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.update(
            "string",
            status="active",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.list()
        assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        event_subscription = client.event_subscriptions.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[EventSubscription], event_subscription, path=["response"])


class TestAsyncEventSubscriptions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.create(
            url="string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.create(
            url="string",
            shared_secret="x",
            selected_event_category="account.created",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.update(
            "string",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.update(
            "string",
            status="active",
        )
        assert_matches_type(EventSubscription, event_subscription, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.list()
        assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        event_subscription = await client.event_subscriptions.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[EventSubscription], event_subscription, path=["response"])
