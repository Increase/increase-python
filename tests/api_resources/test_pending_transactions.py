# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PendingTransaction
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPendingTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
            description="Hold for pending transaction",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.pending_transactions.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.pending_transactions.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.retrieve(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.pending_transactions.with_raw_response.retrieve(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.pending_transactions.with_streaming_response.retrieve(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            client.pending_transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.list()
        assert_matches_type(SyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.list(
            account_id="account_id",
            category={"in": ["account_transfer_instruction"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
            route_id="route_id",
            status={"in": ["pending"]},
        )
        assert_matches_type(SyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.pending_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(SyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.pending_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = response.parse()
            assert_matches_type(SyncPage[PendingTransaction], pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_release(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.release(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_release(self, client: Increase) -> None:
        response = client.pending_transactions.with_raw_response.release(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_release(self, client: Increase) -> None:
        with client.pending_transactions.with_streaming_response.release(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            client.pending_transactions.with_raw_response.release(
                "",
            )


class TestAsyncPendingTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
            description="Hold for pending transaction",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.pending_transactions.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = await response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.pending_transactions.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=-1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.retrieve(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.pending_transactions.with_raw_response.retrieve(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = await response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.pending_transactions.with_streaming_response.retrieve(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            await async_client.pending_transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.list()
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.list(
            account_id="account_id",
            category={"in": ["account_transfer_instruction"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
            route_id="route_id",
            status={"in": ["pending"]},
        )
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.pending_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = await response.parse()
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.pending_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_release(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.pending_transactions.release(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_release(self, async_client: AsyncIncrease) -> None:
        response = await async_client.pending_transactions.with_raw_response.release(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = await response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncIncrease) -> None:
        async with async_client.pending_transactions.with_streaming_response.release(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            await async_client.pending_transactions.with_raw_response.release(
                "",
            )
