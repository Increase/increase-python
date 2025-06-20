# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntry
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookkeepingEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.retrieve(
            "bookkeeping_entry_id",
        )
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.bookkeeping_entries.with_raw_response.retrieve(
            "bookkeeping_entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = response.parse()
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.bookkeeping_entries.with_streaming_response.retrieve(
            "bookkeeping_entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = response.parse()
            assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookkeeping_entry_id` but received ''"):
            client.bookkeeping_entries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list()
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.bookkeeping_entries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = response.parse()
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.bookkeeping_entries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = response.parse()
            assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBookkeepingEntries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry = await async_client.bookkeeping_entries.retrieve(
            "bookkeeping_entry_id",
        )
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_entries.with_raw_response.retrieve(
            "bookkeeping_entry_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = await response.parse()
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_entries.with_streaming_response.retrieve(
            "bookkeeping_entry_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = await response.parse()
            assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bookkeeping_entry_id` but received ''"):
            await async_client.bookkeeping_entries.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry = await async_client.bookkeeping_entries.list()
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_entry = await async_client.bookkeeping_entries.list(
            account_id="account_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_entries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = await response.parse()
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_entries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = await response.parse()
            assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True
