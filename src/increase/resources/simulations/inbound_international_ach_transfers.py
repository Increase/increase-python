# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.simulations import inbound_international_ach_transfer_create_params
from ...types.simulations.inbound_international_ach_transfer import InboundInternationalACHTransfer

__all__ = ["InboundInternationalACHTransfers", "AsyncInboundInternationalACHTransfers"]


class InboundInternationalACHTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundInternationalACHTransfersWithRawResponse:
        return InboundInternationalACHTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundInternationalACHTransfersWithStreamingResponse:
        return InboundInternationalACHTransfersWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        foreign_payment_amount: int,
        originating_currency_code: str,
        originator_company_entry_description: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        receiving_company_or_individual_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundInternationalACHTransfer:
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
            cast_to=InboundInternationalACHTransfer,
        )


class AsyncInboundInternationalACHTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundInternationalACHTransfersWithRawResponse:
        return AsyncInboundInternationalACHTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundInternationalACHTransfersWithStreamingResponse:
        return AsyncInboundInternationalACHTransfersWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        foreign_payment_amount: int,
        originating_currency_code: str,
        originator_company_entry_description: str | NotGiven = NOT_GIVEN,
        originator_name: str | NotGiven = NOT_GIVEN,
        receiving_company_or_individual_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundInternationalACHTransfer:
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
            cast_to=InboundInternationalACHTransfer,
        )


class InboundInternationalACHTransfersWithRawResponse:
    def __init__(self, inbound_international_ach_transfers: InboundInternationalACHTransfers) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = _legacy_response.to_raw_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class AsyncInboundInternationalACHTransfersWithRawResponse:
    def __init__(self, inbound_international_ach_transfers: AsyncInboundInternationalACHTransfers) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class InboundInternationalACHTransfersWithStreamingResponse:
    def __init__(self, inbound_international_ach_transfers: InboundInternationalACHTransfers) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = to_streamed_response_wrapper(
            inbound_international_ach_transfers.create,
        )


class AsyncInboundInternationalACHTransfersWithStreamingResponse:
    def __init__(self, inbound_international_ach_transfers: AsyncInboundInternationalACHTransfers) -> None:
        self._inbound_international_ach_transfers = inbound_international_ach_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_international_ach_transfers.create,
        )
