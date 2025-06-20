# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundMailItem
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundMailItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_mail_item = client.inbound_mail_items.retrieve(
            "inbound_mail_item_id",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_mail_items.with_raw_response.retrieve(
            "inbound_mail_item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = response.parse()
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.inbound_mail_items.with_streaming_response.retrieve(
            "inbound_mail_item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = response.parse()
            assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_mail_item_id` but received ''"):
            client.inbound_mail_items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_mail_item = client.inbound_mail_items.list()
        assert_matches_type(SyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_mail_item = client.inbound_mail_items.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
            lockbox_id="lockbox_id",
        )
        assert_matches_type(SyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_mail_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = response.parse()
        assert_matches_type(SyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.inbound_mail_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = response.parse()
            assert_matches_type(SyncPage[InboundMailItem], inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundMailItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        inbound_mail_item = await async_client.inbound_mail_items.retrieve(
            "inbound_mail_item_id",
        )
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_mail_items.with_raw_response.retrieve(
            "inbound_mail_item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = await response.parse()
        assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_mail_items.with_streaming_response.retrieve(
            "inbound_mail_item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = await response.parse()
            assert_matches_type(InboundMailItem, inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbound_mail_item_id` but received ''"):
            await async_client.inbound_mail_items.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        inbound_mail_item = await async_client.inbound_mail_items.list()
        assert_matches_type(AsyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_mail_item = await async_client.inbound_mail_items.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            limit=1,
            lockbox_id="lockbox_id",
        )
        assert_matches_type(AsyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_mail_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_mail_item = await response.parse()
        assert_matches_type(AsyncPage[InboundMailItem], inbound_mail_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_mail_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_mail_item = await response.parse()
            assert_matches_type(AsyncPage[InboundMailItem], inbound_mail_item, path=["response"])

        assert cast(Any, response.is_closed) is True
