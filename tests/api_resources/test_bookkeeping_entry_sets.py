# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntrySet
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookkeepingEntrySets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.bookkeeping_entry_sets.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = response.parse()
            assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.retrieve(
            "bookkeeping_entry_set_id",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.bookkeeping_entry_sets.with_raw_response.retrieve(
            "bookkeeping_entry_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.bookkeeping_entry_sets.with_streaming_response.retrieve(
            "bookkeeping_entry_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = response.parse()
            assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_entry_set_id` but received ''"
        ):
            client.bookkeeping_entry_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.list()
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry_set = client.bookkeeping_entry_sets.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            transaction_id="transaction_id",
        )
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.bookkeeping_entry_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = response.parse()
        assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.bookkeeping_entry_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = response.parse()
            assert_matches_type(SyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBookkeepingEntrySets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await async_client.bookkeeping_entry_sets.create(
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
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await async_client.bookkeeping_entry_sets.create(
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
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_entry_sets.with_raw_response.create(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = await response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_entry_sets.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = await response.parse()
            assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await async_client.bookkeeping_entry_sets.retrieve(
            "bookkeeping_entry_set_id",
        )
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_entry_sets.with_raw_response.retrieve(
            "bookkeeping_entry_set_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = await response.parse()
        assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_entry_sets.with_streaming_response.retrieve(
            "bookkeeping_entry_set_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = await response.parse()
            assert_matches_type(BookkeepingEntrySet, bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_entry_set_id` but received ''"
        ):
            await async_client.bookkeeping_entry_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await async_client.bookkeeping_entry_sets.list()
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry_set = await async_client.bookkeeping_entry_sets.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            transaction_id="transaction_id",
        )
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_entry_sets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry_set = await response.parse()
        assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_entry_sets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry_set = await response.parse()
            assert_matches_type(AsyncPage[BookkeepingEntrySet], bookkeeping_entry_set, path=["response"])

        assert cast(Any, response.is_closed) is True
