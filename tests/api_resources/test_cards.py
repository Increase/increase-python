# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.card import Card
from increase.types.card_details import CardDetails

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.cards.create(
            account_id="string",
        )
        assert isinstance(resource, Card)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.cards.create(
            account_id="string",
            description="x",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            digital_wallet={
                "email": "x",
                "phone": "x",
            },
        )
        assert isinstance(resource, Card)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.cards.retrieve(
            "string",
        )
        assert isinstance(resource, Card)

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        resource = client.cards.update(
            "string",
        )
        assert isinstance(resource, Card)

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        resource = client.cards.update(
            "string",
            description="x",
            status="active",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            digital_wallet={
                "email": "x",
                "phone": "x",
            },
        )
        assert isinstance(resource, Card)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.cards.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.cards.list(
            cursor="string",
            limit=0,
            account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_retrieve_sensitive_details(self, client: Increase) -> None:
        resource = client.cards.retrieve_sensitive_details(
            "string",
        )
        assert isinstance(resource, CardDetails)


class TestAsyncCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.cards.create(
            account_id="string",
        )
        assert isinstance(resource, Card)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.cards.create(
            account_id="string",
            description="x",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            digital_wallet={
                "email": "x",
                "phone": "x",
            },
        )
        assert isinstance(resource, Card)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.cards.retrieve(
            "string",
        )
        assert isinstance(resource, Card)

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        resource = await client.cards.update(
            "string",
        )
        assert isinstance(resource, Card)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.cards.update(
            "string",
            description="x",
            status="active",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            digital_wallet={
                "email": "x",
                "phone": "x",
            },
        )
        assert isinstance(resource, Card)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.cards.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.cards.list(
            cursor="string",
            limit=0,
            account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        resource = await client.cards.retrieve_sensitive_details(
            "string",
        )
        assert isinstance(resource, CardDetails)
