# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import (
    InboundRealTimePaymentsTransferSimulationResult,
    real_time_payments_transfer_create_inbound_params,
)

__all__ = ["RealTimePaymentsTransfers", "AsyncRealTimePaymentsTransfers"]


class RealTimePaymentsTransfers(SyncAPIResource):
    def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_name: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        remittance_information: str | NotGiven = NOT_GIVEN,
        request_for_payment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real Time Payments transfer to your account.

        Real Time
        Payments are a beta feature.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real Time Payments Transfer is
              for.

          amount: The transfer amount in USD cents. Must be positive.

          debtor_account_number: The account number of the account that sent the transfer.

          debtor_name: The name provided by the sender of the transfer.

          debtor_routing_number: The routing number of the account that sent the transfer.

          remittance_information: Additional information included with the transfer.

          request_for_payment_id: The identifier of a pending Request for Payment that this transfer will fulfill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "request_for_payment_id": request_for_payment_id,
                    "debtor_name": debtor_name,
                    "debtor_account_number": debtor_account_number,
                    "debtor_routing_number": debtor_routing_number,
                    "remittance_information": remittance_information,
                },
                real_time_payments_transfer_create_inbound_params.RealTimePaymentsTransferCreateInboundParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )


class AsyncRealTimePaymentsTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_name: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        remittance_information: str | NotGiven = NOT_GIVEN,
        request_for_payment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real Time Payments transfer to your account.

        Real Time
        Payments are a beta feature.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real Time Payments Transfer is
              for.

          amount: The transfer amount in USD cents. Must be positive.

          debtor_account_number: The account number of the account that sent the transfer.

          debtor_name: The name provided by the sender of the transfer.

          debtor_routing_number: The routing number of the account that sent the transfer.

          remittance_information: Additional information included with the transfer.

          request_for_payment_id: The identifier of a pending Request for Payment that this transfer will fulfill.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "request_for_payment_id": request_for_payment_id,
                    "debtor_name": debtor_name,
                    "debtor_account_number": debtor_account_number,
                    "debtor_routing_number": debtor_routing_number,
                    "remittance_information": remittance_information,
                },
                real_time_payments_transfer_create_inbound_params.RealTimePaymentsTransferCreateInboundParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )
