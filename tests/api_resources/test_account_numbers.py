# File generated from our OpenAPI spec by Stainless.

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
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccountNumbers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            inbound_ach={"debit_status": "blocked"},
            name="x",
            status="disabled",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.account_numbers.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.account_numbers.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_number = client.account_numbers.list()
        assert_matches_type(SyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_number = client.account_numbers.list(
            account_id="string",
            ach_debit_status="allowed",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="active",
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
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
            inbound_ach={"debit_status": "allowed"},
            inbound_checks={"status": "allowed"},
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.account_numbers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.account_numbers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            name="Rent payments",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.retrieve(
            "string",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.account_numbers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.account_numbers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            inbound_ach={"debit_status": "blocked"},
            name="x",
            status="disabled",
        )
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIncrease) -> None:
        response = await client.account_numbers.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AccountNumber, account_number, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncIncrease) -> None:
        async with client.account_numbers.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AccountNumber, account_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.list()
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account_number = await client.account_numbers.list(
            account_id="string",
            ach_debit_status="allowed",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="active",
        )
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.account_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_number = response.parse()
        assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.account_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_number = await response.parse()
            assert_matches_type(AsyncPage[AccountNumber], account_number, path=["response"])

        assert cast(Any, response.is_closed) is True
