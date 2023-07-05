# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletToken"]


class DigitalWalletToken(BaseModel):
    id: str
    """The Digital Wallet Token identifier."""

    card_id: str
    """The identifier for the Card this Digital Wallet Token belongs to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card was created.
    """

    status: Literal["active", "inactive", "suspended", "deactivated"]
    """This indicates if payments can be made with the Digital Wallet Token.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently cancelled.
    """

    token_requestor: Literal["apple_pay", "google_pay"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    """

    type: Literal["digital_wallet_token"]
    """A constant representing the object's type.

    For this resource it will always be `digital_wallet_token`.
    """
