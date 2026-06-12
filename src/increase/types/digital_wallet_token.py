# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletToken", "Cardholder", "Decline", "Device", "DynamicPrimaryAccountNumber", "Update"]


class Cardholder(BaseModel):
    """The cardholder information given when the Digital Wallet Token was created."""

    name: Optional[str] = None
    """Name of the cardholder, for example "John Smith"."""


class Decline(BaseModel):
    """
    If the Digital Wallet Token was declined during provisioning, details about the decline.
    """

    reason: Literal[
        "card_not_active",
        "no_verification_method",
        "webhook_timed_out",
        "webhook_declined",
        "incorrect_card_verification_code",
        "declined_by_token_requestor",
    ]
    """The reason the token provisioning was declined.

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
    """


class Device(BaseModel):
    """The device that was used to create the Digital Wallet Token."""

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


class DynamicPrimaryAccountNumber(BaseModel):
    """The redacted Dynamic Primary Account Number."""

    first6: str
    """The first 6 digits of the token's Dynamic Primary Account Number."""

    last4: str
    """The last 4 digits of the token's Dynamic Primary Account Number."""


class Update(BaseModel):
    status: Literal["active", "inactive", "suspended", "deactivated", "declined"]
    """The status the update changed this Digital Wallet Token to.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
    - `declined` - The digital wallet token was declined during provisioning.
    """

    timestamp: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the update happened.
    """


class DigitalWalletToken(BaseModel):
    """
    A Digital Wallet Token is created when a user adds a Card to their Apple Pay or Google Pay app. The Digital Wallet Token can be used for purchases just like a Card.
    """

    id: str
    """The Digital Wallet Token identifier."""

    card_id: str
    """The identifier for the Card this Digital Wallet Token belongs to."""

    cardholder: Cardholder
    """The cardholder information given when the Digital Wallet Token was created."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Digital Wallet Token was created.
    """

    decline: Optional[Decline] = None
    """
    If the Digital Wallet Token was declined during provisioning, details about the
    decline.
    """

    device: Device
    """The device that was used to create the Digital Wallet Token."""

    dynamic_primary_account_number: Optional[DynamicPrimaryAccountNumber] = None
    """The redacted Dynamic Primary Account Number."""

    status: Literal["active", "inactive", "suspended", "deactivated", "declined"]
    """This indicates if payments can be made with the Digital Wallet Token.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
    - `declined` - The digital wallet token was declined during provisioning.
    """

    token_requestor: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    - `samsung_pay` - Samsung Pay
    - `unknown` - Unknown
    """

    type: Literal["digital_wallet_token"]
    """A constant representing the object's type.

    For this resource it will always be `digital_wallet_token`.
    """

    updates: List[Update]
    """Updates to the Digital Wallet Token."""
