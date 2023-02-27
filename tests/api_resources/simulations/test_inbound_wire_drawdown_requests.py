# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundWireDrawdownRequest

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestInboundWireDrawdownRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            recipient_account_number_id="string",
            originator_account_number="x",
            originator_routing_number="x",
            beneficiary_account_number="x",
            beneficiary_routing_number="x",
            amount=0,
            currency="x",
            message_to_recipient="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            recipient_account_number_id="string",
            originator_account_number="x",
            originator_routing_number="x",
            beneficiary_account_number="x",
            beneficiary_routing_number="x",
            amount=0,
            currency="x",
            message_to_recipient="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
            originator_name="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            beneficiary_name="x",
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])


class TestAsyncInboundWireDrawdownRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.simulations.inbound_wire_drawdown_requests.create(
            recipient_account_number_id="string",
            originator_account_number="x",
            originator_routing_number="x",
            beneficiary_account_number="x",
            beneficiary_routing_number="x",
            amount=0,
            currency="x",
            message_to_recipient="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await client.simulations.inbound_wire_drawdown_requests.create(
            recipient_account_number_id="string",
            originator_account_number="x",
            originator_routing_number="x",
            beneficiary_account_number="x",
            beneficiary_routing_number="x",
            amount=0,
            currency="x",
            message_to_recipient="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
            originator_name="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            beneficiary_name="x",
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])
