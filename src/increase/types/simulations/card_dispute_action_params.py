# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardDisputeActionParams"]


class CardDisputeActionParams(TypedDict, total=False):
    status: Required[Literal["accepted", "rejected"]]
    """The status to move the dispute to."""

    explanation: str
    """Why the dispute was rejected. Not required for accepting disputes."""
