# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardAuthorizeParams"]


class CardAuthorizeParams(TypedDict, total=False):
    amount: Required[int]
    """The authorization amount in cents."""

    card_id: str
    """The identifier of the Card to be authorized."""

    digital_wallet_token_id: str
    """The identifier of the Digital Wallet Token to be authorized."""

    event_subscription_id: str
    """The identifier of the Event Subscription to use.

    If provided, will override the default real time event subscription. Because you
    can only create one real time decision event subscription, you can use this
    field to route events to any specified event subscription for testing purposes.
    """

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: str
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: str
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    physical_card_id: str
    """The identifier of the Physical Card to be authorized."""
