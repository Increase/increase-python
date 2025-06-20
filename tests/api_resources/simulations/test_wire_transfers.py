# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import WireTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_reverse(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.reverse(
            "wire_transfer_id",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_reverse(self, client: Increase) -> None:
        response = client.simulations.wire_transfers.with_raw_response.reverse(
            "wire_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_streaming_response_reverse(self, client: Increase) -> None:
        with client.simulations.wire_transfers.with_streaming_response.reverse(
            "wire_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = response.parse()
            assert_matches_type(WireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reverse(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wire_transfer_id` but received ''"):
            client.simulations.wire_transfers.with_raw_response.reverse(
                "",
            )

    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.submit(
            "wire_transfer_id",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.wire_transfers.with_raw_response.submit(
            "wire_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.wire_transfers.with_streaming_response.submit(
            "wire_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = response.parse()
            assert_matches_type(WireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wire_transfer_id` but received ''"):
            client.simulations.wire_transfers.with_raw_response.submit(
                "",
            )


class TestAsyncWireTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_reverse(self, async_client: AsyncIncrease) -> None:
        wire_transfer = await async_client.simulations.wire_transfers.reverse(
            "wire_transfer_id",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_reverse(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.wire_transfers.with_raw_response.reverse(
            "wire_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = await response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_reverse(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.wire_transfers.with_streaming_response.reverse(
            "wire_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = await response.parse()
            assert_matches_type(WireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reverse(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wire_transfer_id` but received ''"):
            await async_client.simulations.wire_transfers.with_raw_response.reverse(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        wire_transfer = await async_client.simulations.wire_transfers.submit(
            "wire_transfer_id",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.wire_transfers.with_raw_response.submit(
            "wire_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = await response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.wire_transfers.with_streaming_response.submit(
            "wire_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = await response.parse()
            assert_matches_type(WireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wire_transfer_id` but received ''"):
            await async_client.simulations.wire_transfers.with_raw_response.submit(
                "",
            )
