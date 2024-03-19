# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookkeepingAccount"]


class BookkeepingAccount(BaseModel):
    id: str
    """The account identifier."""

    account_id: Optional[str] = None
    """The API Account associated with this bookkeeping account."""

    compliance_category: Optional[Literal["commingled_cash", "customer_balance"]] = None
    """The compliance category of the account.

    - `commingled_cash` - A cash in an commingled Increase Account.
    - `customer_balance` - A customer balance.
    """

    entity_id: Optional[str] = None
    """The Entity associated with this bookkeeping account."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    name: str
    """The name you choose for the account."""

    type: Literal["bookkeeping_account"]
    """A constant representing the object's type.

    For this resource it will always be `bookkeeping_account`.
    """
