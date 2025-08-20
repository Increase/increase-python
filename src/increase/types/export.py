# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Export"]


class Export(BaseModel):
    id: str
    """The Export identifier."""

    category: Literal[
        "account_statement_ofx",
        "account_statement_bai2",
        "transaction_csv",
        "balance_csv",
        "bookkeeping_account_balance_csv",
        "entity_csv",
        "vendor_csv",
        "dashboard_table_csv",
    ]
    """The category of the Export.

    We may add additional possible values for this enum over time; your application
    should be able to handle that gracefully.

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
    """

    created_at: datetime
    """The time the Export was created."""

    file_download_url: Optional[str] = None
    """A URL at which the Export's file can be downloaded.

    This will be present when the Export's status transitions to `complete`.
    """

    file_id: Optional[str] = None
    """The File containing the contents of the Export.

    This will be present when the Export's status transitions to `complete`.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    status: Literal["pending", "complete", "failed"]
    """The status of the Export.

    - `pending` - Increase is generating the export.
    - `complete` - The export has been successfully generated.
    - `failed` - The export failed to generate. Increase will reach out to you to
      resolve the issue.
    """

    type: Literal["export"]
    """A constant representing the object's type.

    For this resource it will always be `export`.
    """
