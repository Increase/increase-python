# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardProfileCreateParams", "DigitalWallets", "DigitalWalletsTextColor", "PhysicalCards"]


class CardProfileCreateParams(TypedDict, total=False):
    description: Required[str]
    """A description you can use to identify the Card Profile."""

    digital_wallets: Required[DigitalWallets]
    """How Cards should appear in digital wallets such as Apple Pay.

    Different wallets will use these values to render card artwork appropriately for
    their app.
    """

    physical_cards: PhysicalCards
    """How physical cards should be designed and shipped."""


class DigitalWalletsTextColor(TypedDict, total=False):
    blue: Required[int]
    """The value of the blue channel in the RGB color."""

    green: Required[int]
    """The value of the green channel in the RGB color."""

    red: Required[int]
    """The value of the red channel in the RGB color."""


class DigitalWallets(TypedDict, total=False):
    app_icon_file_id: Required[str]
    """The identifier of the File containing the card's icon image."""

    background_image_file_id: Required[str]
    """The identifier of the File containing the card's front image."""

    card_description: Required[str]
    """A user-facing description for the card itself."""

    issuer_name: Required[str]
    """A user-facing description for whoever is issuing the card."""

    contact_email: str
    """An email address the user can contact to receive support for their card."""

    contact_phone: str
    """A phone number the user can contact to receive support for their card."""

    contact_website: str
    """A website the user can visit to view and receive support for their card."""

    text_color: DigitalWalletsTextColor
    """The Card's text color, specified as an RGB triple. The default is white."""


class PhysicalCards(TypedDict, total=False):
    carrier_image_file_id: Required[str]
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: Required[str]
    """A phone number the user can contact to receive support for their card."""

    front_image_file_id: Required[str]
    """The identifier of the File containing the physical card's front image."""
