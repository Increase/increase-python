# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase._client import Increase, AsyncIncrease
from increase.types.simulations import (
    DigitalWalletTokenRequestCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestDigitalWalletTokenRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        digital_wallet_token_request = client.simulations.digital_wallet_token_requests.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.digital_wallet_token_requests.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token_request = response.parse()
        assert_matches_type(DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.digital_wallet_token_requests.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token_request = response.parse()
            assert_matches_type(
                DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncDigitalWalletTokenRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        digital_wallet_token_request = await client.simulations.digital_wallet_token_requests.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.simulations.digital_wallet_token_requests.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token_request = response.parse()
        assert_matches_type(DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.simulations.digital_wallet_token_requests.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token_request = await response.parse()
            assert_matches_type(
                DigitalWalletTokenRequestCreateResponse, digital_wallet_token_request, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
