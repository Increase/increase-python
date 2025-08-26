# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PendingTransaction",
    "Source",
    "SourceAccountTransferInstruction",
    "SourceACHTransferInstruction",
    "SourceCardAuthorization",
    "SourceCardAuthorizationAdditionalAmounts",
    "SourceCardAuthorizationAdditionalAmountsClinic",
    "SourceCardAuthorizationAdditionalAmountsDental",
    "SourceCardAuthorizationAdditionalAmountsPrescription",
    "SourceCardAuthorizationAdditionalAmountsSurcharge",
    "SourceCardAuthorizationAdditionalAmountsTotalCumulative",
    "SourceCardAuthorizationAdditionalAmountsTotalHealthcare",
    "SourceCardAuthorizationAdditionalAmountsTransit",
    "SourceCardAuthorizationAdditionalAmountsUnknown",
    "SourceCardAuthorizationAdditionalAmountsVision",
    "SourceCardAuthorizationNetworkDetails",
    "SourceCardAuthorizationNetworkDetailsVisa",
    "SourceCardAuthorizationNetworkIdentifiers",
    "SourceCardAuthorizationVerification",
    "SourceCardAuthorizationVerificationCardVerificationCode",
    "SourceCardAuthorizationVerificationCardholderAddress",
    "SourceCardPushTransferInstruction",
    "SourceCheckDepositInstruction",
    "SourceCheckTransferInstruction",
    "SourceInboundFundsHold",
    "SourceInboundWireTransferReversal",
    "SourceRealTimePaymentsTransferInstruction",
    "SourceSwiftTransferInstruction",
    "SourceWireTransferInstruction",
]


class SourceAccountTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    transfer_id: str
    """The identifier of the Account Transfer that led to this Pending Transaction."""


class SourceACHTransferInstruction(BaseModel):
    amount: int
    """The pending amount in USD cents."""

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Pending Transaction."""


class SourceCardAuthorizationAdditionalAmountsClinic(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsDental(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsPrescription(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsSurcharge(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsTotalCumulative(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsTotalHealthcare(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsTransit(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsUnknown(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmountsVision(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardAuthorizationAdditionalAmounts(BaseModel):
    clinic: Optional[SourceCardAuthorizationAdditionalAmountsClinic] = None
    """The part of this transaction amount that was for clinic-related services."""

    dental: Optional[SourceCardAuthorizationAdditionalAmountsDental] = None
    """The part of this transaction amount that was for dental-related services."""

    prescription: Optional[SourceCardAuthorizationAdditionalAmountsPrescription] = None
    """The part of this transaction amount that was for healthcare prescriptions."""

    surcharge: Optional[SourceCardAuthorizationAdditionalAmountsSurcharge] = None
    """The surcharge amount charged for this transaction by the merchant."""

    total_cumulative: Optional[SourceCardAuthorizationAdditionalAmountsTotalCumulative] = None
    """
    The total amount of a series of incremental authorizations, optionally provided.
    """

    total_healthcare: Optional[SourceCardAuthorizationAdditionalAmountsTotalHealthcare] = None
    """The total amount of healthcare-related additional amounts."""

    transit: Optional[SourceCardAuthorizationAdditionalAmountsTransit] = None
    """The part of this transaction amount that was for transit-related services."""

    unknown: Optional[SourceCardAuthorizationAdditionalAmountsUnknown] = None
    """An unknown additional amount."""

    vision: Optional[SourceCardAuthorizationAdditionalAmountsVision] = None
    """The part of this transaction amount that was for vision-related services."""


class SourceCardAuthorizationNetworkDetailsVisa(BaseModel):
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


class SourceCardAuthorizationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[SourceCardAuthorizationNetworkDetailsVisa] = None
    """Fields specific to the `visa` network."""


class SourceCardAuthorizationNetworkIdentifiers(BaseModel):
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


class SourceCardAuthorizationVerificationCardVerificationCode(BaseModel):
    result: Literal["not_checked", "match", "no_match"]
    """The result of verifying the Card Verification Code.

    - `not_checked` - No card verification code was provided in the authorization
      request.
    - `match` - The card verification code matched the one on file.
    - `no_match` - The card verification code did not match the one on file.
    """


class SourceCardAuthorizationVerificationCardholderAddress(BaseModel):
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


class SourceCardAuthorizationVerification(BaseModel):
    card_verification_code: SourceCardAuthorizationVerificationCardVerificationCode
    """
    Fields related to verification of the Card Verification Code, a 3-digit code on
    the back of the card.
    """

    cardholder_address: SourceCardAuthorizationVerificationCardholderAddress
    """
    Cardholder address provided in the authorization request and the address on file
    we verified it against.
    """


class SourceCardAuthorization(BaseModel):
    id: str
    """The Card Authorization identifier."""

    actioner: Literal["user", "increase", "network"]
    """
    Whether this authorization was approved by Increase, the card network through
    stand-in processing, or the user through a real-time decision.

    - `user` - This object was actioned by the user through a real-time decision.
    - `increase` - This object was actioned by Increase without user intervention.
    - `network` - This object was actioned by the network, through stand-in
      processing.
    """

    additional_amounts: SourceCardAuthorizationAdditionalAmounts
    """
    Additional amounts associated with the card authorization, such as ATM
    surcharges fees. These are usually a subset of the `amount` field and are used
    to provide more detailed information about the transaction.
    """

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: str
    """The ID of the Card Payment this transaction belongs to."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
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

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) when this authorization
    will expire and the pending transaction will be released.
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

    network_details: SourceCardAuthorizationNetworkDetails
    """Fields specific to the `network`."""

    network_identifiers: SourceCardAuthorizationNetworkIdentifiers
    """Network-specific identifiers for a specific request or transaction."""

    network_risk_score: Optional[int] = None
    """The risk score generated by the card network.

    For Visa this is the Visa Advanced Authorization risk score, from 0 to 99, where
    99 is the riskiest.
    """

    pending_transaction_id: Optional[str] = None
    """The identifier of the Pending Transaction associated with this Transaction."""

    physical_card_id: Optional[str] = None
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    presentment_amount: int
    """The pending amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
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

    real_time_decision_id: Optional[str] = None
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    terminal_id: Optional[str] = None
    """
    The terminal identifier (commonly abbreviated as TID) of the terminal the card
    is transacting with.
    """

    type: Literal["card_authorization"]
    """A constant representing the object's type.

    For this resource it will always be `card_authorization`.
    """

    verification: SourceCardAuthorizationVerification
    """Fields related to verification of cardholder-provided values."""


class SourceCardPushTransferInstruction(BaseModel):
    amount: int
    """The transfer amount in USD cents."""

    transfer_id: str
    """The identifier of the Card Push Transfer that led to this Pending Transaction."""


class SourceCheckDepositInstruction(BaseModel):
    amount: int
    """The pending amount in USD cents."""

    back_image_file_id: Optional[str] = None
    """
    The identifier of the File containing the image of the back of the check that
    was deposited.
    """

    check_deposit_id: Optional[str] = None
    """The identifier of the Check Deposit."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    front_image_file_id: str
    """
    The identifier of the File containing the image of the front of the check that
    was deposited.
    """


