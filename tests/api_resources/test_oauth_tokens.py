# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import OAuthToken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        oauth_token = client.oauth_tokens.create(
            grant_type="authorization_code",
        )
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        oauth_token = client.oauth_tokens.create(
            grant_type="authorization_code",
            client_id="12345",
            client_secret="supersecret",
            code="123",
            production_token="x",
        )
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.oauth_tokens.with_raw_response.create(
            grant_type="authorization_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_token = response.parse()
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.oauth_tokens.with_streaming_response.create(
            grant_type="authorization_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_token = response.parse()
            assert_matches_type(OAuthToken, oauth_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuthTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        oauth_token = await async_client.oauth_tokens.create(
            grant_type="authorization_code",
        )
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        oauth_token = await async_client.oauth_tokens.create(
            grant_type="authorization_code",
            client_id="12345",
            client_secret="supersecret",
            code="123",
            production_token="x",
        )
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.oauth_tokens.with_raw_response.create(
            grant_type="authorization_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_token = await response.parse()
        assert_matches_type(OAuthToken, oauth_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.oauth_tokens.with_streaming_response.create(
            grant_type="authorization_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_token = await response.parse()
            assert_matches_type(OAuthToken, oauth_token, path=["response"])

        assert cast(Any, response.is_closed) is True
