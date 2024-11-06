# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardDisputeActionParams"]


class CardDisputeActionParams(TypedDict, total=False):
    status: Required[Literal["pending_user_information", "accepted", "rejected", "lost", "won"]]
    """The status to move the dispute to.

    - `pending_user_information` - Increase has requested more information related
      to the Card Dispute from you.
    - `accepted` - The Card Dispute has been accepted and your funds have been
      returned. The card dispute will eventually transition into `won` or `lost`
      depending on the outcome.
    - `rejected` - The Card Dispute has been rejected.
    - `lost` - The Card Dispute has been lost and funds previously credited from the
      acceptance have been debited.
    - `won` - The Card Dispute has been won and no further action can be taken.
    """

    explanation: str
    """Why the dispute was rejected. Not required for accepting disputes."""
