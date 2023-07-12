# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import InboundFundsHoldReleaseResponse

__all__ = ["InboundFundsHolds", "AsyncInboundFundsHolds"]


class InboundFundsHolds(SyncAPIResource):
    def release(
        self,
        inbound_funds_hold_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundFundsHoldReleaseResponse:
        """
        This endpoint simulates immediately releasing an inbound funds hold, which might
        be created as a result of e.g., an ACH debit.

        Args:
          inbound_funds_hold_id: The inbound funds hold to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
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


class AsyncInboundFundsHolds(AsyncAPIResource):
    async def release(
        self,
        inbound_funds_hold_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundFundsHoldReleaseResponse:
        """
        This endpoint simulates immediately releasing an inbound funds hold, which might
        be created as a result of e.g., an ACH debit.

        Args:
          inbound_funds_hold_id: The inbound funds hold to release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
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
