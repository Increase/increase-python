# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["IntrafiAccountEnrollmentListParams", "Status"]


class IntrafiAccountEnrollmentListParams(TypedDict, total=False):
    account_id: str
    """Filter IntraFi Account Enrollments to the one belonging to an account."""

    cursor: str
    """Return the page of entries after this one."""

    idempotency_key: str
    """
    Filter records to the one with the specified `idempotency_key` you chose for
    that object. This value is unique across Increase and is used to ensure that a
    request is only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

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
