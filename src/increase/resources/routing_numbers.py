# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import routing_number_list_params
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
from ..types.routing_number_list_response import RoutingNumberListResponse

__all__ = ["RoutingNumbersResource", "AsyncRoutingNumbersResource"]


class RoutingNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return RoutingNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return RoutingNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        routing_number: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[RoutingNumberListResponse]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          routing_number: Filter financial institutions by routing number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/routing_numbers",
            page=SyncPage[RoutingNumberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "routing_number": routing_number,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    routing_number_list_params.RoutingNumberListParams,
                ),
            ),
            model=RoutingNumberListResponse,
        )


class AsyncRoutingNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutingNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncRoutingNumbersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        routing_number: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RoutingNumberListResponse, AsyncPage[RoutingNumberListResponse]]:
        """
        You can use this API to confirm if a routing number is valid, such as when a
        user is providing you with bank account details. Since routing numbers uniquely
        identify a bank, this will always return 0 or 1 entry. In Sandbox, the only
        valid routing number for this method is 110000000.

        Args:
          routing_number: Filter financial institutions by routing number.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/routing_numbers",
            page=AsyncPage[RoutingNumberListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "routing_number": routing_number,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    routing_number_list_params.RoutingNumberListParams,
                ),
            ),
            model=RoutingNumberListResponse,
        )


class RoutingNumbersResourceWithRawResponse:
    def __init__(self, routing_numbers: RoutingNumbersResource) -> None:
        self._routing_numbers = routing_numbers

        self.list = to_raw_response_wrapper(
            routing_numbers.list,
        )


class AsyncRoutingNumbersResourceWithRawResponse:
    def __init__(self, routing_numbers: AsyncRoutingNumbersResource) -> None:
        self._routing_numbers = routing_numbers

        self.list = async_to_raw_response_wrapper(
            routing_numbers.list,
        )


class RoutingNumbersResourceWithStreamingResponse:
    def __init__(self, routing_numbers: RoutingNumbersResource) -> None:
        self._routing_numbers = routing_numbers

        self.list = to_streamed_response_wrapper(
            routing_numbers.list,
        )


class AsyncRoutingNumbersResourceWithStreamingResponse:
    def __init__(self, routing_numbers: AsyncRoutingNumbersResource) -> None:
        self._routing_numbers = routing_numbers

        self.list = async_to_streamed_response_wrapper(
            routing_numbers.list,
        )
