# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import InboundFundsHoldReleaseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInboundFundsHolds:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_release(self, client: Increase) -> None:
        inbound_funds_hold = client.simulations.inbound_funds_holds.release(
            "string",
        )
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])


class TestAsyncInboundFundsHolds:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_release(self, client: AsyncIncrease) -> None:
        inbound_funds_hold = await client.simulations.inbound_funds_holds.release(
            "string",
        )
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])
