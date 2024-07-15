# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardIncrementCreateParams"]


class CardIncrementCreateParams(TypedDict, total=False):
    amount: Required[int]
    """
    The amount of the increment in minor units in the card authorization's currency.
    """

    card_payment_id: Required[str]
    """The identifier of the Card Payment to create a increment on."""

    event_subscription_id: str
    """The identifier of the Event Subscription to use.

    If provided, will override the default real time event subscription. Because you
    can only create one real time decision event subscription, you can use this
    field to route events to any specified event subscription for testing purposes.
    """
