# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.limit import Limit

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLimits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.limits.create(
            metric="count",
            model_id="x",
            value=0,
        )
        assert isinstance(resource, Limit)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.limits.create(
            metric="count",
            interval="transaction",
            model_id="x",
            value=0,
        )
        assert isinstance(resource, Limit)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.limits.retrieve(
            "string",
        )
        assert isinstance(resource, Limit)

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        resource = client.limits.update(
            "string",
            status="inactive",
        )
        assert isinstance(resource, Limit)

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        resource = client.limits.update(
            "string",
            status="inactive",
        )
        assert isinstance(resource, Limit)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.limits.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.limits.list(
            cursor="string",
            limit=0,
            model_id="x",
            status="x",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncLimits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.limits.create(
            metric="count",
            model_id="x",
            value=0,
        )
        assert isinstance(resource, Limit)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.limits.create(
            metric="count",
            interval="transaction",
            model_id="x",
            value=0,
        )
        assert isinstance(resource, Limit)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.limits.retrieve(
            "string",
        )
        assert isinstance(resource, Limit)

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        resource = await client.limits.update(
            "string",
            status="inactive",
        )
        assert isinstance(resource, Limit)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.limits.update(
            "string",
            status="inactive",
        )
        assert isinstance(resource, Limit)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.limits.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.limits.list(
            cursor="string",
            limit=0,
            model_id="x",
            status="x",
        )
        assert isinstance(resource, AsyncPage)
