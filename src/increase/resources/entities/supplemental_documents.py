# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import Entity
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.entities import (
    SupplementalDocument,
    supplemental_document_list_params,
    supplemental_document_create_params,
)

__all__ = ["SupplementalDocuments", "AsyncSupplementalDocuments"]


class SupplementalDocuments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupplementalDocumentsWithRawResponse:
        return SupplementalDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupplementalDocumentsWithStreamingResponse:
        return SupplementalDocumentsWithStreamingResponse(self)

    def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a supplemental document for an Entity

        Args:
          entity_id: The identifier of the Entity to associate with the supplemental document.

          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body=maybe_transform(
                {"file_id": file_id}, supplemental_document_create_params.SupplementalDocumentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SupplementalDocument]:
        """
        List Entity Supplemental Document Submissions

        Args:
          entity_id: The identifier of the Entity to list supplemental documents for.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_supplemental_documents",
            page=SyncPage[SupplementalDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    supplemental_document_list_params.SupplementalDocumentListParams,
                ),
            ),
            model=SupplementalDocument,
        )


class AsyncSupplementalDocuments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupplementalDocumentsWithRawResponse:
        return AsyncSupplementalDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupplementalDocumentsWithStreamingResponse:
        return AsyncSupplementalDocumentsWithStreamingResponse(self)

    async def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a supplemental document for an Entity

        Args:
          entity_id: The identifier of the Entity to associate with the supplemental document.

          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body=maybe_transform(
                {"file_id": file_id}, supplemental_document_create_params.SupplementalDocumentCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SupplementalDocument, AsyncPage[SupplementalDocument]]:
        """
        List Entity Supplemental Document Submissions

        Args:
          entity_id: The identifier of the Entity to list supplemental documents for.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_supplemental_documents",
            page=AsyncPage[SupplementalDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    supplemental_document_list_params.SupplementalDocumentListParams,
                ),
            ),
            model=SupplementalDocument,
        )


class SupplementalDocumentsWithRawResponse:
    def __init__(self, supplemental_documents: SupplementalDocuments) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = _legacy_response.to_raw_response_wrapper(
            supplemental_documents.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            supplemental_documents.list,
        )


class AsyncSupplementalDocumentsWithRawResponse:
    def __init__(self, supplemental_documents: AsyncSupplementalDocuments) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = _legacy_response.async_to_raw_response_wrapper(
            supplemental_documents.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            supplemental_documents.list,
        )


class SupplementalDocumentsWithStreamingResponse:
    def __init__(self, supplemental_documents: SupplementalDocuments) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = to_streamed_response_wrapper(
            supplemental_documents.create,
        )
        self.list = to_streamed_response_wrapper(
            supplemental_documents.list,
        )


class AsyncSupplementalDocumentsWithStreamingResponse:
    def __init__(self, supplemental_documents: AsyncSupplementalDocuments) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = async_to_streamed_response_wrapper(
            supplemental_documents.create,
        )
        self.list = async_to_streamed_response_wrapper(
            supplemental_documents.list,
        )
