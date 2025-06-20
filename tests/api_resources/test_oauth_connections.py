# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import OAuthConnection
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.retrieve(
            "x",
        )
        assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.oauth_connections.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.oauth_connections.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = response.parse()
            assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

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
        assert_matches_type(SyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.list(
            cursor="cursor",
            limit=1,
            oauth_application_id="oauth_application_id",
            status={"in": ["active"]},
        )
        assert_matches_type(SyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.oauth_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = response.parse()
        assert_matches_type(SyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.oauth_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = response.parse()
            assert_matches_type(SyncPage[OAuthConnection], oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuthConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        oauth_connection = await async_client.oauth_connections.retrieve(
            "x",
        )
        assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.oauth_connections.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = await response.parse()
        assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.oauth_connections.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = await response.parse()
            assert_matches_type(OAuthConnection, oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_connection_id` but received ''"):
            await async_client.oauth_connections.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        oauth_connection = await async_client.oauth_connections.list()
        assert_matches_type(AsyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        oauth_connection = await async_client.oauth_connections.list(
            cursor="cursor",
            limit=1,
            oauth_application_id="oauth_application_id",
            status={"in": ["active"]},
        )
        assert_matches_type(AsyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.oauth_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_connection = await response.parse()
        assert_matches_type(AsyncPage[OAuthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.oauth_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_connection = await response.parse()
            assert_matches_type(AsyncPage[OAuthConnection], oauth_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
