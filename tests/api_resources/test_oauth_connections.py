# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.oauth_connection import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestOauthConnections:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.oauth_connections.retrieve(
            "string",
        )
        assert isinstance(resource, OauthConnection)

    def test_method_list(self) -> None:
        resource = self.client.oauth_connections.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.oauth_connections.list(
            {
                "cursor": "x",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncOauthConnections:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.oauth_connections.retrieve(
            "string",
        )
        assert isinstance(resource, OauthConnection)

    async def test_method_list(self) -> None:
        resource = await self.client.oauth_connections.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.oauth_connections.list(
            {
                "cursor": "x",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)
