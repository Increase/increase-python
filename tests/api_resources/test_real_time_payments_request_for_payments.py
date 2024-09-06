# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    RealTimePaymentsRequestForPayment,
)
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealTimePaymentsRequestForPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.real_time_payments_request_for_payments.with_raw_response.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.real_time_payments_request_for_payments.with_streaming_response.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.retrieve(
            "request_for_payment_id",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.real_time_payments_request_for_payments.with_raw_response.retrieve(
            "request_for_payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.real_time_payments_request_for_payments.with_streaming_response.retrieve(
            "request_for_payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `request_for_payment_id` but received ''"
        ):
            client.real_time_payments_request_for_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.list()
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.list(
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
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.real_time_payments_request_for_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.real_time_payments_request_for_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = response.parse()
            assert_matches_type(
                SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncRealTimePaymentsRequestForPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await async_client.real_time_payments_request_for_payments.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_request_for_payments.with_raw_response.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = await response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_request_for_payments.with_streaming_response.create(
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = await response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await async_client.real_time_payments_request_for_payments.retrieve(
            "request_for_payment_id",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_request_for_payments.with_raw_response.retrieve(
            "request_for_payment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = await response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_request_for_payments.with_streaming_response.retrieve(
            "request_for_payment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = await response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `request_for_payment_id` but received ''"
        ):
            await async_client.real_time_payments_request_for_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await async_client.real_time_payments_request_for_payments.list()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await async_client.real_time_payments_request_for_payments.list(
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
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_request_for_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = await response.parse()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_request_for_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            real_time_payments_request_for_payment = await response.parse()
            assert_matches_type(
                AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
