# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundMailItem", "Check"]


class Check(BaseModel):
    amount: int
    """The amount of the check."""

    back_file_id: Optional[str] = None
    """The identifier for the File containing the back of the check."""

    front_file_id: Optional[str] = None
    """The identifier for the File containing the front of the check."""


class InboundMailItem(BaseModel):
    id: str
    """The Inbound Mail Item identifier."""

    checks: List[Check]
    """The checks in the mail item."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Inbound
    Mail Item was created.
    """

    file_id: str
    """The identifier for the File containing the scanned contents of the mail item."""

    lockbox_id: Optional[str] = None
    """The identifier for the Lockbox that received this mail item.

    For mail items that could not be processed due to an invalid address, this will
    be null.
    """

    recipient_name: Optional[str] = None
    """The recipient name as written on the mail item."""

    rejection_reason: Optional[Literal["no_matching_lockbox", "no_check", "lockbox_not_active"]] = None
    """If the mail item has been rejected, why it was rejected.

    - `no_matching_lockbox` - The mail item does not match any lockbox.
    - `no_check` - The mail item does not contain a check.
    - `lockbox_not_active` - The Lockbox or its associated Account is not active.
    """

    status: Literal["pending", "processed", "rejected"]
    """If the mail item has been processed.

    - `pending` - The mail item is pending processing.
    - `processed` - The mail item has been processed.
    - `rejected` - The mail item has been rejected.
    """

    type: Literal["inbound_mail_item"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_mail_item`.
    """
