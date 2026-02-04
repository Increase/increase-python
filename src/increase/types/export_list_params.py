# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExportListParams", "CreatedAt", "Form1099Int", "Form1099Misc", "Status"]


class ExportListParams(TypedDict, total=False):
    category: Literal[
        "account_statement_ofx",
        "account_statement_bai2",
        "transaction_csv",
        "balance_csv",
        "bookkeeping_account_balance_csv",
        "entity_csv",
        "vendor_csv",
        "dashboard_table_csv",
        "account_verification_letter",
        "funding_instructions",
        "form_1099_int",
        "form_1099_misc",
    ]
    """Filter Exports for those with the specified category.

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
    - `dashboard_table_csv` - Certain dashboard tables are available as CSV exports.
      This export cannot be created via the API.
    - `account_verification_letter` - A PDF of an account verification letter.
    - `funding_instructions` - A PDF of funding instructions.
    - `form_1099_int` - A PDF of an Internal Revenue Service Form 1099-INT.
    - `form_1099_misc` - A PDF of an Internal Revenue Service Form 1099-MISC.
    """

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    form_1099_int: Form1099Int

    form_1099_misc: Form1099Misc

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


class Form1099Int(TypedDict, total=False):
    account_id: str
    """Filter Form 1099-INT Exports to those for the specified Account."""


class Form1099Misc(TypedDict, total=False):
    account_id: str
    """Filter Form 1099-MISC Exports to those for the specified Account."""


_StatusReservedKeywords = TypedDict(
    "_StatusReservedKeywords",
    {
        "in": List[Literal["pending", "complete", "failed"]],
    },
    total=False,
)


class Status(_StatusReservedKeywords, total=False):
    pass
