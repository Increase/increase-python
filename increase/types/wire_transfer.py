# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Approval", "Cancellation", "Reversal", "Submission", "WireTransfer"]


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


class Reversal(BaseModel):
    amount: int
    """The amount that was reversed."""

    description: str
    """The description on the reversal message from Fedwire."""

    financial_institution_to_financial_institution_information: Optional[str]
    """Additional financial institution information included in the wire reversal."""

    input_cycle_date: str
    """The Fedwire cycle date for the wire reversal."""

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    previous_message_input_cycle_date: str
    """The Fedwire cycle date for the wire transfer that was reversed."""

    previous_message_input_message_accountability_data: str
    """The Fedwire transaction identifier for the wire transfer that was reversed."""

    previous_message_input_sequence_number: str
    """The Fedwire sequence number for the wire transfer that was reversed."""

    previous_message_input_source: str
    """The Fedwire input source identifier for the wire transfer that was reversed."""

    receiver_financial_institution_information: Optional[str]
    """
    Information included in the wire reversal for the receiving financial
    institution.
    """


class Submission(BaseModel):
    input_message_accountability_data: str
    """The accountability data for the submission."""


class WireTransfer(BaseModel):
    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The destination account number."""

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

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For wire transfers this is always equal to `usd`.
    """

    id: str
    """The wire transfer's identifier."""

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    network: Literal["wire"]
    """The transfer's network."""

    reversal: Optional[Reversal]
    """If your transfer is reversed, this will contain details of the reversal."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal[
        "canceled",
        "requires_attention",
        "pending_approval",
        "rejected",
        "reversed",
        "complete",
        "pending_creating",
        "pending_sending",
    ]
    """The lifecycle status of the transfer."""

    submission: Optional[Submission]
    """
    After the transfer is submitted to Fedwire, this will contain supplemental
    details.
    """

    template_id: Optional[str]
    """If the transfer was created from a template, this will be the template's ID."""

    transaction_id: Optional[str]
    """The ID for the transaction funding the transfer."""

    type: Literal["wire_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `wire_transfer`.
    """
