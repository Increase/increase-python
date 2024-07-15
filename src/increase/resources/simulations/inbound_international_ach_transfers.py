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
from ...types.simulations import inbound_international_ach_transfer_create_params
from ...types.simulations.inbound_international_ach_transfer_create_response import (
    InboundInternationalACHTransferCreateResponse,
)

__all__ = ["InboundInternationalACHTransfersResource", "AsyncInboundInternationalACHTransfersResource"]


class InboundInternationalACHTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundInternationalACHTransfersResourceWithRawResponse:
        return InboundInternationalACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundInternationalACHTransfersResourceWithStreamingResponse:
        return InboundInternationalACHTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        foreign_payment_amount: int,
        originating_currency_code: str,
        originator_company_entry_description: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        receiver_identification_number: str | NotGiven = NOT_GIVEN,
        receiving_company_or_individual_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundInternationalACHTransferCreateResponse:
        """Simulates an inbound international ACH transfer to your account.

        This imitates
        initiating a transfer to an Increase account from a different financial
        institution. The transfer may be either a credit or a debit depending on if the
        `amount` is positive or negative. The result of calling this API will contain
        the created transfer. .

        Args:
          account_number_id: The identifier of the Account Number the inbound international ACH Transfer is
              for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          foreign_payment_amount: The amount in the minor unit of the foreign payment currency. For dollars, for
              example, this is cents.

          originating_currency_code: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
              originating bank account.

          originator_company_entry_description: A description field set by the originator.

          originator_name: Either the name of the originator or an intermediary money transmitter.

          receiver_identification_number: An identification number the originator uses for the receiver.

          receiving_company_or_individual_name: The name of the receiver of the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_international_ach_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "foreign_payment_amount": foreign_payment_amount,
                    "originating_currency_code": originating_currency_code,
                    "originator_company_entry_description": originator_company_entry_description,
                    "originator_name": originator_name,
                    "receiver_identification_number": receiver_identification_number,
                    "receiving_company_or_individual_name": receiving_company_or_individual_name,
                },
                inbound_international_ach_transfer_create_params.InboundInternationalACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundInternationalACHTransferCreateResponse,
        )


class AsyncInboundInternationalACHTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundInternationalACHTransfersResourceWithRawResponse:
        return AsyncInboundInternationalACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundInternationalACHTransfersResourceWithStreamingResponse:
        return AsyncInboundInternationalACHTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        foreign_payment_amount: int,
        originating_currency_code: str,
        originator_company_entry_description: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        receiver_identification_number: str | NotGiven = NOT_GIVEN,
        receiving_company_or_individual_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundInternationalACHTransferCreateResponse:
        """Simulates an inbound international ACH transfer to your account.

        This imitates
        initiating a transfer to an Increase account from a different financial
        institution. The transfer may be either a credit or a debit depending on if the
        `amount` is positive or negative. The result of calling this API will contain
        the created transfer. .

        Args:
          account_number_id: The identifier of the Account Number the inbound international ACH Transfer is
              for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          foreign_payment_amount: The amount in the minor unit of the foreign payment currency. For dollars, for
              example, this is cents.

          originating_currency_code: The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
              originating bank account.

          originator_company_entry_description: A description field set by the originator.

          originator_name: Either the name of the originator or an intermediary money transmitter.

          receiver_identification_number: An identification number the originator uses for the receiver.

          receiving_company_or_individual_name: The name of the receiver of the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_international_ach_transfers",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "foreign_payment_amount": foreign_payment_amount,
                    "originating_currency_code": originating_currency_code,
                    "originator_company_entry_description": originator_company_entry_description,
                    "originator_name": originator_name,
                    "receiver_identification_number": receiver_identification_number,
                    "receiving_company_or_individual_name": receiving_company_or_individual_name,
                },
                inbound_international_ach_transfer_create_params.InboundInternationalACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundInternationalACHTransferCreateResponse,
        )


class InboundInternationalACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_international_ach_transfers: InboundInternationalACHTransfersResource) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = to_raw_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class AsyncInboundInternationalACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_international_ach_transfers: AsyncInboundInternationalACHTransfersResource) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = async_to_raw_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class InboundInternationalACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_international_ach_transfers: InboundInternationalACHTransfersResource) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = to_streamed_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class AsyncInboundInternationalACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_international_ach_transfers: AsyncInboundInternationalACHTransfersResource) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_international_ach_transfers.create,
        )
