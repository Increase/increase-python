# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimePaymentsTransfer
from increase._client import Increase, AsyncIncrease
from increase.types.simulations import (
    InboundRealTimePaymentsTransferSimulationResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


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
    def test_raw_response_complete(self, client: Increase) -> None:
        response = client.simulations.real_time_payments_transfers.with_raw_response.complete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Increase) -> None:
        with client.simulations.real_time_payments_transfers.with_streaming_response.complete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            debtor_account_number="x",
            debtor_name="x",
            debtor_routing_number="xxxxxxxxx",
            remittance_information="x",
            request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    def test_raw_response_create_inbound(self, client: Increase) -> None:
        response = client.simulations.real_time_payments_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    def test_streaming_response_create_inbound(self, client: Increase) -> None:
        with client.simulations.real_time_payments_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(
                InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


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
    async def test_raw_response_complete(self, client: AsyncIncrease) -> None:
        response = await client.simulations.real_time_payments_transfers.with_raw_response.complete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, client: AsyncIncrease) -> None:
        async with client.simulations.real_time_payments_transfers.with_streaming_response.complete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    async def test_method_create_inbound_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            debtor_account_number="x",
            debtor_name="x",
            debtor_routing_number="xxxxxxxxx",
            remittance_information="x",
            request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    async def test_raw_response_create_inbound(self, client: AsyncIncrease) -> None:
        response = await client.simulations.real_time_payments_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create_inbound(self, client: AsyncIncrease) -> None:
        async with client.simulations.real_time_payments_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(
                InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
