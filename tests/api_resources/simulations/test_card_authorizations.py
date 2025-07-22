# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import CardAuthorizationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardAuthorizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_authorization = client.simulations.card_authorizations.create(
            amount=1000,
        )
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_authorization = client.simulations.card_authorizations.create(
            amount=1000,
            authenticated_card_payment_id="authenticated_card_payment_id",
            card_id="card_oubs0hwk5rn6knuecxg2",
            decline_reason="account_closed",
            digital_wallet_token_id="digital_wallet_token_id",
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_city="New York",
            merchant_country="US",
            merchant_descriptor="AMAZON.COM",
            merchant_state="NY",
            network_details={"visa": {"stand_in_processing_reason": "issuer_error"}},
            network_risk_score=0,
            physical_card_id="physical_card_id",
            processing_category={"category": "account_funding"},
            terminal_id="x",
        )
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_authorizations.with_raw_response.create(
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization = response.parse()
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_authorizations.with_streaming_response.create(
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization = response.parse()
            assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardAuthorizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_authorization = await async_client.simulations.card_authorizations.create(
            amount=1000,
        )
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_authorization = await async_client.simulations.card_authorizations.create(
            amount=1000,
            authenticated_card_payment_id="authenticated_card_payment_id",
            card_id="card_oubs0hwk5rn6knuecxg2",
            decline_reason="account_closed",
            digital_wallet_token_id="digital_wallet_token_id",
            event_subscription_id="event_subscription_001dzz0r20rcdxgb013zqb8m04g",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_city="New York",
            merchant_country="US",
            merchant_descriptor="AMAZON.COM",
            merchant_state="NY",
            network_details={"visa": {"stand_in_processing_reason": "issuer_error"}},
            network_risk_score=0,
            physical_card_id="physical_card_id",
            processing_category={"category": "account_funding"},
            terminal_id="x",
        )
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_authorizations.with_raw_response.create(
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization = await response.parse()
        assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_authorizations.with_streaming_response.create(
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization = await response.parse()
            assert_matches_type(CardAuthorizationCreateResponse, card_authorization, path=["response"])

        assert cast(Any, response.is_closed) is True
