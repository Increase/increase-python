# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookkeepingAccount"]


class BookkeepingAccount(BaseModel):
    account_id: Optional[str]
    """The API Account associated with this bookkeeping account."""

    compliance_category: Optional[Literal["commingled_cash", "customer_balance"]]
    """The compliance category of the account."""

    entity_id: Optional[str]
    """The Entity associated with this bookkeeping account."""

    id: str
    """The account identifier."""

    name: str
    """The name you choose for the account."""

    type: Literal["bookkeeping_account"]
    """A constant representing the object's type.

    For this resource it will always be `bookkeeping_account`.
    """
