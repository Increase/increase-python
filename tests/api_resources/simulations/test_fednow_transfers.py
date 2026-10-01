# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import FednowTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFednowTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Increase) -> None:
        fednow_transfer = client.simulations.fednow_transfers.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_method_complete_with_all_params(self, client: Increase) -> None:
        fednow_transfer = client.simulations.fednow_transfers.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
            rejection={"reject_reason_code": "account_closed"},
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Increase) -> None:
        response = client.simulations.fednow_transfers.with_raw_response.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        fednow_transfer = response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Increase) -> None:
        with client.simulations.fednow_transfers.with_streaming_response.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed

            fednow_transfer = response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            client.simulations.fednow_transfers.with_raw_response.complete(
                fednow_transfer_id="",
            )


class TestAsyncFednowTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.simulations.fednow_transfers.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.simulations.fednow_transfers.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
            rejection={"reject_reason_code": "account_closed"},
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.fednow_transfers.with_raw_response.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        fednow_transfer = await response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.fednow_transfers.with_streaming_response.complete(
            fednow_transfer_id="fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed

            fednow_transfer = await response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            await async_client.simulations.fednow_transfers.with_raw_response.complete(
                fednow_transfer_id="",
            )
