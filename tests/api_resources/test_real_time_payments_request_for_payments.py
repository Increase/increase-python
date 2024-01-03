# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    RealTimePaymentsRequestForPayment,
)
from increase._utils import parse_date, parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestRealTimePaymentsRequestForPayments:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.create(
            amount=100,
            debtor={
                "name": "Ian Crease",
                "address": {"country": "US"},
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
                "name": "Ian Crease",
                "address": {"country": "US"},
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_payments_request_for_payment = client.real_time_payments_request_for_payments.retrieve(
            "string",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.real_time_payments_request_for_payments.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
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
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.real_time_payments_request_for_payments.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )


class TestAsyncRealTimePaymentsRequestForPayments:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await client.real_time_payments_request_for_payments.create(
            amount=100,
            debtor={
                "name": "Ian Crease",
                "address": {"country": "US"},
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
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.real_time_payments_request_for_payments.with_raw_response.create(
            amount=100,
            debtor={
                "name": "Ian Crease",
                "address": {"country": "US"},
            },
            destination_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            expires_at=parse_date("2025-12-31"),
            remittance_information="Invoice 29582",
            source_account_number="987654321",
            source_routing_number="101050001",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await client.real_time_payments_request_for_payments.retrieve(
            "string",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.real_time_payments_request_for_payments.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await client.real_time_payments_request_for_payments.list()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_request_for_payment = await client.real_time_payments_request_for_payments.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.real_time_payments_request_for_payments.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        real_time_payments_request_for_payment = response.parse()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_request_for_payment, path=["response"]
        )
