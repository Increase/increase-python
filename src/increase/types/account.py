# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Account
    currency.
    """

    entity_id: Optional[str]
    """The identifier for the Entity the Account belongs to."""

    id: str
    """The Account identifier."""

    informational_entity_id: Optional[str]
    """
    The identifier of an Entity that, while not owning the Account, is associated
    with its activity.
    """

    interest_accrued: str
    """
    The interest accrued but not yet paid, expressed as a string containing a
    floating-point value.
    """

    interest_accrued_at: Optional[date]
    """
    The latest [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which
    interest was accrued.
    """

    interest_rate: str
    """
    The Interest Rate currently being earned on the account, as a string containing
    a decimal number. For example, a 1% interest rate would be represented as
    "0.01".
    """

    name: str
    """The name you choose for the Account."""

    status: Literal["open", "closed"]
    """The status of the Account."""

    type: Literal["account"]
    """A constant representing the object's type.

    For this resource it will always be `account`.
    """
