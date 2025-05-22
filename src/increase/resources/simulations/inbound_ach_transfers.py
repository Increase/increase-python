# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

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
from ...types.simulations import inbound_ach_transfer_create_params
from ...types.inbound_ach_transfer import InboundACHTransfer

__all__ = ["InboundACHTransfersResource", "AsyncInboundACHTransfersResource"]


class InboundACHTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return InboundACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return InboundACHTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        addenda: inbound_ach_transfer_create_params.Addenda | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        receiver_id_number: str | NotGiven = NOT_GIVEN,
        receiver_name: str | NotGiven = NOT_GIVEN,
        resolve_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
            "point_of_sale",
            "telephone_initiated",
            "customer_initiated",
            "accounts_receivable",
            "machine_transfer",
            "shared_network_transaction",
            "represented_check",
            "back_office_conversion",
            "point_of_purchase",
            "check_truncation",
            "destroyed_check",
            "international_ach_transaction",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """Simulates an inbound ACH transfer to your account.

        This imitates initiating a
        transfer to an Increase account from a different financial institution. The
        transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. The result of calling this API will contain the created
        transfer. You can pass a `resolve_at` parameter to allow for a window to
        [action on the Inbound ACH Transfer](https://increase.com/documentation/receiving-ach-transfers).
        Alternatively, if you don't pass the `resolve_at` parameter the result will
        contain either a [Transaction](#transactions) or a
        [Declined Transaction](#declined-transactions) depending on whether or not the
        transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          addenda: Additional information to include in the transfer.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: Data associated with the transfer set by the sender.

          company_entry_description: The description of the transfer set by the sender.

          company_id: The sender's company ID.

          company_name: The name of the sender.

          receiver_id_number: The ID of the receiver of the transfer.

          receiver_name: The name of the receiver of the transfer.

          resolve_at: The time at which the transfer should be resolved. If not provided will resolve
              immediately.

          standard_entry_class_code: The standard entry class code for the transfer.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).
              - `point_of_sale` - Point of Sale (POS).
              - `telephone_initiated` - Telephone Initiated (TEL).
              - `customer_initiated` - Customer Initiated (CIE).
              - `accounts_receivable` - Accounts Receivable (ARC).
              - `machine_transfer` - Machine Transfer (MTE).
              - `shared_network_transaction` - Shared Network Transaction (SHR).
              - `represented_check` - Represented Check (RCK).
              - `back_office_conversion` - Back Office Conversion (BOC).
              - `point_of_purchase` - Point of Purchase (POP).
              - `check_truncation` - Check Truncation (TRC).
              - `destroyed_check` - Destroyed Check (XCK).
              - `international_ach_transaction` - International ACH Transaction (IAT).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/inbound_ach_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "addenda": addenda,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_id": company_id,
                    "company_name": company_name,
                    "receiver_id_number": receiver_id_number,
                    "receiver_name": receiver_name,
                    "resolve_at": resolve_at,
                    "standard_entry_class_code": standard_entry_class_code,
                },
                inbound_ach_transfer_create_params.InboundACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )


class AsyncInboundACHTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundACHTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundACHTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundACHTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncInboundACHTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_number_id: str,
        amount: int,
        addenda: inbound_ach_transfer_create_params.Addenda | NotGiven = NOT_GIVEN,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        receiver_id_number: str | NotGiven = NOT_GIVEN,
        receiver_name: str | NotGiven = NOT_GIVEN,
        resolve_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        standard_entry_class_code: Literal[
            "corporate_credit_or_debit",
            "corporate_trade_exchange",
            "prearranged_payments_and_deposit",
            "internet_initiated",
            "point_of_sale",
            "telephone_initiated",
            "customer_initiated",
            "accounts_receivable",
            "machine_transfer",
            "shared_network_transaction",
            "represented_check",
            "back_office_conversion",
            "point_of_purchase",
            "check_truncation",
            "destroyed_check",
            "international_ach_transaction",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InboundACHTransfer:
        """Simulates an inbound ACH transfer to your account.

        This imitates initiating a
        transfer to an Increase account from a different financial institution. The
        transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. The result of calling this API will contain the created
        transfer. You can pass a `resolve_at` parameter to allow for a window to
        [action on the Inbound ACH Transfer](https://increase.com/documentation/receiving-ach-transfers).
        Alternatively, if you don't pass the `resolve_at` parameter the result will
        contain either a [Transaction](#transactions) or a
        [Declined Transaction](#declined-transactions) depending on whether or not the
        transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          addenda: Additional information to include in the transfer.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: Data associated with the transfer set by the sender.

          company_entry_description: The description of the transfer set by the sender.

          company_id: The sender's company ID.

          company_name: The name of the sender.

          receiver_id_number: The ID of the receiver of the transfer.

          receiver_name: The name of the receiver of the transfer.

          resolve_at: The time at which the transfer should be resolved. If not provided will resolve
              immediately.

          standard_entry_class_code: The standard entry class code for the transfer.

              - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
              - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
              - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
              - `internet_initiated` - Internet Initiated (WEB).
              - `point_of_sale` - Point of Sale (POS).
              - `telephone_initiated` - Telephone Initiated (TEL).
              - `customer_initiated` - Customer Initiated (CIE).
              - `accounts_receivable` - Accounts Receivable (ARC).
              - `machine_transfer` - Machine Transfer (MTE).
              - `shared_network_transaction` - Shared Network Transaction (SHR).
              - `represented_check` - Represented Check (RCK).
              - `back_office_conversion` - Back Office Conversion (BOC).
              - `point_of_purchase` - Point of Purchase (POP).
              - `check_truncation` - Check Truncation (TRC).
              - `destroyed_check` - Destroyed Check (XCK).
              - `international_ach_transaction` - International ACH Transaction (IAT).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_ach_transfers",
            body=await async_maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "addenda": addenda,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_id": company_id,
                    "company_name": company_name,
                    "receiver_id_number": receiver_id_number,
                    "receiver_name": receiver_name,
                    "resolve_at": resolve_at,
                    "standard_entry_class_code": standard_entry_class_code,
                },
                inbound_ach_transfer_create_params.InboundACHTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InboundACHTransfer,
        )


class InboundACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_ach_transfers: InboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.create = to_raw_response_wrapper(
            inbound_ach_transfers.create,
        )


class AsyncInboundACHTransfersResourceWithRawResponse:
    def __init__(self, inbound_ach_transfers: AsyncInboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.create = async_to_raw_response_wrapper(
            inbound_ach_transfers.create,
        )


class InboundACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_ach_transfers: InboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.create = to_streamed_response_wrapper(
            inbound_ach_transfers.create,
        )


class AsyncInboundACHTransfersResourceWithStreamingResponse:
    def __init__(self, inbound_ach_transfers: AsyncInboundACHTransfersResource) -> None:
        self._inbound_ach_transfers = inbound_ach_transfers

        self.create = async_to_streamed_response_wrapper(
            inbound_ach_transfers.create,
        )
