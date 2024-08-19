# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DigitalWalletTokenRequestCreateParams"]


class DigitalWalletTokenRequestCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The identifier of the Card to be authorized."""
