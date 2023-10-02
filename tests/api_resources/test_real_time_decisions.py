# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimeDecision

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRealTimeDecisions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.retrieve(
            "string",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.action(
            "string",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        real_time_decision = client.real_time_decisions.action(
            "string",
            card_authorization={"decision": "approve"},
            digital_wallet_authentication={"result": "success"},
            digital_wallet_token={
                "approval": {
                    "card_profile_id": "string",
                    "phone": "x",
                    "email": "x",
                },
                "decline": {"reason": "x"},
            },
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])


class TestAsyncRealTimeDecisions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        real_time_decision = await client.real_time_decisions.retrieve(
            "string",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_method_action(self, client: AsyncIncrease) -> None:
        real_time_decision = await client.real_time_decisions.action(
            "string",
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])

    @parametrize
    async def test_method_action_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_decision = await client.real_time_decisions.action(
            "string",
            card_authorization={"decision": "approve"},
            digital_wallet_authentication={"result": "success"},
            digital_wallet_token={
                "approval": {
                    "card_profile_id": "string",
                    "phone": "x",
                    "email": "x",
                },
                "decline": {"reason": "x"},
            },
        )
        assert_matches_type(RealTimeDecision, real_time_decision, path=["response"])
