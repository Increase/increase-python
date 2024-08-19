# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardFuelConfirmationCreateParams"]


class CardFuelConfirmationCreateParams(TypedDict, total=False):
    amount: Required[int]
    """
    The amount of the fuel_confirmation in minor units in the card authorization's
    currency.
    """

    card_payment_id: Required[str]
    """The identifier of the Card Payment to create a fuel_confirmation on."""
