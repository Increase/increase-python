# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountNumber
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountNumbers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account_number = client.account_numbers.create(
            account_id="string",
            name="x",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account_number = client.account_numbers.retrieve(
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        account_number = client.account_numbers.update(
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.update(
            "string",
            name="x",
            status="active",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_number = client.account_numbers.list()
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.list(
            cursor="string",
            limit=0,
            status="active",
            account_id="string",
        )
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])


class TestAsyncAccountNumbers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.create(
            account_id="string",
            name="x",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.retrieve(
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.update(
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.update(
            "string",
            name="x",
            status="active",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.list()
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.list(
            cursor="string",
            limit=0,
            status="active",
            account_id="string",
        )
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])
