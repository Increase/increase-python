# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import InboundWireDrawdownRequest
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import inbound_wire_drawdown_request_create_params

__all__ = ["InboundWireDrawdownRequests", "AsyncInboundWireDrawdownRequests"]


class InboundWireDrawdownRequests(SyncAPIResource):
    def create(
        self,
        *,
        amount: int,
        beneficiary_account_number: str,
        beneficiary_routing_number: str,
        currency: str,
        message_to_recipient: str,
        originator_account_number: str,
        originator_routing_number: str,
        recipient_account_number_id: str,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line1: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line2: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line3: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line4: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireDrawdownRequest:
        """
        Simulates the receival of an
        [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

        Args:
          amount: The amount being requested in cents.

          beneficiary_account_number: The drawdown request's beneficiary's account number.

          beneficiary_routing_number: The drawdown request's beneficiary's routing number.

          currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
              requested. Will always be "USD".

          message_to_recipient: A message from the drawdown request's originator.

          originator_account_number: The drawdown request's originator's account number.

          originator_routing_number: The drawdown request's originator's routing number.

          recipient_account_number_id: The Account Number to which the recipient of this request is being requested to
              send funds from.

          beneficiary_address_line1: Line 1 of the drawdown request's beneficiary's address.

          beneficiary_address_line2: Line 2 of the drawdown request's beneficiary's address.

          beneficiary_address_line3: Line 3 of the drawdown request's beneficiary's address.

          beneficiary_name: The drawdown request's beneficiary's name.

          originator_address_line1: Line 1 of the drawdown request's originator's address.

          originator_address_line2: Line 2 of the drawdown request's originator's address.

          originator_address_line3: Line 3 of the drawdown request's originator's address.

          originator_name: The drawdown request's originator's name.

          originator_to_beneficiary_information_line1: Line 1 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line2: Line 2 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line3: Line 3 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line4: Line 4 of the information conveyed from the originator of the message to the
              beneficiary.

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
                    "beneficiary_account_number": beneficiary_account_number,
                    "beneficiary_routing_number": beneficiary_routing_number,
                    "currency": currency,
                    "message_to_recipient": message_to_recipient,
                    "originator_account_number": originator_account_number,
                    "originator_routing_number": originator_routing_number,
                    "recipient_account_number_id": recipient_account_number_id,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "beneficiary_name": beneficiary_name,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "originator_to_beneficiary_information_line1": originator_to_beneficiary_information_line1,
                    "originator_to_beneficiary_information_line2": originator_to_beneficiary_information_line2,
                    "originator_to_beneficiary_information_line3": originator_to_beneficiary_information_line3,
                    "originator_to_beneficiary_information_line4": originator_to_beneficiary_information_line4,
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


class AsyncInboundWireDrawdownRequests(AsyncAPIResource):
    async def create(
        self,
        *,
        amount: int,
        beneficiary_account_number: str,
        beneficiary_routing_number: str,
        currency: str,
        message_to_recipient: str,
        originator_account_number: str,
        originator_routing_number: str,
        recipient_account_number_id: str,
        beneficiary_address_line1: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line2: str | NotGiven = NOT_GIVEN,
        beneficiary_address_line3: str | NotGiven = NOT_GIVEN,
        beneficiary_name: str | NotGiven = NOT_GIVEN,
        originator_address_line1: str | NotGiven = NOT_GIVEN,
        originator_address_line2: str | NotGiven = NOT_GIVEN,
        originator_address_line3: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line1: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line2: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line3: str | NotGiven = NOT_GIVEN,
        originator_to_beneficiary_information_line4: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundWireDrawdownRequest:
        """
        Simulates the receival of an
        [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

        Args:
          amount: The amount being requested in cents.

          beneficiary_account_number: The drawdown request's beneficiary's account number.

          beneficiary_routing_number: The drawdown request's beneficiary's routing number.

          currency: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
              requested. Will always be "USD".

          message_to_recipient: A message from the drawdown request's originator.

          originator_account_number: The drawdown request's originator's account number.

          originator_routing_number: The drawdown request's originator's routing number.

          recipient_account_number_id: The Account Number to which the recipient of this request is being requested to
              send funds from.

          beneficiary_address_line1: Line 1 of the drawdown request's beneficiary's address.

          beneficiary_address_line2: Line 2 of the drawdown request's beneficiary's address.

          beneficiary_address_line3: Line 3 of the drawdown request's beneficiary's address.

          beneficiary_name: The drawdown request's beneficiary's name.

          originator_address_line1: Line 1 of the drawdown request's originator's address.

          originator_address_line2: Line 2 of the drawdown request's originator's address.

          originator_address_line3: Line 3 of the drawdown request's originator's address.

          originator_name: The drawdown request's originator's name.

          originator_to_beneficiary_information_line1: Line 1 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line2: Line 2 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line3: Line 3 of the information conveyed from the originator of the message to the
              beneficiary.

          originator_to_beneficiary_information_line4: Line 4 of the information conveyed from the originator of the message to the
              beneficiary.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_wire_drawdown_requests",
            body=maybe_transform(
                {
                    "amount": amount,
                    "beneficiary_account_number": beneficiary_account_number,
                    "beneficiary_routing_number": beneficiary_routing_number,
                    "currency": currency,
                    "message_to_recipient": message_to_recipient,
                    "originator_account_number": originator_account_number,
                    "originator_routing_number": originator_routing_number,
                    "recipient_account_number_id": recipient_account_number_id,
                    "beneficiary_address_line1": beneficiary_address_line1,
                    "beneficiary_address_line2": beneficiary_address_line2,
                    "beneficiary_address_line3": beneficiary_address_line3,
                    "beneficiary_name": beneficiary_name,
                    "originator_address_line1": originator_address_line1,
                    "originator_address_line2": originator_address_line2,
                    "originator_address_line3": originator_address_line3,
                    "originator_name": originator_name,
                    "originator_to_beneficiary_information_line1": originator_to_beneficiary_information_line1,
                    "originator_to_beneficiary_information_line2": originator_to_beneficiary_information_line2,
                    "originator_to_beneficiary_information_line3": originator_to_beneficiary_information_line3,
                    "originator_to_beneficiary_information_line4": originator_to_beneficiary_information_line4,
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
