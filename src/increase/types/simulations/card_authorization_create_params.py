# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardAuthorizationCreateParams", "NetworkDetails", "NetworkDetailsVisa"]


class CardAuthorizationCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The authorization amount in cents."""

    authenticated_card_payment_id: str
    """
    The identifier of a Card Payment with a `card_authentication` if you want to
    simulate an authenticated authorization.
    """

    card_id: str
    """The identifier of the Card to be authorized."""

    decline_reason: Literal[
        "account_closed",
        "card_not_active",
        "card_canceled",
        "physical_card_not_active",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "cvv2_mismatch",
        "card_expiration_mismatch",
        "transaction_not_allowed",
        "breaches_limit",
        "webhook_declined",
        "webhook_timed_out",
        "declined_by_stand_in_processing",
        "invalid_physical_card",
        "missing_original_authorization",
        "suspected_fraud",
    ]
    """Forces a card decline with a specific reason.

    No real time decision will be sent.

    - `account_closed` - The account has been closed.
    - `card_not_active` - The Card was not active.
    - `card_canceled` - The Card has been canceled.
    - `physical_card_not_active` - The Physical Card was not active.
    - `entity_not_active` - The account's entity was not active.
    - `group_locked` - The account was inactive.
    - `insufficient_funds` - The Card's Account did not have a sufficient available
      balance.
    - `cvv2_mismatch` - The given CVV2 did not match the card's value.
    - `card_expiration_mismatch` - The given expiration date did not match the
      card's value. Only applies when a CVV2 is present.
    - `transaction_not_allowed` - The attempted card transaction is not allowed per
      Increase's terms.
    - `breaches_limit` - The transaction was blocked by a Limit.
    - `webhook_declined` - Your application declined the transaction via webhook.
    - `webhook_timed_out` - Your application webhook did not respond without the
      required timeout.
    - `declined_by_stand_in_processing` - Declined by stand-in processing.
    - `invalid_physical_card` - The card read had an invalid CVV, dCVV, or
      authorization request cryptogram.
    - `missing_original_authorization` - The original card authorization for this
      incremental authorization does not exist.
    - `suspected_fraud` - The transaction was suspected to be fraudulent. Please
      reach out to support@increase.com for more information.
    """

    digital_wallet_token_id: str
    """The identifier of the Digital Wallet Token to be authorized."""

    direction: Literal["settlement", "refund"]
    """
    The direction describes the direction the funds will move, either from the
    cardholder to the merchant or from the merchant to the cardholder.

    - `settlement` - A regular card authorization where funds are debited from the
      cardholder.
    - `refund` - A refund card authorization, sometimes referred to as a credit
      voucher authorization, where funds are credited to the cardholder.
    """

    event_subscription_id: str
    """The identifier of the Event Subscription to use.

    If provided, will override the default real time event subscription. Because you
    can only create one real time decision event subscription, you can use this
    field to route events to any specified event subscription for testing purposes.
    """

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

    merchant_city: str
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    merchant_state: str
    """The state the merchant resides in."""

    network_details: NetworkDetails
    """Fields specific to a given card network."""

    physical_card_id: str
    """The identifier of the Physical Card to be authorized."""

    terminal_id: str
    """
    The terminal identifier (commonly abbreviated as TID) of the terminal the card
    is transacting with.
    """


class NetworkDetailsVisa(TypedDict, total=False):
    stand_in_processing_reason: Literal[
        "issuer_error",
        "invalid_physical_card",
        "invalid_cardholder_authentication_verification_value",
        "internal_visa_error",
        "merchant_transaction_advisory_service_authentication_required",
        "payment_fraud_disruption_acquirer_block",
        "other",
    ]
    """The reason code for the stand-in processing.

    - `issuer_error` - Increase failed to process the authorization in a timely
      manner.
    - `invalid_physical_card` - The physical card read had an invalid CVV, dCVV, or
      authorization request cryptogram.
    - `invalid_cardholder_authentication_verification_value` - The 3DS cardholder
      authentication verification value was invalid.
    - `internal_visa_error` - An internal Visa error occurred. Visa uses this reason
      code for certain expected occurrences as well, such as Application Transaction
      Counter (ATC) replays.
    - `merchant_transaction_advisory_service_authentication_required` - The merchant
      has enabled Visa's Transaction Advisory Service and requires further
      authentication to perform the transaction. In practice this is often utilized
      at fuel pumps to tell the cardholder to see the cashier.
    - `payment_fraud_disruption_acquirer_block` - The transaction was blocked by
      Visa's Payment Fraud Disruption service due to fraudulent Acquirer behavior,
      such as card testing.
    - `other` - An unspecific reason for stand-in processing.
    """


class NetworkDetails(TypedDict, total=False):
    visa: Required[NetworkDetailsVisa]
    """Fields specific to the Visa network."""
