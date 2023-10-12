# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import OauthConnection
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
    def test_method_list(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.list()
        assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        oauth_connection = client.oauth_connections.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[OauthConnection], oauth_connection, path=["response"])


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
    async def test_method_list(self, client: AsyncIncrease) -> None:
        oauth_connection = await client.oauth_connections.list()
        assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        oauth_connection = await client.oauth_connections.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[OauthConnection], oauth_connection, path=["response"])
