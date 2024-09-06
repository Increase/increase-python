# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundWireTransfer"]


class InboundWireTransfer(BaseModel):
    id: str
    """The inbound wire transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    amount: int
    """The amount in USD cents."""

    beneficiary_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    beneficiary_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    beneficiary_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    beneficiary_name: Optional[str] = None
    """A name set by the sender."""

    beneficiary_reference: Optional[str] = None
    """A free-form reference string set by the sender, to help identify the transfer."""

    description: str
    """An Increase-constructed description of the transfer."""

    input_message_accountability_data: Optional[str] = None
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the originating bank.
    """

    originator_address_line1: Optional[str] = None
    """The address of the wire originator, set by the sending bank."""

    originator_address_line2: Optional[str] = None
    """The address of the wire originator, set by the sending bank."""

    originator_address_line3: Optional[str] = None
    """The address of the wire originator, set by the sending bank."""

    originator_name: Optional[str] = None
    """The originator of the wire, set by the sending bank."""

    originator_routing_number: Optional[str] = None
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    originator_to_beneficiary_information: Optional[str] = None
    """An Increase-created concatenation of the Originator-to-Beneficiary lines."""

    originator_to_beneficiary_information_line1: Optional[str] = None
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line2: Optional[str] = None
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line3: Optional[str] = None
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line4: Optional[str] = None
    """A free-form message set by the wire originator."""

    sender_reference: Optional[str] = None
    """The sending bank's reference number for the wire transfer."""

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
