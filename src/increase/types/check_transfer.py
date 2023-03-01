# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckTransfer", "ReturnAddress", "Submission", "StopPaymentRequest", "Deposit"]


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


class Submission(BaseModel):
    check_number: str
    """The identitying number of the check."""


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


class Deposit(BaseModel):
    back_image_file_id: Optional[str]
    """The ID for the File containing the image of the rear of the check."""

    front_image_file_id: Optional[str]
    """The ID for the File containing the image of the front of the check."""

    type: Literal["check_transfer_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_deposit`.
    """


class CheckTransfer(BaseModel):
    account_id: str
    """The identifier of the Account from which funds will be transferred."""

    address_city: str
    """The city of the check's destination."""

    address_line1: str
    """The street address of the check's destination."""

    address_line2: Optional[str]
    """The second line of the address of the check's destination."""

    address_state: str
    """The state of the check's destination."""

    address_zip: str
    """The postal code of the check's destination."""

    amount: int
    """The transfer amount in USD cents."""

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

    id: str
    """The Check transfer's identifier."""

    mailed_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was mailed.
    """

    message: str
    """The descriptor that will be printed on the memo field on the check."""

    note: Optional[str]
    """The descriptor that will be printed on the letter included with the check."""

    recipient_name: str
    """The name that will be printed on the check."""

    return_address: Optional[ReturnAddress]
    """The return address to be printed on the check."""

    status: Literal[
        "pending_approval",
        "pending_submission",
        "submitting",
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

    template_id: Optional[str]
    """If the transfer was created from a template, this will be the template's ID."""

    transaction_id: Optional[str]
    """The ID for the transaction caused by the transfer."""

    type: Literal["check_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer`.
    """
