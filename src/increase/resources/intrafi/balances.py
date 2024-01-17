# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.intrafi import IntrafiBalance

__all__ = ["Balances", "AsyncBalances"]


class Balances(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesWithRawResponse:
        return BalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesWithStreamingResponse:
        return BalancesWithStreamingResponse(self)

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


class AsyncBalances(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesWithRawResponse:
        return AsyncBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesWithStreamingResponse:
        return AsyncBalancesWithStreamingResponse(self)

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


class BalancesWithRawResponse:
    def __init__(self, balances: Balances) -> None:
        self._balances = balances

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            balances.retrieve,
        )


class AsyncBalancesWithRawResponse:
    def __init__(self, balances: AsyncBalances) -> None:
        self._balances = balances

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            balances.retrieve,
        )


class BalancesWithStreamingResponse:
    def __init__(self, balances: Balances) -> None:
        self._balances = balances

        self.retrieve = to_streamed_response_wrapper(
            balances.retrieve,
        )


class AsyncBalancesWithStreamingResponse:
    def __init__(self, balances: AsyncBalances) -> None:
        self._balances = balances

        self.retrieve = async_to_streamed_response_wrapper(
            balances.retrieve,
        )
