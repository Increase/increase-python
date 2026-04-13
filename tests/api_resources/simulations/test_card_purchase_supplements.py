# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardPurchaseSupplement
from increase._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardPurchaseSupplements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_purchase_supplement = client.simulations.card_purchase_supplements.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_purchase_supplement = client.simulations.card_purchase_supplements.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
            invoice={
                "discount_amount": 100,
                "duty_tax_amount": 200,
                "order_date": parse_date("2023-07-20"),
                "shipping_amount": 300,
                "shipping_destination_country_code": "US",
                "shipping_destination_postal_code": "10045",
                "shipping_source_postal_code": "10045",
                "shipping_tax_amount": 400,
                "shipping_tax_rate": "0.2",
                "unique_value_added_tax_invoice_reference": "12302",
            },
            line_items=[
                {
                    "discount_amount": 0,
                    "item_commodity_code": "001",
                    "item_descriptor": "Coffee",
                    "item_quantity": "1",
                    "product_code": "101",
                    "sales_tax_amount": 0,
                    "sales_tax_rate": "-16699",
                    "total_amount": 500,
                    "unit_cost": "5",
                    "unit_of_measure_code": "NMB",
                }
            ],
        )
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_purchase_supplements.with_raw_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_purchase_supplement = response.parse()
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_purchase_supplements.with_streaming_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_purchase_supplement = response.parse()
            assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardPurchaseSupplements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_purchase_supplement = await async_client.simulations.card_purchase_supplements.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_purchase_supplement = await async_client.simulations.card_purchase_supplements.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
            invoice={
                "discount_amount": 100,
                "duty_tax_amount": 200,
                "order_date": parse_date("2023-07-20"),
                "shipping_amount": 300,
                "shipping_destination_country_code": "US",
                "shipping_destination_postal_code": "10045",
                "shipping_source_postal_code": "10045",
                "shipping_tax_amount": 400,
                "shipping_tax_rate": "0.2",
                "unique_value_added_tax_invoice_reference": "12302",
            },
            line_items=[
                {
                    "discount_amount": 0,
                    "item_commodity_code": "001",
                    "item_descriptor": "Coffee",
                    "item_quantity": "1",
                    "product_code": "101",
                    "sales_tax_amount": 0,
                    "sales_tax_rate": "-16699",
                    "total_amount": 500,
                    "unit_cost": "5",
                    "unit_of_measure_code": "NMB",
                }
            ],
        )
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_purchase_supplements.with_raw_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_purchase_supplement = await response.parse()
        assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_purchase_supplements.with_streaming_response.create(
            transaction_id="transaction_uyrp7fld2ium70oa7oi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_purchase_supplement = await response.parse()
            assert_matches_type(CardPurchaseSupplement, card_purchase_supplement, path=["response"])

        assert cast(Any, response.is_closed) is True
