# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    LockboxAddress,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockboxAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.create()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.create(
            description="Lockbox Address 1",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.lockbox_addresses.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.lockbox_addresses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.lockbox_addresses.with_raw_response.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.lockbox_addresses.with_streaming_response.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_address_id` but received ''"):
            client.lockbox_addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
            description="x",
            status="disabled",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.lockbox_addresses.with_raw_response.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.lockbox_addresses.with_streaming_response.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_address_id` but received ''"):
            client.lockbox_addresses.with_raw_response.update(
                lockbox_address_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.list()
        assert_matches_type(SyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        lockbox_address = client.lockbox_addresses.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.lockbox_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = response.parse()
        assert_matches_type(SyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.lockbox_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = response.parse()
            assert_matches_type(SyncPage[LockboxAddress], lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLockboxAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.create()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.create(
            description="Lockbox Address 1",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockbox_addresses.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = await response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockbox_addresses.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = await response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockbox_addresses.with_raw_response.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = await response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockbox_addresses.with_streaming_response.retrieve(
            "lockbox_address_lw6sbzl9ol5dfd8hdml6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = await response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_address_id` but received ''"):
            await async_client.lockbox_addresses.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
            description="x",
            status="disabled",
        )
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockbox_addresses.with_raw_response.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = await response.parse()
        assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockbox_addresses.with_streaming_response.update(
            lockbox_address_id="lockbox_address_lw6sbzl9ol5dfd8hdml6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = await response.parse()
            assert_matches_type(LockboxAddress, lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_address_id` but received ''"):
            await async_client.lockbox_addresses.with_raw_response.update(
                lockbox_address_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.list()
        assert_matches_type(AsyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox_address = await async_client.lockbox_addresses.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockbox_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox_address = await response.parse()
        assert_matches_type(AsyncPage[LockboxAddress], lockbox_address, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockbox_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox_address = await response.parse()
            assert_matches_type(AsyncPage[LockboxAddress], lockbox_address, path=["response"])

        assert cast(Any, response.is_closed) is True
