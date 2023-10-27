# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import WireTransfer
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestWireTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
            account_number="987654321",
            beneficiary_address_line1="33 Liberty Street",
            beneficiary_address_line2="New York",
            beneficiary_address_line3="NY 10045",
            external_account_id="string",
            require_approval=True,
            routing_number="101050001",
            unique_identifier="x",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.retrieve(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.list()
        assert_matches_type(SyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=1,
            unique_identifier="x",
        )
        assert_matches_type(SyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(SyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.approve(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.approve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.cancel(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.cancel(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_reverse(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.reverse(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_raw_response_reverse(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.reverse(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        wire_transfer = client.wire_transfers.submit(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.wire_transfers.with_raw_response.submit(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])


class TestAsyncWireTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
            account_number="987654321",
            beneficiary_address_line1="33 Liberty Street",
            beneficiary_address_line2="New York",
            beneficiary_address_line3="NY 10045",
            external_account_id="string",
            require_approval=True,
            routing_number="101050001",
            unique_identifier="x",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            beneficiary_name="Ian Crease",
            message_to_recipient="New account transfer",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.retrieve(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.list()
        assert_matches_type(AsyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            external_account_id="string",
            limit=1,
            unique_identifier="x",
        )
        assert_matches_type(AsyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(AsyncPage[WireTransfer], wire_transfer, path=["response"])

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.approve(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.approve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_method_cancel(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.cancel(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.cancel(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_reverse(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.reverse(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_raw_response_reverse(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.reverse(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_submit(self, client: AsyncIncrease) -> None:
        wire_transfer = await client.wire_transfers.submit(
            "string",
        )
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_raw_response_submit(self, client: AsyncIncrease) -> None:
        response = await client.wire_transfers.with_raw_response.submit(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(WireTransfer, wire_transfer, path=["response"])
