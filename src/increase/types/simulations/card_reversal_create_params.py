# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardReversalCreateParams"]


class CardReversalCreateParams(TypedDict, total=False):
    card_payment_id: Required[str]
    """The identifier of the Card Payment to create a reversal on."""

    amount: int
    """The amount of the reversal in minor units in the card authorization's currency.

    This defaults to the authorization amount.
    """
