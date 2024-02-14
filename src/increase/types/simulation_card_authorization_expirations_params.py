# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SimulationCardAuthorizationExpirationsParams"]


class SimulationCardAuthorizationExpirationsParams(TypedDict, total=False):
    card_payment_id: Required[str]
    """The identifier of the Card Payment to expire."""
