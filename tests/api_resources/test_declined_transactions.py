# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import DeclinedTransaction
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestDeclinedTransactions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        declined_transaction = client.declined_transactions.retrieve(
            "string",
        )
        assert_matches_type(DeclinedTransaction, declined_transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        declined_transaction = client.declined_transactions.list()
        assert_matches_type(SyncPage[DeclinedTransaction], declined_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        declined_transaction = client.declined_transactions.list(
            account_id="string",
            category={"in": ["ach_decline", "card_decline", "check_decline"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
            route_id="string",
        )
        assert_matches_type(SyncPage[DeclinedTransaction], declined_transaction, path=["response"])


class TestAsyncDeclinedTransactions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        declined_transaction = await client.declined_transactions.retrieve(
            "string",
        )
        assert_matches_type(DeclinedTransaction, declined_transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        declined_transaction = await client.declined_transactions.list()
        assert_matches_type(AsyncPage[DeclinedTransaction], declined_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        declined_transaction = await client.declined_transactions.list(
            account_id="string",
            category={"in": ["ach_decline", "card_decline", "check_decline"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
            route_id="string",
        )
        assert_matches_type(AsyncPage[DeclinedTransaction], declined_transaction, path=["response"])
