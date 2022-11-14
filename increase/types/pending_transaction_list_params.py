# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["Status", "PendingTransactionListParams"]

_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[Literal["pending", "complete"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords):
    pass


class PendingTransactionListParams(TypedDict, total=False):
    account_id: str
    """Filter pending transactions to those belonging to the specified Account."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    route_id: str
    """Filter pending transactions to those belonging to the specified Route."""

    source_id: str
    """Filter pending transactions to those caused by the specified source."""

    status: Status
