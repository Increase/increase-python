# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACHTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_acknowledge(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.acknowledge(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_acknowledge(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.acknowledge(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_acknowledge(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.acknowledge(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_acknowledge(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.acknowledge(
                "",
            )

    @parametrize
    def test_method_create_notification_of_change(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_create_notification_of_change(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create_notification_of_change(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_notification_of_change(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.create_notification_of_change(
                ach_transfer_id="",
                change_code="incorrect_routing_number",
                corrected_data="123456789",
            )

    @parametrize
    def test_method_return(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_return_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            reason="insufficient_fund",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_return(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_return(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_return(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.return_(
                ach_transfer_id="",
            )

    @parametrize
    def test_method_settle(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.settle(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_settle(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.settle(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_settle(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.settle(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_settle(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.settle(
                "",
            )

    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.submit(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.submit(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.submit(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.submit(
                "",
            )


class TestAsyncACHTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_acknowledge(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.acknowledge(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_acknowledge(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.acknowledge(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = await response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_acknowledge(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.acknowledge(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_acknowledge(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.acknowledge(
                "",
            )

    @parametrize
    async def test_method_create_notification_of_change(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create_notification_of_change(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = await response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create_notification_of_change(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.create_notification_of_change(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_notification_of_change(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.create_notification_of_change(
                ach_transfer_id="",
                change_code="incorrect_routing_number",
                corrected_data="123456789",
            )

    @parametrize
    async def test_method_return(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_return_with_all_params(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
            reason="insufficient_fund",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_return(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = await response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_return(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.return_(
            ach_transfer_id="ach_transfer_uoxatyh3lt5evrsdvo7q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_return(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.return_(
                ach_transfer_id="",
            )

    @parametrize
    async def test_method_settle(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.settle(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_settle(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.settle(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = await response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_settle(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.settle(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_settle(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.settle(
                "",
            )

    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.submit(
            "ach_transfer_id",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.submit(
            "ach_transfer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = await response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.submit(
            "ach_transfer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.submit(
                "",
            )
