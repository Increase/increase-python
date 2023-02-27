# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import WireTransferSimulation

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.create_inbound(
            account_number_id="string",
            amount=1,
        )
        assert_matches_type(WireTransferSimulation, wire_transfer, path=["response"])

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.create_inbound(
            account_number_id="string",
            amount=1,
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
            beneficiary_name="x",
            beneficiary_reference="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            originator_name="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(WireTransferSimulation, wire_transfer, path=["response"])


class TestAsyncWireTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.simulations.wire_transfers.create_inbound(
            account_number_id="string",
            amount=1,
        )
        assert_matches_type(WireTransferSimulation, wire_transfer, path=["response"])

    @parametrize
    async def test_method_create_inbound_with_all_params(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.simulations.wire_transfers.create_inbound(
            account_number_id="string",
            amount=1,
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
            beneficiary_name="x",
            beneficiary_reference="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            originator_name="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(WireTransferSimulation, wire_transfer, path=["response"])
