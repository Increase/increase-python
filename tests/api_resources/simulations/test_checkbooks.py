# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Checkbook

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckbooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_mail(self, client: Increase) -> None:
        checkbook = client.simulations.checkbooks.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_raw_response_mail(self, client: Increase) -> None:

        response = client.simulations.checkbooks.with_raw_response.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_streaming_response_mail(self, client: Increase) -> None:
        with client.simulations.checkbooks.with_streaming_response.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mail(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            client.simulations.checkbooks.with_raw_response.mail(
                "",
            )


class TestAsyncCheckbooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_mail(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.simulations.checkbooks.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_raw_response_mail(self, async_client: AsyncIncrease) -> None:

        response = await async_client.simulations.checkbooks.with_raw_response.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = await response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_streaming_response_mail(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.checkbooks.with_streaming_response.mail(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = await response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mail(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            await async_client.simulations.checkbooks.with_raw_response.mail(
                "",
            )
