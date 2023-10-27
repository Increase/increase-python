# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ExportCreateParams",
    "AccountStatementOfx",
    "AccountStatementOfxCreatedAt",
    "BalanceCsv",
    "BalanceCsvCreatedAt",
    "BookkeepingAccountBalanceCsv",
    "BookkeepingAccountBalanceCsvCreatedAt",
    "TransactionCsv",
    "TransactionCsvCreatedAt",
]


class ExportCreateParams(TypedDict, total=False):
    category: Required[
        Literal["account_statement_ofx", "transaction_csv", "balance_csv", "bookkeeping_account_balance_csv"]
    ]
    """The type of Export to create.

    - `account_statement_ofx` - Export an Open Financial Exchange (OFX) file of
      transactions and balances for a given time range and Account.
    - `transaction_csv` - Export a CSV of all transactions for a given time range.
    - `balance_csv` - Export a CSV of account balances for the dates in a given
      range.
    - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
      balances for the dates in a given range.
    """

    account_statement_ofx: AccountStatementOfx
    """Options for the created export.

    Required if `category` is equal to `account_statement_ofx`.
    """

    balance_csv: BalanceCsv
    """Options for the created export.

    Required if `category` is equal to `balance_csv`.
    """

    bookkeeping_account_balance_csv: BookkeepingAccountBalanceCsv
    """Options for the created export.

    Required if `category` is equal to `bookkeeping_account_balance_csv`.
    """

    transaction_csv: TransactionCsv
    """Options for the created export.

    Required if `category` is equal to `transaction_csv`.
    """


class AccountStatementOfxCreatedAt(TypedDict, total=False):
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


class AccountStatementOfx(TypedDict, total=False):
    account_id: Required[str]
    """The Account to create a statement for."""

    created_at: AccountStatementOfxCreatedAt
    """Filter results by time range on the `created_at` attribute."""


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


class BookkeepingAccountBalanceCsvCreatedAt(TypedDict, total=False):
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


class BookkeepingAccountBalanceCsv(TypedDict, total=False):
    bookkeeping_account_id: str
    """Filter exported Transactions to the specified BookkeepingAccount."""

    created_at: BookkeepingAccountBalanceCsvCreatedAt
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
