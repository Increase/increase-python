# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookkeepingBalanceLookup"]


class BookkeepingBalanceLookup(BaseModel):
    balance: int
    """
    The Bookkeeping Account's current balance, representing the sum of all
    Bookkeeping Entries on the Bookkeeping Account.
    """

    bookkeeping_account_id: str
    """The identifier for the account for which the balance was queried."""

    type: Literal["bookkeeping_balance_lookup"]
    """A constant representing the object's type.

    For this resource it will always be `bookkeeping_balance_lookup`.
    """
