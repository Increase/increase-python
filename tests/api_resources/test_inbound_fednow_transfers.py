# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundFednowTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundFednowTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_fednow_transfer = client.inbound_fednow_transfers.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        )
        assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_fednow_transfers.with_raw_response.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_fednow_transfer = response.parse()
        assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.inbound_fednow_transfers.with_streaming_response.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_fednow_transfer = response.parse()
            assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_fednow_transfer_id` but received ''"
        ):
            client.inbound_fednow_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_fednow_transfer = client.inbound_fednow_transfers.list()
        assert_matches_type(SyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_fednow_transfer = client.inbound_fednow_transfers.list(
            account_id="account_id",
            account_number_id="account_number_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_fednow_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_fednow_transfer = response.parse()
        assert_matches_type(SyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.inbound_fednow_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_fednow_transfer = response.parse()
            assert_matches_type(SyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundFednowTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        inbound_fednow_transfer = await async_client.inbound_fednow_transfers.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        )
        assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_fednow_transfers.with_raw_response.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_fednow_transfer = await response.parse()
        assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_fednow_transfers.with_streaming_response.retrieve(
            "inbound_fednow_transfer_ctxxbc07oh5ke5w1hk20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_fednow_transfer = await response.parse()
            assert_matches_type(InboundFednowTransfer, inbound_fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_fednow_transfer_id` but received ''"
        ):
            await async_client.inbound_fednow_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        inbound_fednow_transfer = await async_client.inbound_fednow_transfers.list()
        assert_matches_type(AsyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_fednow_transfer = await async_client.inbound_fednow_transfers.list(
            account_id="account_id",
            account_number_id="account_number_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_fednow_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_fednow_transfer = await response.parse()
        assert_matches_type(AsyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_fednow_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_fednow_transfer = await response.parse()
            assert_matches_type(AsyncPage[InboundFednowTransfer], inbound_fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
