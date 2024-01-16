# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardDispute
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCardDisputes:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_dispute = client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
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
            "string",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.retrieve(
            "string",
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
            cursor="string",
            limit=1,
            status={"in": ["pending_reviewing", "accepted", "rejected"]},
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
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card_dispute = await client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.card_disputes.with_raw_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.card_disputes.with_streaming_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            explanation="Unauthorized recurring transaction.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        card_dispute = await client.card_disputes.retrieve(
            "string",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.card_disputes.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.card_disputes.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await client.card_disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        card_dispute = await client.card_disputes.list()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        card_dispute = await client.card_disputes.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status={"in": ["pending_reviewing", "accepted", "rejected"]},
        )
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.card_disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.card_disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True
