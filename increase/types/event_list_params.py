# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CreatedAt", "Category", "EventListParams"]


class CreatedAt(TypedDict, total=False):
    after: str
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: str
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: str
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: str
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """


_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[
            Literal[
                "account.created",
                "account.updated",
                "account_number.created",
                "account_number.updated",
                "account_transfer.created",
                "account_transfer.updated",
                "ach_prenotification.created",
                "ach_prenotification.updated",
                "ach_transfer.created",
                "ach_transfer.updated",
                "card.created",
                "card.updated",
                "card_authorization_decision.created",
                "card_dispute.created",
                "card_dispute.updated",
                "check_deposit.created",
                "check_deposit.updated",
                "check_transfer.created",
                "check_transfer.updated",
                "declined_transaction.created",
                "entity.created",
                "entity.updated",
                "file.created",
                "group.updated",
                "group.heartbeat",
                "oauth_connection.created",
                "oauth_connection.deactivated",
                "pending_transaction.created",
                "pending_transaction.updated",
                "real_time_payments_transfer.created",
                "real_time_payments_transfer.updated",
                "transaction.created",
                "wire_drawdown_request.created",
                "wire_drawdown_request.updated",
                "wire_transfer.created",
                "wire_transfer.updated",
            ]
        ],
    },
    total=False,
)


class Category(_CategoryReservedKeywords):
    pass


class EventListParams(TypedDict, total=False):
    associated_object_id: str
    """Filter Events to those belonging to the object with the provided identifier."""

    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
