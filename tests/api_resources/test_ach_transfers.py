# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHTransfer
from increase._utils import parse_date, parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestACHTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
            account_number="987654321",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date=parse_date("2019-12-27"),
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            require_approval=True,
            routing_number="101050001",
            standard_entry_class_code="corporate_credit_or_debit",
            unique_identifier="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.ach_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.ach_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.ach_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.ach_transfers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.list()
        assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=1,
            unique_identifier="x",
        )
        assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.ach_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.ach_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(SyncPage[ACHTransfer], ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.approve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.ach_transfers.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.ach_transfers.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        ach_transfer = client.ach_transfers.cancel(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.ach_transfers.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.ach_transfers.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
            account_number="987654321",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            effective_date=parse_date("2019-12-27"),
            external_account_id="string",
            funding="checking",
            individual_id="x",
            individual_name="x",
            require_approval=True,
            routing_number="101050001",
            standard_entry_class_code="corporate_credit_or_debit",
            unique_identifier="x",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.ach_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.ach_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            statement_descriptor="New ACH transfer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.ach_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.ach_transfers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.list()
        assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=1,
            unique_identifier="x",
        )
        assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.ach_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.ach_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(AsyncPage[ACHTransfer], ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.approve(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, client: AsyncIncrease) -> None:
        response = await client.ach_transfers.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, client: AsyncIncrease) -> None:
        async with client.ach_transfers.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, client: AsyncIncrease) -> None:
        ach_transfer = await client.ach_transfers.cancel(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, client: AsyncIncrease) -> None:
        response = await client.ach_transfers.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, client: AsyncIncrease) -> None:
        async with client.ach_transfers.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
