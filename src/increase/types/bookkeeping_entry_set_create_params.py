# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BookkeepingEntrySetCreateParams", "Entry"]


class BookkeepingEntrySetCreateParams(TypedDict, total=False):
    entries: Required[Iterable[Entry]]
    """The bookkeeping entries."""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date of the transaction.

    Optional if `transaction_id` is provided, in which case we use the `date` of
    that transaction. Required otherwise.
    """

    transaction_id: str
    """The identifier of the Transaction related to this entry set, if any."""


class Entry(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the Bookkeeping Account impacted by this entry."""

    amount: Required[int]
    """The entry amount in the minor unit of the account currency.

    For dollars, for example, this is cents. Debit entries have positive amounts;
    credit entries have negative amounts.
    """
