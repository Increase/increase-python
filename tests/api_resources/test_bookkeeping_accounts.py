# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingAccount
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBookkeepingAccounts:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.create(
            name="x",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.create(
            name="x",
            account_id="string",
            compliance_category="commingled_cash",
            entity_id="string",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.list()
        assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])


class TestAsyncBookkeepingAccounts:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        bookkeeping_account = await client.bookkeeping_accounts.create(
            name="x",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_account = await client.bookkeeping_accounts.create(
            name="x",
            account_id="string",
            compliance_category="commingled_cash",
            entity_id="string",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        bookkeeping_account = await client.bookkeeping_accounts.list()
        assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_account = await client.bookkeeping_accounts.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])
