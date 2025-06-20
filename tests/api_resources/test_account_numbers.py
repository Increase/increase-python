# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    AccountNumber,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account_number = client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
            inbound_ach={"debit_status": "allowed"},
            inbound_checks={"status": "allowed"},
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account_number = client.account_numbers.retrieve(
            "account_number_id",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.retrieve(
            "account_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.retrieve(
            "account_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_number_id` but received ''"):
            client.account_numbers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        account_number = client.account_numbers.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            inbound_ach={"debit_status": "blocked"},
            inbound_checks={"status": "allowed"},
            name="x",
            status="disabled",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_number_id` but received ''"):
            client.account_numbers.with_raw_response.update(
                account_number_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_number = client.account_numbers.list()
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.list(
            account_id="account_id",
            ach_debit_status={"in": ["allowed"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
            inbound_ach={"debit_status": "allowed"},
            inbound_checks={"status": "allowed"},
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_numbers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = await response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_numbers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.retrieve(
            "account_number_id",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_numbers.with_raw_response.retrieve(
            "account_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = await response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_numbers.with_streaming_response.retrieve(
            "account_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_number_id` but received ''"):
            await async_client.account_numbers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            inbound_ach={"debit_status": "blocked"},
            inbound_checks={"status": "allowed"},
            name="x",
            status="disabled",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_numbers.with_raw_response.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = await response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_numbers.with_streaming_response.update(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_number_id` but received ''"):
            await async_client.account_numbers.with_raw_response.update(
                account_number_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.list()
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        account_number = await async_client.account_numbers.list(
            account_id="account_id",
            ach_debit_status={"in": ["allowed"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.account_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = await response.parse()
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.account_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

        assert cast(Any, response.is_closed) is True
