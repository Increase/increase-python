# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckbookCheck"]


class CheckbookCheck(BaseModel):
    """A Checkbook Check is a single check within a Checkbook."""

    id: str
    """The Checkbook Check's identifier."""

    check_number: int
    """The check number printed on the check."""

    checkbook_id: str
    """The identifier of the Checkbook the check belongs to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Checkbook Check was created.
    """

    status: Literal["pending_deposit", "deposited", "stopped", "requires_attention"]
    """The status of the Checkbook Check.

    - `pending_deposit` - The check has not yet been deposited.
    - `deposited` - The check has been deposited.
    - `stopped` - The check has been stopped and can no longer be deposited.
    - `requires_attention` - The check requires attention from an Increase operator.
    """

    type: Literal["checkbook_check"]
    """A constant representing the object's type.

    For this resource it will always be `checkbook_check`.
    """
