# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Program"]


class Program(BaseModel):
    """Programs determine the compliance and commercial terms of Accounts.

    By default, you have a Commercial Banking program for managing your own funds. If you are lending or managing funds on behalf of your customers, or otherwise engaged in regulated activity, we will work together to create additional Programs for you.
    """

    id: str
    """The Program identifier."""

    bank: Literal["core_bank", "first_internet_bank", "grasshopper_bank"]
    """The Bank the Program is with.

    - `core_bank` - Core Bank
    - `first_internet_bank` - First Internet Bank of Indiana
    - `grasshopper_bank` - Grasshopper Bank
    """

    billing_account_id: Optional[str] = None
    """The Program billing account."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Program
    was created.
    """

    default_digital_card_profile_id: Optional[str] = None
    """The default configuration for digital cards attached to this Program."""

    interest_rate: str
    """
    The Interest Rate currently being earned on the accounts in this program, as a
    string containing a decimal number. For example, a 1% interest rate would be
    represented as "0.01".
    """

    name: str
    """The name of the Program."""

    type: Literal["program"]
    """A constant representing the object's type.

    For this resource it will always be `program`.
    """

    updated_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Program
    was last updated.
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
