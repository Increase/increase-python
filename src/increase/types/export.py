# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Export"]


class Export(BaseModel):
    id: str
    """The Export identifier."""

    category: Literal["transaction_csv", "balance_csv"]
    """The category of the Export.

    We may add additional possible values for this enum over time; your application
    should be able to handle that gracefully.

    - `transaction_csv` - Export a CSV of all transactions for a given time range.
    - `balance_csv` - Export a CSV of account balances for the dates in a given
      range.
    """

    created_at: datetime
    """The time the Export was created."""

    file_download_url: Optional[str]
    """A URL at which the Export's file can be downloaded.

    This will be present when the Export's status transitions to `complete`.
    """

    file_id: Optional[str]
    """The File containing the contents of the Export.

    This will be present when the Export's status transitions to `complete`.
    """

    status: Literal["pending", "complete"]
    """The status of the Export.

    - `pending` - Increase is generating the export.
    - `complete` - The export has been successfully generated.
    """

    type: Literal["export"]
    """A constant representing the object's type.

    For this resource it will always be `export`.
    """
