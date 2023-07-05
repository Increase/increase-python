# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountNumber"]


class AccountNumber(BaseModel):
    id: str
    """The Account Number identifier."""

    account_id: str
    """The identifier for the account this Account Number belongs to."""

    account_number: str
    """The account number."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    Number was created.
    """

    name: str
    """The name you choose for the Account Number."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if payments can be made to the Account Number.

    - `active` - The account number is active.
    - `disabled` - The account number is temporarily disabled.
    - `canceled` - The account number is permanently disabled.
    """

    type: Literal["account_number"]
    """A constant representing the object's type.

    For this resource it will always be `account_number`.
    """
