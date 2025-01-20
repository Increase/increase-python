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
from ...types.wire_transfer import WireTransfer

__all__ = ["WireTransfersResource", "AsyncWireTransfersResource"]


class WireTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return WireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return WireTransfersResourceWithStreamingResponse(self)

    def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal
        Reserve due to error conditions. This will also create a
        [Transaction](#transaction) to account for the returned funds. This Wire
        Transfer must first have a `status` of `complete`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to reverse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )


class AsyncWireTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncWireTransfersResourceWithStreamingResponse(self)

    async def reverse(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal
        Reserve due to error conditions. This will also create a
        [Transaction](#transaction) to account for the returned funds. This Wire
        Transfer must first have a `status` of `complete`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to reverse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )

    async def submit(
        self,
        wire_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireTransfer:
        """
        Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_creating`.

        Args:
          wire_transfer_id: The identifier of the Wire Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_transfer_id:
            raise ValueError(f"Expected a non-empty value for `wire_transfer_id` but received {wire_transfer_id!r}")
        return await self._post(
            f"/simulations/wire_transfers/{wire_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireTransfer,
        )


class WireTransfersResourceWithRawResponse:
    def __init__(self, wire_transfers: WireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.reverse = to_raw_response_wrapper(
            wire_transfers.reverse,
        )
        self.submit = to_raw_response_wrapper(
            wire_transfers.submit,
        )


class AsyncWireTransfersResourceWithRawResponse:
    def __init__(self, wire_transfers: AsyncWireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.reverse = async_to_raw_response_wrapper(
            wire_transfers.reverse,
        )
        self.submit = async_to_raw_response_wrapper(
            wire_transfers.submit,
        )


class WireTransfersResourceWithStreamingResponse:
    def __init__(self, wire_transfers: WireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.reverse = to_streamed_response_wrapper(
            wire_transfers.reverse,
        )
        self.submit = to_streamed_response_wrapper(
            wire_transfers.submit,
        )


class AsyncWireTransfersResourceWithStreamingResponse:
    def __init__(self, wire_transfers: AsyncWireTransfersResource) -> None:
        self._wire_transfers = wire_transfers

        self.reverse = async_to_streamed_response_wrapper(
            wire_transfers.reverse,
        )
        self.submit = async_to_streamed_response_wrapper(
            wire_transfers.submit,
        )
