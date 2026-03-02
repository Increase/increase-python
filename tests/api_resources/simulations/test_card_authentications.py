# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardPayment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardAuthentications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_authentication = client.simulations.card_authentications.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_authentication = client.simulations.card_authentications.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            category="payment_authentication",
            device_channel="app",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_country="US",
            merchant_name="x",
            purchase_amount=1000,
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.simulations.card_authentications.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.simulations.card_authentications.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_challenge_attempts(self, client: Increase) -> None:
        card_authentication = client.simulations.card_authentications.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_raw_response_challenge_attempts(self, client: Increase) -> None:
        response = client.simulations.card_authentications.with_raw_response.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_streaming_response_challenge_attempts(self, client: Increase) -> None:
        with client.simulations.card_authentications.with_streaming_response.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_challenge_attempts(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_payment_id` but received ''"):
            client.simulations.card_authentications.with_raw_response.challenge_attempts(
                card_payment_id="",
                one_time_code="123456",
            )

    @parametrize
    def test_method_challenges(self, client: Increase) -> None:
        card_authentication = client.simulations.card_authentications.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_raw_response_challenges(self, client: Increase) -> None:
        response = client.simulations.card_authentications.with_raw_response.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    def test_streaming_response_challenges(self, client: Increase) -> None:
        with client.simulations.card_authentications.with_streaming_response.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_challenges(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_payment_id` but received ''"):
            client.simulations.card_authentications.with_raw_response.challenges(
                "",
            )


class TestAsyncCardAuthentications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_authentication = await async_client.simulations.card_authentications.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_authentication = await async_client.simulations.card_authentications.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
            category="payment_authentication",
            device_channel="app",
            merchant_acceptor_id="5665270011000168",
            merchant_category_code="5734",
            merchant_country="US",
            merchant_name="x",
            purchase_amount=1000,
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_authentications.with_raw_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = await response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_authentications.with_streaming_response.create(
            card_id="card_oubs0hwk5rn6knuecxg2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = await response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_challenge_attempts(self, async_client: AsyncIncrease) -> None:
        card_authentication = await async_client.simulations.card_authentications.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_raw_response_challenge_attempts(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_authentications.with_raw_response.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = await response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_streaming_response_challenge_attempts(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_authentications.with_streaming_response.challenge_attempts(
            card_payment_id="card_payment_nd3k2kacrqjli8482ave",
            one_time_code="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = await response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_challenge_attempts(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_payment_id` but received ''"):
            await async_client.simulations.card_authentications.with_raw_response.challenge_attempts(
                card_payment_id="",
                one_time_code="123456",
            )

    @parametrize
    async def test_method_challenges(self, async_client: AsyncIncrease) -> None:
        card_authentication = await async_client.simulations.card_authentications.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        )
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_raw_response_challenges(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.card_authentications.with_raw_response.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authentication = await response.parse()
        assert_matches_type(CardPayment, card_authentication, path=["response"])

    @parametrize
    async def test_streaming_response_challenges(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.card_authentications.with_streaming_response.challenges(
            "card_payment_nd3k2kacrqjli8482ave",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authentication = await response.parse()
            assert_matches_type(CardPayment, card_authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_challenges(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_payment_id` but received ''"):
            await async_client.simulations.card_authentications.with_raw_response.challenges(
                "",
            )
