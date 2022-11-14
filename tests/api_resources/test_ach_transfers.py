# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import AsyncPage, SyncPage

from increase.types.ach_transfer import ACHTransfer

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")

class TestACHTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.ach_transfers.create(
            account_id="string",
            amount=0,
            statement_descriptor="x",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.ach_transfers.create(
            account_id="string",
            account_number="x",
            addendum="x",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date="2019-12-27T18:11:19.117Z",
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
            statement_descriptor="x",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.ach_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.ach_transfers.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.ach_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            external_account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, SyncPage)
class TestAsyncACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.ach_transfers.create(
            account_id="string",
            amount=0,
            statement_descriptor="x",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.ach_transfers.create(
            account_id="string",
            account_number="x",
            addendum="x",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date="2019-12-27T18:11:19.117Z",
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
            statement_descriptor="x",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.ach_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, ACHTransfer)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.ach_transfers.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.ach_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            external_account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, AsyncPage)