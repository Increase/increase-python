# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.pending_transaction import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPendingTransactions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.pending_transactions.retrieve(
            "string",
        )
        assert isinstance(resource, PendingTransaction)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.pending_transactions.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_optional_params(self, client: Increase) -> None:
        resource = client.pending_transactions.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "route_id": "string",
                "source_id": "string",
                "status": {"in": ["pending", "pending", "pending"]},
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncPendingTransactions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.pending_transactions.retrieve(
            "string",
        )
        assert isinstance(resource, PendingTransaction)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.pending_transactions.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.pending_transactions.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "route_id": "string",
                "source_id": "string",
                "status": {"in": ["pending", "pending", "pending"]},
            },
        )
        assert isinstance(resource, AsyncPage)
