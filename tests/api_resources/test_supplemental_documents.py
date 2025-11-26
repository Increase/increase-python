# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    EntitySupplementalDocument,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSupplementalDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        supplemental_document = client.supplemental_documents.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.supplemental_documents.with_raw_response.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.supplemental_documents.with_streaming_response.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = response.parse()
            assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        supplemental_document = client.supplemental_documents.list(
            entity_id="entity_id",
        )
        assert_matches_type(SyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        supplemental_document = client.supplemental_documents.list(
            entity_id="entity_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.supplemental_documents.with_raw_response.list(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = response.parse()
        assert_matches_type(SyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.supplemental_documents.with_streaming_response.list(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = response.parse()
            assert_matches_type(SyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSupplementalDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        supplemental_document = await async_client.supplemental_documents.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.supplemental_documents.with_raw_response.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = await response.parse()
        assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.supplemental_documents.with_streaming_response.create(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = await response.parse()
            assert_matches_type(EntitySupplementalDocument, supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        supplemental_document = await async_client.supplemental_documents.list(
            entity_id="entity_id",
        )
        assert_matches_type(AsyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        supplemental_document = await async_client.supplemental_documents.list(
            entity_id="entity_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.supplemental_documents.with_raw_response.list(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplemental_document = await response.parse()
        assert_matches_type(AsyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.supplemental_documents.with_streaming_response.list(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplemental_document = await response.parse()
            assert_matches_type(AsyncPage[EntitySupplementalDocument], supplemental_document, path=["response"])

        assert cast(Any, response.is_closed) is True
