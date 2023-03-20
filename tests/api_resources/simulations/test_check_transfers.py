# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckTransfer

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_deposit(self, client: Increase) -> None:
        check_transfer = client.simulations.check_transfers.deposit(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_mail(self, client: Increase) -> None:
        check_transfer = client.simulations.check_transfers.mail(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_method_return(self, client: Increase) -> None:
        check_transfer = client.simulations.check_transfers.return_(
            "string",
            reason="mail_delivery_failure",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])


class TestAsyncCheckTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_deposit(self, client: AsyncIncrease) -> None:
        check_transfer = await client.simulations.check_transfers.deposit(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_mail(self, client: AsyncIncrease) -> None:
        check_transfer = await client.simulations.check_transfers.mail(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_method_return(self, client: AsyncIncrease) -> None:
        check_transfer = await client.simulations.check_transfers.return_(
            "string",
            reason="mail_delivery_failure",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])
