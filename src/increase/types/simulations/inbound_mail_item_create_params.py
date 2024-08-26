# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundMailItemCreateParams"]


class InboundMailItemCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The amount of the check to be simulated, in cents."""

    lockbox_id: Required[str]
    """The identifier of the Lockbox to simulate inbound mail to."""

    contents_file_id: str
    """The file containing the PDF contents.

    If not present, a default check image file will be used.
    """
