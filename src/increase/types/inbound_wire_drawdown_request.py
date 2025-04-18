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

    beneficiary_account_number: str
    """The drawdown request's beneficiary's account number."""

    beneficiary_address_line1: Optional[str] = None
    """Line 1 of the drawdown request's beneficiary's address."""

    beneficiary_address_line2: Optional[str] = None
    """Line 2 of the drawdown request's beneficiary's address."""

    beneficiary_address_line3: Optional[str] = None
    """Line 3 of the drawdown request's beneficiary's address."""

    beneficiary_name: Optional[str] = None
    """The drawdown request's beneficiary's name."""

    beneficiary_routing_number: str
    """The drawdown request's beneficiary's routing number."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the inbound wire drawdown requested was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    message_to_recipient: Optional[str] = None
    """A message from the drawdown request's originator."""

    originator_account_number: Optional[str] = None
    """The drawdown request's originator's account number."""

    originator_address_line1: Optional[str] = None
    """Line 1 of the drawdown request's originator's address."""

    originator_address_line2: Optional[str] = None
    """Line 2 of the drawdown request's originator's address."""

    originator_address_line3: Optional[str] = None
    """Line 3 of the drawdown request's originator's address."""

    originator_name: Optional[str] = None
    """The drawdown request's originator's name."""

    originator_routing_number: str
    """The drawdown request's originator's routing number."""

    originator_to_beneficiary_information_line1: Optional[str] = None
    """
    Line 1 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line2: Optional[str] = None
    """
    Line 2 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line3: Optional[str] = None
    """
    Line 3 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line4: Optional[str] = None
    """
    Line 4 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    recipient_account_number_id: str
    """
    The Account Number from which the recipient of this request is being requested
    to send funds.
    """

    type: Literal["inbound_wire_drawdown_request"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_wire_drawdown_request`.
    """
