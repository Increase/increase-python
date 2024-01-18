# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardProfile

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_profile_id` but received ''"):
            client.simulations.card_profiles.with_raw_response.approve(
                "",
            )


class TestAsyncCardProfiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        card_profile = await async_client.simulations.card_profiles.approve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_profiles.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_profiles.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_profile_id` but received ''"):
            await async_client.simulations.card_profiles.with_raw_response.approve(
                "",
            )
