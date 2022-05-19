# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.types.simulations.wire_transfer_simulation import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create_inbound(self) -> None:
        resource = self.client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)

    def test_method_create_inbound_with_optional_params(self) -> None:
        resource = self.client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)


class TestAsyncWireTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create_inbound(self) -> None:
        resource = await self.client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)

    async def test_method_create_inbound_with_optional_params(self) -> None:
        resource = await self.client.simulations.wire_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, WireTransferSimulation)
