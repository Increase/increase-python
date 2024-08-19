# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalCardProfile", "TextColor"]


class TextColor(BaseModel):
    blue: int
    """The value of the blue channel in the RGB color."""

    green: int
    """The value of the green channel in the RGB color."""

    red: int
    """The value of the red channel in the RGB color."""


class DigitalCardProfile(BaseModel):
    id: str
    """The Card Profile identifier."""

    app_icon_file_id: str
    """The identifier of the File containing the card's icon image."""

    background_image_file_id: str
    """The identifier of the File containing the card's front image."""

    card_description: str
    """A user-facing description for the card itself."""

    contact_email: Optional[str] = None
    """An email address the user can contact to receive support for their card."""

    contact_phone: Optional[str] = None
    """A phone number the user can contact to receive support for their card."""

    contact_website: Optional[str] = None
    """A website the user can visit to view and receive support for their card."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    description: str
    """A description you can use to identify the Card Profile."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    issuer_name: str
    """A user-facing description for whoever is issuing the card."""

    status: Literal["pending", "rejected", "active", "archived"]
    """The status of the Card Profile.

    - `pending` - The Card Profile is awaiting review from Increase and/or
      processing by card networks.
    - `rejected` - There is an issue with the Card Profile preventing it from use.
    - `active` - The Card Profile can be assigned to Cards.
    - `archived` - The Card Profile is no longer in use.
    """

    text_color: TextColor
    """The Card's text color, specified as an RGB triple."""

    type: Literal["digital_card_profile"]
    """A constant representing the object's type.

    For this resource it will always be `digital_card_profile`.
    """
