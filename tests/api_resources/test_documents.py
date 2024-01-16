# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Document
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestDocuments:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        document = client.documents.retrieve(
            "string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.documents.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.documents.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        document = client.documents.list()
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        document = client.documents.list(
            category={"in": ["form_1099_int", "proof_of_authorization", "company_information"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            limit=1,
        )
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        document = await client.documents.retrieve(
            "string",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.documents.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.documents.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        document = await client.documents.list()
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        document = await client.documents.list(
            category={"in": ["form_1099_int", "proof_of_authorization", "company_information"]},
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True
