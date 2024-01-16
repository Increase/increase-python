# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_streaming_response_shipment_advance(self, client: Increase) -> None:
        with client.simulations.physical_cards.with_streaming_response.shipment_advance(
            "string",
            shipment_status="shipped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_shipment_advance(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            client.simulations.physical_cards.with_raw_response.shipment_advance(
                "",
                shipment_status="shipped",
            )


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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_shipment_advance(self, client: AsyncIncrease) -> None:
        async with client.simulations.physical_cards.with_streaming_response.shipment_advance(
            "string",
            shipment_status="shipped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_shipment_advance(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            await client.simulations.physical_cards.with_raw_response.shipment_advance(
                "",
                shipment_status="shipped",
            )
