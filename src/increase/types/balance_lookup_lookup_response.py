# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BalanceLookupLookupResponse"]


class BalanceLookupLookupResponse(BaseModel):
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

    type: Literal["balance_lookup"]
    """A constant representing the object's type.

    For this resource it will always be `balance_lookup`.
    """
