# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease

from increase.types.simulations.inbound_real_time_payments_transfer_simulation_result import (
    InboundRealTimePaymentsTransferSimulationResult,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRealTimePaymentsTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        resource = client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=0,
        )
        assert isinstance(resource, InboundRealTimePaymentsTransferSimulationResult)


class TestAsyncRealTimePaymentsTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=0,
        )
        assert isinstance(resource, InboundRealTimePaymentsTransferSimulationResult)
