# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    id: str
    """The Account identifier."""

    account_revenue_rate: Optional[str] = None
    """
    The account revenue rate currently being earned on the account, as a string
    containing a decimal number. For example, a 1% account revenue rate would be
    represented as "0.01". Account revenue is a type of non-interest income accrued
    on the account.
    """

    bank: Literal["core_bank", "first_internet_bank", "grasshopper_bank"]
    """The bank the Account is with.

    - `core_bank` - Core Bank
    - `first_internet_bank` - First Internet Bank of Indiana
    - `grasshopper_bank` - Grasshopper Bank
    """

    closed_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    was closed.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Account
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    entity_id: str
    """The identifier for the Entity the Account belongs to."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    informational_entity_id: Optional[str] = None
    """
    The identifier of an Entity that, while not owning the Account, is associated
    with its activity.
    """

    interest_accrued: str
    """
    The interest accrued but not yet paid, expressed as a string containing a
    floating-point value.
    """

    interest_accrued_at: Optional[date] = None
    """
    The latest [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which
    interest was accrued.
    """

    interest_rate: str
    """
    The interest rate currently being earned on the account, as a string containing
    a decimal number. For example, a 1% interest rate would be represented as
    "0.01".
    """

    name: str
    """The name you choose for the Account."""

    program_id: str
    """
    The identifier of the Program determining the compliance and commercial terms of
    this Account.
    """

    status: Literal["closed", "open"]
    """The status of the Account.

    - `closed` - Closed Accounts on which no new activity can occur.
    - `open` - Open Accounts that are ready to use.
    """

    type: Literal["account"]
    """A constant representing the object's type.

    For this resource it will always be `account`.
    """
