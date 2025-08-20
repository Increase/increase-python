# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Export
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        export = client.exports.create(
            category="transaction_csv",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        export = client.exports.create(
            category="transaction_csv",
            account_statement_bai2={
                "account_id": "account_id",
                "effective_date": parse_date("2019-12-27"),
            },
            account_statement_ofx={
                "account_id": "account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            },
            balance_csv={
                "account_id": "account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "program_id": "program_id",
            },
            bookkeeping_account_balance_csv={
                "bookkeeping_account_id": "bookkeeping_account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            },
            entity_csv={"status": {"in": ["active"]}},
            transaction_csv={
                "account_id": "account_in71c4amph0vgo2qllky",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "program_id": "program_id",
            },
            vendor_csv={},
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.exports.with_raw_response.create(
            category="transaction_csv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.exports.with_streaming_response.create(
            category="transaction_csv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        export = client.exports.retrieve(
            "export_id",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.exports.with_raw_response.retrieve(
            "export_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.exports.with_streaming_response.retrieve(
            "export_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            client.exports.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        export = client.exports.list()
        assert_matches_type(SyncPage[Export], export, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        export = client.exports.list(
            category={"in": ["account_statement_ofx"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending"]},
        )
        assert_matches_type(SyncPage[Export], export, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(SyncPage[Export], export, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(SyncPage[Export], export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        export = await async_client.exports.create(
            category="transaction_csv",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        export = await async_client.exports.create(
            category="transaction_csv",
            account_statement_bai2={
                "account_id": "account_id",
                "effective_date": parse_date("2019-12-27"),
            },
            account_statement_ofx={
                "account_id": "account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            },
            balance_csv={
                "account_id": "account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "program_id": "program_id",
            },
            bookkeeping_account_balance_csv={
                "bookkeeping_account_id": "bookkeeping_account_id",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
            },
            entity_csv={"status": {"in": ["active"]}},
            transaction_csv={
                "account_id": "account_in71c4amph0vgo2qllky",
                "created_at": {
                    "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "program_id": "program_id",
            },
            vendor_csv={},
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.exports.with_raw_response.create(
            category="transaction_csv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.exports.with_streaming_response.create(
            category="transaction_csv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        export = await async_client.exports.retrieve(
            "export_id",
        )
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.exports.with_raw_response.retrieve(
            "export_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(Export, export, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.exports.with_streaming_response.retrieve(
            "export_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(Export, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `export_id` but received ''"):
            await async_client.exports.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        export = await async_client.exports.list()
        assert_matches_type(AsyncPage[Export], export, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        export = await async_client.exports.list(
            category={"in": ["account_statement_ofx"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending"]},
        )
        assert_matches_type(AsyncPage[Export], export, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(AsyncPage[Export], export, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(AsyncPage[Export], export, path=["response"])

        assert cast(Any, response.is_closed) is True
