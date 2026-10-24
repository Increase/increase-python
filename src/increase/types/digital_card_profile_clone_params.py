# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "DigitalCardProfileCloneParams",
    "ApplePay",
    "ApplePayAssociatedApplicationIdentifier",
    "ApplePayAssociatedStoreIdentifier",
    "TextColor",
]


class DigitalCardProfileCloneParams(TypedDict, total=False):
    app_icon_file_id: str
    """The identifier of the File containing the card's icon image."""

    apple_pay: ApplePay
    """Apple Pay specific settings for the Card Profile.

    Each list you leave out is copied from the original Card Profile.
    """

    background_image_file_id: str
    """The identifier of the File containing the card's front image."""

    card_description: str
    """A user-facing description for the card itself."""

    contact_email: str
    """An email address the user can contact to receive support for their card."""

    contact_name: str
    """
    The name of your company or card program, shown to the user as who to contact
    for support with their card.
    """

    contact_phone: str
    """A phone number the user can contact to receive support for their card."""

    contact_website: str
    """A website the user can visit to view and receive support for their card."""

    description: str
    """A description you can use to identify the Card Profile."""

    text_color: TextColor
    """The Card's text color, specified as an RGB triple. The default is white."""


class ApplePayAssociatedApplicationIdentifier(TypedDict, total=False):
    identifier: Required[str]
    """
    The application identifier, composed of your Apple Developer Team ID and the
    application's bundle identifier, like `ABCDE12345.com.example.app`.
    """


class ApplePayAssociatedStoreIdentifier(TypedDict, total=False):
    identifier: Required[str]
    """The numeric App Store identifier."""


class ApplePay(TypedDict, total=False):
    """Apple Pay specific settings for the Card Profile.

    Each list you leave out is copied from the original Card Profile.
    """

    associated_application_identifiers: Iterable[ApplePayAssociatedApplicationIdentifier]
    """The applications to associate with cards using this Card Profile."""

    associated_store_identifiers: Iterable[ApplePayAssociatedStoreIdentifier]
    """
    The App Store listings of the applications to associate with cards using this
    Card Profile.
    """


class TextColor(TypedDict, total=False):
    """The Card's text color, specified as an RGB triple. The default is white."""

    blue: Required[int]
    """The value of the blue channel in the RGB color."""

    green: Required[int]
    """The value of the green channel in the RGB color."""

    red: Required[int]
    """The value of the red channel in the RGB color."""
