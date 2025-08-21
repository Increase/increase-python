# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundWireTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundWireTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_wire_transfer = client.simulations.inbound_wire_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_wire_transfer = client.simulations.inbound_wire_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            creditor_address_line1="x",
            creditor_address_line2="x",
            creditor_address_line3="x",
            creditor_name="x",
            debtor_address_line1="x",
            debtor_address_line2="x",
            debtor_address_line3="x",
            debtor_name="x",
            end_to_end_identification="x",
            instructing_agent_routing_number="x",
            instruction_identification="x",
            unique_end_to_end_transaction_reference="x",
            unstructured_remittance_information="x",
            wire_drawdown_request_id="wire_drawdown_request_id",
        )
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_wire_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_transfer = response.parse()
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_wire_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_transfer = response.parse()
            assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundWireTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_wire_transfer = await async_client.simulations.inbound_wire_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_wire_transfer = await async_client.simulations.inbound_wire_transfers.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            creditor_address_line1="x",
            creditor_address_line2="x",
            creditor_address_line3="x",
            creditor_name="x",
            debtor_address_line1="x",
            debtor_address_line2="x",
            debtor_address_line3="x",
            debtor_name="x",
            end_to_end_identification="x",
            instructing_agent_routing_number="x",
            instruction_identification="x",
            unique_end_to_end_transaction_reference="x",
            unstructured_remittance_information="x",
            wire_drawdown_request_id="wire_drawdown_request_id",
        )
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_wire_transfers.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_transfer = await response.parse()
        assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_wire_transfers.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_transfer = await response.parse()
            assert_matches_type(InboundWireTransfer, inbound_wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
