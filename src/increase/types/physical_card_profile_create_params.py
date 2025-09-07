# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCardProfileCreateParams", "FrontText"]


class PhysicalCardProfileCreateParams(TypedDict, total=False):
    carrier_image_file_id: Required[str]
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: Required[str]
    """A phone number the user can contact to receive support for their card."""

    description: Required[str]
    """A description you can use to identify the Card Profile."""

    front_image_file_id: Required[str]
    """The identifier of the File containing the physical card's front image."""

    program_id: Required[str]
    """The identifier for the Program that this Physical Card Profile falls under."""

    back_color: Literal["black", "white"]
    """The color of the text on the back of the card. Defaults to "black".

    - `black` - Black personalization color.
    - `white` - White personalization color.
    """

    card_stock_reference: str
    """A reference ID provided by the fulfillment provider for the card stock used.

    Only used if you've ordered card stock separately.
    """

    carrier_stock_reference: str
    """A reference ID provided by the fulfillment provider for the carrier stock used.

    Only used if you've ordered carrier stock separately.
    """

    front_color: Literal["black", "white"]
    """The color of the design on the front of the card. Defaults to "black".

    - `black` - Black personalization color.
    - `white` - White personalization color.
    """

    front_text: FrontText
    """Text printed on the front of the card.

    Reach out to [support@increase.com](mailto:support@increase.com) for more
    information.
    """


class FrontText(TypedDict, total=False):
    line1: Required[str]
    """The first line of text on the front of the card."""

    line2: str
    """The second line of text on the front of the card.

    Providing a second line moves the first line slightly higher and prints the
    second line in the spot where the first line would have otherwise been printed.
    """
