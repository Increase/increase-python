# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    CardPayment,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_card_authorization_expirations(self, client: Increase) -> None:
        simulation = client.simulations.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_raw_response_card_authorization_expirations(self, client: Increase) -> None:
        response = client.simulations.with_raw_response.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_streaming_response_card_authorization_expirations(self, client: Increase) -> None:
        with client.simulations.with_streaming_response.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_card_fuel_confirmations(self, client: Increase) -> None:
        simulation = client.simulations.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_raw_response_card_fuel_confirmations(self, client: Increase) -> None:
        response = client.simulations.with_raw_response.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_streaming_response_card_fuel_confirmations(self, client: Increase) -> None:
        with client.simulations.with_streaming_response.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_card_increments(self, client: Increase) -> None:
        simulation = client.simulations.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_method_card_increments_with_all_params(self, client: Increase) -> None:
        simulation = client.simulations.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            event_subscription_id="string",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_raw_response_card_increments(self, client: Increase) -> None:
        response = client.simulations.with_raw_response.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_streaming_response_card_increments(self, client: Increase) -> None:
        with client.simulations.with_streaming_response.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_card_reversals(self, client: Increase) -> None:
        simulation = client.simulations.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_method_card_reversals_with_all_params(self, client: Increase) -> None:
        simulation = client.simulations.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            amount=1,
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_raw_response_card_reversals(self, client: Increase) -> None:
        response = client.simulations.with_raw_response.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    def test_streaming_response_card_reversals(self, client: Increase) -> None:
        with client.simulations.with_streaming_response.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_card_authorization_expirations(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_raw_response_card_authorization_expirations(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.with_raw_response.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_card_authorization_expirations(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.with_streaming_response.card_authorization_expirations(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_card_fuel_confirmations(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_raw_response_card_fuel_confirmations(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.with_raw_response.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_card_fuel_confirmations(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.with_streaming_response.card_fuel_confirmations(
            amount=5000,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_card_increments(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_method_card_increments_with_all_params(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            event_subscription_id="string",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_raw_response_card_increments(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.with_raw_response.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_card_increments(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.with_streaming_response.card_increments(
            amount=500,
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_card_reversals(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_method_card_reversals_with_all_params(self, async_client: AsyncIncrease) -> None:
        simulation = await async_client.simulations.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            amount=1,
        )
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_raw_response_card_reversals(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.with_raw_response.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulation = response.parse()
        assert_matches_type(CardPayment, simulation, path=["response"])

    @parametrize
    async def test_streaming_response_card_reversals(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.with_streaming_response.card_reversals(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulation = await response.parse()
            assert_matches_type(CardPayment, simulation, path=["response"])

        assert cast(Any, response.is_closed) is True
