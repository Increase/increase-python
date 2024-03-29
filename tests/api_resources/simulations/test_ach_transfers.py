# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ACHTransfer, InboundACHTransfer
from increase._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACHTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_id="x",
            company_name="x",
            receiver_id_number="x",
            receiver_name="x",
            resolve_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_create_inbound(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create_inbound(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_notification_of_change(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_raw_response_notification_of_change(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    def test_streaming_response_notification_of_change(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_notification_of_change(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.notification_of_change(
                "",
                change_code="incorrect_routing_number",
                corrected_data="123456789",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_return(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.return_(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_return_with_all_params(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.return_(
            "string",
            reason="insufficient_fund",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_raw_response_return(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.return_(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_streaming_response_return(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.return_(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_path_params_return(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.return_(
                "",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_submit(self, client: Increase) -> None:
        ach_transfer = client.simulations.ach_transfers.submit(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_raw_response_submit(self, client: Increase) -> None:
        response = client.simulations.ach_transfers.with_raw_response.submit(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_streaming_response_submit(self, client: Increase) -> None:
        with client.simulations.ach_transfers.with_streaming_response.submit(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_path_params_submit(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            client.simulations.ach_transfers.with_raw_response.submit(
                "",
            )


class TestAsyncACHTransfers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_inbound(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_method_create_inbound_with_all_params(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            company_descriptive_date="x",
            company_discretionary_data="x",
            company_entry_description="x",
            company_id="x",
            company_name="x",
            receiver_id_number="x",
            receiver_name="x",
            resolve_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(InboundACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_notification_of_change(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_raw_response_notification_of_change(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_notification_of_change(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.notification_of_change(
            "string",
            change_code="incorrect_routing_number",
            corrected_data="123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_notification_of_change(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.notification_of_change(
                "",
                change_code="incorrect_routing_number",
                corrected_data="123456789",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_return(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.return_(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_return_with_all_params(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.return_(
            "string",
            reason="insufficient_fund",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_raw_response_return(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.return_(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_streaming_response_return(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.return_(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_path_params_return(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.return_(
                "",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_submit(self, async_client: AsyncIncrease) -> None:
        ach_transfer = await async_client.simulations.ach_transfers.submit(
            "string",
        )
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.ach_transfers.with_raw_response.submit(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ach_transfer = response.parse()
        assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.ach_transfers.with_streaming_response.submit(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ach_transfer = await response.parse()
            assert_matches_type(ACHTransfer, ach_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ach_transfer_id` but received ''"):
            await async_client.simulations.ach_transfers.with_raw_response.submit(
                "",
            )
