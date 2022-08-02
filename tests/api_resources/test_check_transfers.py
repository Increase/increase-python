# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.check_transfer import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.check_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "amount": 1000,
                "message": "Check payment",
                "recipient_name": "Ian Crease",
            },
        )
        assert isinstance(resource, CheckTransfer)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.check_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "amount": 1000,
                "message": "Check payment",
                "recipient_name": "Ian Crease",
            },
        )
        assert isinstance(resource, CheckTransfer)

    def test_method_retrieve(self) -> None:
        resource = self.client.check_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    def test_method_list(self) -> None:
        resource = self.client.check_transfers.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.check_transfers.list(
            {
                "cursor": "string",
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

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    def test_method_stop_payment(self) -> None:
        resource = self.client.check_transfers.stop_payment(
            "string",
        )
        assert isinstance(resource, CheckTransfer)


class TestAsyncCheckTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.check_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "amount": 1000,
                "message": "Check payment",
                "recipient_name": "Ian Crease",
            },
        )
        assert isinstance(resource, CheckTransfer)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.check_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "amount": 1000,
                "message": "Check payment",
                "recipient_name": "Ian Crease",
            },
        )
        assert isinstance(resource, CheckTransfer)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.check_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    async def test_method_list(self) -> None:
        resource = await self.client.check_transfers.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.check_transfers.list(
            {
                "cursor": "string",
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

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    async def test_method_stop_payment(self) -> None:
        resource = await self.client.check_transfers.stop_payment(
            "string",
        )
        assert isinstance(resource, CheckTransfer)
