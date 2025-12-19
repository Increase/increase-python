# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Export

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        export = client.simulations.exports.create(
            category="form_1099_int",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        export = client.simulations.exports.create(
            category="form_1099_int",
            form_1099_int={"account_id": "account_in71c4amph0vgo2qllky"},
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.exports.with_raw_response.create(
            category="form_1099_int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.exports.with_streaming_response.create(
            category="form_1099_int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        export = await async_client.simulations.exports.create(
            category="form_1099_int",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        export = await async_client.simulations.exports.create(
            category="form_1099_int",
            form_1099_int={"account_id": "account_in71c4amph0vgo2qllky"},
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.exports.with_raw_response.create(
            category="form_1099_int",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.exports.with_streaming_response.create(
            category="form_1099_int",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True
