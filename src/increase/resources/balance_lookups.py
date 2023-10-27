# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import datetime

from ..types import BalanceLookupLookupResponse, balance_lookup_lookup_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Increase, AsyncIncrease

__all__ = ["BalanceLookups", "AsyncBalanceLookups"]


class BalanceLookups(SyncAPIResource):
    with_raw_response: BalanceLookupsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.with_raw_response = BalanceLookupsWithRawResponse(self)

    def lookup(
        self,
        *,
        account_id: str,
        at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceLookupLookupResponse:
        """
        Look up the balance for an Account

        Args:
          account_id: The Account to query the balance for.

          at_time: The moment to query the balance at. If not set, returns the current balances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/balance_lookups",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "at_time": at_time,
                },
                balance_lookup_lookup_params.BalanceLookupLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceLookupLookupResponse,
        )


class AsyncBalanceLookups(AsyncAPIResource):
    with_raw_response: AsyncBalanceLookupsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBalanceLookupsWithRawResponse(self)

    async def lookup(
        self,
        *,
        account_id: str,
        at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceLookupLookupResponse:
        """
        Look up the balance for an Account

        Args:
          account_id: The Account to query the balance for.

          at_time: The moment to query the balance at. If not set, returns the current balances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/balance_lookups",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "at_time": at_time,
                },
                balance_lookup_lookup_params.BalanceLookupLookupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceLookupLookupResponse,
        )


class BalanceLookupsWithRawResponse:
    def __init__(self, balance_lookups: BalanceLookups) -> None:
        self.lookup = to_raw_response_wrapper(
            balance_lookups.lookup,
        )


class AsyncBalanceLookupsWithRawResponse:
    def __init__(self, balance_lookups: AsyncBalanceLookups) -> None:
        self.lookup = async_to_raw_response_wrapper(
            balance_lookups.lookup,
        )
