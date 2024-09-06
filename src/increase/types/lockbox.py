# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Lockbox", "Address"]


class Address(BaseModel):
    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: str
    """The second line of the address."""

    postal_code: str
    """The postal code of the address."""

    recipient: Optional[str] = None
    """The recipient line of the address.

    This will include the recipient name you provide when creating the address, as
    well as an ATTN suffix to help route the mail to your lockbox. Mail senders must
    include this ATTN line to receive mail at this Lockbox.
    """

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """


class Lockbox(BaseModel):
    id: str
    """The Lockbox identifier."""

    account_id: str
    """
    The identifier for the Account checks sent to this lockbox will be deposited
    into.
    """

    address: Address
    """The mailing address for the Lockbox."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Lockbox
    was created.
    """

    description: Optional[str] = None
    """The description you choose for the Lockbox."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    recipient_name: Optional[str] = None
    """The recipient name you choose for the Lockbox."""

    status: Literal["active", "inactive"]
    """This indicates if mail can be sent to this address.

    - `active` - This Lockbox is active. Checks mailed to it will be deposited
      automatically.
    - `inactive` - This Lockbox is inactive. Checks mailed to it will not be
      deposited.
    """

    type: Literal["lockbox"]
    """A constant representing the object's type.

    For this resource it will always be `lockbox`.
    """
