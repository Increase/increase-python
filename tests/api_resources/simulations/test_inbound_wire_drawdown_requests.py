# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundWireDrawdownRequest
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInboundWireDrawdownRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            beneficiary_address_line1="33 Liberty Street",
            beneficiary_address_line2="New York, NY, 10045",
            beneficiary_address_line3="x",
            beneficiary_name="Ian Crease",
            originator_address_line1="33 Liberty Street",
            originator_address_line2="New York, NY, 10045",
            originator_address_line3="x",
            originator_name="Ian Crease",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_wire_drawdown_requests.with_raw_response.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_wire_drawdown_requests.with_streaming_response.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_drawdown_request = response.parse()
            assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundWireDrawdownRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            beneficiary_address_line1="33 Liberty Street",
            beneficiary_address_line2="New York, NY, 10045",
            beneficiary_address_line3="x",
            beneficiary_name="Ian Crease",
            originator_address_line1="33 Liberty Street",
            originator_address_line2="New York, NY, 10045",
            originator_address_line3="x",
            originator_name="Ian Crease",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.simulations.inbound_wire_drawdown_requests.with_raw_response.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.simulations.inbound_wire_drawdown_requests.with_streaming_response.create(
            amount=10000,
            beneficiary_account_number="987654321",
            beneficiary_routing_number="101050001",
            currency="USD",
            message_to_recipient="Invoice 29582",
            originator_account_number="987654321",
            originator_routing_number="101050001",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_drawdown_request = await response.parse()
            assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True
