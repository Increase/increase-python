# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CheckTransfer",
    "Approval",
    "Cancellation",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "Mailing",
    "PhysicalCheck",
    "PhysicalCheckMailingAddress",
    "PhysicalCheckReturnAddress",
    "StopPaymentRequest",
    "Submission",
    "ThirdParty",
]


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


class Mailing(BaseModel):
    image_id: Optional[str] = None
    """
    The ID of the file corresponding to an image of the check that was mailed, if
    available.
    """

    mailed_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was mailed.
    """


class PhysicalCheckMailingAddress(BaseModel):
    city: Optional[str] = None
    """The city of the check's destination."""

    line1: Optional[str] = None
    """The street address of the check's destination."""

    line2: Optional[str] = None
    """The second line of the address of the check's destination."""

    name: Optional[str] = None
    """The name component of the check's mailing address."""

    postal_code: Optional[str] = None
    """The postal code of the check's destination."""

    state: Optional[str] = None
    """The state of the check's destination."""


class PhysicalCheckReturnAddress(BaseModel):
    city: Optional[str] = None
    """The city of the check's destination."""

    line1: Optional[str] = None
    """The street address of the check's destination."""

    line2: Optional[str] = None
    """The second line of the address of the check's destination."""

    name: Optional[str] = None
    """The name component of the check's return address."""

    postal_code: Optional[str] = None
    """The postal code of the check's destination."""

    state: Optional[str] = None
    """The state of the check's destination."""


class PhysicalCheck(BaseModel):
    mailing_address: PhysicalCheckMailingAddress
    """Details for where Increase will mail the check."""

    memo: Optional[str] = None
    """The descriptor that will be printed on the memo field on the check."""

    note: Optional[str] = None
    """The descriptor that will be printed on the letter included with the check."""

    recipient_name: str
    """The name that will be printed on the check."""

    return_address: Optional[PhysicalCheckReturnAddress] = None
    """The return address to be printed on the check."""


class StopPaymentRequest(BaseModel):
    reason: Literal["mail_delivery_failed", "rejected_by_increase", "not_authorized", "unknown"]
    """The reason why this transfer was stopped.

    - `mail_delivery_failed` - The check could not be delivered.
    - `rejected_by_increase` - The check was canceled by an Increase operator who
      will provide details out-of-band.
    - `not_authorized` - The check was not authorized.
    - `unknown` - The check was stopped for another reason.
    """

    requested_at: datetime
    """The time the stop-payment was requested."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
    """


class Submission(BaseModel):
    submitted_at: datetime
    """When this check transfer was submitted to our check printer."""


class ThirdParty(BaseModel):
    check_number: Optional[str] = None
    """The check number that will be printed on the check."""


class CheckTransfer(BaseModel):
    id: str
    """The Check transfer's identifier."""

    account_id: str
    """The identifier of the Account from which funds will be transferred."""

    account_number: str
    """The account number printed on the check."""

    amount: int
    """The transfer amount in USD cents."""

    approval: Optional[Approval] = None
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    approved_inbound_check_deposit_id: Optional[str] = None
    """
    If the Check Transfer was successfully deposited, this will contain the
    identifier of the Inbound Check Deposit object with details of the deposit.
    """

    cancellation: Optional[Cancellation] = None
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    check_number: str
    """The check number printed on the check."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the transfer, either via the API or the dashboard."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    fulfillment_method: Literal["physical_check", "third_party"]
    """Whether Increase will print and mail the check or if you will do it yourself.

    - `physical_check` - Increase will print and mail a physical check.
    - `third_party` - Increase will not print a check; you are responsible for
      printing and mailing a check with the provided account number, routing number,
      check number, and amount.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    mailing: Optional[Mailing] = None
    """
    If the check has been mailed by Increase, this will contain details of the
    shipment.
    """

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer.

    A pending transaction is created when the transfer
    [requires approval](https://increase.com/documentation/transfer-approvals#transfer-approvals)
    by someone else in your organization.
    """

    physical_check: Optional[PhysicalCheck] = None
    """Details relating to the physical check that Increase will print and mail.

    Will be present if and only if `fulfillment_method` is equal to
    `physical_check`.
    """

    routing_number: str
    """The routing number printed on the check."""

    source_account_number_id: Optional[str] = None
    """
    The identifier of the Account Number from which to send the transfer and print
    on the check.
    """

    status: Literal[
        "pending_approval",
        "pending_submission",
        "pending_mailing",
        "mailed",
        "canceled",
        "deposited",
        "stopped",
        "rejected",
        "requires_attention",
        "returned",
    ]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is awaiting approval.
    - `pending_submission` - The transfer is pending submission.
    - `pending_mailing` - The check is queued for mailing.
    - `mailed` - The check has been mailed.
    - `canceled` - The transfer has been canceled.
    - `deposited` - The check has been deposited.
    - `stopped` - A stop-payment was requested for this check.
    - `rejected` - The transfer has been rejected.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `returned` - The transfer has been returned.
    """

    stop_payment_request: Optional[StopPaymentRequest] = None
    """
    After a stop-payment is requested on the check, this will contain supplemental
    details.
    """

    submission: Optional[Submission] = None
    """After the transfer is submitted, this will contain supplemental details."""

    third_party: Optional[ThirdParty] = None
    """Details relating to the custom fulfillment you will perform.

    Will be present if and only if `fulfillment_method` is equal to `third_party`.
    """

    type: Literal["check_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer`.
    """
