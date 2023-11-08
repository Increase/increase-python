# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntrySet
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestBookkeepingEntrySets:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
            date=parse_datetime("2020-01-31T23:59:59Z"),
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.bookkeeping_entry_sets.with_raw_response.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.retrieve(
            "string",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.bookkeeping_entry_sets.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.list()
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.list(
            cursor="string",
            limit=1,
            transaction_id="string",
        )
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.bookkeeping_entry_sets.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])


class TestAsyncBookkeepingEntrySets:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
            date=parse_datetime("2020-01-31T23:59:59Z"),
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.bookkeeping_entry_sets.with_raw_response.create(
            entries=[
                {
                    "account_id": "bookkeeping_account_9husfpw68pzmve9dvvc7",
                    "amount": 100,
                },
                {
                    "account_id": "bookkeeping_account_t2obldz1rcu15zr54umg",
                    "amount": -100,
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.retrieve(
            "string",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.bookkeeping_entry_sets.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.list()
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.list(
            cursor="string",
            limit=1,
            transaction_id="string",
        )
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.bookkeeping_entry_sets.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])
