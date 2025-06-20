# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundACHTransfer
from increase._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundACHTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_ach_transfer = client.simulations.inbound_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer = client.simulations.inbound_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            addenda={
                "category": "freeform",
                "freeform": {"entries": [{"payment_related_information": "x"}]},
            },
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_id="x",
            company_name="x",
            receiver_id_number="x",
            receiver_name="x",
            resolve_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_ach_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_ach_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundACHTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.simulations.inbound_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.simulations.inbound_ach_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            addenda={
                "category": "freeform",
                "freeform": {"entries": [{"payment_related_information": "x"}]},
            },
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_id="x",
            company_name="x",
            receiver_id_number="x",
            receiver_name="x",
            resolve_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_ach_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = await response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_ach_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
