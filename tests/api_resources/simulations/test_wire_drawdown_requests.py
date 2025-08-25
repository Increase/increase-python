# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import WireDrawdownRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireDrawdownRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_refuse(self, client: Increase) -> None:
        wire_drawdown_request = client.simulations.wire_drawdown_requests.refuse(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_refuse(self, client: Increase) -> None:
        response = client.simulations.wire_drawdown_requests.with_raw_response.refuse(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_refuse(self, client: Increase) -> None:
        with client.simulations.wire_drawdown_requests.with_streaming_response.refuse(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refuse(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            client.simulations.wire_drawdown_requests.with_raw_response.refuse(
                "",
            )

    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        wire_drawdown_request = client.simulations.wire_drawdown_requests.submit(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.wire_drawdown_requests.with_raw_response.submit(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.wire_drawdown_requests.with_streaming_response.submit(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            client.simulations.wire_drawdown_requests.with_raw_response.submit(
                "",
            )


class TestAsyncWireDrawdownRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_refuse(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.simulations.wire_drawdown_requests.refuse(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_refuse(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.wire_drawdown_requests.with_raw_response.refuse(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = await response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_refuse(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.wire_drawdown_requests.with_streaming_response.refuse(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = await response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refuse(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            await async_client.simulations.wire_drawdown_requests.with_raw_response.refuse(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.simulations.wire_drawdown_requests.submit(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.wire_drawdown_requests.with_raw_response.submit(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = await response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.wire_drawdown_requests.with_streaming_response.submit(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = await response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            await async_client.simulations.wire_drawdown_requests.with_raw_response.submit(
                "",
            )
