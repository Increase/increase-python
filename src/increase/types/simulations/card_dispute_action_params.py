# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardDisputeActionParams"]


class CardDisputeActionParams(TypedDict, total=False):
    status: Required[Literal["accepted", "rejected"]]
    """The status to move the dispute to.

    - `accepted` - The Card Dispute has been accepted and your funds have been
      returned.
    - `rejected` - The Card Dispute has been rejected.
    """

    explanation: str
    """Why the dispute was rejected. Not required for accepting disputes."""
