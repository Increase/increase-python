# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.simulations.ach_tranfer import *
from increase.types.simulations.ach_transfer_simulation import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestACHTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create_inbound(self) -> None:
        resource = self.client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    def test_method_create_inbound_with_optional_params(self) -> None:
        resource = self.client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    def test_method_return(self) -> None:
        resource = self.client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    def test_method_submit(self) -> None:
        resource = self.client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTranfer)


class TestAsyncACHTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create_inbound(self) -> None:
        resource = await self.client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    async def test_method_create_inbound_with_optional_params(self) -> None:
        resource = await self.client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    async def test_method_return(self) -> None:
        resource = await self.client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    async def test_method_submit(self) -> None:
        resource = await self.client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTranfer)
