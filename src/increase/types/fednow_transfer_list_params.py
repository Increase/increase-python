# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FednowTransferListParams", "CreatedAt", "Status"]


class FednowTransferListParams(TypedDict, total=False):
    account_id: str
    """Filter FedNow Transfers to those that originated from the specified Account."""

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    external_account_id: str
    """Filter FedNow Transfers to those made to the specified External Account."""

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


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """


_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[
            Literal[
                "pending_reviewing",
                "canceled",
                "reviewing_rejected",
                "requires_attention",
                "pending_approval",
                "pending_submitting",
                "pending_response",
                "complete",
                "rejected",
            ]
        ],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
