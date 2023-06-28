# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ACHTransfer", "Approval", "Cancellation", "NotificationsOfChange", "Return", "Submission"]


class Approval(BaseModel):
    approved_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """

    approved_by: Optional[str]
    """
    If the Transfer was approved by a user in the dashboard, the email address of
    that user.
    """


class Cancellation(BaseModel):
    canceled_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """

    canceled_by: Optional[str]
    """
    If the Transfer was canceled by a user in the dashboard, the email address of
    that user.
    """


class NotificationsOfChange(BaseModel):
    change_code: str
    """The type of change that occurred."""

    corrected_data: str
    """The corrected data."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the notification occurred.
    """


class Return(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    raw_return_reason_code: str
    """The three character ACH return code, in the range R01 to R85."""

    return_reason_code: Literal[
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
        "account_sold_to_another_dfi",
        "addenda_error",
        "beneficiary_or_account_holder_deceased",
        "customer_advised_not_within_authorization_terms",
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
    """Why the ACH Transfer was returned."""

    transaction_id: str
    """The identifier of the Tranasaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class Submission(BaseModel):
    submitted_at: datetime
    """When the ACH transfer was sent to FedACH."""

    trace_number: str
    """The trace number for the submission."""


class ACHTransfer(BaseModel):
    id: str
    """The ACH transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The destination account number."""

    addendum: Optional[str]
    """Additional information that will be sent to the recipient."""

    amount: int
    """The transfer amount in USD cents.

    A positive amount indicates a credit transfer pushing funds to the receiving
    account. A negative amount indicates a debit transfer pulling funds from the
    receiving account.
    """

    approval: Optional[Approval]
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    cancellation: Optional[Cancellation]
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    company_descriptive_date: Optional[str]
    """The description of the date of the transfer."""

    company_discretionary_data: Optional[str]
    """The data you chose to associate with the transfer."""

    company_entry_description: Optional[str]
    """The description of the transfer you set to be shown to the recipient."""

    company_name: Optional[str]
    """The name by which the recipient knows you."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For ACH transfers this is always equal to `usd`.
    """

    effective_date: Optional[date]
    """
    The transfer effective date in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    external_account_id: Optional[str]
    """The identifier of the External Account the transfer was made to, if any."""

    funding: Literal["checking", "savings"]
    """The type of the account to which the transfer will be sent."""

    individual_id: Optional[str]
    """Your identifer for the transfer recipient."""

    individual_name: Optional[str]
    """The name of the transfer recipient.

    This value is information and not verified by the recipient's bank.
    """

    network: Literal["ach"]
    """The transfer's network."""

    notifications_of_change: List[NotificationsOfChange]
    """
    If the receiving bank accepts the transfer but notifies that future transfers
    should use different details, this will contain those details.
    """

    return_: Optional[Return] = FieldInfo(alias="return")
    """If your transfer is returned, this will contain details of the return."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit", "prearranged_payments_and_deposit", "internet_initiated"
    ]
    """The Standard Entry Class (SEC) code to use for the transfer."""

    statement_descriptor: str
    """The descriptor that will show on the recipient's bank statement."""

    status: Literal[
        "pending_approval",
        "canceled",
        "pending_reviewing",
        "pending_submission",
        "submitted",
        "returned",
        "requires_attention",
        "rejected",
    ]
    """The lifecycle status of the transfer."""

    submission: Optional[Submission]
    """
    After the transfer is submitted to FedACH, this will contain supplemental
    details.
    """

    transaction_id: Optional[str]
    """The ID for the transaction funding the transfer."""

    type: Literal["ach_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `ach_transfer`.
    """
