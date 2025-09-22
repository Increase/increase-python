# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    CardDetails,
    CardIframeURL,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        card_detail = client.card_details.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        )
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.card_details.with_raw_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = response.parse()
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.card_details.with_streaming_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = response.parse()
            assert_matches_type(CardDetails, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.card_details.with_raw_response.update(
                card_id="",
                pin="1234",
            )

    @parametrize
    def test_method_create_details_iframe(self, client: Increase) -> None:
        card_detail = client.card_details.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    def test_method_create_details_iframe_with_all_params(self, client: Increase) -> None:
        card_detail = client.card_details.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
            physical_card_id="physical_card_id",
        )
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    def test_raw_response_create_details_iframe(self, client: Increase) -> None:
        response = client.card_details.with_raw_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = response.parse()
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    def test_streaming_response_create_details_iframe(self, client: Increase) -> None:
        with client.card_details.with_streaming_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = response.parse()
            assert_matches_type(CardIframeURL, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_details_iframe(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.card_details.with_raw_response.create_details_iframe(
                card_id="",
            )

    @parametrize
    def test_method_details(self, client: Increase) -> None:
        card_detail = client.card_details.details(
            "card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    def test_raw_response_details(self, client: Increase) -> None:
        response = client.card_details.with_raw_response.details(
            "card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = response.parse()
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    def test_streaming_response_details(self, client: Increase) -> None:
        with client.card_details.with_streaming_response.details(
            "card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = response.parse()
            assert_matches_type(CardDetails, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_details(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.card_details.with_raw_response.details(
                "",
            )


class TestAsyncCardDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        card_detail = await async_client.card_details.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        )
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_details.with_raw_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = await response.parse()
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_details.with_streaming_response.update(
            card_id="card_oubs0hwk5rn6knuecxg2",
            pin="1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = await response.parse()
            assert_matches_type(CardDetails, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.card_details.with_raw_response.update(
                card_id="",
                pin="1234",
            )

    @parametrize
    async def test_method_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        card_detail = await async_client.card_details.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    async def test_method_create_details_iframe_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_detail = await async_client.card_details.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
            physical_card_id="physical_card_id",
        )
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    async def test_raw_response_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_details.with_raw_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = await response.parse()
        assert_matches_type(CardIframeURL, card_detail, path=["response"])

    @parametrize
    async def test_streaming_response_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_details.with_streaming_response.create_details_iframe(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = await response.parse()
            assert_matches_type(CardIframeURL, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_details_iframe(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.card_details.with_raw_response.create_details_iframe(
                card_id="",
            )

    @parametrize
    async def test_method_details(self, async_client: AsyncIncrease) -> None:
        card_detail = await async_client.card_details.details(
            "card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    async def test_raw_response_details(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_details.with_raw_response.details(
            "card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_detail = await response.parse()
        assert_matches_type(CardDetails, card_detail, path=["response"])

    @parametrize
    async def test_streaming_response_details(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_details.with_streaming_response.details(
            "card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_detail = await response.parse()
            assert_matches_type(CardDetails, card_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_details(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.card_details.with_raw_response.details(
                "",
            )
