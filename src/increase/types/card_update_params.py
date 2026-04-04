# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CardUpdateParams",
    "AuthorizationControls",
    "AuthorizationControlsMaximumAuthorizationCount",
    "AuthorizationControlsMerchantAcceptorIdentifier",
    "AuthorizationControlsMerchantAcceptorIdentifierAllowed",
    "AuthorizationControlsMerchantAcceptorIdentifierBlocked",
    "AuthorizationControlsMerchantCategoryCode",
    "AuthorizationControlsMerchantCategoryCodeAllowed",
    "AuthorizationControlsMerchantCategoryCodeBlocked",
    "AuthorizationControlsMerchantCountry",
    "AuthorizationControlsMerchantCountryAllowed",
    "AuthorizationControlsMerchantCountryBlocked",
    "AuthorizationControlsSpendingLimit",
    "AuthorizationControlsSpendingLimitMerchantCategoryCode",
    "BillingAddress",
    "DigitalWallet",
]


class CardUpdateParams(TypedDict, total=False):
    authorization_controls: AuthorizationControls
    """Controls that restrict how this card can be used."""

    billing_address: BillingAddress
    """The card's updated billing address."""

    description: str
    """The description you choose to give the card."""

    digital_wallet: DigitalWallet
    """
    The contact information used in the two-factor steps for digital wallet card
    creation. At least one field must be present to complete the digital wallet
    steps.
    """

    entity_id: str
    """The Entity the card belongs to.

    You only need to supply this in rare situations when the card is not for the
    Account holder.
    """

    status: Literal["active", "disabled", "canceled"]
    """The status to update the Card with.

    - `active` - The card is active.
    - `disabled` - The card is temporarily disabled.
    - `canceled` - The card is permanently canceled.
    """


class AuthorizationControlsMaximumAuthorizationCount(TypedDict, total=False):
    """Limits the number of authorizations that can be approved on this card."""

    all_time: Required[int]
    """
    The maximum number of authorizations that can be approved on this card over its
    lifetime.
    """


class AuthorizationControlsMerchantAcceptorIdentifierAllowed(TypedDict, total=False):
    identifier: Required[str]
    """The Merchant Acceptor ID."""


class AuthorizationControlsMerchantAcceptorIdentifierBlocked(TypedDict, total=False):
    identifier: Required[str]
    """The Merchant Acceptor ID."""


class AuthorizationControlsMerchantAcceptorIdentifier(TypedDict, total=False):
    """
    Restricts which Merchant Acceptor IDs are allowed or blocked for authorizations on this card.
    """

    allowed: Iterable[AuthorizationControlsMerchantAcceptorIdentifierAllowed]
    """The Merchant Acceptor IDs that are allowed for authorizations on this card.

    Authorizations with Merchant Acceptor IDs not in this list will be declined.
    """

    blocked: Iterable[AuthorizationControlsMerchantAcceptorIdentifierBlocked]
    """The Merchant Acceptor IDs that are blocked for authorizations on this card.

    Authorizations with Merchant Acceptor IDs in this list will be declined.
    """


class AuthorizationControlsMerchantCategoryCodeAllowed(TypedDict, total=False):
    code: Required[str]
    """The Merchant Category Code."""


class AuthorizationControlsMerchantCategoryCodeBlocked(TypedDict, total=False):
    code: Required[str]
    """The Merchant Category Code."""


class AuthorizationControlsMerchantCategoryCode(TypedDict, total=False):
    """
    Restricts which Merchant Category Codes are allowed or blocked for authorizations on this card.
    """

    allowed: Iterable[AuthorizationControlsMerchantCategoryCodeAllowed]
    """The Merchant Category Codes that are allowed for authorizations on this card.

    Authorizations with Merchant Category Codes not in this list will be declined.
    """

    blocked: Iterable[AuthorizationControlsMerchantCategoryCodeBlocked]
    """The Merchant Category Codes that are blocked for authorizations on this card.

    Authorizations with Merchant Category Codes in this list will be declined.
    """


