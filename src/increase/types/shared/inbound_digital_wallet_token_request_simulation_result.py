# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InboundDigitalWalletTokenRequestSimulationResult"]


class InboundDigitalWalletTokenRequestSimulationResult(BaseModel):
    decline_reason: Optional[
        Literal["card_not_active", "no_verification_method", "webhook_timed_out", "webhook_declined"]
    ]
    """
    If the simulated tokenization attempt was declined, this field contains details
    as to why.
    """

    type: Literal["inbound_digital_wallet_token_request_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_digital_wallet_token_request_simulation_result`.
    """
