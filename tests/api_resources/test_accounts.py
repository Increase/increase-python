# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.account import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.accounts.create(
            {"name": "New Account!"},
        )
        assert isinstance(resource, Account)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.accounts.create(
            {
                "entity_id": "string",
                "name": "New Account!",
            },
        )
        assert isinstance(resource, Account)

    def test_method_retrieve(self) -> None:
        resource = self.client.accounts.retrieve(
            "string",
        )
        assert isinstance(resource, Account)

    def test_method_list(self) -> None:
        resource = self.client.accounts.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.accounts.list(
            {
                "cursor": "string",
                "limit": 0,
                "entity_id": "string",
                "status": "open",
            },
        )
        assert isinstance(resource, SyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    def test_method_close(self) -> None:
        resource = self.client.accounts.close(
            "string",
        )
        assert isinstance(resource, Account)


class TestAsyncAccounts:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.accounts.create(
            {"name": "New Account!"},
        )
        assert isinstance(resource, Account)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.accounts.create(
            {
                "entity_id": "string",
                "name": "New Account!",
            },
        )
        assert isinstance(resource, Account)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.accounts.retrieve(
            "string",
        )
        assert isinstance(resource, Account)

    async def test_method_list(self) -> None:
        resource = await self.client.accounts.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.accounts.list(
            {
                "cursor": "string",
                "limit": 0,
                "entity_id": "string",
                "status": "open",
            },
        )
        assert isinstance(resource, AsyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    async def test_method_close(self) -> None:
        resource = await self.client.accounts.close(
            "string",
        )
        assert isinstance(resource, Account)
