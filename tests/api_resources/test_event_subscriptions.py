# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.event_subscription import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEventSubscriptions:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.event_subscriptions.create(
            {"url": "https://website.com/webhooks"},
        )
        assert isinstance(resource, EventSubscription)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.event_subscriptions.create(
            {
                "url": "https://website.com/webhooks",
                "shared_secret": "x",
            },
        )
        assert isinstance(resource, EventSubscription)

    def test_method_retrieve(self) -> None:
        resource = self.client.event_subscriptions.retrieve(
            "string",
        )
        assert isinstance(resource, EventSubscription)

    def test_method_update(self) -> None:
        resource = self.client.event_subscriptions.update(
            "string",
            {},
        )
        assert isinstance(resource, EventSubscription)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.event_subscriptions.update(
            "string",
            {"status": "active"},
        )
        assert isinstance(resource, EventSubscription)

    def test_method_list(self) -> None:
        resource = self.client.event_subscriptions.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.event_subscriptions.list(
            {
                "cursor": "x",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncEventSubscriptions:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.event_subscriptions.create(
            {"url": "https://website.com/webhooks"},
        )
        assert isinstance(resource, EventSubscription)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.event_subscriptions.create(
            {
                "url": "https://website.com/webhooks",
                "shared_secret": "x",
            },
        )
        assert isinstance(resource, EventSubscription)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.event_subscriptions.retrieve(
            "string",
        )
        assert isinstance(resource, EventSubscription)

    async def test_method_update(self) -> None:
        resource = await self.client.event_subscriptions.update(
            "string",
            {},
        )
        assert isinstance(resource, EventSubscription)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.event_subscriptions.update(
            "string",
            {"status": "active"},
        )
        assert isinstance(resource, EventSubscription)

    async def test_method_list(self) -> None:
        resource = await self.client.event_subscriptions.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.event_subscriptions.list(
            {
                "cursor": "x",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)
