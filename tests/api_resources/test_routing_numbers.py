# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import AsyncPage, SyncPage


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRoutingNumbers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.routing_numbers.list(
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.routing_numbers.list(
            cursor="string",
            limit=0,
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, SyncPage)


class TestAsyncRoutingNumbers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.routing_numbers.list(
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.routing_numbers.list(
            cursor="string",
            limit=0,
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, AsyncPage)
