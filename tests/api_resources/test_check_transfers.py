# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import CheckTransfer
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.check_transfers.create(
            account_id="string",
            address_line1="x",
            address_city="x",
            address_state="x",
            address_zip="x",
            amount=1,
            message="x",
            recipient_name="x",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.check_transfers.create(
            account_id="string",
            address_line1="x",
            address_line2="x",
            address_city="x",
            address_state="x",
            address_zip="x",
            return_address={
                "name": "x",
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            amount=1,
            message="x",
            note="x",
            recipient_name="x",
            require_approval=True,
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.check_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.check_transfers.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.check_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        resource = client.check_transfers.approve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        resource = client.check_transfers.cancel(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    def test_method_stop_payment(self, client: Increase) -> None:
        resource = client.check_transfers.stop_payment(
            "string",
        )
        assert isinstance(resource, CheckTransfer)


class TestAsyncCheckTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.create(
            account_id="string",
            address_line1="x",
            address_city="x",
            address_state="x",
            address_zip="x",
            amount=1,
            message="x",
            recipient_name="x",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.create(
            account_id="string",
            address_line1="x",
            address_line2="x",
            address_city="x",
            address_state="x",
            address_zip="x",
            return_address={
                "name": "x",
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            amount=1,
            message="x",
            note="x",
            recipient_name="x",
            require_approval=True,
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.retrieve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.list(
            cursor="string",
            limit=0,
            account_id="string",
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_approve(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.approve(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @parametrize
    async def test_method_cancel(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.cancel(
            "string",
        )
        assert isinstance(resource, CheckTransfer)

    @pytest.mark.skip(reason="Prism doesn't accept no request body being sent but returns 415 if it is sent")
    @parametrize
    async def test_method_stop_payment(self, client: AsyncIncrease) -> None:
        resource = await client.check_transfers.stop_payment(
            "string",
        )
        assert isinstance(resource, CheckTransfer)
