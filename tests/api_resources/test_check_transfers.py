# File generated from our OpenAPI spec by Stainless.

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
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCheckTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        check_transfer = client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        check_transfer = client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            physical_check={
                "memo": "Check payment",
                "note": "x",
                "recipient_name": "Ian Crease",
                "mailing_address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
                "return_address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
            },
            require_approval=True,
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unique_identifier="x",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        check_transfer = client.check_transfers.retrieve(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.retrieve(
            "string",
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
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            unique_identifier="x",
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
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.approve(
            "string",
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
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.cancel(
            "string",
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

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_method_stop_payment(self, client: Increase) -> None:
        check_transfer = client.check_transfers.stop_payment(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_method_stop_payment_with_all_params(self, client: Increase) -> None:
        check_transfer = client.check_transfers.stop_payment(
            "string",
            reason="mail_delivery_failed",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_raw_response_stop_payment(self, client: Increase) -> None:
        response = client.check_transfers.with_raw_response.stop_payment(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_streaming_response_stop_payment(self, client: Increase) -> None:
        with client.check_transfers.with_streaming_response.stop_payment(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_path_params_stop_payment(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.check_transfers.with_raw_response.stop_payment(
                "",
            )


class TestAsyncCheckTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            fulfillment_method="physical_check",
            physical_check={
                "memo": "Check payment",
                "note": "x",
                "recipient_name": "Ian Crease",
                "mailing_address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
                "return_address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
            },
            require_approval=True,
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unique_identifier="x",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.retrieve(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.check_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.list()
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            unique_identifier="x",
        )
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(AsyncPage[CheckTransfer], check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.approve(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.approve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.approve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.check_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.cancel(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.check_transfers.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_method_stop_payment(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.stop_payment(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_method_stop_payment_with_all_params(self, client: AsyncIncrease) -> None:
        check_transfer = await client.check_transfers.stop_payment(
            "string",
            reason="mail_delivery_failed",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_raw_response_stop_payment(self, client: AsyncIncrease) -> None:
        response = await client.check_transfers.with_raw_response.stop_payment(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_streaming_response_stop_payment(self, client: AsyncIncrease) -> None:
        async with client.check_transfers.with_streaming_response.stop_payment(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_path_params_stop_payment(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.check_transfers.with_raw_response.stop_payment(
                "",
            )
