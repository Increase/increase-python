# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Transaction
from increase.types.simulations import CardAuthorizationSimulation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_authorize(self, client: Increase) -> None:
        card = client.simulations.cards.authorize(
            amount=1000,
        )
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    def test_method_authorize_with_all_params(self, client: Increase) -> None:
        card = client.simulations.cards.authorize(
            amount=1000,
            card_id="card_oubs0hwk5rn6knuecxg2",
            digital_wallet_token_id="string",
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_city="New York",
            merchant_country="US",
            merchant_descriptor="AMAZON.COM",
            physical_card_id="string",
        )
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: Increase) -> None:
        response = client.simulations.cards.with_raw_response.authorize(
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: Increase) -> None:
        with client.simulations.cards.with_streaming_response.authorize(
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_settlement(self, client: Increase) -> None:
        card = client.simulations.cards.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    def test_method_settlement_with_all_params(self, client: Increase) -> None:
        card = client.simulations.cards.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
            amount=1,
        )
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    def test_raw_response_settlement(self, client: Increase) -> None:
        response = client.simulations.cards.with_raw_response.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    def test_streaming_response_settlement(self, client: Increase) -> None:
        with client.simulations.cards.with_streaming_response.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Transaction, card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_authorize(self, async_client: AsyncIncrease) -> None:
        card = await async_client.simulations.cards.authorize(
            amount=1000,
        )
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.simulations.cards.authorize(
            amount=1000,
            card_id="card_oubs0hwk5rn6knuecxg2",
            digital_wallet_token_id="string",
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_city="New York",
            merchant_country="US",
            merchant_descriptor="AMAZON.COM",
            physical_card_id="string",
        )
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.cards.with_raw_response.authorize(
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.cards.with_streaming_response.authorize(
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardAuthorizationSimulation, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_settlement(self, async_client: AsyncIncrease) -> None:
        card = await async_client.simulations.cards.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    async def test_method_settlement_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.simulations.cards.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
            amount=1,
        )
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    async def test_raw_response_settlement(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.cards.with_raw_response.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Transaction, card, path=["response"])

    @parametrize
    async def test_streaming_response_settlement(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.cards.with_streaming_response.settlement(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pending_transaction_id="pending_transaction_k1sfetcau2qbvjbzgju4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Transaction, card, path=["response"])

        assert cast(Any, response.is_closed) is True
