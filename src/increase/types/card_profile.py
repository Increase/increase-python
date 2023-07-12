# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardProfile", "DigitalWallets", "DigitalWalletsTextColor", "PhysicalCards"]


class DigitalWalletsTextColor(BaseModel):
    blue: int
    """The value of the blue channel in the RGB color."""

    green: int
    """The value of the green channel in the RGB color."""

    red: int
    """The value of the red channel in the RGB color."""


class DigitalWallets(BaseModel):
    app_icon_file_id: str
    """The identifier of the File containing the card's icon image."""

    background_image_file_id: str
    """The identifier of the File containing the card's front image."""

    card_description: str
    """A user-facing description for the card itself."""

    contact_email: Optional[str]
    """An email address the user can contact to receive support for their card."""

    contact_phone: Optional[str]
    """A phone number the user can contact to receive support for their card."""

    contact_website: Optional[str]
    """A website the user can visit to view and receive support for their card."""

    issuer_name: str
    """A user-facing description for whoever is issuing the card."""

    text_color: DigitalWalletsTextColor
    """The Card's text color, specified as an RGB triple."""


class PhysicalCards(BaseModel):
    back_image_file_id: str
    """The identifier of the File containing the physical card's back image."""

    carrier_image_file_id: str
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: str
    """A phone number the user can contact to receive support for their card."""

    front_image_file_id: str
    """The identifier of the File containing the physical card's front image."""


class CardProfile(BaseModel):
    id: str
    """The Card Profile identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    description: str
    """A description you can use to identify the Card Profile."""

    digital_wallets: DigitalWallets
    """How Cards should appear in digital wallets such as Apple Pay.

    Different wallets will use these values to render card artwork appropriately for
    their app.
    """

    physical_cards: Optional[PhysicalCards]
    """How physical cards should be designed and shipped."""

    status: Literal["pending", "rejected", "active", "archived"]
    """The status of the Card Profile.

    - `pending` - The Card Profile is awaiting review from Increase and/or
      processing by card networks.
    - `rejected` - There is an issue with the Card Profile preventing it from use.
    - `active` - The Card Profile can be assigned to Cards.
    - `archived` - The Card Profile is no longer in use.
    """

    type: Literal["card_profile"]
    """A constant representing the object's type.

    For this resource it will always be `card_profile`.
    """
