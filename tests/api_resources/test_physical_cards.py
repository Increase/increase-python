# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PhysicalCard
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPhysicalCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        physical_card = client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            card_profile_id="card_profile_cox5y73lob2eqly18piy",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "method": "usps",
                "address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
            },
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        physical_card = client.physical_cards.retrieve(
            "string",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        physical_card = client.physical_cards.update(
            "string",
            status="disabled",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        physical_card = client.physical_cards.list()
        assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        physical_card = client.physical_cards.list(
            card_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])


class TestAsyncPhysicalCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        physical_card = await client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            card_profile_id="card_profile_cox5y73lob2eqly18piy",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "method": "usps",
                "address": {
                    "name": "Ian Crease",
                    "line1": "33 Liberty Street",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10045",
                },
            },
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        physical_card = await client.physical_cards.retrieve(
            "string",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        physical_card = await client.physical_cards.update(
            "string",
            status="disabled",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        physical_card = await client.physical_cards.list()
        assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        physical_card = await client.physical_cards.list(
            card_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])
