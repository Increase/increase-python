# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckDeposit
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckDeposits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        check_deposit = client.check_deposits.create(
            account_id="string",
            amount=0,
            currency="x",
            front_image_file_id="string",
            back_image_file_id="string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        check_deposit = client.check_deposits.retrieve(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list()
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list(
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
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])


class TestAsyncCheckDeposits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.create(
            account_id="string",
            amount=0,
            currency="x",
            front_image_file_id="string",
            back_image_file_id="string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.retrieve(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.list()
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.list(
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
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])
