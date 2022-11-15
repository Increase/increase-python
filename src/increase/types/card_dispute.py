# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Acceptance", "Rejection", "CardDispute"]


class Acceptance(BaseModel):
    accepted_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was accepted.
    """

    card_dispute_id: str
    """The identifier of the Card Dispute that was accepted."""

    transaction_id: str
    """
    The identifier of the Transaction that was created to return the disputed funds
    to your account.
    """


class Rejection(BaseModel):
    card_dispute_id: str
    """The identifier of the Card Dispute that was rejected."""

    explanation: str
    """Why the Card Dispute was rejected."""

    rejected_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was rejected.
    """


class CardDispute(BaseModel):
    acceptance: Optional[Acceptance]
    """
    If the Card Dispute's status is `accepted`, this will contain details of the
    successful dispute.
    """

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    disputed_transaction_id: str
    """The identifier of the Transaction that was disputed."""

    explanation: str
    """Why you disputed the Transaction in question."""

    id: str
    """The Card Dispute identifier."""

    rejection: Optional[Rejection]
    """
    If the Card Dispute's status is `rejected`, this will contain details of the
    unsuccessful dispute.
    """

    status: Literal["pending_reviewing", "accepted", "rejected"]
    """The results of the Dispute investigation."""

    type: Literal["card_dispute"]
    """A constant representing the object's type.

    For this resource it will always be `card_dispute`.
    """
