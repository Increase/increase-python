# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import InboundWireDrawdownRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInboundWireDrawdownRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        inbound_wire_drawdown_request = client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            creditor_address_line1="33 Liberty Street",
            creditor_address_line2="New York, NY, 10045",
            creditor_address_line3="x",
            creditor_name="Ian Crease",
            debtor_account_number="987654321",
            debtor_address_line1="33 Liberty Street",
            debtor_address_line2="New York, NY, 10045",
            debtor_address_line3="x",
            debtor_name="Ian Crease",
            debtor_routing_number="101050001",
            end_to_end_identification="x",
            instruction_identification="x",
            unique_end_to_end_transaction_reference="x",
            unstructured_remittance_information="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.inbound_wire_drawdown_requests.with_raw_response.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.inbound_wire_drawdown_requests.with_streaming_response.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_drawdown_request = response.parse()
            assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInboundWireDrawdownRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await async_client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        inbound_wire_drawdown_request = await async_client.simulations.inbound_wire_drawdown_requests.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            creditor_address_line1="33 Liberty Street",
            creditor_address_line2="New York, NY, 10045",
            creditor_address_line3="x",
            creditor_name="Ian Crease",
            debtor_account_number="987654321",
            debtor_address_line1="33 Liberty Street",
            debtor_address_line2="New York, NY, 10045",
            debtor_address_line3="x",
            debtor_name="Ian Crease",
            debtor_routing_number="101050001",
            end_to_end_identification="x",
            instruction_identification="x",
            unique_end_to_end_transaction_reference="x",
            unstructured_remittance_information="x",
        )
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.inbound_wire_drawdown_requests.with_raw_response.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound_wire_drawdown_request = await response.parse()
        assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.inbound_wire_drawdown_requests.with_streaming_response.create(
            amount=10000,
            creditor_account_number="987654321",
            creditor_routing_number="101050001",
            currency="USD",
            recipient_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound_wire_drawdown_request = await response.parse()
            assert_matches_type(InboundWireDrawdownRequest, inbound_wire_drawdown_request, path=["response"])

        assert cast(Any, response.is_closed) is True
