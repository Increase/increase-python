# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountStatement
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccountStatements:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account_statement = client.simulations.account_statements.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.account_statements.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.account_statements.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_statement = response.parse()
            assert_matches_type(AccountStatement, account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountStatements:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account_statement = await client.simulations.account_statements.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.simulations.account_statements.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.simulations.account_statements.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_statement = await response.parse()
            assert_matches_type(AccountStatement, account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True
