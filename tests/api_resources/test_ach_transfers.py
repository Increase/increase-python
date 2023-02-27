# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHTransfer
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestACHTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.create(
            account_id="string",
            amount=0,
            statement_descriptor="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.create(
            account_id="string",
            account_number="x",
            addendum="x",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date="2019-12-27",
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            require_approval=True,
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
            statement_descriptor="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.list()
        assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.list(
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
        assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.approve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.cancel(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])


class TestAsyncACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.create(
            account_id="string",
            amount=0,
            statement_descriptor="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.create(
            account_id="string",
            account_number="x",
            addendum="x",
            amount=0,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date="2019-12-27",
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            require_approval=True,
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
            statement_descriptor="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.list()
        assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.list(
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
        assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.approve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_cancel(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.cancel(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])
