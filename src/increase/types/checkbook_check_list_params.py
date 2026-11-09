# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CheckbookCheckListParams"]


class CheckbookCheckListParams(TypedDict, total=False):
    account_number_id: str
    """Filter Checkbook Checks to those drawn on the specified Account Number."""

    check_number: int
    """Filter Checkbook Checks to the one with the specified check number."""

    checkbook_id: str
    """Filter Checkbook Checks to those belonging to the specified Checkbook."""

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.

    Defaults to `100`.
    """
