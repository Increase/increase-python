# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhysicalCardProfileCreateParams"]


class PhysicalCardProfileCreateParams(TypedDict, total=False):
    carrier_image_file_id: Required[str]
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: Required[str]
    """A phone number the user can contact to receive support for their card."""

    description: Required[str]
    """A description you can use to identify the Card Profile."""

    front_image_file_id: Required[str]
    """The identifier of the File containing the physical card's front image."""
