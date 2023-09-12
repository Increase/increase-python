# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CardProfileListParams", "PhysicalCardsStatus", "Status"]


class CardProfileListParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    physical_cards_status: PhysicalCardsStatus

    status: Status


_PhysicalCardsStatusReservedKeywords = TypedDict(
    "_PhysicalCardsStatusReservedKeywords",
    {
        "in": List[
            Literal["not_eligible", "rejected", "pending_creating", "pending_reviewing", "pending_submitting", "active"]
        ],
    },
    total=False,
)


class PhysicalCardsStatus(_PhysicalCardsStatusReservedKeywords, total=False):
    pass


_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[Literal["pending", "rejected", "active", "archived"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
