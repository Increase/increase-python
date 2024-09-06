# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountStatement

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        account_statement = await async_client.simulations.account_statements.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.account_statements.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = await response.parse()
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.account_statements.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_statement = await response.parse()
            assert_matches_type(AccountStatement, account_statement, path=["response"])

        assert cast(Any, response.is_closed) is True
