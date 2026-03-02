# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardAuthenticationCreateParams"]


class CardAuthenticationCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The identifier of the Card to be authorized."""

    category: Literal["payment_authentication", "non_payment_authentication"]
    """The category of the card authentication attempt.

    - `payment_authentication` - The authentication attempt is for a payment.
    - `non_payment_authentication` - The authentication attempt is not for a
      payment.
    """

    device_channel: Literal["app", "browser", "three_ds_requestor_initiated"]
    """The device channel of the card authentication attempt.

    - `app` - The authentication attempt was made from an app.
    - `browser` - The authentication attempt was made from a browser.
    - `three_ds_requestor_initiated` - The authentication attempt was initiated by
      the 3DS Requestor.
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

    merchant_country: str
    """The country the merchant resides in."""

    merchant_name: str
    """The name of the merchant"""

    purchase_amount: int
    """The purchase amount in cents."""
