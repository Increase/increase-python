# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PendingTransaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPendingTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_release_inbound_funds_hold(self, client: Increase) -> None:
        pending_transaction = client.simulations.pending_transactions.release_inbound_funds_hold(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_raw_response_release_inbound_funds_hold(self, client: Increase) -> None:
        response = client.simulations.pending_transactions.with_raw_response.release_inbound_funds_hold(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    def test_streaming_response_release_inbound_funds_hold(self, client: Increase) -> None:
        with client.simulations.pending_transactions.with_streaming_response.release_inbound_funds_hold(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release_inbound_funds_hold(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            client.simulations.pending_transactions.with_raw_response.release_inbound_funds_hold(
                "",
            )


class TestAsyncPendingTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_release_inbound_funds_hold(self, async_client: AsyncIncrease) -> None:
        pending_transaction = await async_client.simulations.pending_transactions.release_inbound_funds_hold(
            "pending_transaction_id",
        )
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_raw_response_release_inbound_funds_hold(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.pending_transactions.with_raw_response.release_inbound_funds_hold(
            "pending_transaction_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pending_transaction = await response.parse()
        assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_release_inbound_funds_hold(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.pending_transactions.with_streaming_response.release_inbound_funds_hold(
            "pending_transaction_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pending_transaction = await response.parse()
            assert_matches_type(PendingTransaction, pending_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release_inbound_funds_hold(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `pending_transaction_id` but received ''"
        ):
            await async_client.simulations.pending_transactions.with_raw_response.release_inbound_funds_hold(
                "",
            )
