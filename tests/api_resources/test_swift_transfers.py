# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import SwiftTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwiftTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
                "line2": "x",
                "postal_code": "60314",
                "state": "x",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
            require_approval=True,
            routing_number="x",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.swift_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.swift_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.swift_transfers.with_raw_response.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.swift_transfers.with_streaming_response.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            client.swift_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.list()
        assert_matches_type(SyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.list(
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
            status={"in": ["pending_approval"]},
        )
        assert_matches_type(SyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.swift_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = response.parse()
        assert_matches_type(SyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.swift_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = response.parse()
            assert_matches_type(SyncPage[SwiftTransfer], swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.swift_transfers.with_raw_response.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.swift_transfers.with_streaming_response.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            client.swift_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        swift_transfer = client.swift_transfers.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.swift_transfers.with_raw_response.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.swift_transfers.with_streaming_response.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            client.swift_transfers.with_raw_response.cancel(
                "",
            )


class TestAsyncSwiftTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
                "line2": "x",
                "postal_code": "60314",
                "state": "x",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
            require_approval=True,
            routing_number="x",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.swift_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = await response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.swift_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            bank_identification_code="ECBFDEFFTPP",
            creditor_address={
                "city": "Frankfurt",
                "country": "DE",
                "line1": "Sonnemannstrasse 20",
            },
            creditor_name="Ian Crease",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="National Phonograph Company",
            instructed_amount=100,
            instructed_currency="USD",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="New Swift transfer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = await response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.swift_transfers.with_raw_response.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = await response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.swift_transfers.with_streaming_response.retrieve(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = await response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            await async_client.swift_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.list()
        assert_matches_type(AsyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.list(
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
            status={"in": ["pending_approval"]},
        )
        assert_matches_type(AsyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.swift_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = await response.parse()
        assert_matches_type(AsyncPage[SwiftTransfer], swift_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.swift_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = await response.parse()
            assert_matches_type(AsyncPage[SwiftTransfer], swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.swift_transfers.with_raw_response.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = await response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.swift_transfers.with_streaming_response.approve(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = await response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            await async_client.swift_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        swift_transfer = await async_client.swift_transfers.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        )
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.swift_transfers.with_raw_response.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swift_transfer = await response.parse()
        assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.swift_transfers.with_streaming_response.cancel(
            "swift_transfer_29h21xkng03788zwd3fh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swift_transfer = await response.parse()
            assert_matches_type(SwiftTransfer, swift_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `swift_transfer_id` but received ''"):
            await async_client.swift_transfers.with_raw_response.cancel(
                "",
            )
