# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.ach_tranfer import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestACHTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.ach_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "amount": 100,
                "routing_number": "101050001",
                "statement_descriptor": "New ACH transfer",
            },
        )
        assert isinstance(resource, ACHTranfer)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.ach_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "addendum": "x",
                "amount": 100,
                "company_descriptive_date": "x",
                "company_discretionary_data": "x",
                "company_entry_description": "x",
                "company_name": "x",
                "effective_date": "2019-12-27T18:11:19.117Z",
                "funding": "checking",
                "individual_id": "x",
                "individual_name": "x",
                "routing_number": "101050001",
                "standard_entry_class_code": "corporate_credit_or_debit",
                "statement_descriptor": "New ACH transfer",
            },
        )
        assert isinstance(resource, ACHTranfer)

    def test_method_retrieve(self) -> None:
        resource = self.client.ach_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    def test_method_list(self) -> None:
        resource = self.client.ach_transfers.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.ach_transfers.list(
            {
                "cursor": "x",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncACHTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.ach_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "amount": 100,
                "routing_number": "101050001",
                "statement_descriptor": "New ACH transfer",
            },
        )
        assert isinstance(resource, ACHTranfer)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.ach_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "addendum": "x",
                "amount": 100,
                "company_descriptive_date": "x",
                "company_discretionary_data": "x",
                "company_entry_description": "x",
                "company_name": "x",
                "effective_date": "2019-12-27T18:11:19.117Z",
                "funding": "checking",
                "individual_id": "x",
                "individual_name": "x",
                "routing_number": "101050001",
                "standard_entry_class_code": "corporate_credit_or_debit",
                "statement_descriptor": "New ACH transfer",
            },
        )
        assert isinstance(resource, ACHTranfer)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.ach_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, ACHTranfer)

    async def test_method_list(self) -> None:
        resource = await self.client.ach_transfers.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.ach_transfers.list(
            {
                "cursor": "x",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, AsyncPage)
