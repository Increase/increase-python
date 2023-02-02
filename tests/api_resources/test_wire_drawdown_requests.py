# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import WireDrawdownRequest
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireDrawdownRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.wire_drawdown_requests.create(
            account_number_id="string",
            amount=1,
            message_to_recipient="x",
            recipient_account_number="x",
            recipient_routing_number="x",
            recipient_name="x",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.wire_drawdown_requests.create(
            account_number_id="string",
            amount=1,
            message_to_recipient="x",
            recipient_account_number="x",
            recipient_routing_number="x",
            recipient_name="x",
            recipient_address_line1="x",
            recipient_address_line2="x",
            recipient_address_line3="x",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.wire_drawdown_requests.retrieve(
            "string",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.wire_drawdown_requests.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.wire_drawdown_requests.list(
            cursor="string",
            limit=0,
        )
        assert isinstance(resource, SyncPage)


class TestAsyncWireDrawdownRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.wire_drawdown_requests.create(
            account_number_id="string",
            amount=1,
            message_to_recipient="x",
            recipient_account_number="x",
            recipient_routing_number="x",
            recipient_name="x",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.wire_drawdown_requests.create(
            account_number_id="string",
            amount=1,
            message_to_recipient="x",
            recipient_account_number="x",
            recipient_routing_number="x",
            recipient_name="x",
            recipient_address_line1="x",
            recipient_address_line2="x",
            recipient_address_line3="x",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.wire_drawdown_requests.retrieve(
            "string",
        )
        assert isinstance(resource, WireDrawdownRequest)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.wire_drawdown_requests.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.wire_drawdown_requests.list(
            cursor="string",
            limit=0,
        )
        assert isinstance(resource, AsyncPage)
