# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardRefundCreateParams"]


class CardRefundCreateParams(TypedDict, total=False):
    transaction_id: Required[str]
    """The identifier for the Transaction to refund.

    The Transaction's source must have a category of card_settlement.
    """
