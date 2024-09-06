# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardAuthorizationExpirationCreateParams"]


class CardAuthorizationExpirationCreateParams(TypedDict, total=False):
    card_payment_id: Required[str]
    """The identifier of the Card Payment to expire."""
