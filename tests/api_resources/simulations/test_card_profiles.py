# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardProfile
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCardProfiles:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        card_profile = client.simulations.card_profiles.approve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.simulations.card_profiles.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.simulations.card_profiles.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardProfiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        card_profile = await client.simulations.card_profiles.approve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, client: AsyncIncrease) -> None:
        response = await client.simulations.card_profiles.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, client: AsyncIncrease) -> None:
        async with client.simulations.card_profiles.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
