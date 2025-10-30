# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

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

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
