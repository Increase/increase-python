# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RoutingNumberListParams"]


class RoutingNumberListParams(TypedDict, total=False):
    routing_number: Required[str]
    """Filter financial institutions by routing number."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
