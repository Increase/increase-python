# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DigitalWalletTokenRequestCreateResponse"]


class DigitalWalletTokenRequestCreateResponse(BaseModel):
    decline_reason: Optional[
        Literal["card_not_active", "no_verification_method", "webhook_timed_out", "webhook_declined"]
    ] = None
    """
    If the simulated tokenization attempt was declined, this field contains details
    as to why.

    - `card_not_active` - The card is not active.
    - `no_verification_method` - The card does not have a two-factor authentication
      method.
    - `webhook_timed_out` - Your webhook timed out when evaluating the token
      provisioning attempt.
    - `webhook_declined` - Your webhook declined the token provisioning attempt.
    """

    digital_wallet_token_id: Optional[str] = None
    """
    If the simulated tokenization attempt was accepted, this field contains the id
    of the Digital Wallet Token that was created.
    """

    type: Literal["inbound_digital_wallet_token_request_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_digital_wallet_token_request_simulation_result`.
    """
