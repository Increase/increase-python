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
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @parametrize
    def test_method_create_inbound_with_optional_params(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_return(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTranfer)


class TestAsyncACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @parametrize
    async def test_method_create_inbound_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.create_inbound(
            {
                "account_number_id": "account_number_v18nkfqm6afpsrvy82b2",
                "amount": 1000,
            },
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_return(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_submit(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTranfer)
