# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckTransfer
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCheckTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_deposit(self, client: Increase) -> None:
        check_transfer = client.simulations.check_transfers.deposit(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_raw_response_deposit(self, client: Increase) -> None:
        response = client.simulations.check_transfers.with_raw_response.deposit(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    def test_streaming_response_deposit(self, client: Increase) -> None:
        with client.simulations.check_transfers.with_streaming_response.deposit(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deposit(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.simulations.check_transfers.with_raw_response.deposit(
                "",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_method_mail(self, client: Increase) -> None:
        check_transfer = client.simulations.check_transfers.mail(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_raw_response_mail(self, client: Increase) -> None:
        response = client.simulations.check_transfers.with_raw_response.mail(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_streaming_response_mail(self, client: Increase) -> None:
        with client.simulations.check_transfers.with_streaming_response.mail(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    def test_path_params_mail(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            client.simulations.check_transfers.with_raw_response.mail(
                "",
            )


class TestAsyncCheckTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_deposit(self, client: AsyncIncrease) -> None:
        check_transfer = await client.simulations.check_transfers.deposit(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_raw_response_deposit(self, client: AsyncIncrease) -> None:
        response = await client.simulations.check_transfers.with_raw_response.deposit(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_deposit(self, client: AsyncIncrease) -> None:
        async with client.simulations.check_transfers.with_streaming_response.deposit(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deposit(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.simulations.check_transfers.with_raw_response.deposit(
                "",
            )

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_method_mail(self, client: AsyncIncrease) -> None:
        check_transfer = await client.simulations.check_transfers.mail(
            "string",
        )
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_raw_response_mail(self, client: AsyncIncrease) -> None:
        response = await client.simulations.check_transfers.with_raw_response.mail(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check_transfer = response.parse()
        assert_matches_type(CheckTransfer, check_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_streaming_response_mail(self, client: AsyncIncrease) -> None:
        async with client.simulations.check_transfers.with_streaming_response.mail(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check_transfer = await response.parse()
            assert_matches_type(CheckTransfer, check_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism incorrectly returns an invalid JSON error")
    @parametrize
    async def test_path_params_mail(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `check_transfer_id` but received ''"):
            await client.simulations.check_transfers.with_raw_response.mail(
                "",
            )
