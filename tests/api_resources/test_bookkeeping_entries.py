# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntry
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestBookkeepingEntries:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.retrieve(
            "string",
        )
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.bookkeeping_entries.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = response.parse()
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.bookkeeping_entries.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = response.parse()
            assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list()
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list(
            cursor="string",
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
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        bookkeeping_entry = await client.bookkeeping_entries.retrieve(
            "string",
        )
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.bookkeeping_entries.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = response.parse()
        assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.bookkeeping_entries.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = await response.parse()
            assert_matches_type(BookkeepingEntry, bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        bookkeeping_entry = await client.bookkeeping_entries.list()
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_entry = await client.bookkeeping_entries.list(
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.bookkeeping_entries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_entry = response.parse()
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.bookkeeping_entries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_entry = await response.parse()
            assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

        assert cast(Any, response.is_closed) is True
