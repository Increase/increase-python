# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionListParams", "Category", "CreatedAt"]


class TransactionListParams(TypedDict, total=False):
    account_id: str
    """Filter Transactions for those belonging to the specified Account."""

    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    route_id: str
    """Filter Transactions for those belonging to the specified route.

    This could be a Card ID or an Account Number ID.
    """


_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[
            Literal[
                "account_transfer_intention",
                "ach_transfer_intention",
                "ach_transfer_rejection",
                "ach_transfer_return",
                "cashback_payment",
                "card_dispute_acceptance",
                "card_dispute_financial",
                "card_dispute_loss",
                "card_refund",
                "card_settlement",
                "card_revenue_payment",
                "check_deposit_acceptance",
                "check_deposit_return",
                "check_transfer_deposit",
                "fee_payment",
                "inbound_ach_transfer",
                "inbound_ach_transfer_return_intention",
                "inbound_check_deposit_return_intention",
                "inbound_check_adjustment",
                "inbound_real_time_payments_transfer_confirmation",
                "inbound_wire_reversal",
                "inbound_wire_transfer",
                "inbound_wire_transfer_reversal",
                "interest_payment",
                "internal_source",
                "real_time_payments_transfer_acknowledgement",
                "sample_funds",
                "wire_transfer_intention",
                "swift_transfer_intention",
                "swift_transfer_return",
                "card_push_transfer_acceptance",
                "account_revenue_payment",
                "other",
            ]
        ],
    },
    total=False,
)


class Category(_CategoryReservedKeywords, total=False):
    pass


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """
