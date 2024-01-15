# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import DigitalWalletToken
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestDigitalWalletTokens:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        digital_wallet_token = client.digital_wallet_tokens.retrieve(
            "string",
        )
        assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.digital_wallet_tokens.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token = response.parse()
        assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.digital_wallet_tokens.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token = response.parse()
            assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        digital_wallet_token = client.digital_wallet_tokens.list()
        assert_matches_type(SyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        digital_wallet_token = client.digital_wallet_tokens.list(
            card_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.digital_wallet_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token = response.parse()
        assert_matches_type(SyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.digital_wallet_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token = response.parse()
            assert_matches_type(SyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDigitalWalletTokens:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        digital_wallet_token = await client.digital_wallet_tokens.retrieve(
            "string",
        )
        assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.digital_wallet_tokens.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token = response.parse()
        assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.digital_wallet_tokens.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token = await response.parse()
            assert_matches_type(DigitalWalletToken, digital_wallet_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        digital_wallet_token = await client.digital_wallet_tokens.list()
        assert_matches_type(AsyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        digital_wallet_token = await client.digital_wallet_tokens.list(
            card_id="string",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.digital_wallet_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_wallet_token = response.parse()
        assert_matches_type(AsyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.digital_wallet_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_wallet_token = await response.parse()
            assert_matches_type(AsyncPage[DigitalWalletToken], digital_wallet_token, path=["response"])

        assert cast(Any, response.is_closed) is True
