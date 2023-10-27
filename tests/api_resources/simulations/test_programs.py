# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Program
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPrograms:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        program = client.simulations.programs.create(
            name="For Benefit Of",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.programs.with_raw_response.create(
            name="For Benefit Of",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = response.parse()
        assert_matches_type(Program, program, path=["response"])


class TestAsyncPrograms:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        program = await client.simulations.programs.create(
            name="For Benefit Of",
        )
        assert_matches_type(Program, program, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.simulations.programs.with_raw_response.create(
            name="For Benefit Of",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        program = response.parse()
        assert_matches_type(Program, program, path=["response"])
