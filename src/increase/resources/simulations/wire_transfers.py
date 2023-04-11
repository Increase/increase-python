# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import (
    WireTransferSimulation,
    wire_transfer_create_inbound_params,
)

__all__ = ["WireTransfers", "AsyncWireTransfers"]


class WireTransfers(SyncAPIResource):
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
    ) -> WireTransferSimulation:
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
            cast_to=WireTransferSimulation,
        )


class AsyncWireTransfers(AsyncAPIResource):
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
    ) -> WireTransferSimulation:
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
            cast_to=WireTransferSimulation,
        )
