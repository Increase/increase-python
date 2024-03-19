# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BookkeepingEntrySetListParams"]


class BookkeepingEntrySetListParams(TypedDict, total=False):
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

    transaction_id: str
    """Filter to the Bookkeeping Entry Set that maps to this Transaction."""
