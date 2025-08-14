# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardValidation
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardValidations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_validation = client.card_validations.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_validation = client.card_validations.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
            cardholder_first_name="Dee",
            cardholder_last_name="Hock",
            cardholder_middle_name="Ward",
            cardholder_postal_code="10045",
            cardholder_street_address="33 Liberty Street",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.card_validations.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = response.parse()
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.card_validations.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = response.parse()
            assert_matches_type(CardValidation, card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card_validation = client.card_validations.retrieve(
            "card_validation_id",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.card_validations.with_raw_response.retrieve(
            "card_validation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = response.parse()
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.card_validations.with_streaming_response.retrieve(
            "card_validation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = response.parse()
            assert_matches_type(CardValidation, card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_validation_id` but received ''"):
            client.card_validations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card_validation = client.card_validations.list()
        assert_matches_type(SyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card_validation = client.card_validations.list(
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
            status={"in": ["requires_attention"]},
        )
        assert_matches_type(SyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.card_validations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = response.parse()
        assert_matches_type(SyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.card_validations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = response.parse()
            assert_matches_type(SyncPage[CardValidation], card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardValidations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_validation = await async_client.card_validations.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_validation = await async_client.card_validations.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
            cardholder_first_name="Dee",
            cardholder_last_name="Hock",
            cardholder_middle_name="Ward",
            cardholder_postal_code="10045",
            cardholder_street_address="33 Liberty Street",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_validations.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = await response.parse()
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_validations.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            card_token_id="outbound_card_token_zlt0ml6youq3q7vcdlg0",
            merchant_category_code="1234",
            merchant_city_name="New York",
            merchant_name="Acme Corp",
            merchant_postal_code="10045",
            merchant_state="NY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = await response.parse()
            assert_matches_type(CardValidation, card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        card_validation = await async_client.card_validations.retrieve(
            "card_validation_id",
        )
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_validations.with_raw_response.retrieve(
            "card_validation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = await response.parse()
        assert_matches_type(CardValidation, card_validation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_validations.with_streaming_response.retrieve(
            "card_validation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = await response.parse()
            assert_matches_type(CardValidation, card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_validation_id` but received ''"):
            await async_client.card_validations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        card_validation = await async_client.card_validations.list()
        assert_matches_type(AsyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_validation = await async_client.card_validations.list(
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
            status={"in": ["requires_attention"]},
        )
        assert_matches_type(AsyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_validations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_validation = await response.parse()
        assert_matches_type(AsyncPage[CardValidation], card_validation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_validations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_validation = await response.parse()
            assert_matches_type(AsyncPage[CardValidation], card_validation, path=["response"])

        assert cast(Any, response.is_closed) is True
