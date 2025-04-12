# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhysicalCardProfile"]


class PhysicalCardProfile(BaseModel):
    id: str
    """The Card Profile identifier."""

    back_image_file_id: Optional[str] = None
    """The identifier of the File containing the physical card's back image."""

    carrier_image_file_id: Optional[str] = None
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: Optional[str] = None
    """A phone number the user can contact to receive support for their card."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    creator: Literal["increase", "user"]
    """The creator of this Physical Card Profile.

    - `increase` - This Physical Card Profile was created by Increase.
    - `user` - This Physical Card Profile was created by you.
    """

    description: str
    """A description you can use to identify the Physical Card Profile."""

    front_image_file_id: Optional[str] = None
    """The identifier of the File containing the physical card's front image."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    is_default: bool
    """
    Whether this Physical Card Profile is the default for all cards in its Increase
    group.
    """

    program_id: str
    """The identifier for the Program this Physical Card Profile belongs to."""

    status: Literal["pending_creating", "pending_reviewing", "rejected", "pending_submitting", "active", "archived"]
    """The status of the Physical Card Profile.

    - `pending_creating` - The Card Profile has not yet been processed by Increase.
    - `pending_reviewing` - The card profile is awaiting review by Increase.
    - `rejected` - There is an issue with the Physical Card Profile preventing it
      from use.
    - `pending_submitting` - The card profile is awaiting submission to the
      fulfillment provider.
    - `active` - The Physical Card Profile has been submitted to the fulfillment
      provider and is ready to use.
    - `archived` - The Physical Card Profile has been archived.
    """

    type: Literal["physical_card_profile"]
    """A constant representing the object's type.

    For this resource it will always be `physical_card_profile`.
    """
