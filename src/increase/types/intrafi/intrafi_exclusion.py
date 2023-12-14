# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IntrafiExclusion"]


class IntrafiExclusion(BaseModel):
    id: str
    """The identifier of this exclusion request."""

    bank_name: str
    """The name of the excluded institution."""

    entity_id: str
    """The entity for which this institution is excluded."""

    excluded_at: Optional[datetime]
    """When this was exclusion was confirmed by IntraFi."""

    fdic_certificate_number: Optional[str]
    """
    The Federal Deposit Insurance Corporation's certificate number for the
    institution.
    """

    status: Literal["pending", "completed", "archived"]
    """The status of the exclusion request.

    - `pending` - The exclusion is being added to the IntraFi network.
    - `completed` - The exclusion has been added to the IntraFi network.
    - `archived` - The exclusion has been removed from the IntraFi network.
    """

    submitted_at: Optional[datetime]
    """When this was exclusion was submitted to IntraFi by Increase."""

    type: Literal["intrafi_exclusion"]
    """A constant representing the object's type.

    For this resource it will always be `intrafi_exclusion`.
    """
