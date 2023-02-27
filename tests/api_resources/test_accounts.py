# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Account
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account = client.accounts.create(
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        account = client.accounts.create(
            entity_id="string",
            informational_entity_id="string",
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account = client.accounts.retrieve(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        account = client.accounts.update(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        account = client.accounts.update(
            "string",
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account = client.accounts.list(
            cursor="string",
            limit=0,
            entity_id="string",
            status="open",
        )
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_close(self, client: Increase) -> None:
        account = client.accounts.close(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account = await client.accounts.create(
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.create(
            entity_id="string",
            informational_entity_id="string",
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account = await client.accounts.retrieve(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        account = await client.accounts.update(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.update(
            "string",
            name="x",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list(
            cursor="string",
            limit=0,
            entity_id="string",
            status="open",
        )
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_close(self, client: AsyncIncrease) -> None:
        account = await client.accounts.close(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])
