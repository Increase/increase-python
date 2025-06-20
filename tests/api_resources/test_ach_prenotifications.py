# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHPrenotification
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACHPrenotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date=parse_date("2019-12-27"),
            individual_id="x",
            individual_name="x",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.ach_prenotifications.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = response.parse()
            assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.retrieve(
            "ach_prenotification_id",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.retrieve(
            "ach_prenotification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.ach_prenotifications.with_streaming_response.retrieve(
            "ach_prenotification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = response.parse()
            assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `ach_prenotification_id` but received ''"
        ):
            client.ach_prenotifications.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.list()
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        ach_prenotification = client.ach_prenotifications.list(
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
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.ach_prenotifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = response.parse()
        assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.ach_prenotifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = response.parse()
            assert_matches_type(SyncPage[ACHPrenotification], ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncACHPrenotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        ach_prenotification = await async_client.ach_prenotifications.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        ach_prenotification = await async_client.ach_prenotifications.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
            addendum="x",
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_name="x",
            credit_debit_indicator="credit",
            effective_date=parse_date("2019-12-27"),
            individual_id="x",
            individual_name="x",
            standard_entry_class_code="corporate_credit_or_debit",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.ach_prenotifications.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = await response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.ach_prenotifications.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            account_number="987654321",
            routing_number="101050001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = await response.parse()
            assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        ach_prenotification = await async_client.ach_prenotifications.retrieve(
            "ach_prenotification_id",
        )
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.ach_prenotifications.with_raw_response.retrieve(
            "ach_prenotification_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = await response.parse()
        assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.ach_prenotifications.with_streaming_response.retrieve(
            "ach_prenotification_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = await response.parse()
            assert_matches_type(ACHPrenotification, ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `ach_prenotification_id` but received ''"
        ):
            await async_client.ach_prenotifications.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        ach_prenotification = await async_client.ach_prenotifications.list()
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        ach_prenotification = await async_client.ach_prenotifications.list(
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
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.ach_prenotifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_prenotification = await response.parse()
        assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.ach_prenotifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_prenotification = await response.parse()
            assert_matches_type(AsyncPage[ACHPrenotification], ach_prenotification, path=["response"])

        assert cast(Any, response.is_closed) is True
