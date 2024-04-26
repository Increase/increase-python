# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimePaymentsTransfer
from increase.types.simulations import (
    InboundRealTimePaymentsTransferSimulationResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealTimePaymentsTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
    def test_path_params_complete(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            client.simulations.real_time_payments_transfers.with_raw_response.complete(
                "",
            )

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_complete(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.simulations.real_time_payments_transfers.complete(
            "string",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.simulations.real_time_payments_transfers.complete(
            "string",
            rejection={"reject_reason_code": "account_closed"},
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.real_time_payments_transfers.with_raw_response.complete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.real_time_payments_transfers.with_streaming_response.complete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            await async_client.simulations.real_time_payments_transfers.with_raw_response.complete(
                "",
            )

    @parametrize
    async def test_method_create_inbound(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.simulations.real_time_payments_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(
            InboundRealTimePaymentsTransferSimulationResult, real_time_payments_transfer, path=["response"]
        )

    @parametrize
    async def test_method_create_inbound_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.simulations.real_time_payments_transfers.create_inbound(
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
    async def test_raw_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.real_time_payments_transfers.with_raw_response.create_inbound(
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
    async def test_streaming_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.real_time_payments_transfers.with_streaming_response.create_inbound(
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
