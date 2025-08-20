# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ExportCreateParams",
    "AccountStatementBai2",
    "AccountStatementOfx",
    "AccountStatementOfxCreatedAt",
    "BalanceCsv",
    "BalanceCsvCreatedAt",
    "BookkeepingAccountBalanceCsv",
    "BookkeepingAccountBalanceCsvCreatedAt",
    "EntityCsv",
    "EntityCsvStatus",
    "TransactionCsv",
    "TransactionCsvCreatedAt",
]


class ExportCreateParams(TypedDict, total=False):
    category: Required[
        Literal[
            "account_statement_ofx",
            "account_statement_bai2",
            "transaction_csv",
            "balance_csv",
            "bookkeeping_account_balance_csv",
            "entity_csv",
            "vendor_csv",
        ]
    ]
    """The type of Export to create.

    - `account_statement_ofx` - Export an Open Financial Exchange (OFX) file of
      transactions and balances for a given time range and Account.
    - `account_statement_bai2` - Export a BAI2 file of transactions and balances for
      a given date and optional Account.
    - `transaction_csv` - Export a CSV of all transactions for a given time range.
    - `balance_csv` - Export a CSV of account balances for the dates in a given
      range.
    - `bookkeeping_account_balance_csv` - Export a CSV of bookkeeping account
      balances for the dates in a given range.
    - `entity_csv` - Export a CSV of entities with a given status.
    - `vendor_csv` - Export a CSV of vendors added to the third-party risk
      management dashboard.
    """

    account_statement_bai2: AccountStatementBai2
    """Options for the created export.

    Required if `category` is equal to `account_statement_bai2`.
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

    entity_csv: EntityCsv
    """Options for the created export.

    Required if `category` is equal to `entity_csv`.
    """

    transaction_csv: TransactionCsv
    """Options for the created export.

    Required if `category` is equal to `transaction_csv`.
    """

    vendor_csv: object
    """Options for the created export.

    Required if `category` is equal to `vendor_csv`.
    """


class AccountStatementBai2(TypedDict, total=False):
    account_id: str
    """The Account to create a BAI2 report for.

    If not provided, all open accounts will be included.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date to create a BAI2 report for.

    If not provided, the current date will be used. The timezone is UTC. If the
    current date is used, the report will include intraday balances, otherwise it
    will include end-of-day balances for the provided date.
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

    program_id: str
    """Filter exported Transactions to the specified Program."""


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
    """Filter exported Transactions to the specified Bookkeeping Account."""

    created_at: BookkeepingAccountBalanceCsvCreatedAt
    """Filter results by time range on the `created_at` attribute."""


_EntityCsvStatusReservedKeywords = TypedDict(
    "_EntityCsvStatusReservedKeywords",
    {
        "in": List[Literal["active", "archived", "disabled"]],
    },
    total=False,
)


class EntityCsvStatus(_EntityCsvStatusReservedKeywords, total=False):
    pass


class EntityCsv(TypedDict, total=False):
    status: EntityCsvStatus
    """Entity statuses to filter by."""


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

    program_id: str
    """Filter exported Transactions to the specified Program."""
