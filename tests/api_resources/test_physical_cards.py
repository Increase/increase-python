# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    PhysicalCard,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhysicalCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        physical_card = client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        physical_card = client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                    "country": "x",
                    "line2": "Unit 2",
                    "line3": "x",
                    "phone_number": "x",
                },
                "method": "usps",
                "schedule": "next_day",
            },
            physical_card_profile_id="physical_card_profile_id",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.physical_cards.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.physical_cards.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        physical_card = client.physical_cards.retrieve(
            "physical_card_id",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.physical_cards.with_raw_response.retrieve(
            "physical_card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.physical_cards.with_streaming_response.retrieve(
            "physical_card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            client.physical_cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        physical_card = client.physical_cards.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.physical_cards.with_raw_response.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.physical_cards.with_streaming_response.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            client.physical_cards.with_raw_response.update(
                physical_card_id="",
                status="disabled",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        physical_card = client.physical_cards.list()
        assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        physical_card = client.physical_cards.list(
            card_id="card_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.physical_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.physical_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(SyncPage[PhysicalCard], physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhysicalCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                    "country": "x",
                    "line2": "Unit 2",
                    "line3": "x",
                    "phone_number": "x",
                },
                "method": "usps",
                "schedule": "next_day",
            },
            physical_card_profile_id="physical_card_profile_id",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_cards.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = await response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_cards.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            cardholder={
                "first_name": "Ian",
                "last_name": "Crease",
            },
            shipment={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "name": "Ian Crease",
                    "postal_code": "10045",
                    "state": "NY",
                },
                "method": "usps",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.retrieve(
            "physical_card_id",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_cards.with_raw_response.retrieve(
            "physical_card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = await response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_cards.with_streaming_response.retrieve(
            "physical_card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            await async_client.physical_cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_cards.with_raw_response.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = await response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_cards.with_streaming_response.update(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            status="disabled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            await async_client.physical_cards.with_raw_response.update(
                physical_card_id="",
                status="disabled",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.list()
        assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.physical_cards.list(
            card_id="card_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = await response.parse()
        assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(AsyncPage[PhysicalCard], physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True
