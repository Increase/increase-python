# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.event import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEvents:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    def test_method_list(self) -> None:
        resource = self.client.events.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.events.list(
            {
                "cursor": "string",
                "limit": 0,
                "associated_object_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "category": {"in": ["account.created", "account.created", "account.created"]},
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncEvents:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    async def test_method_list(self) -> None:
        resource = await self.client.events.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.events.list(
            {
                "cursor": "string",
                "limit": 0,
                "associated_object_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "category": {"in": ["account.created", "account.created", "account.created"]},
            },
        )
        assert isinstance(resource, AsyncPage)
