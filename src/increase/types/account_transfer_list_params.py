# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountTransferListParams", "CreatedAt"]


class AccountTransferListParams(TypedDict, total=False):
    account_id: str
    """Filter Account Transfers to those that originated from the specified Account."""

    created_at: CreatedAt

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
