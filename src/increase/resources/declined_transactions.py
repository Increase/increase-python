# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import DeclinedTransaction, declined_transaction_list_params
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

__all__ = ["DeclinedTransactions", "AsyncDeclinedTransactions"]


class DeclinedTransactions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeclinedTransactionsWithRawResponse:
        return DeclinedTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeclinedTransactionsWithStreamingResponse:
        return DeclinedTransactionsWithStreamingResponse(self)

    def retrieve(
        self,
        declined_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeclinedTransaction:
        """
        Retrieve a Declined Transaction

        Args:
          declined_transaction_id: The identifier of the Declined Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not declined_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `declined_transaction_id` but received {declined_transaction_id!r}"
            )
        return self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        category: declined_transaction_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: declined_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[DeclinedTransaction]:
        """
        List Declined Transactions

        Args:
          account_id: Filter Declined Transactions to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          route_id: Filter Declined Transactions to those belonging to the specified route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/declined_transactions",
            page=SyncPage[DeclinedTransaction],
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
                    },
                    declined_transaction_list_params.DeclinedTransactionListParams,
                ),
            ),
            model=DeclinedTransaction,
        )


class AsyncDeclinedTransactions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeclinedTransactionsWithRawResponse:
        return AsyncDeclinedTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeclinedTransactionsWithStreamingResponse:
        return AsyncDeclinedTransactionsWithStreamingResponse(self)

    async def retrieve(
        self,
        declined_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeclinedTransaction:
        """
        Retrieve a Declined Transaction

        Args:
          declined_transaction_id: The identifier of the Declined Transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not declined_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `declined_transaction_id` but received {declined_transaction_id!r}"
            )
        return await self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        category: declined_transaction_list_params.Category | NotGiven = NOT_GIVEN,
        created_at: declined_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DeclinedTransaction, AsyncPage[DeclinedTransaction]]:
        """
        List Declined Transactions

        Args:
          account_id: Filter Declined Transactions to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          route_id: Filter Declined Transactions to those belonging to the specified route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/declined_transactions",
            page=AsyncPage[DeclinedTransaction],
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
                    },
                    declined_transaction_list_params.DeclinedTransactionListParams,
                ),
            ),
            model=DeclinedTransaction,
        )


class DeclinedTransactionsWithRawResponse:
    def __init__(self, declined_transactions: DeclinedTransactions) -> None:
        self._declined_transactions = declined_transactions

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            declined_transactions.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            declined_transactions.list,
        )


class AsyncDeclinedTransactionsWithRawResponse:
    def __init__(self, declined_transactions: AsyncDeclinedTransactions) -> None:
        self._declined_transactions = declined_transactions

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            declined_transactions.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            declined_transactions.list,
        )


class DeclinedTransactionsWithStreamingResponse:
    def __init__(self, declined_transactions: DeclinedTransactions) -> None:
        self._declined_transactions = declined_transactions

        self.retrieve = to_streamed_response_wrapper(
            declined_transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            declined_transactions.list,
        )


class AsyncDeclinedTransactionsWithStreamingResponse:
    def __init__(self, declined_transactions: AsyncDeclinedTransactions) -> None:
        self._declined_transactions = declined_transactions

        self.retrieve = async_to_streamed_response_wrapper(
            declined_transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            declined_transactions.list,
        )
