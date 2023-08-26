# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboundACHTransferListParams", "CreatedAt"]


class InboundACHTransferListParams(TypedDict, total=False):
    account_id: str
    """Filter Inbound ACH Tranfers to ones belonging to the specified Account."""

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    status: Literal["pending", "declined", "accepted", "returned"]
    """Filter Inbound ACH Transfers to those with the specified status.

    - `pending` - The Inbound ACH Transfer is awaiting action, will transition
      automatically if no action is taken.
    - `declined` - The Inbound ACH Transfer has been declined.
    - `accepted` - The Inbound ACH Transfer is accepted.
    - `returned` - The Inbound ACH Transfer has been returned.
    """


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
