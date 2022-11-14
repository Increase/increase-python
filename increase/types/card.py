# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field
from .._models import BaseModel

from ..types import shared

__all__ = ["BillingAddress", "DigitalWallet", "Card"]

class BillingAddress(BaseModel):
    city: Optional[str]
    """The city of the billing address."""

    line1: Optional[str]
    """The first line of the billing address."""

    line2: Optional[str]
    """The second line of the billing address."""

    postal_code: Optional[str]
    """The postal code of the billing address."""

    state: Optional[str]
    """The US state of the billing address."""

class DigitalWallet(BaseModel):
    email: Optional[str]
    """
    An email address that can be used to verify the cardholder via one-time passcode
    over email.
    """

    phone: Optional[str]
    """
    A phone number that can be used to verify the cardholder via one-time passcode
    over SMS.
    """

class Card(BaseModel):
    account_id: str
    """The identifier for the account this card belongs to."""

    billing_address: BillingAddress
    """The Card's billing address."""

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card was created.
    """

    description: Optional[str]
    """The card's description for display purposes."""

    digital_wallet: Optional[DigitalWallet]
    """
    The contact information used in the two-factor steps for digital wallet card
    creation. At least one field must be present to complete the digital wallet
    steps.
    """

    expiration_month: str
    """The month the card expires in MM format (e.g., August is 08)."""

    expiration_year: str
    """The year the card expires in YYYY format (e.g., 2025)."""

    id: str
    """The card identifier."""

    last4: str
    """The last 4 digits of the Card's Primary Account Number."""

    status: Optional[Literal["active", "disabled", "canceled"]]
    """This indicates if payments can be made with the card."""

    type: Literal["card"]
    """A constant representing the object's type.

    For this resource it will always be `card`.
    """