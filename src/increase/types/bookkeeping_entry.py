# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookkeepingEntry"]


class BookkeepingEntry(BaseModel):
    id: str
    """The entry identifier."""

    account_id: str
    """The identifier for the Account the Entry belongs to."""

    amount: int
    """The Entry amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    entry_set_id: str
    """The identifier for the Account the Entry belongs to."""

    type: Literal["bookkeeping_entry"]
    """A constant representing the object's type.

    For this resource it will always be `bookkeeping_entry`.
    """
