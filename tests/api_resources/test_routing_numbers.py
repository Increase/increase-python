# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RoutingNumberListResponse
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutingNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        routing_number = client.routing_numbers.list(
            routing_number="xxxxxxxxx",
        )
        assert_matches_type(SyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        routing_number = client.routing_numbers.list(
            routing_number="xxxxxxxxx",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.routing_numbers.with_raw_response.list(
            routing_number="xxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_number = response.parse()
        assert_matches_type(SyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.routing_numbers.with_streaming_response.list(
            routing_number="xxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_number = response.parse()
            assert_matches_type(SyncPage[RoutingNumberListResponse], routing_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutingNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        routing_number = await async_client.routing_numbers.list(
            routing_number="xxxxxxxxx",
        )
        assert_matches_type(AsyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        routing_number = await async_client.routing_numbers.list(
            routing_number="xxxxxxxxx",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.routing_numbers.with_raw_response.list(
            routing_number="xxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_number = await response.parse()
        assert_matches_type(AsyncPage[RoutingNumberListResponse], routing_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.routing_numbers.with_streaming_response.list(
            routing_number="xxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_number = await response.parse()
            assert_matches_type(AsyncPage[RoutingNumberListResponse], routing_number, path=["response"])

        assert cast(Any, response.is_closed) is True
