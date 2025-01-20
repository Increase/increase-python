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
from ...types.simulations.inbound_funds_hold_release_response import InboundFundsHoldReleaseResponse

__all__ = ["InboundFundsHoldsResource", "AsyncInboundFundsHoldsResource"]


class InboundFundsHoldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundFundsHoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundFundsHoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundFundsHoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundFundsHoldsResourceWithStreamingResponse(self)

    def release(
        self,
        inbound_funds_hold_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundFundsHoldReleaseResponse:
        """
        This endpoint simulates immediately releasing an Inbound Funds Hold, which might
        be created as a result of e.g., an ACH debit.

        Args:
          inbound_funds_hold_id: The inbound funds hold to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_funds_hold_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_funds_hold_id` but received {inbound_funds_hold_id!r}"
            )
        return self._post(
            f"/simulations/inbound_funds_holds/{inbound_funds_hold_id}/release",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundFundsHoldReleaseResponse,
        )


class AsyncInboundFundsHoldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundFundsHoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundFundsHoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundFundsHoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundFundsHoldsResourceWithStreamingResponse(self)

    async def release(
        self,
        inbound_funds_hold_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundFundsHoldReleaseResponse:
        """
        This endpoint simulates immediately releasing an Inbound Funds Hold, which might
        be created as a result of e.g., an ACH debit.

        Args:
          inbound_funds_hold_id: The inbound funds hold to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not inbound_funds_hold_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_funds_hold_id` but received {inbound_funds_hold_id!r}"
            )
        return await self._post(
            f"/simulations/inbound_funds_holds/{inbound_funds_hold_id}/release",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundFundsHoldReleaseResponse,
        )


class InboundFundsHoldsResourceWithRawResponse:
    def __init__(self, inbound_funds_holds: InboundFundsHoldsResource) -> None:
        self._inbound_funds_holds = inbound_funds_holds

        self.release = to_raw_response_wrapper(
            inbound_funds_holds.release,
        )


class AsyncInboundFundsHoldsResourceWithRawResponse:
    def __init__(self, inbound_funds_holds: AsyncInboundFundsHoldsResource) -> None:
        self._inbound_funds_holds = inbound_funds_holds

        self.release = async_to_raw_response_wrapper(
            inbound_funds_holds.release,
        )


class InboundFundsHoldsResourceWithStreamingResponse:
    def __init__(self, inbound_funds_holds: InboundFundsHoldsResource) -> None:
        self._inbound_funds_holds = inbound_funds_holds

        self.release = to_streamed_response_wrapper(
            inbound_funds_holds.release,
        )


class AsyncInboundFundsHoldsResourceWithStreamingResponse:
    def __init__(self, inbound_funds_holds: AsyncInboundFundsHoldsResource) -> None:
        self._inbound_funds_holds = inbound_funds_holds

        self.release = async_to_streamed_response_wrapper(
            inbound_funds_holds.release,
        )
