# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhysicalCheckBatch", "MailingAddress", "ReturnAddress"]


class MailingAddress(BaseModel):
    """The mailing address of the parcel."""

    city: str
    """The city of the address."""

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    name: str
    """The name component of the address."""

    phone: Optional[str] = None
    """The phone number that is used for delivery issues."""

    postal_code: str
    """The postal code of the address."""

    state: str
    """The state of the address."""


class ReturnAddress(BaseModel):
    """The return address of the parcel."""

    city: str
    """The city of the return address."""

    line1: str
    """The first line of the return address."""

    line2: Optional[str] = None
    """The second line of the return address."""

    name: str
    """The name component of the return address."""

    phone: Optional[str] = None
    """The phone number that is used for delivery issues."""

    postal_code: str
    """The postal code of the return address."""

    state: str
    """The state of the return address."""


class PhysicalCheckBatch(BaseModel):
    """Physical Check Batches are groups of checks that are mailed in the same parcel.

    Tracking updates are propagated to every related Check Transfer.
    """

    id: str
    """The Physical Check Batch's identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Physical Check Batch was created.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    mailing_address: MailingAddress
    """The mailing address of the parcel."""

    return_address: ReturnAddress
    """The return address of the parcel."""

    shipping_method: Literal["usps_first_class", "fedex_overnight"]
    """The shipping method for the parcel.

    - `usps_first_class` - USPS First Class
    - `fedex_overnight` - FedEx Overnight
    """

    status: Literal["pending", "completed", "canceled", "requires_attention"]
    """The lifecycle status of the Physical Check Batch.

    - `pending` - The batch is pending completion and is open to accepting new
      checks.
    - `completed` - The batch has been completed.
    - `canceled` - The batch and all checks related to it have been canceled.
    - `requires_attention` - The batch requires attention from an Increase operator.
    """

    type: Literal["physical_check_batch"]
    """A constant representing the object's type.

    For this resource it will always be `physical_check_batch`.
    """
