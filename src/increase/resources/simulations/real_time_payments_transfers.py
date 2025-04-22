# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import real_time_payments_transfer_complete_params
from ...types.real_time_payments_transfer import RealTimePaymentsTransfer

__all__ = ["RealTimePaymentsTransfersResource", "AsyncRealTimePaymentsTransfersResource"]


class RealTimePaymentsTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return RealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return RealTimePaymentsTransfersResourceWithStreamingResponse(self)

    def complete(
        self,
        real_time_payments_transfer_id: str,
        *,
        rejection: real_time_payments_transfer_complete_params.Rejection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Simulates submission of a
        [Real-Time Payments Transfer](#real-time-payments-transfers) and handling the
        response from the destination financial institution. This transfer must first
        have a `status` of `pending_submission`.

        Args:
          real_time_payments_transfer_id: The identifier of the Real-Time Payments Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_transfer_id` but received {real_time_payments_transfer_id!r}"
            )
        return self._post(
            f"/simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete",
            body=maybe_transform(
                {"rejection": rejection},
                real_time_payments_transfer_complete_params.RealTimePaymentsTransferCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )


class AsyncRealTimePaymentsTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncRealTimePaymentsTransfersResourceWithStreamingResponse(self)

    async def complete(
        self,
        real_time_payments_transfer_id: str,
        *,
        rejection: real_time_payments_transfer_complete_params.Rejection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Simulates submission of a
        [Real-Time Payments Transfer](#real-time-payments-transfers) and handling the
        response from the destination financial institution. This transfer must first
        have a `status` of `pending_submission`.

        Args:
          real_time_payments_transfer_id: The identifier of the Real-Time Payments Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_transfer_id` but received {real_time_payments_transfer_id!r}"
            )
        return await self._post(
            f"/simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete",
            body=await async_maybe_transform(
                {"rejection": rejection},
                real_time_payments_transfer_complete_params.RealTimePaymentsTransferCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )


class RealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, real_time_payments_transfers: RealTimePaymentsTransfersResource) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = to_raw_response_wrapper(
            real_time_payments_transfers.complete,
        )


class AsyncRealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, real_time_payments_transfers: AsyncRealTimePaymentsTransfersResource) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = async_to_raw_response_wrapper(
            real_time_payments_transfers.complete,
        )


class RealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, real_time_payments_transfers: RealTimePaymentsTransfersResource) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = to_streamed_response_wrapper(
            real_time_payments_transfers.complete,
        )


class AsyncRealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, real_time_payments_transfers: AsyncRealTimePaymentsTransfersResource) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = async_to_streamed_response_wrapper(
            real_time_payments_transfers.complete,
        )
