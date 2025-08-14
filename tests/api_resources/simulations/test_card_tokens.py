# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardToken
from increase._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_token = client.simulations.card_tokens.create()
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_token = client.simulations.card_tokens.create(
            capabilities=[
                {
                    "cross_border_push_transfers": "supported",
                    "domestic_push_transfers": "supported",
                    "route": "visa",
                }
            ],
            expiration=parse_date("2019-12-27"),
            last4="1234",
            prefix="41234567",
            primary_account_number_length=16,
        )
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_token = response.parse()
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_tokens.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_token = response.parse()
            assert_matches_type(CardToken, card_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_token = await async_client.simulations.card_tokens.create()
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_token = await async_client.simulations.card_tokens.create(
            capabilities=[
                {
                    "cross_border_push_transfers": "supported",
                    "domestic_push_transfers": "supported",
                    "route": "visa",
                }
            ],
            expiration=parse_date("2019-12-27"),
            last4="1234",
            prefix="41234567",
            primary_account_number_length=16,
        )
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_token = await response.parse()
        assert_matches_type(CardToken, card_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_tokens.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_token = await response.parse()
            assert_matches_type(CardToken, card_token, path=["response"])

        assert cast(Any, response.is_closed) is True
