# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bookkeeping_entry_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
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
from ..types.bookkeeping_entry import BookkeepingEntry

__all__ = ["BookkeepingEntriesResource", "AsyncBookkeepingEntriesResource"]


class BookkeepingEntriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookkeepingEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return BookkeepingEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookkeepingEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return BookkeepingEntriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        bookkeeping_entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingEntry:
        """
        Retrieve a Bookkeeping Entry

        Args:
          bookkeeping_entry_id: The identifier of the Bookkeeping Entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bookkeeping_entry_id:
            raise ValueError(
                f"Expected a non-empty value for `bookkeeping_entry_id` but received {bookkeeping_entry_id!r}"
            )
        return self._get(
            f"/bookkeeping_entries/{bookkeeping_entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookkeepingEntry,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BookkeepingEntry]:
        """
        List Bookkeeping Entries

        Args:
          account_id: The identifier for the Bookkeeping Account to filter by.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bookkeeping_entries",
            page=SyncPage[BookkeepingEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    bookkeeping_entry_list_params.BookkeepingEntryListParams,
                ),
            ),
            model=BookkeepingEntry,
        )


class AsyncBookkeepingEntriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookkeepingEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookkeepingEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookkeepingEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncBookkeepingEntriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        bookkeeping_entry_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingEntry:
        """
        Retrieve a Bookkeeping Entry

        Args:
          bookkeeping_entry_id: The identifier of the Bookkeeping Entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bookkeeping_entry_id:
            raise ValueError(
                f"Expected a non-empty value for `bookkeeping_entry_id` but received {bookkeeping_entry_id!r}"
            )
        return await self._get(
            f"/bookkeeping_entries/{bookkeeping_entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookkeepingEntry,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BookkeepingEntry, AsyncPage[BookkeepingEntry]]:
        """
        List Bookkeeping Entries

        Args:
          account_id: The identifier for the Bookkeeping Account to filter by.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bookkeeping_entries",
            page=AsyncPage[BookkeepingEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    bookkeeping_entry_list_params.BookkeepingEntryListParams,
                ),
            ),
            model=BookkeepingEntry,
        )


class BookkeepingEntriesResourceWithRawResponse:
    def __init__(self, bookkeeping_entries: BookkeepingEntriesResource) -> None:
        self._bookkeeping_entries = bookkeeping_entries

        self.retrieve = to_raw_response_wrapper(
            bookkeeping_entries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bookkeeping_entries.list,
        )


class AsyncBookkeepingEntriesResourceWithRawResponse:
    def __init__(self, bookkeeping_entries: AsyncBookkeepingEntriesResource) -> None:
        self._bookkeeping_entries = bookkeeping_entries

        self.retrieve = async_to_raw_response_wrapper(
            bookkeeping_entries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bookkeeping_entries.list,
        )


class BookkeepingEntriesResourceWithStreamingResponse:
    def __init__(self, bookkeeping_entries: BookkeepingEntriesResource) -> None:
        self._bookkeeping_entries = bookkeeping_entries

        self.retrieve = to_streamed_response_wrapper(
            bookkeeping_entries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bookkeeping_entries.list,
        )


class AsyncBookkeepingEntriesResourceWithStreamingResponse:
    def __init__(self, bookkeeping_entries: AsyncBookkeepingEntriesResource) -> None:
        self._bookkeeping_entries = bookkeeping_entries

        self.retrieve = async_to_streamed_response_wrapper(
            bookkeeping_entries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bookkeeping_entries.list,
        )
