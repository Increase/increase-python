# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RealTimePaymentsTransfer", "Approval", "Cancellation", "Submission", "Rejection"]


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


class Submission(BaseModel):
    submitted_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was submitted to The Clearing House.
    """

    transaction_identification: str
    """The Real Time Payments network identification of the transfer."""


class Rejection(BaseModel):
    reject_reason_additional_information: Optional[str]
    """
    Additional information about the rejection provided by the recipient bank when
    the `reject_reason_code` is `NARRATIVE`.
    """

    reject_reason_code: Literal[
        "account_closed",
        "account_blocked",
        "invalid_creditor_account_type",
        "invalid_creditor_account_number",
        "invalid_creditor_financial_institution_identifier",
        "end_customer_deceased",
        "narrative",
        "transaction_forbidden",
        "transaction_type_not_supported",
        "unexpected_amount",
        "amount_exceeds_bank_limits",
        "invalid_creditor_address",
        "unknown_end_customer",
        "invalid_debtor_address",
        "timeout",
        "unsupported_message_for_recipient",
        "recipient_connection_not_available",
        "real_time_payments_suspended",
        "instructed_agent_signed_off",
        "processing_error",
        "other",
    ]
    """
    The reason the transfer was rejected as provided by the recipient bank or the
    Real Time Payments network.
    """

    rejected_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was rejected.
    """


class RealTimePaymentsTransfer(BaseModel):
    account_id: str
    """The Account from which the transfer was sent."""

    amount: int
    """The transfer amount in USD cents."""

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

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    creditor_name: str
    """The name of the transfer's recipient as provided by the sender."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For real time payments transfers this is always equal to `USD`.
    """

    destination_account_number: str
    """The destination account number."""

    destination_routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

    external_account_id: Optional[str]
    """The identifier of the External Account the transfer was made to, if any."""

    id: str
    """The Real Time Payments Transfer's identifier."""

    rejection: Optional[Rejection]
    """
    If the transfer is rejected by Real Time Payments or the destination financial
    institution, this will contain supplemental details.
    """

    remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""

    source_account_number_id: str
    """The Account Number the recipient will see as having sent the transfer."""

    status: Literal[
        "pending_approval", "canceled", "pending_submission", "submitted", "complete", "rejected", "requires_attention"
    ]
    """The lifecycle status of the transfer."""

    submission: Optional[Submission]
    """
    After the transfer is submitted to Real Time Payments, this will contain
    supplemental details.
    """

    transaction_id: Optional[str]
    """The Transaction funding the transfer once it is complete."""

    type: Literal["real_time_payments_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_payments_transfer`.
    """
