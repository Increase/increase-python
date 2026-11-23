# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "DigitalWalletTokenRequest",
    "Cardholder",
    "Declined",
    "Device",
    "Provisioned",
    "TokenRequestorDetails",
    "Verification",
    "VerificationCardholderAddress",
    "Visa",
    "Wallet",
]


class Cardholder(BaseModel):
    """The cardholder adding the card to the digital wallet."""

    name: Optional[str] = None
    """The cardholder's name, as entered in the digital wallet."""


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
        "card_expiration_mismatch",
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
    - `card_expiration_mismatch` - The given expiration date did not match the
      card's value.
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


class TokenRequestorDetails(BaseModel):
    """The digital wallet or merchant that requested the token."""

    identifier: str
    """The identifier assigned to the token requestor by the card network."""

    name: Optional[str] = None
    """The name of the token requestor, for example "Apple Inc."."""


class VerificationCardholderAddress(BaseModel):
    """
    Cardholder address provided in the provisioning request and the address on file we verified it against.
    """

    actual_line1: Optional[str] = None
    """Line 1 of the address on file for the cardholder."""

    actual_postal_code: Optional[str] = None
    """The postal code of the address on file for the cardholder."""

    provided_line1: Optional[str] = None
    """
    The cardholder address line 1 provided for verification in the provisioning
    request.
    """

    provided_postal_code: Optional[str] = None
    """The postal code provided for verification in the provisioning request."""

    result: Literal[
        "not_checked",
        "postal_code_match_address_no_match",
        "postal_code_no_match_address_match",
        "match",
        "no_match",
        "postal_code_match_address_not_checked",
    ]
    """The address verification result.

    - `not_checked` - No address information was provided in the authorization
      request.
    - `postal_code_match_address_no_match` - Postal code matches, but the street
      address does not match or was not provided.
    - `postal_code_no_match_address_match` - Postal code does not match, but the
      street address matches or was not provided.
    - `match` - Postal code and street address match.
    - `no_match` - Postal code and street address do not match.
    - `postal_code_match_address_not_checked` - Postal code matches, but the street
      address was not verified. (deprecated)
    """


class Verification(BaseModel):
    """Fields related to verification of cardholder-provided values."""

    cardholder_address: VerificationCardholderAddress
    """
    Cardholder address provided in the provisioning request and the address on file
    we verified it against.
    """


class Visa(BaseModel):
    """Risk scores provided by Visa for the provisioning request.

    This field will be present in the JSON response if and only if `network` is equal to `visa`.
    """

    network_risk_score: Optional[int] = None
    """Visa's risk score for the card, based on its transaction history, from 0 to 99.

    A higher score indicates a higher risk.
    """

    provisioning_risk_score: Optional[int] = None
    """Visa's risk score for the provisioning request, from 1 to 99.

    A higher score indicates a higher risk.
    """


class Wallet(BaseModel):
    """Details about the digital wallet."""

    account_email_age_days: Optional[int] = None
    """
    The number of days since the email address was added to the cardholder's digital
    wallet account, up to 999.
    """

    account_identifier: Optional[str] = None
    """An identifier for the cardholder's account with the digital wallet."""

    account_score: Optional[int] = None
    """How much the digital wallet trusts the cardholder's account, from 1 to 5.

    A higher score indicates more trust.
    """

    device_score: Optional[int] = None
    """
    How much the digital wallet trusts the device the card is being added to, from 1
    to 5. A higher score indicates more trust.
    """

    email_hash: Optional[str] = None
    """A hash of the email address on the cardholder's digital wallet account."""


class DigitalWalletTokenRequest(BaseModel):
    """
    A Digital Wallet Token Request is created each time a digital wallet app, such as Apple Pay or Google Pay, requests to tokenize a Card.
    """

    id: str
    """The Digital Wallet Token Request identifier."""

    card_id: str
    """The identifier of the Card the tokenization was requested for."""

    cardholder: Cardholder
    """The cardholder adding the card to the digital wallet."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Digital Wallet Token Request was created.
    """

    declined: Optional[Declined] = None
    """Details of the decline. Present if and only if `outcome` is `declined`."""

    device: Device
    """The device that requested the tokenization."""

    network: Literal["visa"]
    """The card network the token is being provisioned on.

    - `visa` - Visa
    """

    outcome: Literal["provisioned", "declined"]
    """The outcome of the tokenization request.

    - `provisioned` - The tokenization request was approved and a Digital Wallet
      Token was provisioned.
    - `declined` - The tokenization request was declined.
    """

    primary_account_number_source: Optional[
        Literal["key_entered", "on_file", "mobile_app", "token", "chip_dip", "contactless_tap"]
    ] = None
    """How the card number was provided to the digital wallet.

    - `key_entered` - The cardholder entered the card number manually.
    - `on_file` - The card number was already on file with the token requestor.
    - `mobile_app` - The card was added from your mobile app using push
      provisioning.
    - `token` - The card number was sourced from an existing token.
    - `chip_dip` - The card number was read from the chip of the physical card.
    - `contactless_tap` - The card number was read by tapping the physical card on
      the device.
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

    token_requestor_details: TokenRequestorDetails
    """The digital wallet or merchant that requested the token."""

    type: Literal["digital_wallet_token_request"]
    """A constant representing the object's type.

    For this resource it will always be `digital_wallet_token_request`.
    """

    verification: Verification
    """Fields related to verification of cardholder-provided values."""

    visa: Optional[Visa] = None
    """Risk scores provided by Visa for the provisioning request.

    This field will be present in the JSON response if and only if `network` is
    equal to `visa`.
    """

    wallet: Wallet
    """Details about the digital wallet."""
