# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types.simulations import InboundFundsHoldReleaseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundFundsHolds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_release(self, client: Increase) -> None:
        inbound_funds_hold = client.simulations.inbound_funds_holds.release(
            "inbound_funds_hold_id",
        )
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

    @parametrize
    def test_raw_response_release(self, client: Increase) -> None:
        response = client.simulations.inbound_funds_holds.with_raw_response.release(
            "inbound_funds_hold_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_funds_hold = response.parse()
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

    @parametrize
    def test_streaming_response_release(self, client: Increase) -> None:
        with client.simulations.inbound_funds_holds.with_streaming_response.release(
            "inbound_funds_hold_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_funds_hold = response.parse()
            assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_funds_hold_id` but received ''"):
            client.simulations.inbound_funds_holds.with_raw_response.release(
                "",
            )


class TestAsyncInboundFundsHolds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_release(self, async_client: AsyncIncrease) -> None:
        inbound_funds_hold = await async_client.simulations.inbound_funds_holds.release(
            "inbound_funds_hold_id",
        )
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

    @parametrize
    async def test_raw_response_release(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_funds_holds.with_raw_response.release(
            "inbound_funds_hold_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_funds_hold = await response.parse()
        assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_funds_holds.with_streaming_response.release(
            "inbound_funds_hold_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_funds_hold = await response.parse()
            assert_matches_type(InboundFundsHoldReleaseResponse, inbound_funds_hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_funds_hold_id` but received ''"):
            await async_client.simulations.inbound_funds_holds.with_raw_response.release(
                "",
            )
