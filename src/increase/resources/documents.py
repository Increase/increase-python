# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import Document, document_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsWithRawResponse:
        return DocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsWithStreamingResponse:
        return DocumentsWithStreamingResponse(self)

    def retrieve(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Retrieve a Document

        Args:
          document_id: The identifier of the Document to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            f"/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        category: document_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: document_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Document]:
        """
        List Documents

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter Documents to ones belonging to the specified Entity.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents",
            page=SyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsWithRawResponse:
        return AsyncDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsWithStreamingResponse:
        return AsyncDocumentsWithStreamingResponse(self)

    async def retrieve(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Retrieve a Document

        Args:
          document_id: The identifier of the Document to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            f"/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def list(
        self,
        *,
        category: document_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: document_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        entity_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Document, AsyncPage[Document]]:
        """
        List Documents

        Args:
          cursor: Return the page of entries after this one.

          entity_id: Filter Documents to ones belonging to the specified Entity.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/documents",
            page=AsyncPage[Document],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "entity_id": entity_id,
                        "limit": limit,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=Document,
        )


class DocumentsWithRawResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            documents.list,
        )


class AsyncDocumentsWithRawResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            documents.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            documents.list,
        )


class DocumentsWithStreamingResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )


class AsyncDocumentsWithStreamingResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
