# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PendingTransactionListParams", "CreatedAt", "Status"]


class PendingTransactionListParams(TypedDict, total=False):
    account_id: str
    """Filter pending transactions to those belonging to the specified Account."""

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    route_id: str
    """Filter pending transactions to those belonging to the specified Route."""

    source_id: str
    """Filter pending transactions to those caused by the specified source."""

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
        "in": List[Literal["pending", "complete"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
