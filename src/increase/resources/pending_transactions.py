# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pending_transaction_list_params
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
from ..types.pending_transaction import PendingTransaction

__all__ = ["PendingTransactionsResource", "AsyncPendingTransactionsResource"]


class PendingTransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PendingTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return PendingTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PendingTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return PendingTransactionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingTransaction:
        """
        Retrieve a Pending Transaction

        Args:
          pending_transaction_id: The identifier of the Pending Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pending_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `pending_transaction_id` but received {pending_transaction_id!r}"
            )
        return self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PendingTransaction,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        category: pending_transaction_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: pending_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        status: pending_transaction_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PendingTransaction]:
        """
        List Pending Transactions

        Args:
          account_id: Filter pending transactions to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          route_id: Filter pending transactions to those belonging to the specified Route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pending_transactions",
            page=SyncPage[PendingTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "route_id": route_id,
                        "status": status,
                    },
                    pending_transaction_list_params.PendingTransactionListParams,
                ),
            ),
            model=PendingTransaction,
        )


class AsyncPendingTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPendingTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPendingTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPendingTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncPendingTransactionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingTransaction:
        """
        Retrieve a Pending Transaction

        Args:
          pending_transaction_id: The identifier of the Pending Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pending_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `pending_transaction_id` but received {pending_transaction_id!r}"
            )
        return await self._get(
            f"/pending_transactions/{pending_transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PendingTransaction,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        category: pending_transaction_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: pending_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        status: pending_transaction_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PendingTransaction, AsyncPage[PendingTransaction]]:
        """
        List Pending Transactions

        Args:
          account_id: Filter pending transactions to those belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          route_id: Filter pending transactions to those belonging to the specified Route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pending_transactions",
            page=AsyncPage[PendingTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "category": category,
                        "created_at": created_at,
                        "cursor": cursor,
                        "limit": limit,
                        "route_id": route_id,
                        "status": status,
                    },
                    pending_transaction_list_params.PendingTransactionListParams,
                ),
            ),
            model=PendingTransaction,
        )


class PendingTransactionsResourceWithRawResponse:
    def __init__(self, pending_transactions: PendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.retrieve = to_raw_response_wrapper(
            pending_transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            pending_transactions.list,
        )


class AsyncPendingTransactionsResourceWithRawResponse:
    def __init__(self, pending_transactions: AsyncPendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.retrieve = async_to_raw_response_wrapper(
            pending_transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            pending_transactions.list,
        )


class PendingTransactionsResourceWithStreamingResponse:
    def __init__(self, pending_transactions: PendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.retrieve = to_streamed_response_wrapper(
            pending_transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            pending_transactions.list,
        )


class AsyncPendingTransactionsResourceWithStreamingResponse:
    def __init__(self, pending_transactions: AsyncPendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.retrieve = async_to_streamed_response_wrapper(
            pending_transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            pending_transactions.list,
        )