class SourceCheckTransferInstruction(BaseModel):
    amount: int
    """The transfer amount in USD cents."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    transfer_id: str
    """The identifier of the Check Transfer that led to this Pending Transaction."""


class SourceInboundFundsHold(BaseModel):
    amount: int
    """The held amount in the minor unit of the account's currency.

    For dollars, for example, this is cents.
    """

    automatically_releases_at: datetime
    """When the hold will be released automatically.

    Certain conditions may cause it to be released before this time.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the hold
    was created.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the hold's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    held_transaction_id: Optional[str] = None
    """The ID of the Transaction for which funds were held."""

    pending_transaction_id: Optional[str] = None
    """The ID of the Pending Transaction representing the held funds."""

    released_at: Optional[datetime] = None
    """When the hold was released (if it has been released)."""

    status: Literal["held", "complete"]
    """The status of the hold.

    - `held` - Funds are still being held.
    - `complete` - Funds have been released.
    """

    type: Literal["inbound_funds_hold"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_funds_hold`.
    """


class SourceInboundWireTransferReversal(BaseModel):
    inbound_wire_transfer_id: str
    """The ID of the Inbound Wire Transfer that is being reversed."""


class SourceRealTimePaymentsTransferInstruction(BaseModel):
    amount: int
    """The transfer amount in USD cents."""

    transfer_id: str
    """
    The identifier of the Real-Time Payments Transfer that led to this Pending
    Transaction.
    """


class SourceSwiftTransferInstruction(BaseModel):
    transfer_id: str
    """The identifier of the Swift Transfer that led to this Pending Transaction."""


class SourceWireTransferInstruction(BaseModel):
    account_number: str
    """The account number for the destination account."""

    amount: int
    """The transfer amount in USD cents."""

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    transfer_id: str
    """The identifier of the Wire Transfer that led to this Pending Transaction."""


class Source(BaseModel):
    account_transfer_instruction: Optional[SourceAccountTransferInstruction] = None
    """An Account Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_instruction`.
    """

    ach_transfer_instruction: Optional[SourceACHTransferInstruction] = None
    """An ACH Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_instruction`.
    """

    card_authorization: Optional[SourceCardAuthorization] = None
    """A Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization`. Card Authorizations are temporary holds placed on
    a customers funds with the intent to later clear a transaction.
    """

    card_push_transfer_instruction: Optional[SourceCardPushTransferInstruction] = None
    """A Card Push Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_push_transfer_instruction`.
    """

    category: Literal[
        "account_transfer_instruction",
        "ach_transfer_instruction",
        "card_authorization",
        "check_deposit_instruction",
        "check_transfer_instruction",
        "inbound_funds_hold",
        "user_initiated_hold",
        "real_time_payments_transfer_instruction",
        "wire_transfer_instruction",
        "inbound_wire_transfer_reversal",
        "swift_transfer_instruction",
        "card_push_transfer_instruction",
        "other",
    ]
    """The type of the resource.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `account_transfer_instruction` - Account Transfer Instruction: details will be
      under the `account_transfer_instruction` object.
    - `ach_transfer_instruction` - ACH Transfer Instruction: details will be under
      the `ach_transfer_instruction` object.
    - `card_authorization` - Card Authorization: details will be under the
      `card_authorization` object.
    - `check_deposit_instruction` - Check Deposit Instruction: details will be under
      the `check_deposit_instruction` object.
    - `check_transfer_instruction` - Check Transfer Instruction: details will be
      under the `check_transfer_instruction` object.
    - `inbound_funds_hold` - Inbound Funds Hold: details will be under the
      `inbound_funds_hold` object.
    - `user_initiated_hold` - User Initiated Hold: details will be under the
      `user_initiated_hold` object.
    - `real_time_payments_transfer_instruction` - Real-Time Payments Transfer
      Instruction: details will be under the
      `real_time_payments_transfer_instruction` object.
    - `wire_transfer_instruction` - Wire Transfer Instruction: details will be under
      the `wire_transfer_instruction` object.
    - `inbound_wire_transfer_reversal` - Inbound Wire Transfer Reversal: details
      will be under the `inbound_wire_transfer_reversal` object.
    - `swift_transfer_instruction` - Swift Transfer Instruction: details will be
      under the `swift_transfer_instruction` object.
    - `card_push_transfer_instruction` - Card Push Transfer Instruction: details
      will be under the `card_push_transfer_instruction` object.
    - `other` - The Pending Transaction was made for an undocumented or deprecated
      reason.
    """

    check_deposit_instruction: Optional[SourceCheckDepositInstruction] = None
    """A Check Deposit Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_instruction`.
    """

    check_transfer_instruction: Optional[SourceCheckTransferInstruction] = None
    """A Check Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_instruction`.
    """

    inbound_funds_hold: Optional[SourceInboundFundsHold] = None
    """An Inbound Funds Hold object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_funds_hold`. We hold funds for certain transaction types to
    account for return windows where funds might still be clawed back by the sending
    institution.
    """

    inbound_wire_transfer_reversal: Optional[SourceInboundWireTransferReversal] = None
    """An Inbound Wire Transfer Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer_reversal`. An Inbound Wire Transfer Reversal is
    created when Increase has received a wire and the User requests that it be
    reversed.
    """

    other: Optional[object] = None
    """
    If the category of this Transaction source is equal to `other`, this field will
    contain an empty object, otherwise it will contain null.
    """

    real_time_payments_transfer_instruction: Optional[SourceRealTimePaymentsTransferInstruction] = None
    """A Real-Time Payments Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_instruction`.
    """

    swift_transfer_instruction: Optional[SourceSwiftTransferInstruction] = None
    """A Swift Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `swift_transfer_instruction`.
    """

    user_initiated_hold: Optional[object] = None
    """An User Initiated Hold object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_initiated_hold`. Created when a user initiates a hold on funds in
    their account.
    """

    wire_transfer_instruction: Optional[SourceWireTransferInstruction] = None
    """A Wire Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_instruction`.
    """


class PendingTransaction(BaseModel):
    id: str
    """The Pending Transaction identifier."""

    account_id: str
    """The identifier for the account this Pending Transaction belongs to."""

    amount: int
    """The Pending Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    balance_impact: Literal["affects_available_balance", "none"]
    """
    How the Pending Transaction affects the balance of its Account while its status
    is `pending`.

    - `affects_available_balance` - This Pending Transaction will decrement the
      available balance on the Account while its status is `pending`.
    - `none` - This Pending Transaction does not affect the available balance on the
      Account.
    """

    completed_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending
    Transaction was completed.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending
    Transaction occurred.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Pending
    Transaction's currency. This will match the currency on the Pending
    Transaction's Account.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    description: str
    """
    For a Pending Transaction related to a transfer, this is the description you
    provide. For a Pending Transaction related to a payment, this is the description
    the vendor provides.
    """

    route_id: Optional[str] = None
    """The identifier for the route this Pending Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card", "lockbox"]] = None
    """The type of the route this Pending Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    - `lockbox` - A Lockbox.
    """

    source: Source
    """
    This is an object giving more details on the network-level event that caused the
    Pending Transaction. For example, for a card transaction this lists the
    merchant's industry and location.
    """

    status: Literal["pending", "complete"]
    """
    Whether the Pending Transaction has been confirmed and has an associated
    Transaction.

    - `pending` - The Pending Transaction is still awaiting confirmation.
    - `complete` - The Pending Transaction is confirmed. An associated Transaction
      exists for this object. The Pending Transaction will no longer count against
      your balance and can generally be hidden from UIs, etc.
    """

    type: Literal["pending_transaction"]
    """A constant representing the object's type.

    For this resource it will always be `pending_transaction`.
    """
