# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BookkeepingEntryListParams"]


class BookkeepingEntryListParams(TypedDict, total=False):
    account_id: str
    """The identifier for the Bookkeeping Account to filter by."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """
