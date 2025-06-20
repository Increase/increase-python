# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    RealTimePaymentsTransfer,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealTimePaymentsTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            debtor_name="x",
            destination_account_number="987654321",
            destination_routing_number="101050001",
            external_account_id="external_account_id",
            require_approval=True,
            ultimate_creditor_name="x",
            ultimate_debtor_name="x",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.real_time_payments_transfers.with_raw_response.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.real_time_payments_transfers.with_streaming_response.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.retrieve(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.real_time_payments_transfers.with_raw_response.retrieve(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.real_time_payments_transfers.with_streaming_response.retrieve(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            client.real_time_payments_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.list()
        assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            external_account_id="external_account_id",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_approval"]},
        )
        assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.real_time_payments_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.real_time_payments_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.approve(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.real_time_payments_transfers.with_raw_response.approve(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.real_time_payments_transfers.with_streaming_response.approve(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            client.real_time_payments_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.cancel(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.real_time_payments_transfers.with_raw_response.cancel(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.real_time_payments_transfers.with_streaming_response.cancel(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            client.real_time_payments_transfers.with_raw_response.cancel(
                "",
            )


class TestAsyncRealTimePaymentsTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            debtor_name="x",
            destination_account_number="987654321",
            destination_routing_number="101050001",
            external_account_id="external_account_id",
            require_approval=True,
            ultimate_creditor_name="x",
            ultimate_debtor_name="x",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_transfers.with_raw_response.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = await response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_transfers.with_streaming_response.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.retrieve(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_transfers.with_raw_response.retrieve(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = await response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_transfers.with_streaming_response.retrieve(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            await async_client.real_time_payments_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.list()
        assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            external_account_id="external_account_id",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_approval"]},
        )
        assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = await response.parse()
        assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.approve(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_transfers.with_raw_response.approve(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = await response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_transfers.with_streaming_response.approve(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            await async_client.real_time_payments_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        real_time_payments_transfer = await async_client.real_time_payments_transfers.cancel(
            "real_time_payments_transfer_id",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_transfers.with_raw_response.cancel(
            "real_time_payments_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_transfer = await response.parse()
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_transfers.with_streaming_response.cancel(
            "real_time_payments_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_transfer = await response.parse()
            assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `real_time_payments_transfer_id` but received ''"
        ):
            await async_client.real_time_payments_transfers.with_raw_response.cancel(
                "",
            )
