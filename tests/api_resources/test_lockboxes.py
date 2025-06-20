# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Lockbox
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        lockbox = client.lockboxes.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        lockbox = client.lockboxes.create(
            account_id="account_in71c4amph0vgo2qllky",
            description="Rent payments",
            recipient_name="x",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.lockboxes.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.lockboxes.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        lockbox = client.lockboxes.retrieve(
            "lockbox_id",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.lockboxes.with_raw_response.retrieve(
            "lockbox_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.lockboxes.with_streaming_response.retrieve(
            "lockbox_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_id` but received ''"):
            client.lockboxes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        lockbox = client.lockboxes.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        lockbox = client.lockboxes.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
            description="x",
            recipient_name="x",
            status="inactive",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.lockboxes.with_raw_response.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.lockboxes.with_streaming_response.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_id` but received ''"):
            client.lockboxes.with_raw_response.update(
                lockbox_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        lockbox = client.lockboxes.list()
        assert_matches_type(SyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        lockbox = client.lockboxes.list(
            account_id="account_id",
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
        assert_matches_type(SyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.lockboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = response.parse()
        assert_matches_type(SyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.lockboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = response.parse()
            assert_matches_type(SyncPage[Lockbox], lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLockboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.create(
            account_id="account_in71c4amph0vgo2qllky",
            description="Rent payments",
            recipient_name="x",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockboxes.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = await response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockboxes.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = await response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.retrieve(
            "lockbox_id",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockboxes.with_raw_response.retrieve(
            "lockbox_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = await response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockboxes.with_streaming_response.retrieve(
            "lockbox_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = await response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_id` but received ''"):
            await async_client.lockboxes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
            description="x",
            recipient_name="x",
            status="inactive",
        )
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockboxes.with_raw_response.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = await response.parse()
        assert_matches_type(Lockbox, lockbox, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockboxes.with_streaming_response.update(
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = await response.parse()
            assert_matches_type(Lockbox, lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lockbox_id` but received ''"):
            await async_client.lockboxes.with_raw_response.update(
                lockbox_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.list()
        assert_matches_type(AsyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        lockbox = await async_client.lockboxes.list(
            account_id="account_id",
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
        assert_matches_type(AsyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.lockboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockbox = await response.parse()
        assert_matches_type(AsyncPage[Lockbox], lockbox, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.lockboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockbox = await response.parse()
            assert_matches_type(AsyncPage[Lockbox], lockbox, path=["response"])

        assert cast(Any, response.is_closed) is True
