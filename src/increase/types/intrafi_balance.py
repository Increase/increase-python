# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntrafiBalance", "Balance", "BalanceBankLocation"]


class BalanceBankLocation(BaseModel):
    city: str
    """The bank's city."""

    state: str
    """The bank's state."""


class Balance(BaseModel):
    id: str
    """The identifier of this balance."""

    balance: int
    """The balance, in minor units of `currency`, held with this bank."""

    bank: str
    """The name of the bank holding these funds."""

    bank_location: Optional[BalanceBankLocation] = None
    """The primary location of the bank."""

    fdic_certificate_number: str
    """The Federal Deposit Insurance Corporation (FDIC) certificate number of the bank.

    Because many banks have the same or similar names, this can be used to uniquely
    identify the institution.
    """


class IntrafiBalance(BaseModel):
    id: str
    """The identifier of this balance."""

    balances: List[Balance]
    """Each entry represents a balance held at a different bank.

    IntraFi separates the total balance across many participating banks in the
    network.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the account
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    effective_date: date
    """The date this balance reflects."""

    total_balance: int
    """The total balance, in minor units of `currency`.

    Increase reports this balance to IntraFi daily.
    """

    type: Literal["intrafi_balance"]
    """A constant representing the object's type.

    For this resource it will always be `intrafi_balance`.
    """
