# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountStatement
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccountStatements:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account_statement = client.account_statements.retrieve(
            "string",
        )
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.account_statements.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_statement = client.account_statements.list()
        assert_matches_type(SyncPage[AccountStatement], account_statement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_statement = client.account_statements.list(
            account_id="string",
            cursor="string",
            limit=1,
            statement_period_start={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(SyncPage[AccountStatement], account_statement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.account_statements.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(SyncPage[AccountStatement], account_statement, path=["response"])


class TestAsyncAccountStatements:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account_statement = await client.account_statements.retrieve(
            "string",
        )
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.account_statements.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(AccountStatement, account_statement, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account_statement = await client.account_statements.list()
        assert_matches_type(AsyncPage[AccountStatement], account_statement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account_statement = await client.account_statements.list(
            account_id="string",
            cursor="string",
            limit=1,
            statement_period_start={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(AsyncPage[AccountStatement], account_statement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.account_statements.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_statement = response.parse()
        assert_matches_type(AsyncPage[AccountStatement], account_statement, path=["response"])
