# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardDispute
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_dispute = client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_dispute = client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
            amount=1,
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card_dispute = client.card_disputes.retrieve(
            "card_dispute_id",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.retrieve(
            "card_dispute_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.retrieve(
            "card_dispute_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            client.card_disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card_dispute = client.card_disputes.list()
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card_dispute = client.card_disputes.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_reviewing"]},
        )
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
            amount=1,
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.retrieve(
            "card_dispute_id",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.retrieve(
            "card_dispute_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.retrieve(
            "card_dispute_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await async_client.card_disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.list()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_reviewing"]},
        )
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True
