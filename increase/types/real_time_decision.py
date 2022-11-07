# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardAuthorization", "DigitalWalletToken", "DigitalWalletAuthentication", "RealTimeDecision"]


class CardAuthorization(BaseModel):
    account_id: str
    """The identifier of the Account the authorization will debit."""

    card_id: str
    """The identifier of the Card that is being authorized."""

    decision: Optional[Literal["approve", "decline"]]
    """Whether or not the authorization was approved."""

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

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    presentment_amount: int
    """
    The amount of the attempted authorization in the currency the card user sees at
    the time of purchase, in the minor unit of that currency. For dollars, for
    example, this is cents.
    """

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    user sees at the time of purchase.
    """

    settlement_amount: int
    """The amount of the attempted authorization in the currency it will be settled in.

    This currency is the same as that of the Account the card belongs to.
    """

    settlement_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    transaction will be settled in.
    """


class DigitalWalletToken(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    decision: Optional[Literal["approve", "decline"]]
    """Whether or not the provisioning request was approved."""

    digital_wallet: Literal["apple_pay", "google_pay"]
    """The digital wallet app being used."""


class DigitalWalletAuthentication(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    channel: Literal["sms", "email"]
    """The channel to send the card user their one-time passcode."""

    digital_wallet: Literal["apple_pay", "google_pay"]
    """The digital wallet app being used."""

    email: Optional[str]
    """The email to send the one-time passcode to if `channel` is equal to `email`."""

    one_time_passcode: str
    """The one-time passcode to send the card user."""

    phone: Optional[str]
    """
    The phone number to send the one-time passcode to if `channel` is equal to
    `sms`.
    """

    result: Optional[Literal["success", "failure"]]
    """Whether your application successfully delivered the one-time passcode."""


class RealTimeDecision(BaseModel):
    card_authorization: Optional[CardAuthorization]
    """Fields related to a card authorization."""

    category: Literal[
        "card_authorization_requested", "digital_wallet_token_requested", "digital_wallet_authentication_requested"
    ]
    """The category of the Real-Time Decision."""

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Real-Time Decision was created.
    """

    digital_wallet_authentication: Optional[DigitalWalletAuthentication]
    """Fields related to a digital wallet authentication attempt."""

    digital_wallet_token: Optional[DigitalWalletToken]
    """Fields related to a digital wallet token provisioning attempt."""

    id: str
    """The Real-Time Decision identifier."""

    status: Literal["pending", "responded", "timed_out"]
    """The status of the Real-Time Decision."""

    timeout_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    your application can no longer respond to the Real-Time Decision.
    """

    type: Literal["real_time_decision"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_decision`.
    """
