# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import fednow_transfer_complete_params
from ...types.fednow_transfer import FednowTransfer

__all__ = ["FednowTransfersResource", "AsyncFednowTransfersResource"]


class FednowTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return FednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return FednowTransfersResourceWithStreamingResponse(self)

    def complete(
        self,
        fednow_transfer_id: str,
        *,
        rejection: fednow_transfer_complete_params.Rejection | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Simulates submission of a [FedNow Transfer](#fednow-transfers) and handling the
        response from the destination financial institution. This transfer must first
        have a `status` of `pending_submitting`.

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return self._post(
            path_template(
                "/simulations/fednow_transfers/{fednow_transfer_id}/complete", fednow_transfer_id=fednow_transfer_id
            ),
            body=maybe_transform(
                {"rejection": rejection}, fednow_transfer_complete_params.FednowTransferCompleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )


class AsyncFednowTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFednowTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFednowTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFednowTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncFednowTransfersResourceWithStreamingResponse(self)

    async def complete(
        self,
        fednow_transfer_id: str,
        *,
        rejection: fednow_transfer_complete_params.Rejection | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> FednowTransfer:
        """
        Simulates submission of a [FedNow Transfer](#fednow-transfers) and handling the
        response from the destination financial institution. This transfer must first
        have a `status` of `pending_submitting`.

        Args:
          fednow_transfer_id: The identifier of the FedNow Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not fednow_transfer_id:
            raise ValueError(f"Expected a non-empty value for `fednow_transfer_id` but received {fednow_transfer_id!r}")
        return await self._post(
            path_template(
                "/simulations/fednow_transfers/{fednow_transfer_id}/complete", fednow_transfer_id=fednow_transfer_id
            ),
            body=await async_maybe_transform(
                {"rejection": rejection}, fednow_transfer_complete_params.FednowTransferCompleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=FednowTransfer,
        )


class FednowTransfersResourceWithRawResponse:
    def __init__(self, fednow_transfers: FednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.complete = to_raw_response_wrapper(
            fednow_transfers.complete,
        )


class AsyncFednowTransfersResourceWithRawResponse:
    def __init__(self, fednow_transfers: AsyncFednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.complete = async_to_raw_response_wrapper(
            fednow_transfers.complete,
        )


class FednowTransfersResourceWithStreamingResponse:
    def __init__(self, fednow_transfers: FednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.complete = to_streamed_response_wrapper(
            fednow_transfers.complete,
        )


class AsyncFednowTransfersResourceWithStreamingResponse:
    def __init__(self, fednow_transfers: AsyncFednowTransfersResource) -> None:
        self._fednow_transfers = fednow_transfers

        self.complete = async_to_streamed_response_wrapper(
            fednow_transfers.complete,
        )
