# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundWireTransfer", "Reversal"]


class Reversal(BaseModel):
    reason: Literal["duplicate", "creditor_request"]
    """The reason for the reversal.

    - `duplicate` - The inbound wire transfer was a duplicate.
    - `creditor_request` - The recipient of the wire transfer requested the funds be
      returned to the sender.
    """

    reversed_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was reversed.
    """


class InboundWireTransfer(BaseModel):
    id: str
    """The inbound wire transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    amount: int
    """The amount in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the inbound wire transfer was created.
    """

    creditor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_name: Optional[str] = None
    """A name set by the sender."""

    debtor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_name: Optional[str] = None
    """A name set by the sender."""

    description: str
    """An Increase-constructed description of the transfer."""

    end_to_end_identification: Optional[str] = None
    """A free-form reference string set by the sender, to help identify the transfer."""

    input_message_accountability_data: Optional[str] = None
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the originating bank.
    """

    instructing_agent_routing_number: Optional[str] = None
    """
    The American Banking Association (ABA) routing number of the bank that sent the
    wire.
    """

    instruction_identification: Optional[str] = None
    """The sending bank's identifier for the wire transfer."""

    reversal: Optional[Reversal] = None
    """
    Information about the reversal of the inbound wire transfer if it has been
    reversed.
    """

    status: Literal["pending", "accepted", "declined", "reversed"]
    """The status of the transfer.

    - `pending` - The Inbound Wire Transfer is awaiting action, will transition
      automatically if no action is taken.
    - `accepted` - The Inbound Wire Transfer is accepted.
    - `declined` - The Inbound Wire Transfer was declined.
    - `reversed` - The Inbound Wire Transfer was reversed.
    """

    type: Literal["inbound_wire_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_wire_transfer`.
    """

    unique_end_to_end_transaction_reference: Optional[str] = None
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the transfer.
    """

    unstructured_remittance_information: Optional[str] = None
    """A free-form message set by the sender."""

    wire_drawdown_request_id: Optional[str] = None
    """The wire drawdown request the inbound wire transfer is fulfilling."""
