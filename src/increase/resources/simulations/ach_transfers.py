# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ...types import ACHTransfer
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import (
    ACHTransferSimulation,
    ach_transfer_return_params,
    ach_transfer_create_inbound_params,
)

__all__ = ["ACHTransfers", "AsyncACHTransfers"]


class ACHTransfers(SyncAPIResource):
    def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        This imitates initiating a
        transaction to an Increase account from a different financial institution. The
        transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. The result of calling this API will be either a
        [Transaction](#transactions) or a [Declined Transaction](#declined-transactions)
        depending on whether or not the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: Data associated with the transfer set by the sender.

          company_entry_description: The description of the transfer set by the sender.

          company_id: The sender's company id.

          company_name: The name of the sender.

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
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_id": company_id,
                    "company_name": company_name,
                },
                ach_transfer_create_inbound_params.ACHTransferCreateInboundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransferSimulation,
        )

    def return_(
        self,
        ach_transfer_id: str,
        *,
        reason: Literal[
            "insufficient_fund",
            "no_account",
            "account_closed",
            "invalid_account_number_structure",
            "account_frozen_entry_returned_per_ofac_instruction",
            "credit_entry_refused_by_receiver",
            "unauthorized_debit_to_consumer_account_using_corporate_sec_code",
            "corporate_customer_advised_not_authorized",
            "payment_stopped",
            "non_transaction_account",
            "uncollected_funds",
            "routing_number_check_digit_error",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "amount_field_error",
            "authorization_revoked_by_customer",
            "invalid_ach_routing_number",
            "file_record_edit_criteria",
            "enr_invalid_individual_name",
            "returned_per_odfi_request",
            "limited_participation_dfi",
            "incorrectly_coded_outbound_international_payment",
            "other",
            "account_sold_to_another_dfi",
            "addenda_error",
            "beneficiary_or_account_holder_deceased",
            "check_truncation_entry_return",
            "corrected_return",
            "duplicate_entry",
            "duplicate_return",
            "enr_duplicate_enrollment",
            "enr_invalid_dfi_account_number",
            "enr_invalid_individual_id_number",
            "enr_invalid_representative_payee_indicator",
            "enr_invalid_transaction_code",
            "enr_return_of_enr_entry",
            "enr_routing_number_check_digit_error",
            "entry_not_processed_by_gateway",
            "field_error",
            "foreign_receiving_dfi_unable_to_settle",
            "iat_entry_coding_error",
            "improper_effective_entry_date",
            "improper_source_document_source_document_presented",
            "invalid_company_id",
            "invalid_foreign_receiving_dfi_identification",
            "invalid_individual_id_number",
            "item_and_rck_entry_presented_for_payment",
            "item_related_to_rck_entry_is_ineligible",
            "mandatory_field_error",
            "misrouted_dishonored_return",
            "misrouted_return",
            "no_errors_found",
            "non_acceptance_of_r62_dishonored_return",
            "non_participant_in_iat_program",
            "permissible_return_entry",
            "permissible_return_entry_not_accepted",
            "rdfi_non_settlement",
            "rdfi_participant_in_check_truncation_program",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "return_not_a_duplicate",
            "return_of_erroneous_or_reversing_debit",
            "return_of_improper_credit_entry",
            "return_of_improper_debit_entry",
            "return_of_xck_entry",
            "source_document_presented_for_payment",
            "state_law_affecting_rck_acceptance",
            "stop_payment_on_item_related_to_rck_entry",
            "stop_payment_on_source_document",
            "timely_original_return",
            "trace_number_error",
            "untimely_dishonored_return",
            "untimely_return",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an [ACH Transfer](#ach-transfers) by the Federal Reserve
        due to an error condition. This will also create a Transaction to account for
        the returned funds. This transfer must first have a `status` of `submitted`.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer you wish to return.

          reason: The reason why the Federal Reserve or destination bank returned this transfer.
              Defaults to `no_account`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            body=maybe_transform({"reason": reason}, ach_transfer_return_params.ACHTransferReturnParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    def submit(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Simulates the submission of an [ACH Transfer](#ach-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_submission`. In production, Increase submits ACH Transfers to the
        Federal Reserve three times per day on weekdays. Since sandbox ACH Transfers are
        not submitted to the Federal Reserve, this endpoint allows you to skip that
        delay and transition the ACH Transfer to a status of `submitted`.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )


class AsyncACHTransfers(AsyncAPIResource):
    async def create_inbound(
        self,
        *,
        account_number_id: str,
        amount: int,
        company_descriptive_date: str | NotGiven = NOT_GIVEN,
        company_discretionary_data: str | NotGiven = NOT_GIVEN,
        company_entry_description: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransferSimulation:
        """Simulates an inbound ACH transfer to your account.

        This imitates initiating a
        transaction to an Increase account from a different financial institution. The
        transfer may be either a credit or a debit depending on if the `amount` is
        positive or negative. The result of calling this API will be either a
        [Transaction](#transactions) or a [Declined Transaction](#declined-transactions)
        depending on whether or not the transfer is allowed.

        Args:
          account_number_id: The identifier of the Account Number the inbound ACH Transfer is for.

          amount: The transfer amount in cents. A positive amount originates a credit transfer
              pushing funds to the receiving account. A negative amount originates a debit
              transfer pulling funds from the receiving account.

          company_descriptive_date: The description of the date of the transfer.

          company_discretionary_data: Data associated with the transfer set by the sender.

          company_entry_description: The description of the transfer set by the sender.

          company_id: The sender's company id.

          company_name: The name of the sender.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/inbound_ach_transfers",
            body=maybe_transform(
                {
                    "account_number_id": account_number_id,
                    "amount": amount,
                    "company_descriptive_date": company_descriptive_date,
                    "company_discretionary_data": company_discretionary_data,
                    "company_entry_description": company_entry_description,
                    "company_id": company_id,
                    "company_name": company_name,
                },
                ach_transfer_create_inbound_params.ACHTransferCreateInboundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransferSimulation,
        )

    async def return_(
        self,
        ach_transfer_id: str,
        *,
        reason: Literal[
            "insufficient_fund",
            "no_account",
            "account_closed",
            "invalid_account_number_structure",
            "account_frozen_entry_returned_per_ofac_instruction",
            "credit_entry_refused_by_receiver",
            "unauthorized_debit_to_consumer_account_using_corporate_sec_code",
            "corporate_customer_advised_not_authorized",
            "payment_stopped",
            "non_transaction_account",
            "uncollected_funds",
            "routing_number_check_digit_error",
            "customer_advised_unauthorized_improper_ineligible_or_incomplete",
            "amount_field_error",
            "authorization_revoked_by_customer",
            "invalid_ach_routing_number",
            "file_record_edit_criteria",
            "enr_invalid_individual_name",
            "returned_per_odfi_request",
            "limited_participation_dfi",
            "incorrectly_coded_outbound_international_payment",
            "other",
            "account_sold_to_another_dfi",
            "addenda_error",
            "beneficiary_or_account_holder_deceased",
            "check_truncation_entry_return",
            "corrected_return",
            "duplicate_entry",
            "duplicate_return",
            "enr_duplicate_enrollment",
            "enr_invalid_dfi_account_number",
            "enr_invalid_individual_id_number",
            "enr_invalid_representative_payee_indicator",
            "enr_invalid_transaction_code",
            "enr_return_of_enr_entry",
            "enr_routing_number_check_digit_error",
            "entry_not_processed_by_gateway",
            "field_error",
            "foreign_receiving_dfi_unable_to_settle",
            "iat_entry_coding_error",
            "improper_effective_entry_date",
            "improper_source_document_source_document_presented",
            "invalid_company_id",
            "invalid_foreign_receiving_dfi_identification",
            "invalid_individual_id_number",
            "item_and_rck_entry_presented_for_payment",
            "item_related_to_rck_entry_is_ineligible",
            "mandatory_field_error",
            "misrouted_dishonored_return",
            "misrouted_return",
            "no_errors_found",
            "non_acceptance_of_r62_dishonored_return",
            "non_participant_in_iat_program",
            "permissible_return_entry",
            "permissible_return_entry_not_accepted",
            "rdfi_non_settlement",
            "rdfi_participant_in_check_truncation_program",
            "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
            "return_not_a_duplicate",
            "return_of_erroneous_or_reversing_debit",
            "return_of_improper_credit_entry",
            "return_of_improper_debit_entry",
            "return_of_xck_entry",
            "source_document_presented_for_payment",
            "state_law_affecting_rck_acceptance",
            "stop_payment_on_item_related_to_rck_entry",
            "stop_payment_on_source_document",
            "timely_original_return",
            "trace_number_error",
            "untimely_dishonored_return",
            "untimely_return",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Simulates the return of an [ACH Transfer](#ach-transfers) by the Federal Reserve
        due to an error condition. This will also create a Transaction to account for
        the returned funds. This transfer must first have a `status` of `submitted`.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer you wish to return.

          reason: The reason why the Federal Reserve or destination bank returned this transfer.
              Defaults to `no_account`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/return",
            body=maybe_transform({"reason": reason}, ach_transfer_return_params.ACHTransferReturnParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )

    async def submit(
        self,
        ach_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ACHTransfer:
        """
        Simulates the submission of an [ACH Transfer](#ach-transfers) to the Federal
        Reserve. This transfer must first have a `status` of `pending_approval` or
        `pending_submission`. In production, Increase submits ACH Transfers to the
        Federal Reserve three times per day on weekdays. Since sandbox ACH Transfers are
        not submitted to the Federal Reserve, this endpoint allows you to skip that
        delay and transition the ACH Transfer to a status of `submitted`.

        Args:
          ach_transfer_id: The identifier of the ACH Transfer you wish to submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/ach_transfers/{ach_transfer_id}/submit",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ACHTransfer,
        )
