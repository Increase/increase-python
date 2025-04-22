# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import file_link_create_params
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
from .._base_client import make_request_options
from ..types.file_link import FileLink

__all__ = ["FileLinksResource", "AsyncFileLinksResource"]


class FileLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return FileLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return FileLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_id: str,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileLink:
        """
        Create a File Link

        Args:
          file_id: The File to create a File Link for.

          expires_at: The time at which the File Link will expire. The default is 1 hour from the time
              of the request. The maxiumum is 1 day from the time of the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/file_links",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "expires_at": expires_at,
                },
                file_link_create_params.FileLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileLink,
        )


class AsyncFileLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncFileLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_id: str,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> FileLink:
        """
        Create a File Link

        Args:
          file_id: The File to create a File Link for.

          expires_at: The time at which the File Link will expire. The default is 1 hour from the time
              of the request. The maxiumum is 1 day from the time of the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/file_links",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "expires_at": expires_at,
                },
                file_link_create_params.FileLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FileLink,
        )


class FileLinksResourceWithRawResponse:
    def __init__(self, file_links: FileLinksResource) -> None:
        self._file_links = file_links

        self.create = to_raw_response_wrapper(
            file_links.create,
        )


class AsyncFileLinksResourceWithRawResponse:
    def __init__(self, file_links: AsyncFileLinksResource) -> None:
        self._file_links = file_links

        self.create = async_to_raw_response_wrapper(
            file_links.create,
        )


class FileLinksResourceWithStreamingResponse:
    def __init__(self, file_links: FileLinksResource) -> None:
        self._file_links = file_links

        self.create = to_streamed_response_wrapper(
            file_links.create,
        )


class AsyncFileLinksResourceWithStreamingResponse:
    def __init__(self, file_links: AsyncFileLinksResource) -> None:
        self._file_links = file_links

        self.create = async_to_streamed_response_wrapper(
            file_links.create,
        )
