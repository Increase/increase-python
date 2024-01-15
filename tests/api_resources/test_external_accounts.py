# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    ExternalAccount,
)
from increase._client import Increase, AsyncIncrease
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
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        external_account = client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.list(
            cursor="string",
            limit=1,
            routing_number="xxxxxxxxx",
            status={"in": ["active", "archived"]},
        )
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

        assert cast(Any, response.is_closed) is True


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
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.external_accounts.with_raw_response.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.external_accounts.with_streaming_response.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.retrieve(
            "string",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.external_accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.external_accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_raw_response_update(self, client: AsyncIncrease) -> None:
        response = await client.external_accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncIncrease) -> None:
        async with client.external_accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.list()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        external_account = await client.external_accounts.list(
            cursor="string",
            limit=1,
            routing_number="xxxxxxxxx",
            status={"in": ["active", "archived"]},
        )
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

        assert cast(Any, response.is_closed) is True
