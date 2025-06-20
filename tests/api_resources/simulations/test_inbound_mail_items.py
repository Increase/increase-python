# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundMailItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundMailItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_mail_item = client.simulations.inbound_mail_items.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_mail_item = client.simulations.inbound_mail_items.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
            contents_file_id="contents_file_id",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_mail_items.with_raw_response.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = response.parse()
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_mail_items.with_streaming_response.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = response.parse()
            assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundMailItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_mail_item = await async_client.simulations.inbound_mail_items.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_mail_item = await async_client.simulations.inbound_mail_items.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
            contents_file_id="contents_file_id",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_mail_items.with_raw_response.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = await response.parse()
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_mail_items.with_streaming_response.create(
            amount=1000,
            lockbox_id="lockbox_3xt21ok13q19advds4t5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = await response.parse()
            assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True
