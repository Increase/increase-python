# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import ACHTransfer
from increase.types.simulations import ACHTransferSimulation

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestACHTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.create_inbound(
            account_number_id="string",
            amount=0,
        )
        assert isinstance(resource, ACHTransferSimulation)

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.create_inbound(
            account_number_id="string",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            company_id="x",
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_return(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTransfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_return_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.return_(
            "string",
            reason="insufficient_fund",
        )
        assert isinstance(resource, ACHTransfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        resource = client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTransfer)


class TestAsyncACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_inbound(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.create_inbound(
            account_number_id="string",
            amount=0,
        )
        assert isinstance(resource, ACHTransferSimulation)

    @parametrize
    async def test_method_create_inbound_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.create_inbound(
            account_number_id="string",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            company_id="x",
        )
        assert isinstance(resource, ACHTransferSimulation)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_return(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.return_(
            "string",
        )
        assert isinstance(resource, ACHTransfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_return_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.return_(
            "string",
            reason="insufficient_fund",
        )
        assert isinstance(resource, ACHTransfer)

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_submit(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.ach_transfers.submit(
            "string",
        )
        assert isinstance(resource, ACHTransfer)
