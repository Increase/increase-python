# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletToken", "Update"]


class Update(BaseModel):
    status: Literal["active", "inactive", "suspended", "deactivated"]
    """The status the update changed this Digital Wallet Token to.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
    """

    timestamp: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the update happened.
    """


class DigitalWalletToken(BaseModel):
    id: str
    """The Digital Wallet Token identifier."""

    card_id: str
    """The identifier for the Card this Digital Wallet Token belongs to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Digital Wallet Token was created.
    """

    status: Literal["active", "inactive", "suspended", "deactivated"]
    """This indicates if payments can be made with the Digital Wallet Token.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
    """

    token_requestor: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    - `samsung_pay` - Samsung Pay
    - `unknown` - Unknown
    """

    type: Literal["digital_wallet_token"]
    """A constant representing the object's type.

    For this resource it will always be `digital_wallet_token`.
    """

    updates: List[Update]
    """Updates to the Digital Wallet Token."""
