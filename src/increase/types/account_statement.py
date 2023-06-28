# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountStatement"]


class AccountStatement(BaseModel):
    id: str
    """The Account Statement identifier."""

    account_id: str
    """The identifier for the Account this Account Statement belongs to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    Statement was created.
    """

    ending_balance: int
    """The Account's balance at the start of its statement period."""

    file_id: str
    """The identifier of the File containing a PDF of the statement."""

    starting_balance: int
    """The Account's balance at the start of its statement period."""

    statement_period_end: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the end
    of the period the Account Statement covers.
    """

    statement_period_start: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the
    start of the period the Account Statement covers.
    """

    type: Literal["account_statement"]
    """A constant representing the object's type.

    For this resource it will always be `account_statement`.
    """
