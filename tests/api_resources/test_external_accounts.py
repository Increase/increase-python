# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    ExternalAccount,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            account_holder="business",
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
            "external_account_id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.retrieve(
            "external_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.retrieve(
            "external_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.external_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        external_account = client.external_accounts.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
            account_holder="business",
            description="New description",
            funding="checking",
            status="active",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.external_accounts.with_raw_response.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.external_accounts.with_streaming_response.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.external_accounts.with_raw_response.update(
                external_account_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        external_account = client.external_accounts.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            routing_number="xxxxxxxxx",
            status={"in": ["active"]},
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
            account_holder="business",
            funding="checking",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.external_accounts.with_raw_response.create(
            account_number="987654321",
            description="Landlord",
            routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.external_accounts.with_streaming_response.create(
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
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.retrieve(
            "external_account_id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.external_accounts.with_raw_response.retrieve(
            "external_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.external_accounts.with_streaming_response.retrieve(
            "external_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.external_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
            account_holder="business",
            description="New description",
            funding="checking",
            status="active",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.external_accounts.with_raw_response.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.external_accounts.with_streaming_response.update(
            external_account_id="external_account_ukk55lr923a3ac0pp7iv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.external_accounts.with_raw_response.update(
                external_account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.list()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        external_account = await async_client.external_accounts.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            routing_number="xxxxxxxxx",
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = await response.parse()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

        assert cast(Any, response.is_closed) is True
