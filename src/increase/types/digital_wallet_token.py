# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletToken", "Cardholder", "Device", "Update"]


class Cardholder(BaseModel):
    name: Optional[str] = None
    """Name of the cardholder, for example "John Smith"."""


class Device(BaseModel):
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


class Update(BaseModel):
    status: Literal["active", "inactive", "suspended", "deactivated"]
    """The status the update changed this Digital Wallet Token to.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
    """

    timestamp: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the update happened.
    """


class DigitalWalletToken(BaseModel):
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

    device: Device
    """The device that was used to create the Digital Wallet Token."""

    status: Literal["active", "inactive", "suspended", "deactivated"]
    """This indicates if payments can be made with the Digital Wallet Token.

    - `active` - The digital wallet token is active.
    - `inactive` - The digital wallet token has been created but not successfully
      activated via two-factor authentication yet.
    - `suspended` - The digital wallet token has been temporarily paused.
    - `deactivated` - The digital wallet token has been permanently canceled.
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
