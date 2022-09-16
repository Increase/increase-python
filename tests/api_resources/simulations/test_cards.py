# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.simulations.transaction import Transaction
from increase.types.simulations.card_authorization_simulation import (
    CardAuthorizationSimulation,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_authorize(self, client: Increase) -> None:
        resource = client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    def test_method_authorize_with_optional_params(self, client: Increase) -> None:
        resource = client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    def test_method_settlement(self, client: Increase) -> None:
        resource = client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)

    @parametrize
    def test_method_settlement_with_optional_params(self, client: Increase) -> None:
        resource = client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
                "amount": 0,
            },
        )
        assert isinstance(resource, Transaction)


class TestAsyncCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_authorize(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    async def test_method_authorize_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    async def test_method_settlement(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)

    @parametrize
    async def test_method_settlement_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
                "amount": 0,
            },
        )
        assert isinstance(resource, Transaction)
