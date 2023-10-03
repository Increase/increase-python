# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase.pagination import SyncPage, AsyncPage
from increase.types.entities import SupplementalDocument

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestSupplementalDocuments:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        supplemental_document = client.entities.supplemental_documents.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(Entity, supplemental_document, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        supplemental_document = client.entities.supplemental_documents.list(
            entity_id="string",
        )
        assert_matches_type(SyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        supplemental_document = client.entities.supplemental_documents.list(
            entity_id="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[SupplementalDocument], supplemental_document, path=["response"])


class TestAsyncSupplementalDocuments:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        supplemental_document = await client.entities.supplemental_documents.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(Entity, supplemental_document, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        supplemental_document = await client.entities.supplemental_documents.list(
            entity_id="string",
        )
        assert_matches_type(AsyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        supplemental_document = await client.entities.supplemental_documents.list(
            entity_id="string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[SupplementalDocument], supplemental_document, path=["response"])
