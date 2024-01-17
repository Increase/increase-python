# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import Document
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import document_create_params

__all__ = ["Documents", "AsyncDocuments"]


class Documents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsWithRawResponse:
        return DocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsWithStreamingResponse:
        return DocumentsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Document:
        """
        Simulates an tax document being created for an account.

        Args:
          account_id: The identifier of the Account the tax document is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/documents",
            body=maybe_transform({"account_id": account_id}, document_create_params.DocumentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Document,
        )


class AsyncDocuments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsWithRawResponse:
        return AsyncDocumentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsWithStreamingResponse:
        return AsyncDocumentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Document:
        """
        Simulates an tax document being created for an account.

        Args:
          account_id: The identifier of the Account the tax document is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/documents",
            body=maybe_transform({"account_id": account_id}, document_create_params.DocumentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Document,
        )


class DocumentsWithRawResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.create = _legacy_response.to_raw_response_wrapper(
            documents.create,
        )


class AsyncDocumentsWithRawResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.create = _legacy_response.async_to_raw_response_wrapper(
            documents.create,
        )


class DocumentsWithStreamingResponse:
    def __init__(self, documents: Documents) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )


class AsyncDocumentsWithStreamingResponse:
    def __init__(self, documents: AsyncDocuments) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
