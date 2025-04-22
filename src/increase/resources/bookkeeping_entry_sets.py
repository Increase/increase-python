# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ..types import bookkeeping_entry_set_list_params, bookkeeping_entry_set_create_params
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
from ..types.bookkeeping_entry_set import BookkeepingEntrySet

__all__ = ["BookkeepingEntrySetsResource", "AsyncBookkeepingEntrySetsResource"]


class BookkeepingEntrySetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookkeepingEntrySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return BookkeepingEntrySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookkeepingEntrySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return BookkeepingEntrySetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        entries: Iterable[bookkeeping_entry_set_create_params.Entry],
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingEntrySet:
        """
        Create a Bookkeeping Entry Set

        Args:
          entries: The bookkeeping entries.

          date: The date of the transaction. Optional if `transaction_id` is provided, in which
              case we use the `date` of that transaction. Required otherwise.

          transaction_id: The identifier of the Transaction related to this entry set, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/bookkeeping_entry_sets",
            body=maybe_transform(
                {
                    "entries": entries,
                    "date": date,
                    "transaction_id": transaction_id,
                },
                bookkeeping_entry_set_create_params.BookkeepingEntrySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingEntrySet,
        )

    def retrieve(
        self,
        bookkeeping_entry_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingEntrySet:
        """
        Retrieve a Bookkeeping Entry Set

        Args:
          bookkeeping_entry_set_id: The identifier of the Bookkeeping Entry Set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bookkeeping_entry_set_id:
            raise ValueError(
                f"Expected a non-empty value for `bookkeeping_entry_set_id` but received {bookkeeping_entry_set_id!r}"
            )
        return self._get(
            f"/bookkeeping_entry_sets/{bookkeeping_entry_set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookkeepingEntrySet,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BookkeepingEntrySet]:
        """
        List Bookkeeping Entry Sets

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          transaction_id: Filter to the Bookkeeping Entry Set that maps to this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bookkeeping_entry_sets",
            page=SyncPage[BookkeepingEntrySet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "transaction_id": transaction_id,
                    },
                    bookkeeping_entry_set_list_params.BookkeepingEntrySetListParams,
                ),
            ),
            model=BookkeepingEntrySet,
        )


class AsyncBookkeepingEntrySetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookkeepingEntrySetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookkeepingEntrySetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookkeepingEntrySetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncBookkeepingEntrySetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        entries: Iterable[bookkeeping_entry_set_create_params.Entry],
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BookkeepingEntrySet:
        """
        Create a Bookkeeping Entry Set

        Args:
          entries: The bookkeeping entries.

          date: The date of the transaction. Optional if `transaction_id` is provided, in which
              case we use the `date` of that transaction. Required otherwise.

          transaction_id: The identifier of the Transaction related to this entry set, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/bookkeeping_entry_sets",
            body=await async_maybe_transform(
                {
                    "entries": entries,
                    "date": date,
                    "transaction_id": transaction_id,
                },
                bookkeeping_entry_set_create_params.BookkeepingEntrySetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BookkeepingEntrySet,
        )

    async def retrieve(
        self,
        bookkeeping_entry_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookkeepingEntrySet:
        """
        Retrieve a Bookkeeping Entry Set

        Args:
          bookkeeping_entry_set_id: The identifier of the Bookkeeping Entry Set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bookkeeping_entry_set_id:
            raise ValueError(
                f"Expected a non-empty value for `bookkeeping_entry_set_id` but received {bookkeeping_entry_set_id!r}"
            )
        return await self._get(
            f"/bookkeeping_entry_sets/{bookkeeping_entry_set_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookkeepingEntrySet,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BookkeepingEntrySet, AsyncPage[BookkeepingEntrySet]]:
        """
        List Bookkeeping Entry Sets

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          transaction_id: Filter to the Bookkeeping Entry Set that maps to this Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/bookkeeping_entry_sets",
            page=AsyncPage[BookkeepingEntrySet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "transaction_id": transaction_id,
                    },
                    bookkeeping_entry_set_list_params.BookkeepingEntrySetListParams,
                ),
            ),
            model=BookkeepingEntrySet,
        )


class BookkeepingEntrySetsResourceWithRawResponse:
    def __init__(self, bookkeeping_entry_sets: BookkeepingEntrySetsResource) -> None:
        self._bookkeeping_entry_sets = bookkeeping_entry_sets

        self.create = to_raw_response_wrapper(
            bookkeeping_entry_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bookkeeping_entry_sets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bookkeeping_entry_sets.list,
        )


class AsyncBookkeepingEntrySetsResourceWithRawResponse:
    def __init__(self, bookkeeping_entry_sets: AsyncBookkeepingEntrySetsResource) -> None:
        self._bookkeeping_entry_sets = bookkeeping_entry_sets

        self.create = async_to_raw_response_wrapper(
            bookkeeping_entry_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bookkeeping_entry_sets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bookkeeping_entry_sets.list,
        )


class BookkeepingEntrySetsResourceWithStreamingResponse:
    def __init__(self, bookkeeping_entry_sets: BookkeepingEntrySetsResource) -> None:
        self._bookkeeping_entry_sets = bookkeeping_entry_sets

        self.create = to_streamed_response_wrapper(
            bookkeeping_entry_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bookkeeping_entry_sets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bookkeeping_entry_sets.list,
        )


class AsyncBookkeepingEntrySetsResourceWithStreamingResponse:
    def __init__(self, bookkeeping_entry_sets: AsyncBookkeepingEntrySetsResource) -> None:
        self._bookkeeping_entry_sets = bookkeeping_entry_sets

        self.create = async_to_streamed_response_wrapper(
            bookkeeping_entry_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bookkeeping_entry_sets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bookkeeping_entry_sets.list,
        )
