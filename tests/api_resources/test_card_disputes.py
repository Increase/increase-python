# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.card_dispute import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCardDisputes:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.card_disputes.create(
            {
                "disputed_transaction_id": "transaction_uyrp7fld2ium70oa7oi",
                "explanation": "Unauthorized recurring transaction.",
            },
        )
        assert isinstance(resource, CardDispute)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.card_disputes.create(
            {
                "disputed_transaction_id": "transaction_uyrp7fld2ium70oa7oi",
                "explanation": "Unauthorized recurring transaction.",
            },
        )
        assert isinstance(resource, CardDispute)

    def test_method_retrieve(self) -> None:
        resource = self.client.card_disputes.retrieve(
            "string",
        )
        assert isinstance(resource, CardDispute)

    def test_method_list(self) -> None:
        resource = self.client.card_disputes.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.card_disputes.list(
            {
                "cursor": "x",
                "limit": 0,
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "status": {"in": ["pending_reviewing", "pending_reviewing", "pending_reviewing"]},
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncCardDisputes:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.card_disputes.create(
            {
                "disputed_transaction_id": "transaction_uyrp7fld2ium70oa7oi",
                "explanation": "Unauthorized recurring transaction.",
            },
        )
        assert isinstance(resource, CardDispute)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.card_disputes.create(
            {
                "disputed_transaction_id": "transaction_uyrp7fld2ium70oa7oi",
                "explanation": "Unauthorized recurring transaction.",
            },
        )
        assert isinstance(resource, CardDispute)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.card_disputes.retrieve(
            "string",
        )
        assert isinstance(resource, CardDispute)

    async def test_method_list(self) -> None:
        resource = await self.client.card_disputes.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.card_disputes.list(
            {
                "cursor": "x",
                "limit": 0,
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "status": {"in": ["pending_reviewing", "pending_reviewing", "pending_reviewing"]},
            },
        )
        assert isinstance(resource, AsyncPage)
