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
from ...types.wire_drawdown_request import WireDrawdownRequest

__all__ = ["WireDrawdownRequestsResource", "AsyncWireDrawdownRequestsResource"]


class WireDrawdownRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return WireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return WireDrawdownRequestsResourceWithStreamingResponse(self)

    def refuse(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being refused by the debtor.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to refuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return self._post(
            f"/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/refuse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    def submit(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being submitted to Fedwire.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return self._post(
            f"/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )


class AsyncWireDrawdownRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncWireDrawdownRequestsResourceWithStreamingResponse(self)

    async def refuse(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being refused by the debtor.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to refuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return await self._post(
            f"/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/refuse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )

    async def submit(
        self,
        wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> WireDrawdownRequest:
        """
        Simulates a Wire Drawdown Request being submitted to Fedwire.

        Args:
          wire_drawdown_request_id: The identifier of the Wire Drawdown Request you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `wire_drawdown_request_id` but received {wire_drawdown_request_id!r}"
            )
        return await self._post(
            f"/simulations/wire_drawdown_requests/{wire_drawdown_request_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WireDrawdownRequest,
        )


class WireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = to_raw_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = to_raw_response_wrapper(
            wire_drawdown_requests.submit,
        )


class AsyncWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = async_to_raw_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = async_to_raw_response_wrapper(
            wire_drawdown_requests.submit,
        )


class WireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: WireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = to_streamed_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = to_streamed_response_wrapper(
            wire_drawdown_requests.submit,
        )


class AsyncWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, wire_drawdown_requests: AsyncWireDrawdownRequestsResource) -> None:
        self._wire_drawdown_requests = wire_drawdown_requests

        self.refuse = async_to_streamed_response_wrapper(
            wire_drawdown_requests.refuse,
        )
        self.submit = async_to_streamed_response_wrapper(
            wire_drawdown_requests.submit,
        )
