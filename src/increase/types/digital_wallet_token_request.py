# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletTokenRequest", "Declined", "Device", "Provisioned"]


class Declined(BaseModel):
    """Details of the decline. Present if and only if `outcome` is `declined`."""

    reason: Literal[
        "card_not_active",
        "no_verification_method",
        "webhook_timed_out",
        "webhook_declined",
        "incorrect_card_verification_code",
        "declined_by_token_requestor",
        "group_locked",
        "account_closed",
        "entity_not_active",
    ]
    """The reason the tokenization was declined.

    - `card_not_active` - The card is not active.
    - `no_verification_method` - The card does not have a two-factor authentication
      method.
    - `webhook_timed_out` - Your webhook timed out when evaluating the token
      provisioning attempt.
    - `webhook_declined` - Your webhook declined the token provisioning attempt.
    - `incorrect_card_verification_code` - The tokenization attempt failed because
      the Card Verification Code (CVC) was incorrect.
    - `declined_by_token_requestor` - The tokenization attempt was declined by the
      token requestor.
    - `group_locked` - The group was locked.
    - `account_closed` - The account has been closed.
    - `entity_not_active` - The account's entity was not active.
    """


class Device(BaseModel):
    """The device that requested the tokenization."""

    device_type: Optional[
        Literal[
            "unknown",
            "mobile_phone",
            "tablet",
            "watch",
            "mobilephone_or_tablet",
            "pc",
            "household_device",
            "wearable_device",
            "automobile_device",
        ]
    ] = None
    """Device type.

    - `unknown` - Unknown
    - `mobile_phone` - Mobile Phone
    - `tablet` - Tablet
    - `watch` - Watch
    - `mobilephone_or_tablet` - Mobile Phone or Tablet
    - `pc` - PC
    - `household_device` - Household Device
    - `wearable_device` - Wearable Device
    - `automobile_device` - Automobile Device
    """

    identifier: Optional[str] = None
    """ID assigned to the device by the digital wallet provider."""

    ip_address: Optional[str] = None
    """IP address of the device."""

    name: Optional[str] = None
    """Name of the device, for example "My Work Phone"."""


class Provisioned(BaseModel):
    """Details of the provisioned Digital Wallet Token.

    Present if and only if `outcome` is `provisioned`.
    """

    digital_wallet_token_id: str
    """The identifier of the Digital Wallet Token that was provisioned."""


class DigitalWalletTokenRequest(BaseModel):
    """
    A Digital Wallet Token Request is created each time a digital wallet app, such as Apple Pay or Google Pay, requests to tokenize a Card.
    """

    id: str
    """The Digital Wallet Token Request identifier."""

    card_id: str
    """The identifier of the Card the tokenization was requested for."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Digital Wallet Token Request was created.
    """

    declined: Optional[Declined] = None
    """Details of the decline. Present if and only if `outcome` is `declined`."""

    device: Device
    """The device that requested the tokenization."""

    outcome: Literal["provisioned", "declined"]
    """The outcome of the tokenization request.

    - `provisioned` - The tokenization request was approved and a Digital Wallet
      Token was provisioned.
    - `declined` - The tokenization request was declined.
    """

    provisioned: Optional[Provisioned] = None
    """Details of the provisioned Digital Wallet Token.

    Present if and only if `outcome` is `provisioned`.
    """

    token_reference_identifier: str
    """The reference identifier assigned by the card network to the token."""

    token_requestor: Literal["apple_pay", "google_pay", "samsung_pay", "garmin_pay", "unknown"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    - `samsung_pay` - Samsung Pay
    - `garmin_pay` - Garmin Pay
    - `unknown` - Unknown
    """

    type: Literal["digital_wallet_token_request"]
    """A constant representing the object's type.

    For this resource it will always be `digital_wallet_token_request`.
    """
