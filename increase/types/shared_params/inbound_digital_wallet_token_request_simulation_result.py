# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List, Dict
from typing_extensions import Literal, TypedDict, Required, Annotated

from .._utils import PropertyInfo

__all__ = ["InboundDigitalWalletTokenRequestSimulationResult"]

class InboundDigitalWalletTokenRequestSimulationResult(TypedDict, total=False):
    decline_reason: Required[Optional[Literal["card_not_active", "no_verification_method", "webhook_timed_out", "webhook_declined"]]]
    """
    If the simulated tokenization attempt was declined, this field contains details
    as to why.
    """

    type: Required[Literal["inbound_digital_wallet_token_request_simulation_result"]]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_digital_wallet_token_request_simulation_result`.
    """