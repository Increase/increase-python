# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account_transfer = client.account_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        account_transfer = client.account_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
            require_approval=True,
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.account_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.account_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account_transfer = client.account_transfers.retrieve(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.account_transfers.with_raw_response.retrieve(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.account_transfers.with_streaming_response.retrieve(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            client.account_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_transfer = client.account_transfers.list()
        assert_matches_type(SyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_transfer = client.account_transfers.list(
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
        assert_matches_type(SyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.account_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(SyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.account_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(SyncPage[AccountTransfer], account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        account_transfer = client.account_transfers.approve(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.account_transfers.with_raw_response.approve(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.account_transfers.with_streaming_response.approve(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            client.account_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        account_transfer = client.account_transfers.cancel(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.account_transfers.with_raw_response.cancel(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.account_transfers.with_streaming_response.cancel(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            client.account_transfers.with_raw_response.cancel(
                "",
            )


class TestAsyncAccountTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
            require_approval=True,
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            description="Creating liquidity",
            destination_account_id="account_uf16sut2ct5bevmq3eh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.retrieve(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_transfers.with_raw_response.retrieve(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_transfers.with_streaming_response.retrieve(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            await async_client.account_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.list()
        assert_matches_type(AsyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.list(
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
        assert_matches_type(AsyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AsyncPage[AccountTransfer], account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AsyncPage[AccountTransfer], account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.approve(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_transfers.with_raw_response.approve(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_transfers.with_streaming_response.approve(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            await async_client.account_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        account_transfer = await async_client.account_transfers.cancel(
            "account_transfer_id",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_transfers.with_raw_response.cancel(
            "account_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = await response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_transfers.with_streaming_response.cancel(
            "account_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            await async_client.account_transfers.with_raw_response.cancel(
                "",
            )
