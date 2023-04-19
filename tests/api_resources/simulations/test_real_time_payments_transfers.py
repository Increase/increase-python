# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimePaymentsTransfer
from increase.types.simulations import InboundRealTimePaymentsTransferSimulationResult

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRealTimePaymentsTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_complete(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.complete(
            "string",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_complete_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.complete(
            "string",
            rejection={"reject_reason_code": "account_closed"},
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=1,
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=1,
            request_for_payment_id="string",
            debtor_name="x",
            debtor_account_number="x",
            debtor_routing_number="xxxxxxxxx",
            remittance_information="x",
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )


class TestAsyncRealTimePaymentsTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_complete(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.complete(
            "string",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.complete(
            "string",
            rejection={"reject_reason_code": "account_closed"},
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=1,
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    async def test_method_create_inbound_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="string",
            amount=1,
            request_for_payment_id="string",
            debtor_name="x",
            debtor_account_number="x",
            debtor_routing_number="xxxxxxxxx",
            remittance_information="x",
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )
