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
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealTimePaymentsRequestsForPayment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {
                    "country": "US",
                    "address_line2": "x",
                    "building_number": "x",
                    "city": "x",
                    "postal_code": "x",
                    "state": "xx",
                    "street_name": "Liberty Street",
                },
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
            creditor_name="National Phonograph Company",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.real_time_payments_requests_for_payment.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.real_time_payments_requests_for_payment.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.real_time_payments_requests_for_payment.with_raw_response.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.real_time_payments_requests_for_payment.with_streaming_response.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received ''",
        ):
            client.real_time_payments_requests_for_payment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.list()
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.list(
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
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.real_time_payments_requests_for_payment.with_raw_response.list()

        assert response.is_closed is True
        real_time_payments_requests_for_payment = response.parse()
        assert_matches_type(
            SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.real_time_payments_requests_for_payment.with_streaming_response.list() as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = response.parse()
            assert_matches_type(
                SyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_method_cancel_with_all_params(self, client: Increase) -> None:
        real_time_payments_requests_for_payment = client.real_time_payments_requests_for_payment.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
            additional_information="x",
            reason="requested_by_customer",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.real_time_payments_requests_for_payment.with_raw_response.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.real_time_payments_requests_for_payment.with_streaming_response.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received ''",
        ):
            client.real_time_payments_requests_for_payment.with_raw_response.cancel(
                real_time_payments_request_for_payment_id="",
            )


class TestAsyncRealTimePaymentsRequestsForPayment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {
                    "country": "US",
                    "address_line2": "x",
                    "building_number": "x",
                    "city": "x",
                    "postal_code": "x",
                    "state": "xx",
                    "street_name": "Liberty Street",
                },
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
            creditor_name="National Phonograph Company",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_requests_for_payment.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = await response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_requests_for_payment.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=100,
            debtor={
                "address": {"country": "US"},
                "name": "Ian Crease",
            },
            debtor_account_number="987654321",
            debtor_routing_number="101050001",
            expires_at=parse_datetime("2020-02-14T23:59:59Z"),
            requested_execution_at=parse_datetime("2020-02-07T23:59:59Z"),
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = await response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_requests_for_payment.with_raw_response.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = await response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_requests_for_payment.with_streaming_response.retrieve(
            "real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = await response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received ''",
        ):
            await async_client.real_time_payments_requests_for_payment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.list()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.list(
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
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_requests_for_payment.with_raw_response.list()

        assert response.is_closed is True
        real_time_payments_requests_for_payment = await response.parse()
        assert_matches_type(
            AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_requests_for_payment.with_streaming_response.list() as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = await response.parse()
            assert_matches_type(
                AsyncPage[RealTimePaymentsRequestForPayment], real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncIncrease) -> None:
        real_time_payments_requests_for_payment = await async_client.real_time_payments_requests_for_payment.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
            additional_information="x",
            reason="requested_by_customer",
        )
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.real_time_payments_requests_for_payment.with_raw_response.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        )

        assert response.is_closed is True
        real_time_payments_requests_for_payment = await response.parse()
        assert_matches_type(
            RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.real_time_payments_requests_for_payment.with_streaming_response.cancel(
            real_time_payments_request_for_payment_id="real_time_payments_request_for_payment_28kcliz1oevcnqyn9qp7",
        ) as response:
            assert not response.is_closed

            real_time_payments_requests_for_payment = await response.parse()
            assert_matches_type(
                RealTimePaymentsRequestForPayment, real_time_payments_requests_for_payment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `real_time_payments_request_for_payment_id` but received ''",
        ):
            await async_client.real_time_payments_requests_for_payment.with_raw_response.cancel(
                real_time_payments_request_for_payment_id="",
            )
