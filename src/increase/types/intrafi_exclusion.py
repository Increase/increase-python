# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntrafiExclusion"]


class IntrafiExclusion(BaseModel):
    id: str
    """The identifier of this exclusion request."""

    bank_name: str
    """The name of the excluded institution."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the exclusion was created.
    """

    entity_id: str
    """The entity for which this institution is excluded."""

    excluded_at: Optional[datetime] = None
    """When this was exclusion was confirmed by IntraFi."""

    fdic_certificate_number: Optional[str] = None
    """
    The Federal Deposit Insurance Corporation's certificate number for the
    institution.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    status: Literal["pending", "completed", "archived"]
    """The status of the exclusion request.

    - `pending` - The exclusion is being added to the IntraFi network.
    - `completed` - The exclusion has been added to the IntraFi network.
    - `archived` - The exclusion has been removed from the IntraFi network.
    """

    submitted_at: Optional[datetime] = None
    """When this was exclusion was submitted to IntraFi by Increase."""

    type: Literal["intrafi_exclusion"]
    """A constant representing the object's type.

    For this resource it will always be `intrafi_exclusion`.
    """
