# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import WireDrawdownRequest
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireDrawdownRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
            debtor_account_number="987654321",
            debtor_external_account_id="debtor_external_account_id",
            debtor_routing_number="101050001",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.wire_drawdown_requests.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.wire_drawdown_requests.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.retrieve(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.wire_drawdown_requests.with_raw_response.retrieve(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.wire_drawdown_requests.with_streaming_response.retrieve(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            client.wire_drawdown_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.list()
        assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        wire_drawdown_request = client.wire_drawdown_requests.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_submission"]},
        )
        assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.wire_drawdown_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = response.parse()
        assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.wire_drawdown_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = response.parse()
            assert_matches_type(SyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWireDrawdownRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.wire_drawdown_requests.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "x",
                "postal_code": "10045",
                "state": "NY",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
            debtor_account_number="987654321",
            debtor_external_account_id="debtor_external_account_id",
            debtor_routing_number="101050001",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.wire_drawdown_requests.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = await response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.wire_drawdown_requests.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=10000,
            creditor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            creditor_name="National Phonograph Company",
            debtor_address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
            },
            debtor_name="Ian Crease",
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = await response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.wire_drawdown_requests.retrieve(
            "wire_drawdown_request_id",
        )
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.wire_drawdown_requests.with_raw_response.retrieve(
            "wire_drawdown_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = await response.parse()
        assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.wire_drawdown_requests.with_streaming_response.retrieve(
            "wire_drawdown_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = await response.parse()
            assert_matches_type(WireDrawdownRequest, wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `wire_drawdown_request_id` but received ''"
        ):
            await async_client.wire_drawdown_requests.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.wire_drawdown_requests.list()
        assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        wire_drawdown_request = await async_client.wire_drawdown_requests.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_submission"]},
        )
        assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.wire_drawdown_requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_drawdown_request = await response.parse()
        assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.wire_drawdown_requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_drawdown_request = await response.parse()
            assert_matches_type(AsyncPage[WireDrawdownRequest], wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True
