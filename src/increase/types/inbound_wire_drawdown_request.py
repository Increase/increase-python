# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundWireDrawdownRequest"]


class InboundWireDrawdownRequest(BaseModel):
    id: str
    """The Wire drawdown request identifier."""

    amount: int
    """The amount being requested in cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the inbound wire drawdown requested was created.
    """

    creditor_account_number: str
    """The creditor's account number."""

    creditor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_name: Optional[str] = None
    """A name set by the sender."""

    creditor_routing_number: str
    """The creditor's routing number."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    debtor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_name: Optional[str] = None
    """A name set by the sender."""

    end_to_end_identification: Optional[str] = None
    """
    A free-form reference string set by the sender, to help identify the drawdown
    request.
    """

    input_message_accountability_data: Optional[str] = None
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the originating bank.
    """

    instruction_identification: Optional[str] = None
    """The sending bank's identifier for the drawdown request."""

    recipient_account_number_id: str
    """
    The Account Number from which the recipient of this request is being requested
    to send funds.
    """

    type: Literal["inbound_wire_drawdown_request"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_wire_drawdown_request`.
    """

    unique_end_to_end_transaction_reference: Optional[str] = None
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the drawdown request.
    """

    unstructured_remittance_information: Optional[str] = None
    """A free-form message set by the sender."""
