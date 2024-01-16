# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.entities import (
    SupplementalDocument,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


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
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entities.supplemental_documents.with_raw_response.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(Entity, supplemental_document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entities.supplemental_documents.with_streaming_response.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = response.parse()
            assert_matches_type(Entity, supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.supplemental_documents.with_raw_response.create(
                "",
                file_id="file_makxrc67oh9l6sg7w9yc",
            )

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
            limit=1,
        )
        assert_matches_type(SyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.entities.supplemental_documents.with_raw_response.list(
            entity_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(SyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.entities.supplemental_documents.with_streaming_response.list(
            entity_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = response.parse()
            assert_matches_type(SyncPage[SupplementalDocument], supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True


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
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.entities.supplemental_documents.with_raw_response.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(Entity, supplemental_document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.entities.supplemental_documents.with_streaming_response.create(
            "string",
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = await response.parse()
            assert_matches_type(Entity, supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await client.entities.supplemental_documents.with_raw_response.create(
                "",
                file_id="file_makxrc67oh9l6sg7w9yc",
            )

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
            limit=1,
        )
        assert_matches_type(AsyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.entities.supplemental_documents.with_raw_response.list(
            entity_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(AsyncPage[SupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.entities.supplemental_documents.with_streaming_response.list(
            entity_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = await response.parse()
            assert_matches_type(AsyncPage[SupplementalDocument], supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True
