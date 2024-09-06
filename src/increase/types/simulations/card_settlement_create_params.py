# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardSettlementCreateParams"]


class CardSettlementCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The identifier of the Card to create a settlement on."""

    pending_transaction_id: Required[str]
    """
    The identifier of the Pending Transaction for the Card Authorization you wish to
    settle.
    """

    amount: int
    """The amount to be settled.

    This defaults to the amount of the Pending Transaction being settled.
    """
