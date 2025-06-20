# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import IntrafiBalance

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntrafiBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_intrafi_balance(self, client: Increase) -> None:
        intrafi_balance = client.intrafi_balances.intrafi_balance(
            "account_id",
        )
        assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

    @parametrize
    def test_raw_response_intrafi_balance(self, client: Increase) -> None:
        response = client.intrafi_balances.with_raw_response.intrafi_balance(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_balance = response.parse()
        assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

    @parametrize
    def test_streaming_response_intrafi_balance(self, client: Increase) -> None:
        with client.intrafi_balances.with_streaming_response.intrafi_balance(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_balance = response.parse()
            assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_intrafi_balance(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intrafi_balances.with_raw_response.intrafi_balance(
                "",
            )


class TestAsyncIntrafiBalances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_intrafi_balance(self, async_client: AsyncIncrease) -> None:
        intrafi_balance = await async_client.intrafi_balances.intrafi_balance(
            "account_id",
        )
        assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

    @parametrize
    async def test_raw_response_intrafi_balance(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi_balances.with_raw_response.intrafi_balance(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_balance = await response.parse()
        assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

    @parametrize
    async def test_streaming_response_intrafi_balance(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi_balances.with_streaming_response.intrafi_balance(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_balance = await response.parse()
            assert_matches_type(IntrafiBalance, intrafi_balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_intrafi_balance(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intrafi_balances.with_raw_response.intrafi_balance(
                "",
            )
