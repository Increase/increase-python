# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Card, CardDetails
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCards:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="Card for Ian Crease",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
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
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.cards.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.cards.with_streaming_response.retrieve(
            "string",
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
            description="New description",
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
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.cards.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.cards.with_streaming_response.update(
            "string",
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
                "",
            )

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
            limit=1,
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
    def test_method_retrieve_sensitive_details(self, client: Increase) -> None:
        card = client.cards.retrieve_sensitive_details(
            "string",
        )
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve_sensitive_details(self, client: Increase) -> None:
        response = client.cards.with_raw_response.retrieve_sensitive_details(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_sensitive_details(self, client: Increase) -> None:
        with client.cards.with_streaming_response.retrieve_sensitive_details(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardDetails, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_sensitive_details(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.cards.with_raw_response.retrieve_sensitive_details(
                "",
            )


class TestAsyncCards:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card = await client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        card = await client.cards.create(
            account_id="account_in71c4amph0vgo2qllky",
            billing_address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "postal_code": "x",
            },
            description="Card for Ian Crease",
            digital_wallet={
                "email": "x",
                "phone": "x",
                "card_profile_id": "string",
            },
            entity_id="string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.cards.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.cards.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        card = await client.cards.retrieve(
            "string",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.cards.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.cards.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await client.cards.with_raw_response.retrieve(
                "",
            )

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
            description="New description",
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
    async def test_raw_response_update(self, client: AsyncIncrease) -> None:
        response = await client.cards.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncIncrease) -> None:
        async with client.cards.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await client.cards.with_raw_response.update(
                "",
            )

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
            limit=1,
        )
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(AsyncPage[Card], card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        card = await client.cards.retrieve_sensitive_details(
            "string",
        )
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        response = await client.cards.with_raw_response.retrieve_sensitive_details(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardDetails, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        async with client.cards.with_streaming_response.retrieve_sensitive_details(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardDetails, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_sensitive_details(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await client.cards.with_raw_response.retrieve_sensitive_details(
                "",
            )
