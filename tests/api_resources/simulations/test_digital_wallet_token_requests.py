# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import DigitalWalletTokenRequestCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


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