class AuthorizationControlsMerchantCountryAllowed(TypedDict, total=False):
    country: Required[str]
    """The ISO 3166-1 alpha-2 country code."""


class AuthorizationControlsMerchantCountryBlocked(TypedDict, total=False):
    country: Required[str]
    """The ISO 3166-1 alpha-2 country code."""


class AuthorizationControlsMerchantCountry(TypedDict, total=False):
    """
    Restricts which merchant countries are allowed or blocked for authorizations on this card.
    """

    allowed: Iterable[AuthorizationControlsMerchantCountryAllowed]
    """The merchant countries that are allowed for authorizations on this card.

    Authorizations with merchant countries not in this list will be declined.
    """

    blocked: Iterable[AuthorizationControlsMerchantCountryBlocked]
    """The merchant countries that are blocked for authorizations on this card.

    Authorizations with merchant countries in this list will be declined.
    """


class AuthorizationControlsSpendingLimitMerchantCategoryCode(TypedDict, total=False):
    code: Required[str]
    """The Merchant Category Code."""


class AuthorizationControlsSpendingLimit(TypedDict, total=False):
    interval: Required[Literal["all_time", "per_transaction", "per_day", "per_week", "per_month"]]
    """The interval at which the spending limit is enforced.

    - `all_time` - The spending limit applies over the lifetime of the card.
    - `per_transaction` - The spending limit applies per transaction.
    - `per_day` - The spending limit applies per day. Resets nightly at midnight
      UTC.
    - `per_week` - The spending limit applies per week. Resets weekly on Mondays at
      midnight UTC.
    - `per_month` - The spending limit applies per month. Resets on the first of the
      month, midnight UTC.
    """

    settlement_amount: Required[int]
    """The maximum settlement amount permitted in the given interval."""

    merchant_category_codes: Iterable[AuthorizationControlsSpendingLimitMerchantCategoryCode]
    """The Merchant Category Codes this spending limit applies to.

    If not set, the limit applies to all transactions.
    """


class AuthorizationControls(TypedDict, total=False):
    """Controls that restrict how this card can be used."""

    maximum_authorization_count: AuthorizationControlsMaximumAuthorizationCount
    """Limits the number of authorizations that can be approved on this card."""

    merchant_acceptor_identifier: AuthorizationControlsMerchantAcceptorIdentifier
    """
    Restricts which Merchant Acceptor IDs are allowed or blocked for authorizations
    on this card.
    """

    merchant_category_code: AuthorizationControlsMerchantCategoryCode
    """
    Restricts which Merchant Category Codes are allowed or blocked for
    authorizations on this card.
    """

    merchant_country: AuthorizationControlsMerchantCountry
    """
    Restricts which merchant countries are allowed or blocked for authorizations on
    this card.
    """

    spending_limits: Iterable[AuthorizationControlsSpendingLimit]
    """Spending limits for this card.

    The most restrictive limit applies if multiple limits match.
    """


class BillingAddress(TypedDict, total=False):
    """The card's updated billing address."""

    city: Required[str]
    """The city of the billing address."""

    line1: Required[str]
    """The first line of the billing address."""

    postal_code: Required[str]
    """The postal code of the billing address."""

    state: Required[str]
    """The US state of the billing address."""

    line2: str
    """The second line of the billing address."""


class DigitalWallet(TypedDict, total=False):
    """
    The contact information used in the two-factor steps for digital wallet card creation. At least one field must be present to complete the digital wallet steps.
    """

    digital_card_profile_id: str
    """The digital card profile assigned to this digital card."""

    email: str
    """
    An email address that can be used to verify the cardholder via one-time passcode
    over email.
    """

    phone: str
    """
    A phone number that can be used to verify the cardholder via one-time passcode
    over SMS.
    """
