# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardRefundCreateParams"]


class CardRefundCreateParams(TypedDict, total=False):
    pending_transaction_id: str
    """The identifier of the Pending Transaction for the refund authorization.

    If this is provided, `transaction` must not be provided as a refund with a
    refund authorized can not be linked to a regular transaction.
    """

    transaction_id: str
    """The identifier for the Transaction to refund.

    The Transaction's source must have a category of card_settlement.
    """
