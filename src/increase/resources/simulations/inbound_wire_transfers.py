# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import inbound_wire_transfer_create_params
from ...types.inbound_wire_transfer import InboundWireTransfer

__all__ = ["InboundWireTransfersResource", "AsyncInboundWireTransfersResource"]


class InboundWireTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundWireTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_reference: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        originator_routing_number: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line1: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line2: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line3: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line4: str | NotGiven = NOT_GIVEN,
        sender_reference: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Simulates an [Inbound Wire Transfer](#inbound-wire-transfers) to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

          beneficiary_address_line1: The sending bank will set beneficiary_address_line1 in production. You can
              simulate any value here.

          beneficiary_address_line2: The sending bank will set beneficiary_address_line2 in production. You can
              simulate any value here.

          beneficiary_address_line3: The sending bank will set beneficiary_address_line3 in production. You can
              simulate any value here.

          beneficiary_name: The sending bank will set beneficiary_name in production. You can simulate any
              value here.

          beneficiary_reference: The sending bank will set beneficiary_reference in production. You can simulate
              any value here.

          originator_address_line1: The sending bank will set originator_address_line1 in production. You can
              simulate any value here.

          originator_address_line2: The sending bank will set originator_address_line2 in production. You can
              simulate any value here.

          originator_address_line3: The sending bank will set originator_address_line3 in production. You can
              simulate any value here.

          originator_name: The sending bank will set originator_name in production. You can simulate any
              value here.

          originator_routing_number: The sending bank will set originator_routing_number in production. You can
              simulate any value here.

          originator_to_beneficiary_information_line1: The sending bank will set originator_to_beneficiary_information_line1 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line2: The sending bank will set originator_to_beneficiary_information_line2 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line3: The sending bank will set originator_to_beneficiary_information_line3 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line4: The sending bank will set originator_to_beneficiary_information_line4 in
              production. You can simulate any value here.

          sender_reference: The sending bank will set sender_reference in production. You can simulate any
              value here.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_wire_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "beneficiary_name": beneficiary_name,
                    "beneficiary_reference": beneficiary_reference,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "originator_routing_number": originator_routing_number,
                    "originator_to_beneficiary_information_line1": originator_to_beneficiary_information_line1,
                    "originator_to_beneficiary_information_line2": originator_to_beneficiary_information_line2,
                    "originator_to_beneficiary_information_line3": originator_to_beneficiary_information_line3,
                    "originator_to_beneficiary_information_line4": originator_to_beneficiary_information_line4,
                    "sender_reference": sender_reference,
                },
                inbound_wire_transfer_create_params.InboundWireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireTransfer,
        )


class AsyncInboundWireTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundWireTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundWireTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundWireTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundWireTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        beneficiary_reference: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        originator_routing_number: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line1: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line2: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line3: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line4: str | NotGiven = NOT_GIVEN,
        sender_reference: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Simulates an [Inbound Wire Transfer](#inbound-wire-transfers) to your account.

        Args:
          account_number_id: The identifier of the Account Number the inbound Wire Transfer is for.

          amount: The transfer amount in cents. Must be positive.

          beneficiary_address_line1: The sending bank will set beneficiary_address_line1 in production. You can
              simulate any value here.

          beneficiary_address_line2: The sending bank will set beneficiary_address_line2 in production. You can
              simulate any value here.

          beneficiary_address_line3: The sending bank will set beneficiary_address_line3 in production. You can
              simulate any value here.

          beneficiary_name: The sending bank will set beneficiary_name in production. You can simulate any
              value here.

          beneficiary_reference: The sending bank will set beneficiary_reference in production. You can simulate
              any value here.

          originator_address_line1: The sending bank will set originator_address_line1 in production. You can
              simulate any value here.

          originator_address_line2: The sending bank will set originator_address_line2 in production. You can
              simulate any value here.

          originator_address_line3: The sending bank will set originator_address_line3 in production. You can
              simulate any value here.

          originator_name: The sending bank will set originator_name in production. You can simulate any
              value here.

          originator_routing_number: The sending bank will set originator_routing_number in production. You can
              simulate any value here.

          originator_to_beneficiary_information_line1: The sending bank will set originator_to_beneficiary_information_line1 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line2: The sending bank will set originator_to_beneficiary_information_line2 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line3: The sending bank will set originator_to_beneficiary_information_line3 in
              production. You can simulate any value here.

          originator_to_beneficiary_information_line4: The sending bank will set originator_to_beneficiary_information_line4 in
              production. You can simulate any value here.

          sender_reference: The sending bank will set sender_reference in production. You can simulate any
              value here.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_wire_transfers",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "beneficiary_name": beneficiary_name,
                    "beneficiary_reference": beneficiary_reference,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "originator_routing_number": originator_routing_number,
                    "originator_to_beneficiary_information_line1": originator_to_beneficiary_information_line1,
                    "originator_to_beneficiary_information_line2": originator_to_beneficiary_information_line2,
                    "originator_to_beneficiary_information_line3": originator_to_beneficiary_information_line3,
                    "originator_to_beneficiary_information_line4": originator_to_beneficiary_information_line4,
                    "sender_reference": sender_reference,
                },
                inbound_wire_transfer_create_params.InboundWireTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundWireTransfer,
        )


class InboundWireTransfersResourceWithRawResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.create = to_raw_response_wrapper(
            inbound_wire_transfers.create,
        )


class AsyncInboundWireTransfersResourceWithRawResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.create = async_to_raw_response_wrapper(
            inbound_wire_transfers.create,
        )


class InboundWireTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: InboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.create = to_streamed_response_wrapper(
            inbound_wire_transfers.create,
        )


class AsyncInboundWireTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_wire_transfers: AsyncInboundWireTransfersResource) -> None:
        self._inbound_wire_transfers = inbound_wire_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_wire_transfers.create,
        )
