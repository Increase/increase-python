# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import InboundWireDrawdownRequest, inbound_wire_drawdown_request_list_params
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

__all__ = ["InboundWireDrawdownRequests", "AsyncInboundWireDrawdownRequests"]


class InboundWireDrawdownRequests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireDrawdownRequestsWithRawResponse:
        return InboundWireDrawdownRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireDrawdownRequestsWithStreamingResponse:
        return InboundWireDrawdownRequestsWithStreamingResponse(self)

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


class AsyncInboundWireDrawdownRequests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireDrawdownRequestsWithRawResponse:
        return AsyncInboundWireDrawdownRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireDrawdownRequestsWithStreamingResponse:
        return AsyncInboundWireDrawdownRequestsWithStreamingResponse(self)

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


class InboundWireDrawdownRequestsWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequests) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class AsyncInboundWireDrawdownRequestsWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequests) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class InboundWireDrawdownRequestsWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequests) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )


class AsyncInboundWireDrawdownRequestsWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequests) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.retrieve = async_to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.list,
        )
