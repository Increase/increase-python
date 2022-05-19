# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field

from ..._models import BaseModel

__all__ = ["Approval", "Cancellation", "NotificationOfChange", "Return", "Submission", "ACHTranfer"]


class Approval(BaseModel):
    approved_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """


class Cancellation(BaseModel):
    canceled_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """


class NotificationOfChange(BaseModel):
    change_code: str
    """The type of change that occurred."""

    corrected_data: str
    """The corrected data."""

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the notification occurred.
    """


class Return(BaseModel):
    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

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
        "addenda_error",
        "limited_participation_dfi",
        "other",
    ]
    """Why the ACH Transfer was returned."""

    transaction_id: str
    """The identifier of the Tranasaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class Submission(BaseModel):
    trace_number: str
    """The trace number for the submission."""


class ACHTranfer(BaseModel):
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

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For ACH transfers this is always equal to `usd`.
    """

    id: str
    """The ACH transfer's identifier."""

    network: Literal["ach"]
    """The transfer's network."""

    notification_of_change: Optional[NotificationOfChange]
    """
    If the receiving bank accepts the transfer but notifies that future transfers
    should use different details, this will contain those details.
    """

    return_: Optional[Return] = Field(alias="return")
    """If your transfer is returned, this will contain details of the return."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    statement_descriptor: str
    """The descriptor that will show on the recipient's bank statement."""

    status: Literal[
        "pending_approval",
        "pending_submission",
        "rejected",
        "returned",
        "canceled",
        "requires_attention",
        "flagged_by_operator",
        "submitted",
    ]
    """The lifecycle status of the transfer."""

    submission: Optional[Submission]
    """
    After the transfer is submitted to FedACH, this will contain supplemental
    details.
    """

    template_id: Optional[str]
    """If the transfer was created from a template, this will be the template's ID."""

    transaction_id: Optional[str]
    """The ID for the transaction funding the transfer."""

    type: Literal["ach_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `ach_transfer`.
    """
