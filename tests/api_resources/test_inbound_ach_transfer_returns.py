# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundACHTransferReturn
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestInboundACHTransferReturns:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_ach_transfer_return = client.inbound_ach_transfer_returns.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransferReturn, inbound_ach_transfer_return, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_ach_transfer_return = client.inbound_ach_transfer_returns.list()
        assert_matches_type(SyncPage[InboundACHTransferReturn], inbound_ach_transfer_return, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer_return = client.inbound_ach_transfer_returns.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[InboundACHTransferReturn], inbound_ach_transfer_return, path=["response"])


class TestAsyncInboundACHTransferReturns:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer_return = await client.inbound_ach_transfer_returns.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransferReturn, inbound_ach_transfer_return, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer_return = await client.inbound_ach_transfer_returns.list()
        assert_matches_type(AsyncPage[InboundACHTransferReturn], inbound_ach_transfer_return, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        inbound_ach_transfer_return = await client.inbound_ach_transfer_returns.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[InboundACHTransferReturn], inbound_ach_transfer_return, path=["response"])
