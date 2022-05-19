# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardAuthorizeParams"]


class CardAuthorizeParams(TypedDict, total=False):
    amount: Required[int]
    """The authorization amount in cents."""

    card_id: Required[str]
    """The identifier of the Card to be authorized."""
