# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import RealTimePaymentsTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRealTimePaymentsTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
            destination_account_number="987654321",
            destination_routing_number="101050001",
            external_account_id="string",
            require_approval=True,
            unique_identifier="x",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.retrieve(
            "string",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.list()
        assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        real_time_payments_transfer = client.real_time_payments_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=0,
            unique_identifier="x",
        )
        assert_matches_type(SyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])


class TestAsyncRealTimePaymentsTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.real_time_payments_transfers.create(
            amount=100,
            creditor_name="Ian Crease",
            remittance_information="Invoice 29582",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            destination_account_number="987654321",
            destination_routing_number="101050001",
            external_account_id="string",
            require_approval=True,
            unique_identifier="x",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.real_time_payments_transfers.retrieve(
            "string",
        )
        assert_matches_type(RealTimePaymentsTransfer, real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.real_time_payments_transfers.list()
        assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        real_time_payments_transfer = await client.real_time_payments_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=0,
            unique_identifier="x",
        )
        assert_matches_type(AsyncPage[RealTimePaymentsTransfer], real_time_payments_transfer, path=["response"])
