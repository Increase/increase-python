# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Transaction

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardRefunds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_refund = response.parse()
        assert_matches_type(Transaction, card_refund, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_refunds.with_streaming_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_refund = response.parse()
            assert_matches_type(Transaction, card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardRefunds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_refund = await async_client.simulations.card_refunds.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(Transaction, card_refund, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_refunds.with_raw_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_refund = await response.parse()
        assert_matches_type(Transaction, card_refund, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_refunds.with_streaming_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_refund = await response.parse()
            assert_matches_type(Transaction, card_refund, path=["response"])

        assert cast(Any, response.is_closed) is True
