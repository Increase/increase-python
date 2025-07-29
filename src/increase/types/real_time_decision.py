# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RealTimeDecision",
    "CardAuthentication",
    "CardAuthenticationChallenge",
    "CardAuthorization",
    "CardAuthorizationAdditionalAmounts",
    "CardAuthorizationAdditionalAmountsClinic",
    "CardAuthorizationAdditionalAmountsDental",
    "CardAuthorizationAdditionalAmountsPrescription",
    "CardAuthorizationAdditionalAmountsSurcharge",
    "CardAuthorizationAdditionalAmountsTotalCumulative",
    "CardAuthorizationAdditionalAmountsTotalHealthcare",
    "CardAuthorizationAdditionalAmountsTransit",
    "CardAuthorizationAdditionalAmountsUnknown",
    "CardAuthorizationAdditionalAmountsVision",
    "CardAuthorizationNetworkDetails",
    "CardAuthorizationNetworkDetailsVisa",
    "CardAuthorizationNetworkIdentifiers",
    "CardAuthorizationRequestDetails",
    "CardAuthorizationRequestDetailsIncrementalAuthorization",
    "CardAuthorizationVerification",
    "CardAuthorizationVerificationCardVerificationCode",
    "CardAuthorizationVerificationCardholderAddress",
    "DigitalWalletAuthentication",
    "DigitalWalletToken",
    "DigitalWalletTokenDevice",
]


class CardAuthentication(BaseModel):
    account_id: str
    """The identifier of the Account the card belongs to."""

    card_id: str
    """The identifier of the Card that is being tokenized."""

    decision: Optional[Literal["approve", "challenge", "deny"]] = None
    """Whether or not the authentication attempt was approved.

    - `approve` - Approve the authentication attempt without triggering a challenge.
    - `challenge` - Request further validation before approving the authentication
      attempt.
    - `deny` - Deny the authentication attempt.
    """

    upcoming_card_payment_id: str
    """The identifier of the Card Payment this authentication attempt will belong to.

    Available in the API once the card authentication has completed.
    """


class CardAuthenticationChallenge(BaseModel):
    account_id: str
    """The identifier of the Account the card belongs to."""

    card_id: str
    """The identifier of the Card that is being tokenized."""

    card_payment_id: str
    """
    The identifier of the Card Payment this authentication challenge attempt belongs
    to.
    """

    one_time_code: str
    """The one-time code delivered to the cardholder."""

    result: Optional[Literal["success", "failure"]] = None
    """Whether or not the challenge was delivered to the cardholder.

    - `success` - Your application successfully delivered the one-time code to the
      cardholder.
    - `failure` - Your application was unable to deliver the one-time code to the
      cardholder.
    """


