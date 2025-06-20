# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckDeposit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckDeposits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_reject(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.reject(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_reject(self, client: Increase) -> None:
        response = client.simulations.check_deposits.with_raw_response.reject(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_reject(self, client: Increase) -> None:
        with client.simulations.check_deposits.with_streaming_response.reject(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reject(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            client.simulations.check_deposits.with_raw_response.reject(
                "",
            )

    @parametrize
    def test_method_return(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.return_(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_return(self, client: Increase) -> None:
        response = client.simulations.check_deposits.with_raw_response.return_(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_return(self, client: Increase) -> None:
        with client.simulations.check_deposits.with_streaming_response.return_(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_return(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            client.simulations.check_deposits.with_raw_response.return_(
                "",
            )

    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        check_deposit = client.simulations.check_deposits.submit(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.check_deposits.with_raw_response.submit(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.check_deposits.with_streaming_response.submit(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            client.simulations.check_deposits.with_raw_response.submit(
                "",
            )


class TestAsyncCheckDeposits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_reject(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.simulations.check_deposits.reject(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_reject(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.check_deposits.with_raw_response.reject(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_reject(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.check_deposits.with_streaming_response.reject(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reject(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            await async_client.simulations.check_deposits.with_raw_response.reject(
                "",
            )

    @parametrize
    async def test_method_return(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.simulations.check_deposits.return_(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_return(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.check_deposits.with_raw_response.return_(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_return(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.check_deposits.with_streaming_response.return_(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_return(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            await async_client.simulations.check_deposits.with_raw_response.return_(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.simulations.check_deposits.submit(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.check_deposits.with_raw_response.submit(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.check_deposits.with_streaming_response.submit(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            await async_client.simulations.check_deposits.with_raw_response.submit(
                "",
            )
