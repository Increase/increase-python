# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.intrafi import IntrafiExclusion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestExclusions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.retrieve(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.list()
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.list(
            cursor="string",
            entity_id="string",
            limit=1,
        )
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.archive(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.archive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])


class TestAsyncExclusions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        exclusion = await client.intrafi.exclusions.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.exclusions.with_raw_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        exclusion = await client.intrafi.exclusions.retrieve(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.exclusions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        exclusion = await client.intrafi.exclusions.list()
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        exclusion = await client.intrafi.exclusions.list(
            cursor="string",
            entity_id="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.exclusions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        exclusion = await client.intrafi.exclusions.archive(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.exclusions.with_raw_response.archive(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])
