# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.event_subscription import EventSubscription

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEventSubscriptions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.event_subscriptions.create(
            {"url": "https://website.com/webhooks"},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    def test_method_create_with_optional_params(self, client: Increase) -> None:
        resource = client.event_subscriptions.create(
            {
                "url": "https://website.com/webhooks",
                "shared_secret": "x",
            },
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.event_subscriptions.retrieve(
            "string",
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        resource = client.event_subscriptions.update(
            "string",
            {},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    def test_method_update_with_optional_params(self, client: Increase) -> None:
        resource = client.event_subscriptions.update(
            "string",
            {"status": "active"},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.event_subscriptions.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_optional_params(self, client: Increase) -> None:
        resource = client.event_subscriptions.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncEventSubscriptions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.create(
            {"url": "https://website.com/webhooks"},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    async def test_method_create_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.create(
            {
                "url": "https://website.com/webhooks",
                "shared_secret": "x",
            },
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.retrieve(
            "string",
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.update(
            "string",
            {},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    async def test_method_update_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.update(
            "string",
            {"status": "active"},
        )
        assert isinstance(resource, EventSubscription)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.event_subscriptions.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)
