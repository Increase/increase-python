# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import supplemental_document_list_params, supplemental_document_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.entity_supplemental_document import EntitySupplementalDocument

__all__ = ["SupplementalDocumentsResource", "AsyncSupplementalDocumentsResource"]


class SupplementalDocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SupplementalDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return SupplementalDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupplementalDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return SupplementalDocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        entity_id: str,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EntitySupplementalDocument:
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
        return self._post(
            "/entity_supplemental_documents",
            body=maybe_transform(
                {
                    "entity_id": entity_id,
                    "file_id": file_id,
                },
                supplemental_document_create_params.SupplementalDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntitySupplementalDocument,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EntitySupplementalDocument]:
        """
        List Entity Supplemental Document Submissions

        Args:
          entity_id: The identifier of the Entity to list supplemental documents for.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_supplemental_documents",
            page=SyncPage[EntitySupplementalDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    supplemental_document_list_params.SupplementalDocumentListParams,
                ),
            ),
            model=EntitySupplementalDocument,
        )


class AsyncSupplementalDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSupplementalDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupplementalDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupplementalDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncSupplementalDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        entity_id: str,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EntitySupplementalDocument:
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
        return await self._post(
            "/entity_supplemental_documents",
            body=await async_maybe_transform(
                {
                    "entity_id": entity_id,
                    "file_id": file_id,
                },
                supplemental_document_create_params.SupplementalDocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntitySupplementalDocument,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EntitySupplementalDocument, AsyncPage[EntitySupplementalDocument]]:
        """
        List Entity Supplemental Document Submissions

        Args:
          entity_id: The identifier of the Entity to list supplemental documents for.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/entity_supplemental_documents",
            page=AsyncPage[EntitySupplementalDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    supplemental_document_list_params.SupplementalDocumentListParams,
                ),
            ),
            model=EntitySupplementalDocument,
        )


class SupplementalDocumentsResourceWithRawResponse:
    def __init__(self, supplemental_documents: SupplementalDocumentsResource) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = to_raw_response_wrapper(
            supplemental_documents.create,
        )
        self.list = to_raw_response_wrapper(
            supplemental_documents.list,
        )


class AsyncSupplementalDocumentsResourceWithRawResponse:
    def __init__(self, supplemental_documents: AsyncSupplementalDocumentsResource) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = async_to_raw_response_wrapper(
            supplemental_documents.create,
        )
        self.list = async_to_raw_response_wrapper(
            supplemental_documents.list,
        )


class SupplementalDocumentsResourceWithStreamingResponse:
    def __init__(self, supplemental_documents: SupplementalDocumentsResource) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = to_streamed_response_wrapper(
            supplemental_documents.create,
        )
        self.list = to_streamed_response_wrapper(
            supplemental_documents.list,
        )


class AsyncSupplementalDocumentsResourceWithStreamingResponse:
    def __init__(self, supplemental_documents: AsyncSupplementalDocumentsResource) -> None:
        self._supplemental_documents = supplemental_documents

        self.create = async_to_streamed_response_wrapper(
            supplemental_documents.create,
        )
        self.list = async_to_streamed_response_wrapper(
            supplemental_documents.list,
        )
