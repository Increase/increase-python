# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardPayment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardAuthorizationExpirations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_authorization_expiration = client.simulations.card_authorization_expirations.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_authorization_expirations.with_raw_response.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization_expiration = response.parse()
        assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_authorization_expirations.with_streaming_response.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization_expiration = response.parse()
            assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardAuthorizationExpirations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_authorization_expiration = await async_client.simulations.card_authorization_expirations.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_authorization_expirations.with_raw_response.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization_expiration = await response.parse()
        assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_authorization_expirations.with_streaming_response.create(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization_expiration = await response.parse()
            assert_matches_type(CardPayment, card_authorization_expiration, path=["response"])

        assert cast(Any, response.is_closed) is True
