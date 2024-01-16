# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import AccountTransfer
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccountTransfers:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_complete(self, client: Increase) -> None:
        account_transfer = client.simulations.account_transfers.complete(
            "string",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_raw_response_complete(self, client: Increase) -> None:
        response = client.simulations.account_transfers.with_raw_response.complete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_streaming_response_complete(self, client: Increase) -> None:
        with client.simulations.account_transfers.with_streaming_response.complete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_path_params_complete(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            client.simulations.account_transfers.with_raw_response.complete(
                "",
            )


class TestAsyncAccountTransfers:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_complete(self, client: AsyncIncrease) -> None:
        account_transfer = await client.simulations.account_transfers.complete(
            "string",
        )
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_raw_response_complete(self, client: AsyncIncrease) -> None:
        response = await client.simulations.account_transfers.with_raw_response.complete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_transfer = response.parse()
        assert_matches_type(AccountTransfer, account_transfer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_streaming_response_complete(self, client: AsyncIncrease) -> None:
        async with client.simulations.account_transfers.with_streaming_response.complete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_transfer = await response.parse()
            assert_matches_type(AccountTransfer, account_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_path_params_complete(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_transfer_id` but received ''"):
            await client.simulations.account_transfers.with_raw_response.complete(
                "",
            )
