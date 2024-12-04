# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RealTimePaymentsTransfer",
    "Acknowledgement",
    "Approval",
    "Cancellation",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "Rejection",
    "Submission",
]


class Acknowledgement(BaseModel):
    acknowledged_at: datetime
    """When the transfer was acknowledged."""


class Approval(BaseModel):
    approved_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """

    approved_by: Optional[str] = None
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

    canceled_by: Optional[str] = None
    """
    If the Transfer was canceled by a user in the dashboard, the email address of
    that user.
    """


class CreatedByAPIKey(BaseModel):
    description: Optional[str] = None
    """The description set for the API key when it was created."""


class CreatedByOAuthApplication(BaseModel):
    name: str
    """The name of the OAuth Application."""


class CreatedByUser(BaseModel):
    email: str
    """The email address of the User."""


class CreatedBy(BaseModel):
    api_key: Optional[CreatedByAPIKey] = None
    """If present, details about the API key that created the transfer."""

    category: Literal["api_key", "oauth_application", "user"]
    """The type of object that created this transfer.

    - `api_key` - An API key. Details will be under the `api_key` object.
    - `oauth_application` - An OAuth application you connected to Increase. Details
      will be under the `oauth_application` object.
    - `user` - A User in the Increase dashboard. Details will be under the `user`
      object.
    """

    oauth_application: Optional[CreatedByOAuthApplication] = None
    """If present, details about the OAuth Application that created the transfer."""

    user: Optional[CreatedByUser] = None
    """If present, details about the User that created the transfer."""


class Rejection(BaseModel):
    reject_reason_additional_information: Optional[str] = None
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
    Real-Time Payments network.

    - `account_closed` - The destination account is closed. Corresponds to the
      Real-Time Payments reason code `AC04`.
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the Real-Time Payments reason code
      `AC06`.
    - `invalid_creditor_account_type` - The destination account is ineligible to
      receive Real-Time Payments transfers. Corresponds to the Real-Time Payments
      reason code `AC14`.
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the Real-Time Payments reason code `AC03`.
    - `invalid_creditor_financial_institution_identifier` - The destination routing
      number is invalid. Corresponds to the Real-Time Payments reason code `RC04`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the Real-Time Payments reason code `MD07`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field.
    - `transaction_forbidden` - Real-Time Payments transfers are not allowed to the
      destination account. Corresponds to the Real-Time Payments reason code `AG01`.
    - `transaction_type_not_supported` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code `AG03`.
    - `unexpected_amount` - The amount of the transfer is different than expected by
      the recipient. Corresponds to the Real-Time Payments reason code `AM09`.
    - `amount_exceeds_bank_limits` - The amount is higher than the recipient is
      authorized to send or receive. Corresponds to the Real-Time Payments reason
      code `AM14`.
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the Real-Time Payments reason code `BE04`.
    - `unknown_end_customer` - The specified creditor is unknown. Corresponds to the
      Real-Time Payments reason code `BE06`.
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the Real-Time Payments reason code `BE07`.
    - `timeout` - There was a timeout processing the transfer. Corresponds to the
      Real-Time Payments reason code `DS24`.
    - `unsupported_message_for_recipient` - Real-Time Payments transfers are not
      enabled for the destination account. Corresponds to the Real-Time Payments
      reason code `NOAT`.
    - `recipient_connection_not_available` - The destination financial institution
      is currently not connected to Real-Time Payments. Corresponds to the Real-Time
      Payments reason code `9912`.
    - `real_time_payments_suspended` - Real-Time Payments is currently unavailable.
      Corresponds to the Real-Time Payments reason code `9948`.
    - `instructed_agent_signed_off` - The destination financial institution is
      currently signed off of Real-Time Payments. Corresponds to the Real-Time
      Payments reason code `9910`.
    - `processing_error` - The transfer was rejected due to an internal Increase
      issue. We have been notified.
    - `other` - Some other error or issue has occurred.
    """

    rejected_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was rejected.
    """


class Submission(BaseModel):
    submitted_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was submitted to The Clearing House.
    """

    transaction_identification: str
    """The Real-Time Payments network identification of the transfer."""


class RealTimePaymentsTransfer(BaseModel):
    id: str
    """The Real-Time Payments Transfer's identifier."""

    account_id: str
    """The Account from which the transfer was sent."""

    acknowledgement: Optional[Acknowledgement] = None
    """
    If the transfer is acknowledged by the recipient bank, this will contain
    supplemental details.
    """

    amount: int
    """The transfer amount in USD cents."""

    approval: Optional[Approval] = None
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    cancellation: Optional[Cancellation] = None
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the transfer, either via the API or the dashboard."""

    creditor_name: str
    """The name of the transfer's recipient.

    This is set by the sender when creating the transfer.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For real-time payments transfers this is always equal to `USD`.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    debtor_name: Optional[str] = None
    """The name of the transfer's sender.

    If not provided, defaults to the name of the account's entity.
    """

    destination_account_number: str
    """The destination account number."""

    destination_routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

    external_account_id: Optional[str] = None
    """The identifier of the External Account the transfer was made to, if any."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer.

    A pending transaction is created when the transfer
    [requires approval](https://increase.com/documentation/transfer-approvals#transfer-approvals)
    by someone else in your organization.
    """

    rejection: Optional[Rejection] = None
    """
    If the transfer is rejected by Real-Time Payments or the destination financial
    institution, this will contain supplemental details.
    """

    remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""

    source_account_number_id: str
    """The Account Number the recipient will see as having sent the transfer."""

    status: Literal[
        "pending_approval",
        "canceled",
        "pending_reviewing",
        "requires_attention",
        "rejected",
        "pending_submission",
        "submitted",
        "complete",
    ]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is pending approval.
    - `canceled` - The transfer has been canceled.
    - `pending_reviewing` - The transfer is pending review by Increase.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `rejected` - The transfer was rejected by the network or the recipient's bank.
    - `pending_submission` - The transfer is queued to be submitted to Real-Time
      Payments.
    - `submitted` - The transfer has been submitted and is pending a response from
      Real-Time Payments.
    - `complete` - The transfer has been sent successfully and is complete.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to Real-Time Payments, this will contain
    supplemental details.
    """

    transaction_id: Optional[str] = None
    """The Transaction funding the transfer once it is complete."""

    type: Literal["real_time_payments_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_payments_transfer`.
    """

    ultimate_creditor_name: Optional[str] = None
    """The name of the ultimate recipient of the transfer.

    Set this if the creditor is an intermediary receiving the payment for someone
    else.
    """

    ultimate_debtor_name: Optional[str] = None
    """The name of the ultimate sender of the transfer.

    Set this if the funds are being sent on behalf of someone who is not the account
    holder at Increase.
    """
