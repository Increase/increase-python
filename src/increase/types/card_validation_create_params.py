# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardValidationCreateParams"]


class CardValidationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account from which to send the validation."""

    card_token_id: Required[str]
    """
    The Increase identifier for the Card Token that represents the card number
    you're validating.
    """

    merchant_category_code: Required[str]
    """
    A four-digit code (MCC) identifying the type of business or service provided by
    the merchant.
    """

    merchant_city_name: Required[str]
    """The city where the merchant (typically your business) is located."""

    merchant_name: Required[str]
    """The merchant name that will appear in the cardholder’s statement descriptor.

    Typically your business name.
    """

    merchant_postal_code: Required[str]
    """The postal code for the merchant’s (typically your business’s) location."""

    merchant_state: Required[str]
    """The U.S. state where the merchant (typically your business) is located."""

    cardholder_first_name: str
    """The cardholder's first name."""

    cardholder_last_name: str
    """The cardholder's last name."""

    cardholder_middle_name: str
    """The cardholder's middle name."""

    cardholder_postal_code: str
    """The postal code of the cardholder's address."""

    cardholder_street_address: str
    """The cardholder's street address."""
