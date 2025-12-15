# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BalanceLookup"]


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

    type: Literal["balance_lookup"]
    """A constant representing the object's type.

    For this resource it will always be `balance_lookup`.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
