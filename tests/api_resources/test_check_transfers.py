# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    CheckTransfer,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        check_transfer = client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        check_transfer = client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            check_number="x",
            physical_check={
                "mailing_address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "postal_code": "10045",
                    "state": "NY",
                    "line2": "x",
                },
                "memo": "Check payment",
                "recipient_name": "Ian Crease",
                "attachment_file_id": "attachment_file_id",
                "note": "x",
                "payer": [{"contents": "x"}],
                "return_address": {
                    "city": "x",
                    "line1": "x",
                    "name": "x",
                    "postal_code": "x",
                    "state": "x",
                    "line2": "x",
                },
                "shipping_method": "usps_first_class",
                "signature_text": "Ian Crease",
            },
            require_approval=True,
            third_party={"recipient_name": "x"},
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        check_transfer = client.check_transfers.retrieve(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.retrieve(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.retrieve(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.check_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        check_transfer = client.check_transfers.list()
        assert_matches_type(SyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        check_transfer = client.check_transfers.list(
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
        assert_matches_type(SyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(SyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(SyncPage[CheckTransfer], check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        check_transfer = client.check_transfers.approve(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.approve(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.approve(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.check_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        check_transfer = client.check_transfers.cancel(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.cancel(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.cancel(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.check_transfers.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_stop_payment(self, client: Increase) -> None:
        check_transfer = client.check_transfers.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_method_stop_payment_with_all_params(self, client: Increase) -> None:
        check_transfer = client.check_transfers.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
            reason="mail_delivery_failed",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_stop_payment(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_stop_payment(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop_payment(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.check_transfers.with_raw_response.stop_payment(
                check_transfer_id="",
            )


class TestAsyncCheckTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            check_number="x",
            physical_check={
                "mailing_address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "postal_code": "10045",
                    "state": "NY",
                    "line2": "x",
                },
                "memo": "Check payment",
                "recipient_name": "Ian Crease",
                "attachment_file_id": "attachment_file_id",
                "note": "x",
                "payer": [{"contents": "x"}],
                "return_address": {
                    "city": "x",
                    "line1": "x",
                    "name": "x",
                    "postal_code": "x",
                    "state": "x",
                    "line2": "x",
                },
                "shipping_method": "usps_first_class",
                "signature_text": "Ian Crease",
            },
            require_approval=True,
            third_party={"recipient_name": "x"},
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.retrieve(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.retrieve(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.retrieve(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await async_client.check_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.list()
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.list(
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
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.approve(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.approve(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.approve(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await async_client.check_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.cancel(
            "check_transfer_id",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.cancel(
            "check_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.cancel(
            "check_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await async_client.check_transfers.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_stop_payment(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_method_stop_payment_with_all_params(self, async_client: AsyncIncrease) -> None:
        check_transfer = await async_client.check_transfers.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
            reason="mail_delivery_failed",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_stop_payment(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_transfers.with_raw_response.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = await response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_stop_payment(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_transfers.with_streaming_response.stop_payment(
            check_transfer_id="check_transfer_30b43acfu9vw8fyc4f5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop_payment(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await async_client.check_transfers.with_raw_response.stop_payment(
                check_transfer_id="",
            )
