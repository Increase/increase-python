# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.card import *
from increase.types.card_detail import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.cards.create(
            {"account_id": "account_in71c4amph0vgo2qllky"},
        )
        assert isinstance(resource, Card)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.cards.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "description": "Card for Ian Crease",
                "billing_address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "postal_code": "x",
                },
            },
        )
        assert isinstance(resource, Card)

    def test_method_retrieve(self) -> None:
        resource = self.client.cards.retrieve(
            "string",
        )
        assert isinstance(resource, Card)

    def test_method_update(self) -> None:
        resource = self.client.cards.update(
            "string",
            {},
        )
        assert isinstance(resource, Card)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.cards.update(
            "string",
            {
                "description": "New description",
                "status": "active",
                "billing_address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "postal_code": "x",
                },
            },
        )
        assert isinstance(resource, Card)

    def test_method_list(self) -> None:
        resource = self.client.cards.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.cards.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, SyncPage)

    def test_method_retrieve_sensitive_details(self) -> None:
        resource = self.client.cards.retrieve_sensitive_details(
            "string",
        )
        assert isinstance(resource, CardDetails)


class TestAsyncCards:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.cards.create(
            {"account_id": "account_in71c4amph0vgo2qllky"},
        )
        assert isinstance(resource, Card)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.cards.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "description": "Card for Ian Crease",
                "billing_address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "postal_code": "x",
                },
            },
        )
        assert isinstance(resource, Card)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.cards.retrieve(
            "string",
        )
        assert isinstance(resource, Card)

    async def test_method_update(self) -> None:
        resource = await self.client.cards.update(
            "string",
            {},
        )
        assert isinstance(resource, Card)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.cards.update(
            "string",
            {
                "description": "New description",
                "status": "active",
                "billing_address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "postal_code": "x",
                },
            },
        )
        assert isinstance(resource, Card)

    async def test_method_list(self) -> None:
        resource = await self.client.cards.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.cards.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_retrieve_sensitive_details(self) -> None:
        resource = await self.client.cards.retrieve_sensitive_details(
            "string",
        )
        assert isinstance(resource, CardDetails)
