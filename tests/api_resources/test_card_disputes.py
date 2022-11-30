# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.card_dispute import CardDispute

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCardDisputes:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.card_disputes.create(
            disputed_transaction_id="string",
            explanation="x",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.card_disputes.retrieve(
            "string",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.card_disputes.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.card_disputes.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
            status={"in": ["pending_reviewing", "pending_reviewing", "pending_reviewing"]},
        )
        assert isinstance(resource, SyncPage)


class TestAsyncCardDisputes:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.card_disputes.create(
            disputed_transaction_id="string",
            explanation="x",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.card_disputes.retrieve(
            "string",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.card_disputes.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.card_disputes.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
            status={"in": ["pending_reviewing", "pending_reviewing", "pending_reviewing"]},
        )
        assert isinstance(resource, AsyncPage)
