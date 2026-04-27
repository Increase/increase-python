# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LockboxAddress", "Address"]


class Address(BaseModel):
    """The mailing address for the Lockbox Address.

    It will be present after Increase generates it.
    """

    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: str
    """The second line of the address."""

    postal_code: str
    """The postal code of the address."""

    state: str
    """
    The two-letter United States Postal Service (USPS) abbreviation for the state of
    the address.
    """


class LockboxAddress(BaseModel):
    """
    Lockbox Addresses are physical locations that can receive mail containing paper checks.
    """

    id: str
    """The Lockbox Address identifier."""

    address: Optional[Address] = None
    """The mailing address for the Lockbox Address.

    It will be present after Increase generates it.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Lockbox
    Address was created.
    """

    description: Optional[str] = None
    """The description you choose for the Lockbox Address."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    status: Literal["pending", "active", "disabled", "canceled"]
    """The status of the Lockbox Address.

    - `pending` - Increase is generating this Lockbox Address.
    - `active` - This Lockbox Address is active.
    - `disabled` - This Lockbox Address is disabled.
    - `canceled` - This Lockbox Address is permanently disabled.
    """

    type: Literal["lockbox_address"]
    """A constant representing the object's type.

    For this resource it will always be `lockbox_address`.
    """
