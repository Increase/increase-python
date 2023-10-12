# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import WireDrawdownRequest
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestWireDrawdownRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            message_to_recipient="Invoice 29582",
            recipient_account_number="987654321",
            recipient_name="Ian Crease",
            recipient_routing_number="101050001",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            message_to_recipient="Invoice 29582",
            recipient_account_number="987654321",
            recipient_name="Ian Crease",
            recipient_routing_number="101050001",
            recipient_address_line1="33 Liberty Street",
            recipient_address_line2="New York, NY, 10045",
            recipient_address_line3="x",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.retrieve(
            "string",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.list()
        assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])


class TestAsyncWireDrawdownRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        wire_drawdown_request = await client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            message_to_recipient="Invoice 29582",
            recipient_account_number="987654321",
            recipient_name="Ian Crease",
            recipient_routing_number="101050001",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        wire_drawdown_request = await client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            message_to_recipient="Invoice 29582",
            recipient_account_number="987654321",
            recipient_name="Ian Crease",
            recipient_routing_number="101050001",
            recipient_address_line1="33 Liberty Street",
            recipient_address_line2="New York, NY, 10045",
            recipient_address_line3="x",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        wire_drawdown_request = await client.wire_drawdown_requests.retrieve(
            "string",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        wire_drawdown_request = await client.wire_drawdown_requests.list()
        assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        wire_drawdown_request = await client.wire_drawdown_requests.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])
