# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckDeposit
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckDeposits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        check_deposit = client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        check_deposit = client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
            description="Vendor payment",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.check_deposits.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
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
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.check_deposits.with_raw_response.retrieve(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.check_deposits.with_streaming_response.retrieve(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            client.check_deposits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list()
        assert_matches_type(SyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        check_deposit = client.check_deposits.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
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
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.check_deposits.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
            description="Vendor payment",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_deposits.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_deposits.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=1000,
            back_image_file_id="file_26khfk98mzfz90a11oqx",
            front_image_file_id="file_hkv175ovmc2tb2v2zbrm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.check_deposits.retrieve(
            "check_deposit_id",
        )
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_deposits.with_raw_response.retrieve(
            "check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(CheckDeposit, check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_deposits.with_streaming_response.retrieve(
            "check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(CheckDeposit, check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_deposit_id` but received ''"):
            await async_client.check_deposits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.check_deposits.list()
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        check_deposit = await async_client.check_deposits.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.check_deposits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_deposit = await response.parse()
        assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.check_deposits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_deposit = await response.parse()
            assert_matches_type(AsyncPage[CheckDeposit], check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True
