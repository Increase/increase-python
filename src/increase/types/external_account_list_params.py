# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ExternalAccountListParams", "Status"]


class ExternalAccountListParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    status: Status


_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[Literal["active", "archived"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
