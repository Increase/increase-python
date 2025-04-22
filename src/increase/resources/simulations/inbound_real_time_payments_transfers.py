# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import inbound_real_time_payments_transfer_create_params
from ...types.inbound_real_time_payments_transfer import InboundRealTimePaymentsTransfer

__all__ = ["InboundRealTimePaymentsTransfersResource", "AsyncInboundRealTimePaymentsTransfersResource"]


class InboundRealTimePaymentsTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundRealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundRealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundRealTimePaymentsTransfersResourceWithStreamingResponse(self)

    def create(
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
    ) -> InboundRealTimePaymentsTransfer:
        """
        Simulates an
        [Inbound Real-Time Payments Transfer](#inbound-real-time-payments-transfers) to
        your account. Real-Time Payments are a beta feature.

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
                inbound_real_time_payments_transfer_create_params.InboundRealTimePaymentsTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundRealTimePaymentsTransfer,
        )


class AsyncInboundRealTimePaymentsTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(self)

    async def create(
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
    ) -> InboundRealTimePaymentsTransfer:
        """
        Simulates an
        [Inbound Real-Time Payments Transfer](#inbound-real-time-payments-transfers) to
        your account. Real-Time Payments are a beta feature.

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
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "debtor_account_number": debtor_account_number,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "remittance_information": remittance_information,
                    "request_for_payment_id": request_for_payment_id,
                },
                inbound_real_time_payments_transfer_create_params.InboundRealTimePaymentsTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundRealTimePaymentsTransfer,
        )


class InboundRealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, inbound_real_time_payments_transfers: InboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.create = to_raw_response_wrapper(
            inbound_real_time_payments_transfers.create,
        )


class AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
    def __init__(self, inbound_real_time_payments_transfers: AsyncInboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.create = async_to_raw_response_wrapper(
            inbound_real_time_payments_transfers.create,
        )


class InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_real_time_payments_transfers: InboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.create = to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.create,
        )


class AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_real_time_payments_transfers: AsyncInboundRealTimePaymentsTransfersResource) -> None:
        self._inbound_real_time_payments_transfers = inbound_real_time_payments_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_real_time_payments_transfers.create,
        )
