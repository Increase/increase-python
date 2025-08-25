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
from ...types.simulations import inbound_wire_drawdown_request_create_params
from ...types.inbound_wire_drawdown_request import InboundWireDrawdownRequest

__all__ = ["InboundWireDrawdownRequestsResource", "AsyncInboundWireDrawdownRequestsResource"]


class InboundWireDrawdownRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundWireDrawdownRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        creditor_account_number: str,
        creditor_routing_number: str,
        currency: str,
        recipient_account_number_id: str,
        creditor_address_line1: str | NotGiven = NOT_GIVEN,
        creditor_address_line2: str | NotGiven = NOT_GIVEN,
        creditor_address_line3: str | NotGiven = NOT_GIVEN,
        creditor_name: str | NotGiven = NOT_GIVEN,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_address_line1: str | NotGiven = NOT_GIVEN,
        debtor_address_line2: str | NotGiven = NOT_GIVEN,
        debtor_address_line3: str | NotGiven = NOT_GIVEN,
        debtor_name: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        end_to_end_identification: str | NotGiven = NOT_GIVEN,
        instruction_identification: str | NotGiven = NOT_GIVEN,
        unique_end_to_end_transaction_reference: str | NotGiven = NOT_GIVEN,
        unstructured_remittance_information: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireDrawdownRequest:
        """
        Simulates receiving an
        [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

        Args:
          amount: The amount being requested in cents.

          creditor_account_number: The creditor's account number.

          creditor_routing_number: The creditor's routing number.

          currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
              requested. Will always be "USD".

          recipient_account_number_id: The Account Number to which the recipient of this request is being requested to
              send funds from.

          creditor_address_line1: A free-form address field set by the sender representing the first line of the
              creditor's address.

          creditor_address_line2: A free-form address field set by the sender representing the second line of the
              creditor's address.

          creditor_address_line3: A free-form address field set by the sender representing the third line of the
              creditor's address.

          creditor_name: A free-form name field set by the sender representing the creditor's name.

          debtor_account_number: The debtor's account number.

          debtor_address_line1: A free-form address field set by the sender representing the first line of the
              debtor's address.

          debtor_address_line2: A free-form address field set by the sender representing the second line of the
              debtor's address.

          debtor_address_line3: A free-form address field set by the sender.

          debtor_name: A free-form name field set by the sender representing the debtor's name.

          debtor_routing_number: The debtor's routing number.

          end_to_end_identification: A free-form reference string set by the sender, to help identify the transfer.

          instruction_identification: The sending bank's identifier for the wire transfer.

          unique_end_to_end_transaction_reference: The Unique End-to-end Transaction Reference
              ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
              of the transfer.

          unstructured_remittance_information: A free-form message set by the sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_wire_drawdown_requests",
            body=maybe_transform(
                {
                    "amount": amount,
                    "creditor_account_number": creditor_account_number,
                    "creditor_routing_number": creditor_routing_number,
                    "currency": currency,
                    "recipient_account_number_id": recipient_account_number_id,
                    "creditor_address_line1": creditor_address_line1,
                    "creditor_address_line2": creditor_address_line2,
                    "creditor_address_line3": creditor_address_line3,
                    "creditor_name": creditor_name,
                    "debtor_account_number": debtor_account_number,
                    "debtor_address_line1": debtor_address_line1,
                    "debtor_address_line2": debtor_address_line2,
                    "debtor_address_line3": debtor_address_line3,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "end_to_end_identification": end_to_end_identification,
                    "instruction_identification": instruction_identification,
                    "unique_end_to_end_transaction_reference": unique_end_to_end_transaction_reference,
                    "unstructured_remittance_information": unstructured_remittance_information,
                },
                inbound_wire_drawdown_request_create_params.InboundWireDrawdownRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireDrawdownRequest,
        )


class AsyncInboundWireDrawdownRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundWireDrawdownRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        creditor_account_number: str,
        creditor_routing_number: str,
        currency: str,
        recipient_account_number_id: str,
        creditor_address_line1: str | NotGiven = NOT_GIVEN,
        creditor_address_line2: str | NotGiven = NOT_GIVEN,
        creditor_address_line3: str | NotGiven = NOT_GIVEN,
        creditor_name: str | NotGiven = NOT_GIVEN,
        debtor_account_number: str | NotGiven = NOT_GIVEN,
        debtor_address_line1: str | NotGiven = NOT_GIVEN,
        debtor_address_line2: str | NotGiven = NOT_GIVEN,
        debtor_address_line3: str | NotGiven = NOT_GIVEN,
        debtor_name: str | NotGiven = NOT_GIVEN,
        debtor_routing_number: str | NotGiven = NOT_GIVEN,
        end_to_end_identification: str | NotGiven = NOT_GIVEN,
        instruction_identification: str | NotGiven = NOT_GIVEN,
        unique_end_to_end_transaction_reference: str | NotGiven = NOT_GIVEN,
        unstructured_remittance_information: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireDrawdownRequest:
        """
        Simulates receiving an
        [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

        Args:
          amount: The amount being requested in cents.

          creditor_account_number: The creditor's account number.

          creditor_routing_number: The creditor's routing number.

          currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
              requested. Will always be "USD".

          recipient_account_number_id: The Account Number to which the recipient of this request is being requested to
              send funds from.

          creditor_address_line1: A free-form address field set by the sender representing the first line of the
              creditor's address.

          creditor_address_line2: A free-form address field set by the sender representing the second line of the
              creditor's address.

          creditor_address_line3: A free-form address field set by the sender representing the third line of the
              creditor's address.

          creditor_name: A free-form name field set by the sender representing the creditor's name.

          debtor_account_number: The debtor's account number.

          debtor_address_line1: A free-form address field set by the sender representing the first line of the
              debtor's address.

          debtor_address_line2: A free-form address field set by the sender representing the second line of the
              debtor's address.

          debtor_address_line3: A free-form address field set by the sender.

          debtor_name: A free-form name field set by the sender representing the debtor's name.

          debtor_routing_number: The debtor's routing number.

          end_to_end_identification: A free-form reference string set by the sender, to help identify the transfer.

          instruction_identification: The sending bank's identifier for the wire transfer.

          unique_end_to_end_transaction_reference: The Unique End-to-end Transaction Reference
              ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
              of the transfer.

          unstructured_remittance_information: A free-form message set by the sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_wire_drawdown_requests",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "creditor_account_number": creditor_account_number,
                    "creditor_routing_number": creditor_routing_number,
                    "currency": currency,
                    "recipient_account_number_id": recipient_account_number_id,
                    "creditor_address_line1": creditor_address_line1,
                    "creditor_address_line2": creditor_address_line2,
                    "creditor_address_line3": creditor_address_line3,
                    "creditor_name": creditor_name,
                    "debtor_account_number": debtor_account_number,
                    "debtor_address_line1": debtor_address_line1,
                    "debtor_address_line2": debtor_address_line2,
                    "debtor_address_line3": debtor_address_line3,
                    "debtor_name": debtor_name,
                    "debtor_routing_number": debtor_routing_number,
                    "end_to_end_identification": end_to_end_identification,
                    "instruction_identification": instruction_identification,
                    "unique_end_to_end_transaction_reference": unique_end_to_end_transaction_reference,
                    "unstructured_remittance_information": unstructured_remittance_information,
                },
                inbound_wire_drawdown_request_create_params.InboundWireDrawdownRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireDrawdownRequest,
        )


class InboundWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.create = to_raw_response_wrapper(
            inbound_wire_drawdown_requests.create,
        )


class AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.create = async_to_raw_response_wrapper(
            inbound_wire_drawdown_requests.create,
        )


class InboundWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: InboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.create = to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.create,
        )


class AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
    def __init__(self, inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequestsResource) -> None:
        self._inbound_wire_drawdown_requests = inbound_wire_drawdown_requests

        self.create = async_to_streamed_response_wrapper(
            inbound_wire_drawdown_requests.create,
        )
