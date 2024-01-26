# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WireTransfer", "Approval", "Cancellation", "Reversal", "Submission"]


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


class Reversal(BaseModel):
    amount: int
    """The amount that was reversed in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the reversal was created.
    """

    description: str
    """
    The description on the reversal message from Fedwire, set by the reversing bank.
    """

    financial_institution_to_financial_institution_information: Optional[str] = None
    """Additional financial institution information included in the wire reversal."""

    input_cycle_date: date
    """The Fedwire cycle date for the wire reversal.

    The "Fedwire day" begins at 9:00 PM Eastern Time on the evening before the
    `cycle date`.
    """

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    originator_routing_number: Optional[str] = None
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    previous_message_input_cycle_date: date
    """
    The Fedwire cycle date for the wire transfer that is being reversed by this
    message.
    """

    previous_message_input_message_accountability_data: str
    """The Fedwire transaction identifier for the wire transfer that was reversed."""

    previous_message_input_sequence_number: str
    """The Fedwire sequence number for the wire transfer that was reversed."""

    previous_message_input_source: str
    """The Fedwire input source identifier for the wire transfer that was reversed."""

    receiver_financial_institution_information: Optional[str] = None
    """
    Information included in the wire reversal for the receiving financial
    institution.
    """

    transaction_id: str
    """The ID for the Transaction associated with the transfer reversal."""

    wire_transfer_id: str
    """The ID for the Wire Transfer that is being reversed."""


class Submission(BaseModel):
    input_message_accountability_data: str
    """The accountability data for the submission."""

    submitted_at: datetime
    """When this wire transfer was submitted to Fedwire."""


class WireTransfer(BaseModel):
    id: str
    """The wire transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The destination account number."""

    amount: int
    """The transfer amount in USD cents."""

    approval: Optional[Approval] = None
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    beneficiary_address_line1: Optional[str] = None
    """The beneficiary's address line 1."""

    beneficiary_address_line2: Optional[str] = None
    """The beneficiary's address line 2."""

    beneficiary_address_line3: Optional[str] = None
    """The beneficiary's address line 3."""

    beneficiary_name: Optional[str] = None
    """The beneficiary's name."""

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

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For wire transfers this is always equal to `usd`.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    external_account_id: Optional[str] = None
    """The identifier of the External Account the transfer was made to, if any."""

    message_to_recipient: Optional[str] = None
    """The message that will show on the recipient's bank statement."""

    network: Literal["wire"]
    """The transfer's network."""

    originator_address_line1: Optional[str] = None
    """The originator's address line 1."""

    originator_address_line2: Optional[str] = None
    """The originator's address line 2."""

    originator_address_line3: Optional[str] = None
    """The originator's address line 3."""

    originator_name: Optional[str] = None
    """The originator's name."""

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer.

    A pending transaction is created when the transfer
    [requires approval](https://increase.com/documentation/transfer-approvals#transfer-approvals)
    by someone else in your organization.
    """

    reversal: Optional[Reversal] = None
    """If your transfer is reversed, this will contain details of the reversal."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal[
        "canceled", "requires_attention", "pending_approval", "rejected", "reversed", "complete", "pending_creating"
    ]
    """The lifecycle status of the transfer.

    - `canceled` - The transfer has been canceled.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `pending_approval` - The transfer is pending approval.
    - `rejected` - The transfer has been rejected.
    - `reversed` - The transfer has been reversed.
    - `complete` - The transfer is complete.
    - `pending_creating` - The transfer is pending creation.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to Fedwire, this will contain supplemental
    details.
    """

    transaction_id: Optional[str] = None
    """The ID for the transaction funding the transfer."""

    type: Literal["wire_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `wire_transfer`.
    """

    unique_identifier: Optional[str] = None
    """The unique identifier you chose for this object."""
