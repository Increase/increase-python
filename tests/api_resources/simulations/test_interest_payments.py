# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase._utils import parse_datetime
from increase.types.simulations import InterestPaymentSimulationResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestInterestPayments:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        interest_payment = client.simulations.interest_payments.create(
            account_id="string",
            amount=1,
        )
        assert_matches_type(InterestPaymentSimulationResult, interest_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        interest_payment = client.simulations.interest_payments.create(
            account_id="string",
            amount=1,
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(InterestPaymentSimulationResult, interest_payment, path=["response"])


class TestAsyncInterestPayments:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        interest_payment = await client.simulations.interest_payments.create(
            account_id="string",
            amount=1,
        )
        assert_matches_type(InterestPaymentSimulationResult, interest_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        interest_payment = await client.simulations.interest_payments.create(
            account_id="string",
            amount=1,
            period_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            period_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(InterestPaymentSimulationResult, interest_payment, path=["response"])
