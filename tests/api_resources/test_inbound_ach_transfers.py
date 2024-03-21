# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    InboundACHTransfer,
)
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundACHTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.inbound_ach_transfers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            client.inbound_ach_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.list()
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.list(
            account_id="string",
            account_number_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="pending",
        )
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.inbound_ach_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(SyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_decline(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.decline(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_decline(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.decline(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_decline(self, client: Increase) -> None:
        with client.inbound_ach_transfers.with_streaming_response.decline(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_decline(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            client.inbound_ach_transfers.with_raw_response.decline(
                "",
            )

    @parametrize
    def test_method_notification_of_change(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.notification_of_change(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_method_notification_of_change_with_all_params(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.notification_of_change(
            "string",
            updated_account_number="987654321",
            updated_routing_number="101050001",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_notification_of_change(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.notification_of_change(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_notification_of_change(self, client: Increase) -> None:
        with client.inbound_ach_transfers.with_streaming_response.notification_of_change(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_notification_of_change(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            client.inbound_ach_transfers.with_raw_response.notification_of_change(
                "",
            )

    @parametrize
    def test_method_transfer_return(self, client: Increase) -> None:
        inbound_ach_transfer = client.inbound_ach_transfers.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_transfer_return(self, client: Increase) -> None:
        response = client.inbound_ach_transfers.with_raw_response.transfer_return(
            "string",
            reason="payment_stopped",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_transfer_return(self, client: Increase) -> None:
        with client.inbound_ach_transfers.with_streaming_response.transfer_return(
            "string",
            reason="payment_stopped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_transfer_return(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            client.inbound_ach_transfers.with_raw_response.transfer_return(
                "",
                reason="payment_stopped",
            )


class TestAsyncInboundACHTransfers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.retrieve(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_ach_transfers.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_ach_transfers.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            await async_client.inbound_ach_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.list()
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.list(
            account_id="string",
            account_number_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status="pending",
        )
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_ach_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_ach_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(AsyncPage[InboundACHTransfer], inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_decline(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.decline(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_decline(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_ach_transfers.with_raw_response.decline(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_decline(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_ach_transfers.with_streaming_response.decline(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_decline(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            await async_client.inbound_ach_transfers.with_raw_response.decline(
                "",
            )

    @parametrize
    async def test_method_notification_of_change(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.notification_of_change(
            "string",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_method_notification_of_change_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.notification_of_change(
            "string",
            updated_account_number="987654321",
            updated_routing_number="101050001",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_notification_of_change(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_ach_transfers.with_raw_response.notification_of_change(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_notification_of_change(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_ach_transfers.with_streaming_response.notification_of_change(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_notification_of_change(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            await async_client.inbound_ach_transfers.with_raw_response.notification_of_change(
                "",
            )

    @parametrize
    async def test_method_transfer_return(self, async_client: AsyncIncrease) -> None:
        inbound_ach_transfer = await async_client.inbound_ach_transfers.transfer_return(
            "string",
            reason="payment_stopped",
        )
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_transfer_return(self, async_client: AsyncIncrease) -> None:
        response = await async_client.inbound_ach_transfers.with_raw_response.transfer_return(
            "string",
            reason="payment_stopped",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_transfer_return(self, async_client: AsyncIncrease) -> None:
        async with async_client.inbound_ach_transfers.with_streaming_response.transfer_return(
            "string",
            reason="payment_stopped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, inbound_ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_transfer_return(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `inbound_ach_transfer_id` but received ''"
        ):
            await async_client.inbound_ach_transfers.with_raw_response.transfer_return(
                "",
                reason="payment_stopped",
            )
