# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inbound_wire_drawdown_request_list_params
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
from ..types.inbound_wire_drawdown_request import InboundWireDrawdownRequest

__all__ = ["InboundWireDrawdownRequestsResource", "AsyncInboundWireDrawdownRequestsResource"]


class InboundWireDrawdownRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundWireDrawdownRequestsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        inbound_wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundWireDrawdownRequest:
        """
        Retrieve an Inbound Wire Drawdown Request

        Args:
          inbound_wire_drawdown_request_id: The identifier of the Inbound Wire Drawdown Request to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_drawdown_request_id` but received {inbound_wire_drawdown_request_id!r}"
            )
        return self._get(
            f"/inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundWireDrawdownRequest,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[InboundWireDrawdownRequest]:
        """
        List Inbound Wire Drawdown Requests

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_wire_drawdown_requests",
            page=SyncPage[InboundWireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_wire_drawdown_request_list_params.InboundWireDrawdownRequestListParams,
                ),
            ),
            model=InboundWireDrawdownRequest,
        )


class AsyncInboundWireDrawdownRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        inbound_wire_drawdown_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundWireDrawdownRequest:
        """
        Retrieve an Inbound Wire Drawdown Request

        Args:
          inbound_wire_drawdown_request_id: The identifier of the Inbound Wire Drawdown Request to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbound_wire_drawdown_request_id:
            raise ValueError(
                f"Expected a non-empty value for `inbound_wire_drawdown_request_id` but received {inbound_wire_drawdown_request_id!r}"
            )
        return await self._get(
            f"/inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundWireDrawdownRequest,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InboundWireDrawdownRequest, AsyncPage[InboundWireDrawdownRequest]]:
        """
        List Inbound Wire Drawdown Requests

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/inbound_wire_drawdown_requests",
            page=AsyncPage[InboundWireDrawdownRequest],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    inbound_wire_drawdown_request_list_params.InboundWireDrawdownRequestListParams,
                ),
            ),
            model=InboundWireDrawdownRequest,
        )


class InboundWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = to_raw_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = async_to_raw_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class InboundWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )
