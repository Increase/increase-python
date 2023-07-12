# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InboundFundsHoldReleaseResponse"]


class InboundFundsHoldReleaseResponse(BaseModel):
    amount: int
    """The held amount in the minor unit of the account's currency.

    For dollars, for example, this is cents.
    """

    automatically_releases_at: datetime
    """When the hold will be released automatically.

    Certain conditions may cause it to be released before this time.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the hold
    was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the hold's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    held_transaction_id: Optional[str]
    """The ID of the Transaction for which funds were held."""

    pending_transaction_id: Optional[str]
    """The ID of the Pending Transaction representing the held funds."""

    released_at: Optional[datetime]
    """When the hold was released (if it has been released)."""

    status: Literal["held", "complete"]
    """The status of the hold.

    - `held` - Funds are still being held.
    - `complete` - Funds have been released.
    """

    type: Literal["inbound_funds_hold"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_funds_hold`.
    """
