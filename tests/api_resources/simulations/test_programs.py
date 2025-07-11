# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Program

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrograms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        program = client.simulations.programs.create(
            name="For Benefit Of",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        program = client.simulations.programs.create(
            name="For Benefit Of",
            bank="blue_ridge_bank",
            reserve_account_id="reserve_account_id",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.programs.with_raw_response.create(
            name="For Benefit Of",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = response.parse()
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.programs.with_streaming_response.create(
            name="For Benefit Of",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = response.parse()
            assert_matches_type(Program, program, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrograms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        program = await async_client.simulations.programs.create(
            name="For Benefit Of",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        program = await async_client.simulations.programs.create(
            name="For Benefit Of",
            bank="blue_ridge_bank",
            reserve_account_id="reserve_account_id",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.programs.with_raw_response.create(
            name="For Benefit Of",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = await response.parse()
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.programs.with_streaming_response.create(
            name="For Benefit Of",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = await response.parse()
            assert_matches_type(Program, program, path=["response"])

        assert cast(Any, response.is_closed) is True
