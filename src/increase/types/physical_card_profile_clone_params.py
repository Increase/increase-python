# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhysicalCardProfileCloneParams", "FrontText"]


class PhysicalCardProfileCloneParams(TypedDict, total=False):
    carrier_image_file_id: str
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: str
    """A phone number the user can contact to receive support for their card."""

    description: str
    """A description you can use to identify the Card Profile."""

    front_image_file_id: str
    """The identifier of the File containing the physical card's front image."""

    front_text: FrontText
    """Text printed on the front of the card.

    Reach out to [support@increase.com](mailto:support@increase.com) for more
    information.
    """

    program_id: str
    """The identifier of the Program to use for the cloned Physical Card Profile."""


class FrontText(TypedDict, total=False):
    line1: Required[str]
    """The first line of text on the front of the card."""

    line2: str
    """The second line of text on the front of the card.

    Providing a second line moves the first line slightly higher and prints the
    second line in the spot where the first line would have otherwise been printed.
    """
