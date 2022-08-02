# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.account_statement import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountStatements:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.account_statements.retrieve(
            "string",
        )
        assert isinstance(resource, AccountStatement)

    def test_method_list(self) -> None:
        resource = self.client.account_statements.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.account_statements.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncAccountStatements:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.account_statements.retrieve(
            "string",
        )
        assert isinstance(resource, AccountStatement)

    async def test_method_list(self) -> None:
        resource = await self.client.account_statements.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.account_statements.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)
