# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Limit
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLimits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        limit = client.limits.create(
            metric="count",
            model_id="x",
            value=0,
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        limit = client.limits.create(
            metric="count",
            model_id="x",
            value=0,
            interval="transaction",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        limit = client.limits.retrieve(
            "string",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        limit = client.limits.update(
            "string",
            status="inactive",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        limit = client.limits.list()
        assert_matches_type(SyncPage[Limit], limit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        limit = client.limits.list(
            cursor="string",
            limit=0,
            model_id="x",
            status="x",
        )
        assert_matches_type(SyncPage[Limit], limit, path=["response"])


class TestAsyncLimits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        limit = await client.limits.create(
            metric="count",
            model_id="x",
            value=0,
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        limit = await client.limits.create(
            metric="count",
            model_id="x",
            value=0,
            interval="transaction",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        limit = await client.limits.retrieve(
            "string",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        limit = await client.limits.update(
            "string",
            status="inactive",
        )
        assert_matches_type(Limit, limit, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        limit = await client.limits.list()
        assert_matches_type(AsyncPage[Limit], limit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        limit = await client.limits.list(
            cursor="string",
            limit=0,
            model_id="x",
            status="x",
        )
        assert_matches_type(AsyncPage[Limit], limit, path=["response"])
