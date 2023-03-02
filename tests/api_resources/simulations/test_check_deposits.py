# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckDeposit

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckDeposits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_reject(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.reject(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_method_return(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.return_(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.submit(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])


class TestAsyncCheckDeposits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_reject(self, client: AsyncIncrease) -> None:
        check_deposit = await client.simulations.check_deposits.reject(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_method_return(self, client: AsyncIncrease) -> None:
        check_deposit = await client.simulations.check_deposits.return_(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_submit(self, client: AsyncIncrease) -> None:
        check_deposit = await client.simulations.check_deposits.submit(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])
