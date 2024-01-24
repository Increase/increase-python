# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import InboundWireTransfer
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import wire_transfer_create_inbound_params

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireTransfersWithRawResponse:
        return WireTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireTransfersWithStreamingResponse:
        return WireTransfersWithStreamingResponse(self)

    def create_inbound(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Simulates an inbound Wire Transfer to your account.

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
                },
                wire_transfer_create_inbound_params.WireTransferCreateInboundParams,
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


class AsyncWireTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireTransfersWithRawResponse:
        return AsyncWireTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireTransfersWithStreamingResponse:
        return AsyncWireTransfersWithStreamingResponse(self)

    async def create_inbound(
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireTransfer:
        """
        Simulates an inbound Wire Transfer to your account.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
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
                },
                wire_transfer_create_inbound_params.WireTransferCreateInboundParams,
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


class WireTransfersWithRawResponse:
    def __init__(self, wire_transfers: WireTransfers) -> None:
        self._wire_transfers = wire_transfers

        self.create_inbound = _legacy_response.to_raw_response_wrapper(
            wire_transfers.create_inbound,
        )


class AsyncWireTransfersWithRawResponse:
    def __init__(self, wire_transfers: AsyncWireTransfers) -> None:
        self._wire_transfers = wire_transfers

        self.create_inbound = _legacy_response.async_to_raw_response_wrapper(
            wire_transfers.create_inbound,
        )


class WireTransfersWithStreamingResponse:
    def __init__(self, wire_transfers: WireTransfers) -> None:
        self._wire_transfers = wire_transfers

        self.create_inbound = to_streamed_response_wrapper(
            wire_transfers.create_inbound,
        )


class AsyncWireTransfersWithStreamingResponse:
    def __init__(self, wire_transfers: AsyncWireTransfers) -> None:
        self._wire_transfers = wire_transfers

        self.create_inbound = async_to_streamed_response_wrapper(
            wire_transfers.create_inbound,
        )
