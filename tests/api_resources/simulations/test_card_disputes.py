# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardDispute

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        card_dispute = client.simulations.card_disputes.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        card_dispute = client.simulations.card_disputes.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
            explanation="This was a valid recurring transaction",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_action(self, client: Increase) -> None:
        response = client.simulations.card_disputes.with_raw_response.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_action(self, client: Increase) -> None:
        with client.simulations.card_disputes.with_streaming_response.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            client.simulations.card_disputes.with_raw_response.action(
                card_dispute_id="",
                status="rejected",
            )


class TestAsyncCardDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_action(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.simulations.card_disputes.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.simulations.card_disputes.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
            explanation="This was a valid recurring transaction",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_action(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_disputes.with_raw_response.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_action(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_disputes.with_streaming_response.action(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            status="rejected",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await async_client.simulations.card_disputes.with_raw_response.action(
                card_dispute_id="",
                status="rejected",
            )
