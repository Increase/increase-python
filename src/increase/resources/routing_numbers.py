# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import RoutingNumber, routing_number_list_params
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

__all__ = ["RoutingNumbers", "AsyncRoutingNumbers"]


class RoutingNumbers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutingNumbersWithRawResponse:
        return RoutingNumbersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutingNumbersWithStreamingResponse:
        return RoutingNumbersWithStreamingResponse(self)

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
    ) -> SyncPage[RoutingNumber]:
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
            page=SyncPage[RoutingNumber],
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
            model=RoutingNumber,
        )


class AsyncRoutingNumbers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutingNumbersWithRawResponse:
        return AsyncRoutingNumbersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutingNumbersWithStreamingResponse:
        return AsyncRoutingNumbersWithStreamingResponse(self)

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
    ) -> AsyncPaginator[RoutingNumber, AsyncPage[RoutingNumber]]:
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
            page=AsyncPage[RoutingNumber],
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
            model=RoutingNumber,
        )


class RoutingNumbersWithRawResponse:
    def __init__(self, routing_numbers: RoutingNumbers) -> None:
        self._routing_numbers = routing_numbers

        self.list = _legacy_response.to_raw_response_wrapper(
            routing_numbers.list,
        )


class AsyncRoutingNumbersWithRawResponse:
    def __init__(self, routing_numbers: AsyncRoutingNumbers) -> None:
        self._routing_numbers = routing_numbers

        self.list = _legacy_response.async_to_raw_response_wrapper(
            routing_numbers.list,
        )


class RoutingNumbersWithStreamingResponse:
    def __init__(self, routing_numbers: RoutingNumbers) -> None:
        self._routing_numbers = routing_numbers

        self.list = to_streamed_response_wrapper(
            routing_numbers.list,
        )


class AsyncRoutingNumbersWithStreamingResponse:
    def __init__(self, routing_numbers: AsyncRoutingNumbers) -> None:
        self._routing_numbers = routing_numbers

        self.list = async_to_streamed_response_wrapper(
            routing_numbers.list,
        )
