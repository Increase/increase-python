# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimeDecision

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealTimeDecisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.retrieve(
            "real_time_decision_id",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.real_time_decisions.with_raw_response.retrieve(
            "real_time_decision_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_decision = response.parse()
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.real_time_decisions.with_streaming_response.retrieve(
            "real_time_decision_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_decision = response.parse()
            assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `real_time_decision_id` but received ''"):
            client.real_time_decisions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
            card_authentication={"decision": "approve"},
            card_authentication_challenge={"result": "success"},
            card_authorization={
                "decision": "approve",
                "decline_reason": "insufficient_funds",
            },
            digital_wallet_authentication={
                "result": "success",
                "success": {
                    "email": "x",
                    "phone": "x",
                },
            },
            digital_wallet_token={
                "approval": {
                    "email": "x",
                    "phone": "x",
                },
                "decline": {"reason": "x"},
            },
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_raw_response_action(self, client: Increase) -> None:
        response = client.real_time_decisions.with_raw_response.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_decision = response.parse()
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_streaming_response_action(self, client: Increase) -> None:
        with client.real_time_decisions.with_streaming_response.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_decision = response.parse()
            assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `real_time_decision_id` but received ''"):
            client.real_time_decisions.with_raw_response.action(
                real_time_decision_id="",
            )


class TestAsyncRealTimeDecisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        real_time_decision = await async_client.real_time_decisions.retrieve(
            "real_time_decision_id",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_decisions.with_raw_response.retrieve(
            "real_time_decision_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_decision = await response.parse()
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_decisions.with_streaming_response.retrieve(
            "real_time_decision_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_decision = await response.parse()
            assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `real_time_decision_id` but received ''"):
            await async_client.real_time_decisions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_action(self, async_client: AsyncIncrease) -> None:
        real_time_decision = await async_client.real_time_decisions.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_decision = await async_client.real_time_decisions.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
            card_authentication={"decision": "approve"},
            card_authentication_challenge={"result": "success"},
            card_authorization={
                "decision": "approve",
                "decline_reason": "insufficient_funds",
            },
            digital_wallet_authentication={
                "result": "success",
                "success": {
                    "email": "x",
                    "phone": "x",
                },
            },
            digital_wallet_token={
                "approval": {
                    "email": "x",
                    "phone": "x",
                },
                "decline": {"reason": "x"},
            },
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_raw_response_action(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_decisions.with_raw_response.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_decision = await response.parse()
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_streaming_response_action(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_decisions.with_streaming_response.action(
            real_time_decision_id="real_time_decision_j76n2e810ezcg3zh5qtn",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_decision = await response.parse()
            assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `real_time_decision_id` but received ''"):
            await async_client.real_time_decisions.with_raw_response.action(
                real_time_decision_id="",
            )
