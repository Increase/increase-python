# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    ach_debit_status: Literal["disabled", "enabled"]
    """If the Group is allowed to create ACH debits."""

    activation_status: Literal["unactivated", "activated"]
    """If the Group is activated or not."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Group
    was created.
    """

    id: str
    """The Group identifier."""

    type: Literal["group"]
    """A constant representing the object's type.

    For this resource it will always be `group`.
    """
