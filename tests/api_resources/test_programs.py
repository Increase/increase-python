# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Program
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrograms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        program = client.programs.retrieve(
            "program_id",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.programs.with_raw_response.retrieve(
            "program_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = response.parse()
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.programs.with_streaming_response.retrieve(
            "program_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = response.parse()
            assert_matches_type(Program, program, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `program_id` but received ''"):
            client.programs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        program = client.programs.list()
        assert_matches_type(SyncPage[Program], program, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        program = client.programs.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Program], program, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.programs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = response.parse()
        assert_matches_type(SyncPage[Program], program, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.programs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = response.parse()
            assert_matches_type(SyncPage[Program], program, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrograms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        program = await async_client.programs.retrieve(
            "program_id",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.programs.with_raw_response.retrieve(
            "program_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = await response.parse()
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.programs.with_streaming_response.retrieve(
            "program_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = await response.parse()
            assert_matches_type(Program, program, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `program_id` but received ''"):
            await async_client.programs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        program = await async_client.programs.list()
        assert_matches_type(AsyncPage[Program], program, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        program = await async_client.programs.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Program], program, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.programs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = await response.parse()
        assert_matches_type(AsyncPage[Program], program, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.programs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            program = await response.parse()
            assert_matches_type(AsyncPage[Program], program, path=["response"])

        assert cast(Any, response.is_closed) is True
