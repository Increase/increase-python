# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookkeepingEntrySet", "Entry"]


class Entry(BaseModel):
    id: str
    """The entry identifier."""

    account_id: str
    """The bookkeeping account impacted by the entry."""

    amount: int
    """The amount of the entry in minor units."""


class BookkeepingEntrySet(BaseModel):
    id: str
    """The entry set identifier."""

    date: datetime
    """The timestamp of the entry set."""

    entries: List[Entry]
    """The entries."""

    transaction_id: Optional[str]
    """The transaction identifier, if any."""

    type: Literal["bookkeeping_entry_set"]
    """A constant representing the object's type.

    For this resource it will always be `bookkeeping_entry_set`.
    """
