# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StopPaymentRequest", "CheckTransfer"]


class StopPaymentRequest(BaseModel):
    requested_at: str
    """The time the stop-payment was requested."""

    transaction_id: str
    """The transaction ID of the corresponding credit transaction."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
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

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    id: str
    """The Check transfer's identifier."""

    mailed_at: Optional[str]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was mailed.
    """

    message: str
    """The descriptor that is printed on the check."""

    recipient_name: str
    """The name that will be printed on the check."""

    status: Literal[
        "pending_submission",
        "submitting",
        "pending_mailing",
        "canceled",
        "requires_attention",
        "flagged_by_operator",
        "mailed",
        "pending_approval",
        "rejected",
        "submitted",
        "deposited",
        "stopped",
    ]
    """The lifecycle status of the transfer."""

    stop_payment_request: Optional[StopPaymentRequest]
    """
    After a stop-payment is requested on the check, this will contain supplemental
    details.
    """

    submitted_at: Optional[str]
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
