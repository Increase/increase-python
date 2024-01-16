# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PendingTransaction
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPendingTransactions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        pending_transaction = client.pending_transactions.retrieve(
            "string",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.pending_transactions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.pending_transactions.with_streaming_response.retrieve(
            "string",
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
            account_id="string",
            category={"in": ["account_transfer_instruction", "ach_transfer_instruction", "card_authorization"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            route_id="string",
            source_id="string",
            status={"in": ["pending", "complete"]},
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


class TestAsyncPendingTransactions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        pending_transaction = await client.pending_transactions.retrieve(
            "string",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.pending_transactions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.pending_transactions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            await client.pending_transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        pending_transaction = await client.pending_transactions.list()
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        pending_transaction = await client.pending_transactions.list(
            account_id="string",
            category={"in": ["account_transfer_instruction", "ach_transfer_instruction", "card_authorization"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            route_id="string",
            source_id="string",
            status={"in": ["pending", "complete"]},
        )
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.pending_transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.pending_transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(AsyncPage[PendingTransaction], pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
