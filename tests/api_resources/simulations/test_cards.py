# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.types.simulations.transaction import *
from increase.types.simulations.card_authorization_simulation import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_authorize(self) -> None:
        resource = self.client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    def test_method_authorize_with_optional_params(self) -> None:
        resource = self.client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    def test_method_settlement(self) -> None:
        resource = self.client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)

    def test_method_settlement_with_optional_params(self) -> None:
        resource = self.client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)


class TestAsyncCards:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_authorize(self) -> None:
        resource = await self.client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    async def test_method_authorize_with_optional_params(self) -> None:
        resource = await self.client.simulations.cards.authorize(
            {
                "amount": 1000,
                "card_id": "card_oubs0hwk5rn6knuecxg2",
            },
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    async def test_method_settlement(self) -> None:
        resource = await self.client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)

    async def test_method_settlement_with_optional_params(self) -> None:
        resource = await self.client.simulations.cards.settlement(
            {
                "card_id": "card_oubs0hwk5rn6knuecxg2",
                "pending_transaction_id": "pending_transaction_k1sfetcau2qbvjbzgju4",
            },
        )
        assert isinstance(resource, Transaction)
