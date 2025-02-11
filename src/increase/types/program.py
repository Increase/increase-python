# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Program"]


class Program(BaseModel):
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
