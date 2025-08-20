# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    Card,
    CardDetails,
    CardIframeURL,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card = client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card = client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
            billing_address={
                "city": "x",
                "line1": "x",
                "postal_code": "x",
                "state": "x",
                "line2": "x",
            },
            description="Card for Ian Crease",
            digital_wallet={
                "digital_card_profile_id": "digital_card_profile_id",
                "email": "x",
                "phone": "x",
            },
            entity_id="entity_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.cards.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.cards.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card = client.cards.retrieve(
            "card_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.cards.with_raw_response.retrieve(
            "card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.cards.with_streaming_response.retrieve(
            "card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        card = client.cards.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        card = client.cards.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            billing_address={
                "city": "x",
                "line1": "x",
                "postal_code": "x",
                "state": "x",
                "line2": "x",
            },
            description="New description",
            digital_wallet={
                "digital_card_profile_id": "digital_card_profile_id",
                "email": "x",
                "phone": "x",
            },
            entity_id="entity_id",
            status="active",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.cards.with_raw_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.cards.with_streaming_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.update(
                card_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card = client.cards.list()
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card = client.cards.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(SyncPage[Card], card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_details_iframe(self, client: Increase) -> None:
        card = client.cards.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    def test_method_create_details_iframe_with_all_params(self, client: Increase) -> None:
        card = client.cards.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
            physical_card_id="physical_card_id",
        )
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    def test_raw_response_create_details_iframe(self, client: Increase) -> None:
        response = client.cards.with_raw_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    def test_streaming_response_create_details_iframe(self, client: Increase) -> None:
        with client.cards.with_streaming_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardIframeURL, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_details_iframe(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.create_details_iframe(
                card_id="",
            )

    @parametrize
    def test_method_details(self, client: Increase) -> None:
        card = client.cards.details(
            "card_id",
        )
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    def test_raw_response_details(self, client: Increase) -> None:
        response = client.cards.with_raw_response.details(
            "card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    def test_streaming_response_details(self, client: Increase) -> None:
        with client.cards.with_streaming_response.details(
            "card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDetails, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_details(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.details(
                "",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
            billing_address={
                "city": "x",
                "line1": "x",
                "postal_code": "x",
                "state": "x",
                "line2": "x",
            },
            description="Card for Ian Crease",
            digital_wallet={
                "digital_card_profile_id": "digital_card_profile_id",
                "email": "x",
                "phone": "x",
            },
            entity_id="entity_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.retrieve(
            "card_id",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.retrieve(
            "card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.retrieve(
            "card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            billing_address={
                "city": "x",
                "line1": "x",
                "postal_code": "x",
                "state": "x",
                "line2": "x",
            },
            description="New description",
            digital_wallet={
                "digital_card_profile_id": "digital_card_profile_id",
                "email": "x",
                "phone": "x",
            },
            entity_id="entity_id",
            status="active",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.update(
                card_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.list()
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(AsyncPage[Card], card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    async def test_method_create_details_iframe_with_all_params(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
            physical_card_id="physical_card_id",
        )
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    async def test_raw_response_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardIframeURL, card, path=["response"])

    @parametrize
    async def test_streaming_response_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardIframeURL, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.create_details_iframe(
                card_id="",
            )

    @parametrize
    async def test_method_details(self, async_client: AsyncIncrease) -> None:
        card = await async_client.cards.details(
            "card_id",
        )
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    async def test_raw_response_details(self, async_client: AsyncIncrease) -> None:
        response = await async_client.cards.with_raw_response.details(
            "card_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    async def test_streaming_response_details(self, async_client: AsyncIncrease) -> None:
        async with async_client.cards.with_streaming_response.details(
            "card_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDetails, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_details(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.cards.with_raw_response.details(
                "",
            )
