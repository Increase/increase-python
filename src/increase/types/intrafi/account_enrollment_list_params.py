# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AccountEnrollmentListParams", "Status"]


class AccountEnrollmentListParams(TypedDict, total=False):
    account_id: str
    """Filter IntraFi Account Enrollments to the one belonging to an account."""

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
        "in": List[Literal["pending_enrolling", "enrolled", "pending_unenrolling", "unenrolled", "requires_attention"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
