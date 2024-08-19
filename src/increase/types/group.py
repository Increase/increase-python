# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """The Group identifier."""

    ach_debit_status: Literal["disabled", "enabled"]
    """If the Group is allowed to create ACH debits.

    - `disabled` - The Group cannot make ACH debits.
    - `enabled` - The Group can make ACH debits.
    """

    activation_status: Literal["unactivated", "activated"]
    """If the Group is activated or not.

    - `unactivated` - The Group is not activated.
    - `activated` - The Group is activated.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Group
    was created.
    """

    type: Literal["group"]
    """A constant representing the object's type.

    For this resource it will always be `group`.
    """
