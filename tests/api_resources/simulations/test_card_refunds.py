# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Transaction
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCardRefunds:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_refund = client.simulations.card_refunds.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(Transaction, card_refund, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_refunds.with_raw_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_refund = response.parse()
        assert_matches_type(Transaction, card_refund, path=["response"])


class TestAsyncCardRefunds:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card_refund = await client.simulations.card_refunds.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(Transaction, card_refund, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.simulations.card_refunds.with_raw_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_refund = response.parse()
        assert_matches_type(Transaction, card_refund, path=["response"])
