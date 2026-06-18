# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BalanceLookup", "Loan", "LoanReceivables"]


class LoanReceivables(BaseModel):
    """The receivables balances for the loan."""

    purchasable_balance: int
    """The balance of seasoned receivables available to be purchased."""

    purchased_balance: int
    """The balance of receivables that have been purchased."""


class Loan(BaseModel):
    """The loan balances for the Account."""

    due_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the loan
    payment is due.
    """

    due_balance: int
    """The total amount due on the loan."""

    past_due_balance: int
    """The amount past due on the loan."""

    receivables: Optional[LoanReceivables] = None
    """The receivables balances for the loan."""


class BalanceLookup(BaseModel):
    """
    Represents a request to lookup the balance of an Account at a given point in time.
    """

    account_id: str
    """The identifier for the account for which the balance was queried."""

    available_balance: int
    """
    The Account's available balance, representing the current balance less any open
    Pending Transactions on the Account.
    """

    current_balance: int
    """
    The Account's current balance, representing the sum of all posted Transactions
    on the Account.
    """

    loan: Optional[Loan] = None
    """The loan balances for the Account."""

    type: Literal["balance_lookup"]
    """A constant representing the object's type.

    For this resource it will always be `balance_lookup`.
    """
