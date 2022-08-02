# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.account_transfer import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.account_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 100,
                "description": "Creating liquidity",
                "destination_account_id": "account_uf16sut2ct5bevmq3eh",
            },
        )
        assert isinstance(resource, AccountTransfer)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.account_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 100,
                "description": "Creating liquidity",
                "destination_account_id": "account_uf16sut2ct5bevmq3eh",
            },
        )
        assert isinstance(resource, AccountTransfer)

    def test_method_retrieve(self) -> None:
        resource = self.client.account_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, AccountTransfer)

    def test_method_list(self) -> None:
        resource = self.client.account_transfers.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.account_transfers.list(
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


class TestAsyncAccountTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.account_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 100,
                "description": "Creating liquidity",
                "destination_account_id": "account_uf16sut2ct5bevmq3eh",
            },
        )
        assert isinstance(resource, AccountTransfer)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.account_transfers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 100,
                "description": "Creating liquidity",
                "destination_account_id": "account_uf16sut2ct5bevmq3eh",
            },
        )
        assert isinstance(resource, AccountTransfer)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.account_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, AccountTransfer)

    async def test_method_list(self) -> None:
        resource = await self.client.account_transfers.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.account_transfers.list(
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
