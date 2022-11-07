# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.ach_prenotification import ACHPrenotification

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestACHPrenotifications:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.ach_prenotifications.create(
            account_number="x",
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.ach_prenotifications.create(
            account_number="x",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date="2019-12-27T18:11:19.117Z",
            individual_id="x",
            individual_name="x",
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.ach_prenotifications.retrieve(
            "string",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.ach_prenotifications.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.ach_prenotifications.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncACHPrenotifications:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.ach_prenotifications.create(
            account_number="x",
            routing_number="xxxxxxxxx",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.ach_prenotifications.create(
            account_number="x",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date="2019-12-27T18:11:19.117Z",
            individual_id="x",
            individual_name="x",
            routing_number="xxxxxxxxx",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.ach_prenotifications.retrieve(
            "string",
        )
        assert isinstance(resource, ACHPrenotification)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.ach_prenotifications.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.ach_prenotifications.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, AsyncPage)
