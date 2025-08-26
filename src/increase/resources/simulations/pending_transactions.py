# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.pending_transaction import PendingTransaction

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

    def release_inbound_funds_hold(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PendingTransaction:
        """
        This endpoint simulates immediately releasing an Inbound Funds Hold, which might
        be created as a result of, for example, an ACH debit.

        Args:
          pending_transaction_id: The pending transaction to release. The pending transaction must have a
              `inbound_funds_hold` source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not pending_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `pending_transaction_id` but received {pending_transaction_id!r}"
            )
        return self._post(
            f"/simulations/pending_transactions/{pending_transaction_id}/release_inbound_funds_hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PendingTransaction,
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

    async def release_inbound_funds_hold(
        self,
        pending_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PendingTransaction:
        """
        This endpoint simulates immediately releasing an Inbound Funds Hold, which might
        be created as a result of, for example, an ACH debit.

        Args:
          pending_transaction_id: The pending transaction to release. The pending transaction must have a
              `inbound_funds_hold` source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not pending_transaction_id:
            raise ValueError(
                f"Expected a non-empty value for `pending_transaction_id` but received {pending_transaction_id!r}"
            )
        return await self._post(
            f"/simulations/pending_transactions/{pending_transaction_id}/release_inbound_funds_hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PendingTransaction,
        )


class PendingTransactionsResourceWithRawResponse:
    def __init__(self, pending_transactions: PendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.release_inbound_funds_hold = to_raw_response_wrapper(
            pending_transactions.release_inbound_funds_hold,
        )


class AsyncPendingTransactionsResourceWithRawResponse:
    def __init__(self, pending_transactions: AsyncPendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.release_inbound_funds_hold = async_to_raw_response_wrapper(
            pending_transactions.release_inbound_funds_hold,
        )


class PendingTransactionsResourceWithStreamingResponse:
    def __init__(self, pending_transactions: PendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.release_inbound_funds_hold = to_streamed_response_wrapper(
            pending_transactions.release_inbound_funds_hold,
        )


class AsyncPendingTransactionsResourceWithStreamingResponse:
    def __init__(self, pending_transactions: AsyncPendingTransactionsResource) -> None:
        self._pending_transactions = pending_transactions

        self.release_inbound_funds_hold = async_to_streamed_response_wrapper(
            pending_transactions.release_inbound_funds_hold,
        )
