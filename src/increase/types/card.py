# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Card",
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


class AuthorizationControlsMaximumAuthorizationCount(BaseModel):
    """Limits the number of authorizations that can be approved on this card."""

    all_time: Optional[int] = None
    """
    The maximum number of authorizations that can be approved on this card over its
    lifetime.
    """


class AuthorizationControlsMerchantAcceptorIdentifierAllowed(BaseModel):
    identifier: str
    """The Merchant Acceptor ID."""


class AuthorizationControlsMerchantAcceptorIdentifierBlocked(BaseModel):
    identifier: str
    """The Merchant Acceptor ID."""


class AuthorizationControlsMerchantAcceptorIdentifier(BaseModel):
    """
    Restricts which Merchant Acceptor IDs are allowed or blocked for authorizations on this card.
    """

    allowed: Optional[List[AuthorizationControlsMerchantAcceptorIdentifierAllowed]] = None
    """The Merchant Acceptor IDs that are allowed for authorizations on this card."""

    blocked: Optional[List[AuthorizationControlsMerchantAcceptorIdentifierBlocked]] = None
    """The Merchant Acceptor IDs that are blocked for authorizations on this card."""


class AuthorizationControlsMerchantCategoryCodeAllowed(BaseModel):
    code: str
    """The Merchant Category Code (MCC)."""


class AuthorizationControlsMerchantCategoryCodeBlocked(BaseModel):
    code: str
    """The Merchant Category Code (MCC)."""


class AuthorizationControlsMerchantCategoryCode(BaseModel):
    """
    Restricts which Merchant Category Codes are allowed or blocked for authorizations on this card.
    """

    allowed: Optional[List[AuthorizationControlsMerchantCategoryCodeAllowed]] = None
    """The Merchant Category Codes that are allowed for authorizations on this card."""

    blocked: Optional[List[AuthorizationControlsMerchantCategoryCodeBlocked]] = None
    """The Merchant Category Codes that are blocked for authorizations on this card."""


class AuthorizationControlsMerchantCountryAllowed(BaseModel):
    country: str
    """The ISO 3166-1 alpha-2 country code."""


class AuthorizationControlsMerchantCountryBlocked(BaseModel):
    country: str
    """The ISO 3166-1 alpha-2 country code."""


class AuthorizationControlsMerchantCountry(BaseModel):
    """
    Restricts which merchant countries are allowed or blocked for authorizations on this card.
    """

    allowed: Optional[List[AuthorizationControlsMerchantCountryAllowed]] = None
    """The merchant countries that are allowed for authorizations on this card."""

    blocked: Optional[List[AuthorizationControlsMerchantCountryBlocked]] = None
    """The merchant countries that are blocked for authorizations on this card."""


class AuthorizationControlsSpendingLimitMerchantCategoryCode(BaseModel):
    code: str
    """The Merchant Category Code (MCC)."""


class AuthorizationControlsSpendingLimit(BaseModel):
    interval: Literal["all_time", "per_transaction", "per_day", "per_week", "per_month"]
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

    merchant_category_codes: Optional[List[AuthorizationControlsSpendingLimitMerchantCategoryCode]] = None
    """The Merchant Category Codes (MCCs) this spending limit applies to.

    If not set, the limit applies to all transactions.
    """

    settlement_amount: int
    """The maximum settlement amount permitted in the given interval."""


class AuthorizationControls(BaseModel):
    """Controls that restrict how this card can be used."""

    maximum_authorization_count: Optional[AuthorizationControlsMaximumAuthorizationCount] = None
    """Limits the number of authorizations that can be approved on this card."""

    merchant_acceptor_identifier: Optional[AuthorizationControlsMerchantAcceptorIdentifier] = None
    """
    Restricts which Merchant Acceptor IDs are allowed or blocked for authorizations
    on this card.
    """

    merchant_category_code: Optional[AuthorizationControlsMerchantCategoryCode] = None
    """
    Restricts which Merchant Category Codes are allowed or blocked for
    authorizations on this card.
    """

    merchant_country: Optional[AuthorizationControlsMerchantCountry] = None
    """
    Restricts which merchant countries are allowed or blocked for authorizations on
    this card.
    """

    spending_limits: Optional[List[AuthorizationControlsSpendingLimit]] = None
    """Spending limits for this card.

    The most restrictive limit applies if multiple limits match.
    """


class BillingAddress(BaseModel):
    """The Card's billing address."""

    city: Optional[str] = None
    """The city of the billing address."""

    line1: Optional[str] = None
    """The first line of the billing address."""

    line2: Optional[str] = None
    """The second line of the billing address."""

    postal_code: Optional[str] = None
    """The postal code of the billing address."""

    state: Optional[str] = None
    """The US state of the billing address."""


class DigitalWallet(BaseModel):
    """
    The contact information used in the two-factor steps for digital wallet card creation. At least one field must be present to complete the digital wallet steps.
    """

    digital_card_profile_id: Optional[str] = None
    """The digital card profile assigned to this digital card.

    Card profiles may also be assigned at the program level.
    """

    email: Optional[str] = None
    """
    An email address that can be used to verify the cardholder via one-time passcode
    over email.
    """

    phone: Optional[str] = None
    """
    A phone number that can be used to verify the cardholder via one-time passcode
    over SMS.
    """


class Card(BaseModel):
    """Cards are commercial credit cards.

    They'll immediately work for online purchases after you create them. All cards maintain a credit limit of 100% of the Account’s available balance at the time of transaction. Funds are deducted from the Account upon transaction settlement.
    """

    id: str
    """The card identifier."""

    account_id: str
    """The identifier for the account this card belongs to."""

    authorization_controls: Optional[AuthorizationControls] = None
    """Controls that restrict how this card can be used."""

    billing_address: BillingAddress
    """The Card's billing address."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card was created.
    """

    description: Optional[str] = None
    """The card's description for display purposes."""

    digital_wallet: Optional[DigitalWallet] = None
    """
    The contact information used in the two-factor steps for digital wallet card
    creation. At least one field must be present to complete the digital wallet
    steps.
    """

    entity_id: Optional[str] = None
    """The identifier for the entity associated with this card."""

    expiration_month: int
    """The month the card expires in M format (e.g., August is 8)."""

    expiration_year: int
    """The year the card expires in YYYY format (e.g., 2025)."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    last4: str
    """The last 4 digits of the Card's Primary Account Number."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if payments can be made with the card.

    - `active` - The card is active.
    - `disabled` - The card is temporarily disabled.
    - `canceled` - The card is permanently canceled.
    """

    type: Literal["card"]
    """A constant representing the object's type.

    For this resource it will always be `card`.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
