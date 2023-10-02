# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Card, CardDetails
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card = client.cards.create(
            account_id="string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card = client.cards.create(
            account_id="string",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="x",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card = client.cards.retrieve(
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        card = client.cards.update(
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        card = client.cards.update(
            "string",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="x",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
            status="active",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card = client.cards.list()
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card = client.cards.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_method_retrieve_sensitive_details(self, client: Increase) -> None:
        card = client.cards.retrieve_sensitive_details(
            "string",
        )
        assert_matches_type(CardDetails, card, path=["response"])


class TestAsyncCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card = await client.cards.create(
            account_id="string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        card = await client.cards.create(
            account_id="string",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="x",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        card = await client.cards.retrieve(
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        card = await client.cards.update(
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        card = await client.cards.update(
            "string",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="x",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
            status="active",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        card = await client.cards.list()
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        card = await client.cards.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_method_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        card = await client.cards.retrieve_sensitive_details(
            "string",
        )
        assert_matches_type(CardDetails, card, path=["response"])
