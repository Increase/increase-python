# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import WireTransfer
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWireTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.wire_transfers.create(
            account_id="string",
            amount=0,
            message_to_recipient="x",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.wire_transfers.create(
            account_id="string",
            account_number="x",
            routing_number="xxxxxxxxx",
            external_account_id="string",
            amount=0,
            message_to_recipient="x",
            beneficiary_name="x",
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.wire_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.wire_transfers.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.wire_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            external_account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, SyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_reverse(self, client: Increase) -> None:
        resource = client.wire_transfers.reverse(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        resource = client.wire_transfers.submit(
            "string",
        )
        assert isinstance(resource, WireTransfer)


class TestAsyncWireTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.create(
            account_id="string",
            amount=0,
            message_to_recipient="x",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.create(
            account_id="string",
            account_number="x",
            routing_number="xxxxxxxxx",
            external_account_id="string",
            amount=0,
            message_to_recipient="x",
            beneficiary_name="x",
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            external_account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, AsyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_reverse(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.reverse(
            "string",
        )
        assert isinstance(resource, WireTransfer)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_submit(self, client: AsyncIncrease) -> None:
        resource = await client.wire_transfers.submit(
            "string",
        )
        assert isinstance(resource, WireTransfer)
