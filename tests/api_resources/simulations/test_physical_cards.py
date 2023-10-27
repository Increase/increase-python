# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PhysicalCard
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPhysicalCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_shipment_advance(self, client: Increase) -> None:
        physical_card = client.simulations.physical_cards.shipment_advance(
            "string",
            shipment_status="shipped",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_raw_response_shipment_advance(self, client: Increase) -> None:
        response = client.simulations.physical_cards.with_raw_response.shipment_advance(
            "string",
            shipment_status="shipped",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])


class TestAsyncPhysicalCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_shipment_advance(self, client: AsyncIncrease) -> None:
        physical_card = await client.simulations.physical_cards.shipment_advance(
            "string",
            shipment_status="shipped",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_raw_response_shipment_advance(self, client: AsyncIncrease) -> None:
        response = await client.simulations.physical_cards.with_raw_response.shipment_advance(
            "string",
            shipment_status="shipped",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])
