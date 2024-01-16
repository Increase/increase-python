# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import OauthConnection
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestOauthConnections:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.retrieve(
            "string",
        )
        assert_matches_type(OauthConnection, oauth_connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.oauth_connections.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(OauthConnection, oauth_connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.oauth_connections.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = response.parse()
            assert_matches_type(OauthConnection, oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_connection_id` but received ''"):
            client.oauth_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.list()
        assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.list(
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.oauth_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.oauth_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = response.parse()
            assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOauthConnections:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        oauth_connection = await client.oauth_connections.retrieve(
            "string",
        )
        assert_matches_type(OauthConnection, oauth_connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.oauth_connections.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(OauthConnection, oauth_connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.oauth_connections.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = await response.parse()
            assert_matches_type(OauthConnection, oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_connection_id` but received ''"):
            await client.oauth_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        oauth_connection = await client.oauth_connections.list()
        assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        oauth_connection = await client.oauth_connections.list(
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.oauth_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.oauth_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = await response.parse()
            assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
