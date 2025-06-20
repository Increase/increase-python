# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundCheckDeposit
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundCheckDeposits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_check_deposit = client.inbound_check_deposits.retrieve(
            "inbound_check_deposit_id",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_check_deposits.with_raw_response.retrieve(
            "inbound_check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.inbound_check_deposits.with_streaming_response.retrieve(
            "inbound_check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            client.inbound_check_deposits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_check_deposit = client.inbound_check_deposits.list()
        assert_matches_type(SyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_check_deposit = client.inbound_check_deposits.list(
            account_id="account_id",
            check_transfer_id="check_transfer_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_check_deposits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(SyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.inbound_check_deposits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(SyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_decline(self, client: Increase) -> None:
        inbound_check_deposit = client.inbound_check_deposits.decline(
            "inbound_check_deposit_id",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_decline(self, client: Increase) -> None:
        response = client.inbound_check_deposits.with_raw_response.decline(
            "inbound_check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_decline(self, client: Increase) -> None:
        with client.inbound_check_deposits.with_streaming_response.decline(
            "inbound_check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_decline(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            client.inbound_check_deposits.with_raw_response.decline(
                "",
            )

    @parametrize
    def test_method_return(self, client: Increase) -> None:
        inbound_check_deposit = client.inbound_check_deposits.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_raw_response_return(self, client: Increase) -> None:
        response = client.inbound_check_deposits.with_raw_response.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    def test_streaming_response_return(self, client: Increase) -> None:
        with client.inbound_check_deposits.with_streaming_response.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_return(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            client.inbound_check_deposits.with_raw_response.return_(
                inbound_check_deposit_id="",
                reason="altered_or_fictitious",
            )


class TestAsyncInboundCheckDeposits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.inbound_check_deposits.retrieve(
            "inbound_check_deposit_id",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_check_deposits.with_raw_response.retrieve(
            "inbound_check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_check_deposits.with_streaming_response.retrieve(
            "inbound_check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            await async_client.inbound_check_deposits.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.inbound_check_deposits.list()
        assert_matches_type(AsyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.inbound_check_deposits.list(
            account_id="account_id",
            check_transfer_id="check_transfer_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_check_deposits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(AsyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_check_deposits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(AsyncPage[InboundCheckDeposit], inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_decline(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.inbound_check_deposits.decline(
            "inbound_check_deposit_id",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_decline(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_check_deposits.with_raw_response.decline(
            "inbound_check_deposit_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_decline(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_check_deposits.with_streaming_response.decline(
            "inbound_check_deposit_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_decline(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            await async_client.inbound_check_deposits.with_raw_response.decline(
                "",
            )

    @parametrize
    async def test_method_return(self, async_client: AsyncIncrease) -> None:
        inbound_check_deposit = await async_client.inbound_check_deposits.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        )
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_raw_response_return(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_check_deposits.with_raw_response.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_check_deposit = await response.parse()
        assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

    @parametrize
    async def test_streaming_response_return(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_check_deposits.with_streaming_response.return_(
            inbound_check_deposit_id="inbound_check_deposit_zoshvqybq0cjjm31mra",
            reason="altered_or_fictitious",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_check_deposit = await response.parse()
            assert_matches_type(InboundCheckDeposit, inbound_check_deposit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_return(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_check_deposit_id` but received ''"
        ):
            await async_client.inbound_check_deposits.with_raw_response.return_(
                inbound_check_deposit_id="",
                reason="altered_or_fictitious",
            )
