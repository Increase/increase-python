# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDispute", "Acceptance", "Loss", "Rejection", "Win"]


class Acceptance(BaseModel):
    accepted_at: datetime
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


class Loss(BaseModel):
    card_dispute_id: str
    """The identifier of the Card Dispute that was lost."""

    explanation: str
    """Why the Card Dispute was lost."""

    lost_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was lost.
    """

    transaction_id: str
    """
    The identifier of the Transaction that was created to debit the disputed funds
    from your account.
    """


class Rejection(BaseModel):
    card_dispute_id: str
    """The identifier of the Card Dispute that was rejected."""

    explanation: str
    """Why the Card Dispute was rejected."""

    rejected_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was rejected.
    """


class Win(BaseModel):
    card_dispute_id: str
    """The identifier of the Card Dispute that was won."""

    won_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was won.
    """


class CardDispute(BaseModel):
    id: str
    """The Card Dispute identifier."""

    acceptance: Optional[Acceptance] = None
    """
    If the Card Dispute's status is `accepted`, this will contain details of the
    successful dispute.
    """

    amount: Optional[int] = None
    """The amount of the dispute, if provided, or the transaction amount otherwise."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    disputed_transaction_id: str
    """The identifier of the Transaction that was disputed."""

    explanation: str
    """Why you disputed the Transaction in question."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    loss: Optional[Loss] = None
    """
    If the Card Dispute's status is `lost`, this will contain details of the lost
    dispute.
    """

    rejection: Optional[Rejection] = None
    """
    If the Card Dispute's status is `rejected`, this will contain details of the
    unsuccessful dispute.
    """

    status: Literal["pending_reviewing", "pending_user_information", "accepted", "rejected", "lost", "won"]
    """The results of the Dispute investigation.

    - `pending_reviewing` - The Card Dispute is pending review.
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

    type: Literal["card_dispute"]
    """A constant representing the object's type.

    For this resource it will always be `card_dispute`.
    """

    win: Optional[Win] = None
    """
    If the Card Dispute's status is `won`, this will contain details of the won
    dispute.
    """
