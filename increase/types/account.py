# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    balance: int
    """The current balance of the Account in the minor unit of the currency.

    For dollars, for example, this is cents.
    """

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    was created.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Account
    currency.
    """

    entity_id: Optional[str]
    """The identifier for the Entity the Account belongs to."""

    id: str
    """The Account identifier."""

    interest_accrued: str
    """
    The interest accrued but not yet paid, expressed as a string containing a
    floating-point value.
    """

    interest_accrued_at: Optional[str]
    """
    The latest [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which
    interest was accrued.
    """

    name: str
    """The name you choose for the Account."""

    status: Literal["open", "closed"]
    """The status of the Account."""

    type: Literal["account"]
    """A constant representing the object's type.

    For this resource it will always be `account`.
    """
