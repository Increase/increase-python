# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExportCreateParams", "BalanceCsv", "BalanceCsvCreatedAt", "TransactionCsv", "TransactionCsvCreatedAt"]


class ExportCreateParams(TypedDict, total=False):
    category: Required[Literal["transaction_csv", "balance_csv"]]
    """The type of Export to create.

    - `transaction_csv` - Export a CSV of all transactions for a given time range.
    - `balance_csv` - Export a CSV of account balances for the dates in a given
      range.
    """

    balance_csv: BalanceCsv
    """Options for the created export.

    Required if `category` is equal to `balance_csv`.
    """

    transaction_csv: TransactionCsv
    """Options for the created export.

    Required if `category` is equal to `transaction_csv`.
    """


class BalanceCsvCreatedAt(TypedDict, total=False):
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


class BalanceCsv(TypedDict, total=False):
    account_id: str
    """Filter exported Transactions to the specified Account."""

    created_at: BalanceCsvCreatedAt
    """Filter results by time range on the `created_at` attribute."""


class TransactionCsvCreatedAt(TypedDict, total=False):
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


class TransactionCsv(TypedDict, total=False):
    account_id: str
    """Filter exported Transactions to the specified Account."""

    created_at: TransactionCsvCreatedAt
    """Filter results by time range on the `created_at` attribute."""
