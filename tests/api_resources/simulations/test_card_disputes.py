# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardDispute

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCardDisputes:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        card_dispute = client.simulations.card_disputes.action(
            "string",
            status="rejected",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        card_dispute = client.simulations.card_disputes.action(
            "string",
            status="rejected",
            explanation="This was a valid recurring transaction",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])


class TestAsyncCardDisputes:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_action(self, client: AsyncIncrease) -> None:
        card_dispute = await client.simulations.card_disputes.action(
            "string",
            status="rejected",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, client: AsyncIncrease) -> None:
        card_dispute = await client.simulations.card_disputes.action(
            "string",
            status="rejected",
            explanation="This was a valid recurring transaction",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])
