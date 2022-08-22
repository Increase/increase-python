# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.simulations.wire_transfer_simulation import WireTransferSimulation

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        resource = client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)

    @parametrize
    def test_method_create_inbound_with_optional_params(self, client: Increase) -> None:
        resource = client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)


class TestAsyncWireTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)

    @parametrize
    async def test_method_create_inbound_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)
