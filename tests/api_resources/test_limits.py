# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.limit import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLimits:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.limits.create(
            {
                "metric": "volume",
                "model_id": "account0",
                "value": 1234,
            },
        )
        assert isinstance(resource, Limit)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.limits.create(
            {
                "metric": "volume",
                "interval": "month",
                "model_id": "account0",
                "value": 1234,
            },
        )
        assert isinstance(resource, Limit)

    def test_method_retrieve(self) -> None:
        resource = self.client.limits.retrieve(
            "string",
        )
        assert isinstance(resource, Limit)

    def test_method_update(self) -> None:
        resource = self.client.limits.update(
            "string",
            {"status": "inactive"},
        )
        assert isinstance(resource, Limit)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.limits.update(
            "string",
            {"status": "inactive"},
        )
        assert isinstance(resource, Limit)

    def test_method_list(self) -> None:
        resource = self.client.limits.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.limits.list(
            {
                "cursor": "string",
                "limit": 0,
                "model_id": "x",
                "status": "x",
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncLimits:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.limits.create(
            {
                "metric": "volume",
                "model_id": "account0",
                "value": 1234,
            },
        )
        assert isinstance(resource, Limit)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.limits.create(
            {
                "metric": "volume",
                "interval": "month",
                "model_id": "account0",
                "value": 1234,
            },
        )
        assert isinstance(resource, Limit)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.limits.retrieve(
            "string",
        )
        assert isinstance(resource, Limit)

    async def test_method_update(self) -> None:
        resource = await self.client.limits.update(
            "string",
            {"status": "inactive"},
        )
        assert isinstance(resource, Limit)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.limits.update(
            "string",
            {"status": "inactive"},
        )
        assert isinstance(resource, Limit)

    async def test_method_list(self) -> None:
        resource = await self.client.limits.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.limits.list(
            {
                "cursor": "string",
                "limit": 0,
                "model_id": "x",
                "status": "x",
            },
        )
        assert isinstance(resource, AsyncPage)
