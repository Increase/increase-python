# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckDeposit
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCheckDeposits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        check_deposit = client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.check_deposits.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.check_deposits.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        check_deposit = client.check_deposits.retrieve(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.check_deposits.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.check_deposits.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list()
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.check_deposits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.check_deposits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckDeposits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.check_deposits.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.check_deposits.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            currency="USD",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.retrieve(
            "string",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.check_deposits.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.check_deposits.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.list()
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        check_deposit = await client.check_deposits.list(
            account_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.check_deposits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.check_deposits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True
