# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Transaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardSettlements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_settlement = client.simulations.card_settlements.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_settlement = client.simulations.card_settlements.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
            amount=1,
        )
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_settlements.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_settlement = response.parse()
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_settlements.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_settlement = response.parse()
            assert_matches_type(Transaction, card_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardSettlements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_settlement = await async_client.simulations.card_settlements.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_settlement = await async_client.simulations.card_settlements.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
            amount=1,
        )
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_settlements.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_settlement = await response.parse()
        assert_matches_type(Transaction, card_settlement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_settlements.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_settlement = await response.parse()
            assert_matches_type(Transaction, card_settlement, path=["response"])

        assert cast(Any, response.is_closed) is True
