# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "FednowTransfer",
    "Acknowledgement",
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
    """Additional information about the rejection provided by the recipient bank."""

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
        "amount_exceeds_bank_limits",
        "invalid_creditor_address",
        "invalid_debtor_address",
        "timeout",
        "processing_error",
        "other",
    ]
    """
    The reason the transfer was rejected as provided by the recipient bank or the
    FedNow network.

    - `account_closed` - The destination account is closed. Corresponds to the
      FedNow reason code `AC04`.
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the FedNow reason code `AC06`.
    - `invalid_creditor_account_type` - The destination account is ineligible to
      receive FedNow transfers. Corresponds to the FedNow reason code `AC14`.
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the FedNow reason code `AC03`.
    - `invalid_creditor_financial_institution_identifier` - The destination routing
      number is invalid. Corresponds to the FedNow reason code `RC04`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the FedNow reason code `MD07`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field. Corresponds to the FedNow reason code `NARR`.
    - `transaction_forbidden` - FedNow transfers are not allowed to the destination
      account. Corresponds to the FedNow reason code `AG01`.
    - `transaction_type_not_supported` - FedNow transfers are not enabled for the
      destination account. Corresponds to the FedNow reason code `AG03`.
    - `amount_exceeds_bank_limits` - The amount is higher than the recipient is
      authorized to send or receive. Corresponds to the FedNow reason code `E990`.
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the FedNow reason code `BE04`.
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the FedNow reason code `BE07`.
    - `timeout` - There was a timeout processing the transfer. Corresponds to the
      FedNow reason code `E997`.
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
    message_identification: str
    """The FedNow network identification of the message submitted."""

    submitted_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was submitted to FedNow.
    """


class FednowTransfer(BaseModel):
    id: str
    """The FedNow Transfer's identifier."""

    account_id: str
    """The Account from which the transfer was sent."""

    account_number: str
    """The destination account number."""

    acknowledgement: Optional[Acknowledgement] = None
    """
    If the transfer is acknowledged by the recipient bank, this will contain
    supplemental details.
    """

    amount: int
    """The transfer amount in USD cents."""

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

    currency: Literal["USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For FedNow transfers this is always equal to `USD`.

    - `USD` - US Dollar (USD)
    """

    debtor_name: str
    """The name of the transfer's sender.

    If not provided, defaults to the name of the account's entity.
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
    """The ID for the pending transaction representing the transfer."""

    rejection: Optional[Rejection] = None
    """
    If the transfer is rejected by FedNow or the destination financial institution,
    this will contain supplemental details.
    """

    routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

    source_account_number_id: str
    """The Account Number the recipient will see as having sent the transfer."""

    status: Literal[
        "pending_reviewing",
        "canceled",
        "reviewing_rejected",
        "requires_attention",
        "pending_approval",
        "pending_submitting",
        "pending_response",
        "complete",
        "rejected",
    ]
    """The lifecycle status of the transfer.

    - `pending_reviewing` - The transfer is pending review by Increase.
    - `canceled` - The transfer has been canceled.
    - `reviewing_rejected` - The transfer has been rejected by Increase.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `pending_approval` - The transfer is pending approval.
    - `pending_submitting` - The transfer is queued to be submitted to FedNow.
    - `pending_response` - The transfer has been submitted and is pending a response
      from FedNow.
    - `complete` - The transfer has been sent successfully and is complete.
    - `rejected` - The transfer was rejected by the network or the recipient's bank.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to FedNow, this will contain supplemental
    details.
    """

    transaction_id: Optional[str] = None
    """The Transaction funding the transfer once it is complete."""

    type: Literal["fednow_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `fednow_transfer`.
    """

    unique_end_to_end_transaction_reference: str
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the transfer.
    """

    unstructured_remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""
