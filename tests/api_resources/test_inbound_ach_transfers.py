# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundACHTransfer
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestInboundACHTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.list()
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="pending",
        )
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_decline(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.decline(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_decline(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.decline(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_notification_of_change(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.notification_of_change(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_notification_of_change_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.notification_of_change(
            "string",
            updated_account_number="987654321",
            updated_routing_number="101050001",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_notification_of_change(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.notification_of_change(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_transfer_return(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_transfer_return(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])


class TestAsyncInboundACHTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.inbound_ach_transfers.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.list()
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="pending",
        )
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.inbound_ach_transfers.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_decline(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.decline(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_decline(self, client: AsyncIncrease) -> None:
        response = await client.inbound_ach_transfers.with_raw_response.decline(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_notification_of_change(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.notification_of_change(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_notification_of_change_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.notification_of_change(
            "string",
            updated_account_number="987654321",
            updated_routing_number="101050001",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_notification_of_change(self, client: AsyncIncrease) -> None:
        response = await client.inbound_ach_transfers.with_raw_response.notification_of_change(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_transfer_return(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_transfer_return(self, client: AsyncIncrease) -> None:
        response = await client.inbound_ach_transfers.with_raw_response.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])
