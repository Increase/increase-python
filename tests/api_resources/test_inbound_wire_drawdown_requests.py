# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundWireDrawdownRequest
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInboundWireDrawdownRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.inbound_wire_drawdown_requests.retrieve(
            "string",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_wire_drawdown_requests.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.inbound_wire_drawdown_requests.list()
        assert_matches_type(SyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.inbound_wire_drawdown_requests.list(
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_wire_drawdown_requests.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(SyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])


class TestAsyncInboundWireDrawdownRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.inbound_wire_drawdown_requests.retrieve(
            "string",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.inbound_wire_drawdown_requests.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.inbound_wire_drawdown_requests.list()
        assert_matches_type(AsyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.inbound_wire_drawdown_requests.list(
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.inbound_wire_drawdown_requests.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(AsyncPage[InboundWireDrawdownRequest], inbound_wire_drawdown_request, path=["response"])