class CardAuthorizationAdditionalAmountsClinic(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsDental(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsPrescription(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsSurcharge(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsTotalCumulative(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsTotalHealthcare(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsTransit(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsUnknown(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmountsVision(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class CardAuthorizationAdditionalAmounts(BaseModel):
    clinic: Optional[CardAuthorizationAdditionalAmountsClinic] = None
    """The part of this transaction amount that was for clinic-related services."""

    dental: Optional[CardAuthorizationAdditionalAmountsDental] = None
    """The part of this transaction amount that was for dental-related services."""

    prescription: Optional[CardAuthorizationAdditionalAmountsPrescription] = None
    """The part of this transaction amount that was for healthcare prescriptions."""

    surcharge: Optional[CardAuthorizationAdditionalAmountsSurcharge] = None
    """The surcharge amount charged for this transaction by the merchant."""

    total_cumulative: Optional[CardAuthorizationAdditionalAmountsTotalCumulative] = None
    """
    The total amount of a series of incremental authorizations, optionally provided.
    """

    total_healthcare: Optional[CardAuthorizationAdditionalAmountsTotalHealthcare] = None
    """The total amount of healthcare-related additional amounts."""

    transit: Optional[CardAuthorizationAdditionalAmountsTransit] = None
    """The part of this transaction amount that was for transit-related services."""

    unknown: Optional[CardAuthorizationAdditionalAmountsUnknown] = None
    """An unknown additional amount."""

    vision: Optional[CardAuthorizationAdditionalAmountsVision] = None
    """The part of this transaction amount that was for vision-related services."""


class CardAuthorizationNetworkDetailsVisa(BaseModel):
    electronic_commerce_indicator: Optional[
        Literal[
            "mail_phone_order",
            "recurring",
            "installment",
            "unknown_mail_phone_order",
            "secure_electronic_commerce",
            "non_authenticated_security_transaction_at_3ds_capable_merchant",
            "non_authenticated_security_transaction",
            "non_secure_transaction",
        ]
    ] = None
    """
    For electronic commerce transactions, this identifies the level of security used
    in obtaining the customer's payment credential. For mail or telephone order
    transactions, identifies the type of mail or telephone order.

    - `mail_phone_order` - Single transaction of a mail/phone order: Use to indicate
      that the transaction is a mail/phone order purchase, not a recurring
      transaction or installment payment. For domestic transactions in the US
      region, this value may also indicate one bill payment transaction in the
      card-present or card-absent environments.
    - `recurring` - Recurring transaction: Payment indicator used to indicate a
      recurring transaction that originates from an acquirer in the US region.
    - `installment` - Installment payment: Payment indicator used to indicate one
      purchase of goods or services that is billed to the account in multiple
      charges over a period of time agreed upon by the cardholder and merchant from
      transactions that originate from an acquirer in the US region.
    - `unknown_mail_phone_order` - Unknown classification: other mail order: Use to
      indicate that the type of mail/telephone order is unknown.
    - `secure_electronic_commerce` - Secure electronic commerce transaction: Use to
      indicate that the electronic commerce transaction has been authenticated using
      e.g., 3-D Secure
    - `non_authenticated_security_transaction_at_3ds_capable_merchant` -
      Non-authenticated security transaction at a 3-D Secure-capable merchant, and
      merchant attempted to authenticate the cardholder using 3-D Secure: Use to
      identify an electronic commerce transaction where the merchant attempted to
      authenticate the cardholder using 3-D Secure, but was unable to complete the
      authentication because the issuer or cardholder does not participate in the
      3-D Secure program.
    - `non_authenticated_security_transaction` - Non-authenticated security
      transaction: Use to identify an electronic commerce transaction that uses data
      encryption for security however , cardholder authentication is not performed
      using 3-D Secure.
    - `non_secure_transaction` - Non-secure transaction: Use to identify an
      electronic commerce transaction that has no data protection.
    """

    point_of_service_entry_mode: Optional[
        Literal[
            "unknown",
            "manual",
            "magnetic_stripe_no_cvv",
            "optical_code",
            "integrated_circuit_card",
            "contactless",
            "credential_on_file",
            "magnetic_stripe",
            "contactless_magnetic_stripe",
            "integrated_circuit_card_no_cvv",
        ]
    ] = None
    """
    The method used to enter the cardholder's primary account number and card
    expiration date.

    - `unknown` - Unknown
    - `manual` - Manual key entry
    - `magnetic_stripe_no_cvv` - Magnetic stripe read, without card verification
      value
    - `optical_code` - Optical code
    - `integrated_circuit_card` - Contact chip card
    - `contactless` - Contactless read of chip card
    - `credential_on_file` - Transaction initiated using a credential that has
      previously been stored on file
    - `magnetic_stripe` - Magnetic stripe read
    - `contactless_magnetic_stripe` - Contactless read of magnetic stripe data
    - `integrated_circuit_card_no_cvv` - Contact chip card, without card
      verification value
    """

    stand_in_processing_reason: Optional[
        Literal[
            "issuer_error",
            "invalid_physical_card",
            "invalid_cardholder_authentication_verification_value",
            "internal_visa_error",
            "merchant_transaction_advisory_service_authentication_required",
            "payment_fraud_disruption_acquirer_block",
            "other",
        ]
    ] = None
    """Only present when `actioner: network`.

    Describes why a card authorization was approved or declined by Visa through
    stand-in processing.

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


class CardAuthorizationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[CardAuthorizationNetworkDetailsVisa] = None
    """Fields specific to the `visa` network."""


class CardAuthorizationNetworkIdentifiers(BaseModel):
    retrieval_reference_number: Optional[str] = None
    """A life-cycle identifier used across e.g., an authorization and a reversal.

    Expected to be unique per acquirer within a window of time. For some card
    networks the retrieval reference number includes the trace counter.
    """

    trace_number: Optional[str] = None
    """A counter used to verify an individual authorization.

    Expected to be unique per acquirer within a window of time.
    """

    transaction_id: Optional[str] = None
    """
    A globally unique transaction identifier provided by the card network, used
    across multiple life-cycle requests.
    """


class CardAuthorizationRequestDetailsIncrementalAuthorization(BaseModel):
    card_payment_id: str
    """The card payment for this authorization and increment."""

    original_card_authorization_id: str
    """
    The identifier of the card authorization this request is attempting to
    increment.
    """


class CardAuthorizationRequestDetails(BaseModel):
    category: Literal["initial_authorization", "incremental_authorization"]
    """
    The type of this request (e.g., an initial authorization or an incremental
    authorization).

    - `initial_authorization` - A regular, standalone authorization.
    - `incremental_authorization` - An incremental request to increase the amount of
      an existing authorization.
    """

    incremental_authorization: Optional[CardAuthorizationRequestDetailsIncrementalAuthorization] = None
    """Fields specific to the category `incremental_authorization`."""

    initial_authorization: Optional[object] = None
    """Fields specific to the category `initial_authorization`."""


class CardAuthorizationVerificationCardVerificationCode(BaseModel):
    result: Literal["not_checked", "match", "no_match"]
    """The result of verifying the Card Verification Code.

    - `not_checked` - No card verification code was provided in the authorization
      request.
    - `match` - The card verification code matched the one on file.
    - `no_match` - The card verification code did not match the one on file.
    """


class CardAuthorizationVerificationCardholderAddress(BaseModel):
    actual_line1: Optional[str] = None
    """Line 1 of the address on file for the cardholder."""

    actual_postal_code: Optional[str] = None
    """The postal code of the address on file for the cardholder."""

    provided_line1: Optional[str] = None
    """
    The cardholder address line 1 provided for verification in the authorization
    request.
    """

    provided_postal_code: Optional[str] = None
    """The postal code provided for verification in the authorization request."""

    result: Literal[
        "not_checked",
        "postal_code_match_address_not_checked",
        "postal_code_match_address_no_match",
        "postal_code_no_match_address_match",
        "match",
        "no_match",
    ]
    """The address verification result returned to the card network.

    - `not_checked` - No address was provided in the authorization request.
    - `postal_code_match_address_not_checked` - Postal code matches, but the street
      address was not verified.
    - `postal_code_match_address_no_match` - Postal code matches, but the street
      address does not match.
    - `postal_code_no_match_address_match` - Postal code does not match, but the
      street address matches.
    - `match` - Postal code and street address match.
    - `no_match` - Postal code and street address do not match.
    """


class CardAuthorizationVerification(BaseModel):
    card_verification_code: CardAuthorizationVerificationCardVerificationCode
    """
    Fields related to verification of the Card Verification Code, a 3-digit code on
    the back of the card.
    """

    cardholder_address: CardAuthorizationVerificationCardholderAddress
    """
    Cardholder address provided in the authorization request and the address on file
    we verified it against.
    """


class CardAuthorization(BaseModel):
    account_id: str
    """The identifier of the Account the authorization will debit."""

    additional_amounts: CardAuthorizationAdditionalAmounts
    """
    Additional amounts associated with the card authorization, such as ATM
    surcharges fees. These are usually a subset of the `amount` field and are used
    to provide more detailed information about the transaction.
    """

    card_id: str
    """The identifier of the Card that is being authorized."""

    decision: Optional[Literal["approve", "decline"]] = None
    """Whether or not the authorization was approved.

    - `approve` - Approve the authorization.
    - `decline` - Decline the authorization.
    """

    digital_wallet_token_id: Optional[str] = None
    """
    If the authorization was made via a Digital Wallet Token (such as an Apple Pay
    purchase), the identifier of the token that was used.
    """

    direction: Literal["settlement", "refund"]
    """
    The direction describes the direction the funds will move, either from the
    cardholder to the merchant or from the merchant to the cardholder.

    - `settlement` - A regular card authorization where funds are debited from the
      cardholder.
    - `refund` - A refund card authorization, sometimes referred to as a credit
      voucher authorization, where funds are credited to the cardholder.
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

    merchant_city: Optional[str] = None
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    merchant_postal_code: Optional[str] = None
    """The merchant's postal code.

    For US merchants this is either a 5-digit or 9-digit ZIP code, where the first 5
    and last 4 are separated by a dash.
    """

    merchant_state: Optional[str] = None
    """The state the merchant resides in."""

    network_details: CardAuthorizationNetworkDetails
    """Fields specific to the `network`."""

    network_identifiers: CardAuthorizationNetworkIdentifiers
    """Network-specific identifiers for a specific request or transaction."""

    network_risk_score: Optional[int] = None
    """The risk score generated by the card network.

    For Visa this is the Visa Advanced Authorization risk score, from 0 to 99, where
    99 is the riskiest.
    """

    physical_card_id: Optional[str] = None
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    presentment_amount: int
    """
    The amount of the attempted authorization in the currency the card user sees at
    the time of purchase, in the minor unit of that currency. For dollars, for
    example, this is cents.
    """

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    user sees at the time of purchase.
    """

    processing_category: Literal[
        "account_funding",
        "automatic_fuel_dispenser",
        "bill_payment",
        "original_credit",
        "purchase",
        "quasi_cash",
        "refund",
        "cash_disbursement",
        "unknown",
    ]
    """
    The processing category describes the intent behind the authorization, such as
    whether it was used for bill payments or an automatic fuel dispenser.

    - `account_funding` - Account funding transactions are transactions used to
      e.g., fund an account or transfer funds between accounts.
    - `automatic_fuel_dispenser` - Automatic fuel dispenser authorizations occur
      when a card is used at a gas pump, prior to the actual transaction amount
      being known. They are followed by an advice message that updates the amount of
      the pending transaction.
    - `bill_payment` - A transaction used to pay a bill.
    - `original_credit` - Original credit transactions are used to send money to a
      cardholder.
    - `purchase` - A regular purchase.
    - `quasi_cash` - Quasi-cash transactions represent purchases of items which may
      be convertible to cash.
    - `refund` - A refund card authorization, sometimes referred to as a credit
      voucher authorization, where funds are credited to the cardholder.
    - `cash_disbursement` - Cash disbursement transactions are used to withdraw cash
      from an ATM or a point of sale.
    - `unknown` - The processing category is unknown.
    """

    request_details: CardAuthorizationRequestDetails
    """Fields specific to the type of request, such as an incremental authorization."""

    settlement_amount: int
    """The amount of the attempted authorization in the currency it will be settled in.

    This currency is the same as that of the Account the card belongs to.
    """

    settlement_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    transaction will be settled in.
    """

    terminal_id: Optional[str] = None
    """
    The terminal identifier (commonly abbreviated as TID) of the terminal the card
    is transacting with.
    """

    upcoming_card_payment_id: str
    """The identifier of the Card Payment this authorization will belong to.

    Available in the API once the card authorization has completed.
    """

    verification: CardAuthorizationVerification
    """Fields related to verification of cardholder-provided values."""


class DigitalWalletAuthentication(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    channel: Literal["sms", "email"]
    """The channel to send the card user their one-time passcode.

    - `sms` - Send one-time passcodes over SMS.
    - `email` - Send one-time passcodes over email.
    """

    digital_wallet: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    - `samsung_pay` - Samsung Pay
    - `unknown` - Unknown
    """

    email: Optional[str] = None
    """The email to send the one-time passcode to if `channel` is equal to `email`."""

    one_time_passcode: str
    """The one-time passcode to send the card user."""

    phone: Optional[str] = None
    """
    The phone number to send the one-time passcode to if `channel` is equal to
    `sms`.
    """

    result: Optional[Literal["success", "failure"]] = None
    """Whether your application successfully delivered the one-time passcode.

    - `success` - Your application successfully delivered the one-time passcode to
      the cardholder.
    - `failure` - Your application failed to deliver the one-time passcode to the
      cardholder.
    """


class DigitalWalletTokenDevice(BaseModel):
    identifier: Optional[str] = None
    """ID assigned to the device by the digital wallet provider."""


class DigitalWalletToken(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    card_profile_id: Optional[str] = None
    """The identifier of the Card Profile that was set via the real time decision.

    This will be null until the real time decision is responded to or if the real
    time decision did not set a card profile.
    """

    decision: Optional[Literal["approve", "decline"]] = None
    """Whether or not the provisioning request was approved.

    This will be null until the real time decision is responded to.

    - `approve` - Approve the provisioning request.
    - `decline` - Decline the provisioning request.
    """

    device: DigitalWalletTokenDevice
    """Device that is being used to provision the digital wallet token."""

    digital_wallet: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    - `samsung_pay` - Samsung Pay
    - `unknown` - Unknown
    """


class RealTimeDecision(BaseModel):
    id: str
    """The Real-Time Decision identifier."""

    card_authentication: Optional[CardAuthentication] = None
    """Fields related to a 3DS authentication attempt."""

    card_authentication_challenge: Optional[CardAuthenticationChallenge] = None
    """Fields related to a 3DS authentication attempt."""

    card_authorization: Optional[CardAuthorization] = None
    """Fields related to a card authorization."""

    category: Literal[
        "card_authorization_requested",
        "card_authentication_requested",
        "card_authentication_challenge_requested",
        "digital_wallet_token_requested",
        "digital_wallet_authentication_requested",
    ]
    """The category of the Real-Time Decision.

    - `card_authorization_requested` - A card is being authorized.
    - `card_authentication_requested` - 3DS authentication is requested.
    - `card_authentication_challenge_requested` - 3DS authentication challenge
      requires cardholder involvement.
    - `digital_wallet_token_requested` - A card is being loaded into a digital
      wallet.
    - `digital_wallet_authentication_requested` - A card is being loaded into a
      digital wallet and requires cardholder authentication.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Real-Time Decision was created.
    """

    digital_wallet_authentication: Optional[DigitalWalletAuthentication] = None
    """Fields related to a digital wallet authentication attempt."""

    digital_wallet_token: Optional[DigitalWalletToken] = None
    """Fields related to a digital wallet token provisioning attempt."""

    status: Literal["pending", "responded", "timed_out"]
    """The status of the Real-Time Decision.

    - `pending` - The decision is pending action via real-time webhook.
    - `responded` - Your webhook actioned the real-time decision.
    - `timed_out` - Your webhook failed to respond to the authorization in time.
    """

    timeout_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    your application can no longer respond to the Real-Time Decision.
    """

    type: Literal["real_time_decision"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_decision`.
    """
