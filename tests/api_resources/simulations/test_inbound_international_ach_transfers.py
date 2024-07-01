# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import InboundInternationalACHTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundInternationalACHTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_international_ach_transfer = client.simulations.inbound_international_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        )
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_international_ach_transfer = client.simulations.inbound_international_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
            originator_company_entry_description="x",
            originator_name="x",
            receiving_company_or_individual_name="x",
        )
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_international_ach_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_international_ach_transfer = response.parse()
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_international_ach_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_international_ach_transfer = response.parse()
            assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundInternationalACHTransfers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_international_ach_transfer = await async_client.simulations.inbound_international_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        )
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_international_ach_transfer = await async_client.simulations.inbound_international_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
            originator_company_entry_description="x",
            originator_name="x",
            receiving_company_or_individual_name="x",
        )
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_international_ach_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_international_ach_transfer = response.parse()
        assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_international_ach_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            foreign_payment_amount=10650,
            originating_currency_code="NOK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_international_ach_transfer = await response.parse()
            assert_matches_type(InboundInternationalACHTransfer, inbound_international_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
