# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["OAuthConnectionListParams", "Status"]


class OAuthConnectionListParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    oauth_application_id: str
    """
    Filter results to only include OAuth Connections for a specific OAuth
    Application.
    """

    status: Status


_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[Literal["active", "inactive"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
