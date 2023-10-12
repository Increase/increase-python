# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ExternalAccount
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestExternalAccounts:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        external_account = client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
            funding="checking",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        external_account = client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        external_account = client.external_accounts.update(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.update(
            "string",
            description="New description",
            status="active",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.list(
            cursor="string",
            limit=0,
            routing_number="xxxxxxxxx",
            status={"in": ["active", "archived"]},
        )
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])


class TestAsyncExternalAccounts:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
            funding="checking",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.update(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.update(
            "string",
            description="New description",
            status="active",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.list()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.list(
            cursor="string",
            limit=0,
            routing_number="xxxxxxxxx",
            status={"in": ["active", "archived"]},
        )
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])
