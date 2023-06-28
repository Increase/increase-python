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
    """The status of the Export."""

    type: Literal["export"]
    """A constant representing the object's type.

    For this resource it will always be `export`.
    """
