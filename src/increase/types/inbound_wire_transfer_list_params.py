# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboundWireTransferListParams", "CreatedAt"]


class InboundWireTransferListParams(TypedDict, total=False):
    account_id: str
    """Filter Inbound Wire Tranfers to ones belonging to the specified Account."""

    account_number_id: str
    """Filter Inbound Wire Tranfers to ones belonging to the specified Account Number."""

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    status: Literal["pending", "accepted", "declined", "reversed"]
    """Filter Inbound Wire Transfers to those with the specified status.

    - `pending` - The Inbound Wire Transfer is awaiting action, will transition
      automatically if no action is taken.
    - `accepted` - The Inbound Wire Transfer is accepted.
    - `declined` - The Inbound Wire Transfer was declined.
    - `reversed` - The Inbound Wire Transfer was reversed.
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
