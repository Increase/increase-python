# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundCheckDeposit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundCheckDeposits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_check_deposit = client.simulations.inbound_check_deposits.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_check_deposit = client.simulations.inbound_check_deposits.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
            payee_name_analysis="name_matches",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_check_deposits.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_check_deposits.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_adjustment(self, client: Increase) -> None:
        inbound_check_deposit = client.simulations.inbound_check_deposits.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_method_adjustment_with_all_params(self, client: Increase) -> None:
        inbound_check_deposit = client.simulations.inbound_check_deposits.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            amount=1000,
            reason="late_return",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_adjustment(self, client: Increase) -> None:
        response = client.simulations.inbound_check_deposits.with_raw_response.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_adjustment(self, client: Increase) -> None:
        with client.simulations.inbound_check_deposits.with_streaming_response.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_adjustment(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            client.simulations.inbound_check_deposits.with_raw_response.adjustment(
                inbound_check_deposit_id="",
            )


class TestAsyncInboundCheckDeposits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.simulations.inbound_check_deposits.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.simulations.inbound_check_deposits.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
            payee_name_analysis="name_matches",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_check_deposits.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_check_deposits.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            check_number="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_adjustment(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.simulations.inbound_check_deposits.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_method_adjustment_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.simulations.inbound_check_deposits.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            amount=1000,
            reason="late_return",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_adjustment(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_check_deposits.with_raw_response.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_adjustment(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_check_deposits.with_streaming_response.adjustment(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_adjustment(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            await async_client.simulations.inbound_check_deposits.with_raw_response.adjustment(
                inbound_check_deposit_id="",
            )
