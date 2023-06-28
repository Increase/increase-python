# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CheckTransfer",
    "Approval",
    "Cancellation",
    "Deposit",
    "ReturnAddress",
    "ReturnDetails",
    "StopPaymentRequest",
    "Submission",
]


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


class Deposit(BaseModel):
    back_image_file_id: Optional[str]
    """
    The identifier of the API File object containing an image of the back of the
    deposited check.
    """

    deposited_at: datetime
    """When the check was deposited."""

    front_image_file_id: Optional[str]
    """
    The identifier of the API File object containing an image of the front of the
    deposited check.
    """

    type: Literal["check_transfer_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_deposit`.
    """


class ReturnAddress(BaseModel):
    city: Optional[str]
    """The city of the address."""

    line1: Optional[str]
    """The first line of the address."""

    line2: Optional[str]
    """The second line of the address."""

    name: Optional[str]
    """The name of the address."""

    state: Optional[str]
    """The US state of the address."""

    zip: Optional[str]
    """The postal code of the address."""


class ReturnDetails(BaseModel):
    file_id: Optional[str]
    """If available, a document with additional information about the return."""

    reason: Literal["mail_delivery_failure", "refused_by_recipient", "returned_not_authorized"]
    """The reason why the check was returned."""

    returned_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was returned.
    """

    transaction_id: Optional[str]
    """
    The identifier of the Transaction that was created to credit you for the
    returned check.
    """

    transfer_id: str
    """The identifier of the returned Check Transfer."""


class StopPaymentRequest(BaseModel):
    requested_at: datetime
    """The time the stop-payment was requested."""

    transaction_id: str
    """The transaction ID of the corresponding credit transaction."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
    """


class Submission(BaseModel):
    check_number: str
    """The identitying number of the check."""

    submitted_at: datetime
    """When this check transfer was submitted to our check printer."""


class CheckTransfer(BaseModel):
    id: str
    """The Check transfer's identifier."""

    account_id: str
    """The identifier of the Account from which funds will be transferred."""

    address_city: Optional[str]
    """The city of the check's destination."""

    address_line1: Optional[str]
    """The street address of the check's destination."""

    address_line2: Optional[str]
    """The second line of the address of the check's destination."""

    address_state: Optional[str]
    """The state of the check's destination."""

    address_zip: Optional[str]
    """The postal code of the check's destination."""

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

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    deposit: Optional[Deposit]
    """After a check transfer is deposited, this will contain supplemental details."""

    mailed_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was mailed.
    """

    message: Optional[str]
    """The descriptor that will be printed on the memo field on the check."""

    note: Optional[str]
    """The descriptor that will be printed on the letter included with the check."""

    recipient_name: Optional[str]
    """The name that will be printed on the check."""

    return_address: Optional[ReturnAddress]
    """The return address to be printed on the check."""

    return_details: Optional[ReturnDetails]
    """After a check transfer is returned, this will contain supplemental details.

    A check transfer is returned when the receiver mails a never deposited check
    back to the bank printed on the check.
    """

    status: Literal[
        "pending_approval",
        "pending_submission",
        "submitted",
        "pending_mailing",
        "mailed",
        "canceled",
        "deposited",
        "stopped",
        "returned",
        "rejected",
        "requires_attention",
    ]
    """The lifecycle status of the transfer."""

    stop_payment_request: Optional[StopPaymentRequest]
    """
    After a stop-payment is requested on the check, this will contain supplemental
    details.
    """

    submission: Optional[Submission]
    """After the transfer is submitted, this will contain supplemental details."""

    submitted_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was submitted.
    """

    transaction_id: Optional[str]
    """The ID for the transaction caused by the transfer."""

    type: Literal["check_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer`.
    """
