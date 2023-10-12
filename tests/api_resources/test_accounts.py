# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Account
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccounts:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account = client.accounts.create(
            name="New Account!",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        account = client.accounts.create(
            name="New Account!",
            entity_id="entity_n8y8tnk2p9339ti393yi",
            informational_entity_id="string",
            program_id="program_i2v2os4mwza1oetokh9i",
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
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account = client.accounts.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            informational_entity_id="string",
            limit=0,
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
            name="New Account!",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.create(
            name="New Account!",
            entity_id="entity_n8y8tnk2p9339ti393yi",
            informational_entity_id="string",
            program_id="program_i2v2os4mwza1oetokh9i",
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
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            informational_entity_id="string",
            limit=0,
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
