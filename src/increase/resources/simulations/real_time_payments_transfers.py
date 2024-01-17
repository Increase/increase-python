# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import RealTimePaymentsTransfer
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import (
    InboundRealTimePaymentsTransferSimulationResult,
    real_time_payments_transfer_complete_params,
    real_time_payments_transfer_create_inbound_params,
)

__all__ = ["RealTimePaymentsTransfers", "AsyncRealTimePaymentsTransfers"]


class RealTimePaymentsTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealTimePaymentsTransfersWithRawResponse:
        return RealTimePaymentsTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealTimePaymentsTransfersWithStreamingResponse:
        return RealTimePaymentsTransfersWithStreamingResponse(self)

    def complete(
        self,
        real_time_payments_transfer_id: str,
        *,
        rejection: real_time_payments_transfer_complete_params.Rejection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Simulates submission of a Real-Time Payments transfer and handling the response
        from the destination financial institution. This transfer must first have a
        `status` of `pending_submission`.

        Args:
          real_time_payments_transfer_id: The identifier of the Real-Time Payments Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_transfer_id` but received {real_time_payments_transfer_id!r}"
            )
        return self._post(
            f"/simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete",
            body=maybe_transform(
                {"rejection": rejection},
                real_time_payments_transfer_complete_params.RealTimePaymentsTransferCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real-Time Payments transfer to your account.

        Real-Time
        Payments are a beta feature.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real-Time Payments Transfer is
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor_account_number": debtor_account_number,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "remittance_information": remittance_information,
                    "request_for_payment_id": request_for_payment_id,
                },
                real_time_payments_transfer_create_inbound_params.RealTimePaymentsTransferCreateInboundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )


class AsyncRealTimePaymentsTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealTimePaymentsTransfersWithRawResponse:
        return AsyncRealTimePaymentsTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealTimePaymentsTransfersWithStreamingResponse:
        return AsyncRealTimePaymentsTransfersWithStreamingResponse(self)

    async def complete(
        self,
        real_time_payments_transfer_id: str,
        *,
        rejection: real_time_payments_transfer_complete_params.Rejection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> RealTimePaymentsTransfer:
        """
        Simulates submission of a Real-Time Payments transfer and handling the response
        from the destination financial institution. This transfer must first have a
        `status` of `pending_submission`.

        Args:
          real_time_payments_transfer_id: The identifier of the Real-Time Payments Transfer you wish to complete.

          rejection: If set, the simulation will reject the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not real_time_payments_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `real_time_payments_transfer_id` but received {real_time_payments_transfer_id!r}"
            )
        return await self._post(
            f"/simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete",
            body=maybe_transform(
                {"rejection": rejection},
                real_time_payments_transfer_complete_params.RealTimePaymentsTransferCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=RealTimePaymentsTransfer,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundRealTimePaymentsTransferSimulationResult:
        """Simulates an inbound Real-Time Payments transfer to your account.

        Real-Time
        Payments are a beta feature.

        Args:
          account_number_id: The identifier of the Account Number the inbound Real-Time Payments Transfer is
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_real_time_payments_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor_account_number": debtor_account_number,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "remittance_information": remittance_information,
                    "request_for_payment_id": request_for_payment_id,
                },
                real_time_payments_transfer_create_inbound_params.RealTimePaymentsTransferCreateInboundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundRealTimePaymentsTransferSimulationResult,
        )


class RealTimePaymentsTransfersWithRawResponse:
    def __init__(self, real_time_payments_transfers: RealTimePaymentsTransfers) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = _legacy_response.to_raw_response_wrapper(
            real_time_payments_transfers.complete,
        )
        self.create_inbound = _legacy_response.to_raw_response_wrapper(
            real_time_payments_transfers.create_inbound,
        )


class AsyncRealTimePaymentsTransfersWithRawResponse:
    def __init__(self, real_time_payments_transfers: AsyncRealTimePaymentsTransfers) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = _legacy_response.async_to_raw_response_wrapper(
            real_time_payments_transfers.complete,
        )
        self.create_inbound = _legacy_response.async_to_raw_response_wrapper(
            real_time_payments_transfers.create_inbound,
        )


class RealTimePaymentsTransfersWithStreamingResponse:
    def __init__(self, real_time_payments_transfers: RealTimePaymentsTransfers) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = to_streamed_response_wrapper(
            real_time_payments_transfers.complete,
        )
        self.create_inbound = to_streamed_response_wrapper(
            real_time_payments_transfers.create_inbound,
        )


class AsyncRealTimePaymentsTransfersWithStreamingResponse:
    def __init__(self, real_time_payments_transfers: AsyncRealTimePaymentsTransfers) -> None:
        self._real_time_payments_transfers = real_time_payments_transfers

        self.complete = async_to_streamed_response_wrapper(
            real_time_payments_transfers.complete,
        )
        self.create_inbound = async_to_streamed_response_wrapper(
            real_time_payments_transfers.create_inbound,
        )
