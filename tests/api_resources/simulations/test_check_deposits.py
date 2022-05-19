# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.simulations.check_deposit import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckDeposits:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    def test_method_reject(self) -> None:
        resource = self.client.simulations.check_deposits.reject(
            "string",
        )
        assert isinstance(resource, CheckDeposit)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    def test_method_submit(self) -> None:
        resource = self.client.simulations.check_deposits.submit(
            "string",
        )
        assert isinstance(resource, CheckDeposit)


class TestAsyncCheckDeposits:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    async def test_method_reject(self) -> None:
        resource = await self.client.simulations.check_deposits.reject(
            "string",
        )
        assert isinstance(resource, CheckDeposit)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    async def test_method_submit(self) -> None:
        resource = await self.client.simulations.check_deposits.submit(
            "string",
        )
        assert isinstance(resource, CheckDeposit)
