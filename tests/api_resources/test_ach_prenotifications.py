# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHPrenotification
from increase._utils import parse_date, parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestACHPrenotifications:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.create(
            account_number="987654321",
            routing_number="101050001",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.create(
            account_number="987654321",
            routing_number="101050001",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date=parse_date("2019-12-27"),
            individual_id="x",
            individual_name="x",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.create(
            account_number="987654321",
            routing_number="101050001",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.retrieve(
            "string",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.list()
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])


class TestAsyncACHPrenotifications:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        ach_prenotification = await client.ach_prenotifications.create(
            account_number="987654321",
            routing_number="101050001",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        ach_prenotification = await client.ach_prenotifications.create(
            account_number="987654321",
            routing_number="101050001",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date=parse_date("2019-12-27"),
            individual_id="x",
            individual_name="x",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.ach_prenotifications.with_raw_response.create(
            account_number="987654321",
            routing_number="101050001",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        ach_prenotification = await client.ach_prenotifications.retrieve(
            "string",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.ach_prenotifications.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        ach_prenotification = await client.ach_prenotifications.list()
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        ach_prenotification = await client.ach_prenotifications.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.ach_prenotifications.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])
