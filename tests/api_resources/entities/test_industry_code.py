# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndustryCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        industry_code = client.entities.industry_code.create(
            "string",
            industry_code="5132",
        )
        assert_matches_type(Entity, industry_code, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entities.industry_code.with_raw_response.create(
            "string",
            industry_code="5132",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        industry_code = response.parse()
        assert_matches_type(Entity, industry_code, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entities.industry_code.with_streaming_response.create(
            "string",
            industry_code="5132",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            industry_code = response.parse()
            assert_matches_type(Entity, industry_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.industry_code.with_raw_response.create(
                "",
                industry_code="5132",
            )


class TestAsyncIndustryCode:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        industry_code = await async_client.entities.industry_code.create(
            "string",
            industry_code="5132",
        )
        assert_matches_type(Entity, industry_code, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.industry_code.with_raw_response.create(
            "string",
            industry_code="5132",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        industry_code = response.parse()
        assert_matches_type(Entity, industry_code, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.industry_code.with_streaming_response.create(
            "string",
            industry_code="5132",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            industry_code = await response.parse()
            assert_matches_type(Entity, industry_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.industry_code.with_raw_response.create(
                "",
                industry_code="5132",
            )
