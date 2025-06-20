# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    BookkeepingAccount,
    BookkeepingBalanceLookup,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookkeepingAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.create(
            name="New Account!",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.create(
            name="New Account!",
            account_id="account_id",
            compliance_category="commingled_cash",
            entity_id="entity_id",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.bookkeeping_accounts.with_raw_response.create(
            name="New Account!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = response.parse()
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.bookkeeping_accounts.with_streaming_response.create(
            name="New Account!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = response.parse()
            assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.bookkeeping_accounts.with_raw_response.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = response.parse()
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.bookkeeping_accounts.with_streaming_response.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = response.parse()
            assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_account_id` but received ''"
        ):
            client.bookkeeping_accounts.with_raw_response.update(
                bookkeeping_account_id="",
                name="Deprecated Account",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.list()
        assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.bookkeeping_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = response.parse()
        assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.bookkeeping_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = response.parse()
            assert_matches_type(SyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_balance(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        )
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    def test_method_balance_with_all_params(self, client: Increase) -> None:
        bookkeeping_account = client.bookkeeping_accounts.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    def test_raw_response_balance(self, client: Increase) -> None:
        response = client.bookkeeping_accounts.with_raw_response.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = response.parse()
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    def test_streaming_response_balance(self, client: Increase) -> None:
        with client.bookkeeping_accounts.with_streaming_response.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = response.parse()
            assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_balance(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_account_id` but received ''"
        ):
            client.bookkeeping_accounts.with_raw_response.balance(
                bookkeeping_account_id="",
            )


class TestAsyncBookkeepingAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.create(
            name="New Account!",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.create(
            name="New Account!",
            account_id="account_id",
            compliance_category="commingled_cash",
            entity_id="entity_id",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_accounts.with_raw_response.create(
            name="New Account!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = await response.parse()
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_accounts.with_streaming_response.create(
            name="New Account!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = await response.parse()
            assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        )
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_accounts.with_raw_response.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = await response.parse()
        assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_accounts.with_streaming_response.update(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            name="Deprecated Account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = await response.parse()
            assert_matches_type(BookkeepingAccount, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_account_id` but received ''"
        ):
            await async_client.bookkeeping_accounts.with_raw_response.update(
                bookkeeping_account_id="",
                name="Deprecated Account",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.list()
        assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = await response.parse()
        assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = await response.parse()
            assert_matches_type(AsyncPage[BookkeepingAccount], bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_balance(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        )
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    async def test_method_balance_with_all_params(self, async_client: AsyncIncrease) -> None:
        bookkeeping_account = await async_client.bookkeeping_accounts.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    async def test_raw_response_balance(self, async_client: AsyncIncrease) -> None:
        response = await async_client.bookkeeping_accounts.with_raw_response.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookkeeping_account = await response.parse()
        assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

    @parametrize
    async def test_streaming_response_balance(self, async_client: AsyncIncrease) -> None:
        async with async_client.bookkeeping_accounts.with_streaming_response.balance(
            bookkeeping_account_id="bookkeeping_account_e37p1f1iuocw5intf35v",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookkeeping_account = await response.parse()
            assert_matches_type(BookkeepingBalanceLookup, bookkeeping_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_balance(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bookkeeping_account_id` but received ''"
        ):
            await async_client.bookkeeping_accounts.with_raw_response.balance(
                bookkeeping_account_id="",
            )
