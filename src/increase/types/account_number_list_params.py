# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountNumberListParams"]


class AccountNumberListParams(TypedDict, total=False):
    account_id: str
    """Filter Account Numbers to those belonging to the specified Account."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    status: Literal["active", "disabled", "canceled"]
    """The status to retrieve Account Numbers for."""
