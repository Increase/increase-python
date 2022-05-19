# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.wire_transfer import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.wire_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "routing_number": "101050001",
                "amount": 100,
                "message_to_recipient": "New account transfer",
            },
        )
        assert isinstance(resource, WireTransfer)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.wire_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "routing_number": "101050001",
                "amount": 100,
                "message_to_recipient": "New account transfer",
                "beneficiary_name": "Ian Crease",
                "beneficiary_address_line1": "33 Liberty Street",
                "beneficiary_address_line2": "New York",
                "beneficiary_address_line3": "NY 10045",
            },
        )
        assert isinstance(resource, WireTransfer)

    def test_method_retrieve(self) -> None:
        resource = self.client.wire_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    def test_method_list(self) -> None:
        resource = self.client.wire_transfers.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.wire_transfers.list(
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

    @pytest.mark.skip(reason="Prism tests are broken")
    def test_method_reverse(self) -> None:
        resource = self.client.wire_transfers.reverse(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @pytest.mark.skip(reason="Prism tests are broken")
    def test_method_submit(self) -> None:
        resource = self.client.wire_transfers.submit(
            "string",
        )
        assert isinstance(resource, WireTransfer)


class TestAsyncWireTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.wire_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "routing_number": "101050001",
                "amount": 100,
                "message_to_recipient": "New account transfer",
            },
        )
        assert isinstance(resource, WireTransfer)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.wire_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "account_number": "987654321",
                "routing_number": "101050001",
                "amount": 100,
                "message_to_recipient": "New account transfer",
                "beneficiary_name": "Ian Crease",
                "beneficiary_address_line1": "33 Liberty Street",
                "beneficiary_address_line2": "New York",
                "beneficiary_address_line3": "NY 10045",
            },
        )
        assert isinstance(resource, WireTransfer)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.wire_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    async def test_method_list(self) -> None:
        resource = await self.client.wire_transfers.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.wire_transfers.list(
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

    @pytest.mark.skip(reason="Prism tests are broken")
    async def test_method_reverse(self) -> None:
        resource = await self.client.wire_transfers.reverse(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @pytest.mark.skip(reason="Prism tests are broken")
    async def test_method_submit(self) -> None:
        resource = await self.client.wire_transfers.submit(
            "string",
        )
        assert isinstance(resource, WireTransfer)
