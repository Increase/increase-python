# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import Transaction
from increase.types.simulations import CardAuthorizationSimulation

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_authorize(self, client: Increase) -> None:
        resource = client.simulations.cards.authorize(
            amount=0,
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    def test_method_authorize_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.cards.authorize(
            amount=0,
            card_id="string",
            digital_wallet_token_id="string",
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    def test_method_settlement(self, client: Increase) -> None:
        resource = client.simulations.cards.settlement(
            card_id="string",
            pending_transaction_id="string",
        )
        assert isinstance(resource, Transaction)

    @parametrize
    def test_method_settlement_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.cards.settlement(
            card_id="string",
            pending_transaction_id="string",
            amount=0,
        )
        assert isinstance(resource, Transaction)


class TestAsyncCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_authorize(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.authorize(
            amount=0,
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    async def test_method_authorize_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.authorize(
            amount=0,
            card_id="string",
            digital_wallet_token_id="string",
        )
        assert isinstance(resource, CardAuthorizationSimulation)

    @parametrize
    async def test_method_settlement(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.settlement(
            card_id="string",
            pending_transaction_id="string",
        )
        assert isinstance(resource, Transaction)

    @parametrize
    async def test_method_settlement_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.cards.settlement(
            card_id="string",
            pending_transaction_id="string",
            amount=0,
        )
        assert isinstance(resource, Transaction)
