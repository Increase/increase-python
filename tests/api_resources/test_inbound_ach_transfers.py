# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundACHTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


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
            limit=0,
            status="pending",
        )
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_decline(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.decline(
            "string",
        )
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
            updated_account_number="x",
            updated_routing_number="x",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_transfer_return(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.transfer_return(
            "string",
            reason="authorization_revoked_by_customer",
        )
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
            limit=0,
            status="pending",
        )
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_decline(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.decline(
            "string",
        )
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
            updated_account_number="x",
            updated_routing_number="x",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_transfer_return(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer = await client.inbound_ach_transfers.transfer_return(
            "string",
            reason="authorization_revoked_by_customer",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])
