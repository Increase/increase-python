# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.real_time_decision import RealTimeDecision

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRealTimeDecisions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.real_time_decisions.retrieve(
            "string",
        )
        assert isinstance(resource, RealTimeDecision)

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        resource = client.real_time_decisions.action(
            "string",
        )
        assert isinstance(resource, RealTimeDecision)

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        resource = client.real_time_decisions.action(
            "string",
            card_authorization={"decision": "approve"},
            digital_wallet_token={
                "approval": {
                    "card_profile_id": "string",
                    "phone": "x",
                    "email": "x",
                },
                "decline": {"reason": "x"},
            },
            digital_wallet_authentication={"result": "success"},
        )
        assert isinstance(resource, RealTimeDecision)


class TestAsyncRealTimeDecisions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.real_time_decisions.retrieve(
            "string",
        )
        assert isinstance(resource, RealTimeDecision)

    @parametrize
    async def test_method_action(self, client: AsyncIncrease) -> None:
        resource = await client.real_time_decisions.action(
            "string",
        )
        assert isinstance(resource, RealTimeDecision)

    @parametrize
    async def test_method_action_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.real_time_decisions.action(
            "string",
            card_authorization={"decision": "approve"},
            digital_wallet_token={
                "approval": {
                    "card_profile_id": "string",
                    "phone": "x",
                    "email": "x",
                },
                "decline": {"reason": "x"},
            },
            digital_wallet_authentication={"result": "success"},
        )
        assert isinstance(resource, RealTimeDecision)
