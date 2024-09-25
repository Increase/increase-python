# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardDisputeCreateParams"]


class CardDisputeCreateParams(TypedDict, total=False):
    disputed_transaction_id: Required[str]
    """The Transaction you wish to dispute.

    This Transaction must have a `source_type` of `card_settlement`.
    """

    explanation: Required[str]
    """Why you are disputing this Transaction."""

    amount: int
    """The monetary amount of the part of the transaction that is being disputed.

    This is optional and will default to the full amount of the transaction if not
    provided. If provided, the amount must be less than or equal to the amount of
    the transaction.
    """
