# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import Body, Query, Headers
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.inbound_real_time_payments_transfer_simulation_result import (
    InboundRealTimePaymentsTransferSimulationResult,
)

__all__ = ["RealTimePaymentsTransfers", "AsyncRealTimePaymentsTransfers"]


class RealTimePaymentsTransfers(SyncAPIResource):
    def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """
        Simulates an inbound Real Time Payments transfer to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real Time Payments Transfer is
              for.

          amount: The transfer amount in USD cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body={
                "account_number_id": account_number_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )


class AsyncRealTimePaymentsTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """
        Simulates an inbound Real Time Payments transfer to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real Time Payments Transfer is
              for.

          amount: The transfer amount in USD cents. Must be positive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body={
                "account_number_id": account_number_id,
                "amount": amount,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )
