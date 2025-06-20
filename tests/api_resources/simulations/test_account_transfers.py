# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Increase) -> None:
        account_transfer = client.simulations.account_transfers.complete(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Increase) -> None:
        response = client.simulations.account_transfers.with_raw_response.complete(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Increase) -> None:
        with client.simulations.account_transfers.with_streaming_response.complete(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            client.simulations.account_transfers.with_raw_response.complete(
                "",
            )


class TestAsyncAccountTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_complete(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.simulations.account_transfers.complete(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.account_transfers.with_raw_response.complete(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.account_transfers.with_streaming_response.complete(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            await async_client.simulations.account_transfers.with_raw_response.complete(
                "",
            )
