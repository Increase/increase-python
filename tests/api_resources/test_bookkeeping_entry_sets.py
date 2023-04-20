# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntrySet
from increase._utils import parse_datetime

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBookkeepingEntrySets:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.create(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            transaction_id="string",
            entries=[
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])


class TestAsyncBookkeepingEntrySets:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.create(
            entries=[
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await client.bookkeeping_entry_sets.create(
            date=parse_datetime("2019-12-27T18:11:19.117Z"),
            transaction_id="string",
            entries=[
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
                {
                    "account_id": "string",
                    "amount": 0,
                },
            ],
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])
