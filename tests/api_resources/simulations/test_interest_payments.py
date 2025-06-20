# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Transaction
from increase._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        interest_payment = client.simulations.interest_payments.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        interest_payment = client.simulations.interest_payments.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            accrued_on_account_id="accrued_on_account_id",
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.interest_payments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_payment = response.parse()
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.interest_payments.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_payment = response.parse()
            assert_matches_type(Transaction, interest_payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInterestPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        interest_payment = await async_client.simulations.interest_payments.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        interest_payment = await async_client.simulations.interest_payments.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            accrued_on_account_id="accrued_on_account_id",
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.interest_payments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_payment = await response.parse()
        assert_matches_type(Transaction, interest_payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.interest_payments.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_payment = await response.parse()
            assert_matches_type(Transaction, interest_payment, path=["response"])

        assert cast(Any, response.is_closed) is True
