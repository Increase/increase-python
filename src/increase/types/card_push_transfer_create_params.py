# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardPushTransferCreateParams"]


class CardPushTransferCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The transfer amount in USD cents. For Card Push transfers, must be positive."""

    business_application_identifier: Required[
        Literal[
            "account_to_account",
            "business_to_business",
            "money_transfer_bank_initiated",
            "non_card_bill_payment",
            "consumer_bill_payment",
            "card_bill_payment",
            "funds_disbursement",
            "funds_transfer",
            "loyalty_and_offers",
            "merchant_disbursement",
            "merchant_payment",
            "person_to_person",
            "top_up",
            "wallet_transfer",
        ]
    ]
    """
    The Business Application Identifier describes the type of transaction being
    performed. Your program must be approved for the specified Business Application
    Identifier in order to use it.

    - `account_to_account` - Account to Account
    - `business_to_business` - Business to Business
    - `money_transfer_bank_initiated` - Money Transfer Bank Initiated
    - `non_card_bill_payment` - Non-Card Bill Payment
    - `consumer_bill_payment` - Consumer Bill Payment
    - `card_bill_payment` - Card Bill Payment
    - `funds_disbursement` - Funds Disbursement
    - `funds_transfer` - Funds Transfer
    - `loyalty_and_offers` - Loyalty and Offers
    - `merchant_disbursement` - Merchant Disbursement
    - `merchant_payment` - Merchant Payment
    - `person_to_person` - Person to Person
    - `top_up` - Top Up
    - `wallet_transfer` - Wallet Transfer
    """

    card_token_id: Required[str]
    """
    The Increase identifier for the Card Token that represents the card number
    you're pushing funds to.
    """

    merchant_category_code: Required[str]
    """
    The merchant category code (MCC) of the merchant (generally your business)
    sending the transfer. This is a four-digit code that describes the type of
    business or service provided by the merchant. Your program must be approved for
    the specified MCC in order to use it.
    """

    merchant_city_name: Required[str]
    """The city name of the merchant (generally your business) sending the transfer."""

    merchant_name: Required[str]
    """The merchant name shows up as the statement descriptor for the transfer.

    This is typically the name of your business or organization.
    """

    merchant_name_prefix: Required[str]
    """
    For certain Business Application Identifiers, the statement descriptor is
    `merchant_name_prefix*sender_name`, where the `merchant_name_prefix` is a one to
    four character prefix that identifies the merchant.
    """

    merchant_postal_code: Required[str]
    """The postal code of the merchant (generally your business) sending the transfer."""

    merchant_state: Required[str]
    """The state of the merchant (generally your business) sending the transfer."""

    recipient_name: Required[str]
    """The name of the funds recipient."""

    sender_address_city: Required[str]
    """The city of the sender."""

    sender_address_line1: Required[str]
    """The address line 1 of the sender."""

    sender_address_postal_code: Required[str]
    """The postal code of the sender."""

    sender_address_state: Required[str]
    """The state of the sender."""

    sender_name: Required[str]
    """The name of the funds originator."""

    source_account_number_id: Required[str]
    """The identifier of the Account Number from which to send the transfer."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""
