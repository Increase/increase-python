# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.intrafi_balance import IntrafiBalance

__all__ = ["IntrafiBalancesResource", "AsyncIntrafiBalancesResource"]


class IntrafiBalancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntrafiBalancesResourceWithRawResponse:
        return IntrafiBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntrafiBalancesResourceWithStreamingResponse:
        return IntrafiBalancesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiBalance:
        """
        Get IntraFi balances by bank

        Args:
          account_id: The identifier of the Account to get balances for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/intrafi_balances/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiBalance,
        )


class AsyncIntrafiBalancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntrafiBalancesResourceWithRawResponse:
        return AsyncIntrafiBalancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntrafiBalancesResourceWithStreamingResponse:
        return AsyncIntrafiBalancesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntrafiBalance:
        """
        Get IntraFi balances by bank

        Args:
          account_id: The identifier of the Account to get balances for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/intrafi_balances/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntrafiBalance,
        )


class IntrafiBalancesResourceWithRawResponse:
    def __init__(self, intrafi_balances: IntrafiBalancesResource) -> None:
        self._intrafi_balances = intrafi_balances

        self.retrieve = to_raw_response_wrapper(
            intrafi_balances.retrieve,
        )


class AsyncIntrafiBalancesResourceWithRawResponse:
    def __init__(self, intrafi_balances: AsyncIntrafiBalancesResource) -> None:
        self._intrafi_balances = intrafi_balances

        self.retrieve = async_to_raw_response_wrapper(
            intrafi_balances.retrieve,
        )


class IntrafiBalancesResourceWithStreamingResponse:
    def __init__(self, intrafi_balances: IntrafiBalancesResource) -> None:
        self._intrafi_balances = intrafi_balances

        self.retrieve = to_streamed_response_wrapper(
            intrafi_balances.retrieve,
        )


class AsyncIntrafiBalancesResourceWithStreamingResponse:
    def __init__(self, intrafi_balances: AsyncIntrafiBalancesResource) -> None:
        self._intrafi_balances = intrafi_balances

        self.retrieve = async_to_streamed_response_wrapper(
            intrafi_balances.retrieve,
        )
