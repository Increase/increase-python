# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhysicalCardProfileCloneParams"]


class PhysicalCardProfileCloneParams(TypedDict, total=False):
    carrier_image_file_id: str
    """The identifier of the File containing the physical card's carrier image."""

    contact_phone: str
    """A phone number the user can contact to receive support for their card."""

    description: str
    """A description you can use to identify the Card Profile."""

    front_image_file_id: str
    """The identifier of the File containing the physical card's front image."""
