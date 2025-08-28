# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "DeclinedTransaction",
    "Source",
    "SourceACHDecline",
    "SourceCardDecline",
    "SourceCardDeclineAdditionalAmounts",
    "SourceCardDeclineAdditionalAmountsClinic",
    "SourceCardDeclineAdditionalAmountsDental",
    "SourceCardDeclineAdditionalAmountsPrescription",
    "SourceCardDeclineAdditionalAmountsSurcharge",
    "SourceCardDeclineAdditionalAmountsTotalCumulative",
    "SourceCardDeclineAdditionalAmountsTotalHealthcare",
    "SourceCardDeclineAdditionalAmountsTransit",
    "SourceCardDeclineAdditionalAmountsUnknown",
    "SourceCardDeclineAdditionalAmountsVision",
    "SourceCardDeclineNetworkDetails",
    "SourceCardDeclineNetworkDetailsVisa",
    "SourceCardDeclineNetworkIdentifiers",
    "SourceCardDeclineVerification",
    "SourceCardDeclineVerificationCardVerificationCode",
    "SourceCardDeclineVerificationCardholderAddress",
    "SourceCheckDecline",
    "SourceCheckDepositRejection",
    "SourceInboundRealTimePaymentsTransferDecline",
    "SourceWireDecline",
]


class SourceACHDecline(BaseModel):
    id: str
    """The ACH Decline's identifier."""

    amount: int
    """The declined amount in USD cents."""

    inbound_ach_transfer_id: str
    """The identifier of the Inbound ACH Transfer object associated with this decline."""

    originator_company_descriptive_date: Optional[str] = None
    """The descriptive date of the transfer."""

    originator_company_discretionary_data: Optional[str] = None
    """The additional information included with the transfer."""

    originator_company_id: str
    """The identifier of the company that initiated the transfer."""

    originator_company_name: str
    """The name of the company that initiated the transfer."""

    reason: Literal[
        "ach_route_canceled",
        "ach_route_disabled",
        "breaches_limit",
        "entity_not_active",
        "group_locked",
        "transaction_not_allowed",
        "user_initiated",
        "insufficient_funds",
        "returned_per_odfi_request",
        "authorization_revoked_by_customer",
        "payment_stopped",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "beneficiary_or_account_holder_deceased",
        "credit_entry_refused_by_receiver",
        "duplicate_entry",
        "corporate_customer_advised_not_authorized",
    ]
    """Why the ACH transfer was declined.

    - `ach_route_canceled` - The account number is canceled.
    - `ach_route_disabled` - The account number is disabled.
    - `breaches_limit` - The transaction would cause an Increase limit to be
      exceeded.
    - `entity_not_active` - The account's entity is not active.
    - `group_locked` - Your account is inactive.
    - `transaction_not_allowed` - The transaction is not allowed per Increase's
      terms.
    - `user_initiated` - Your integration declined this transfer via the API.
    - `insufficient_funds` - Your account contains insufficient funds.
    - `returned_per_odfi_request` - The originating financial institution asked for
      this transfer to be returned. The receiving bank is complying with the
      request.
    - `authorization_revoked_by_customer` - The customer no longer authorizes this
      transaction.
    - `payment_stopped` - The customer asked for the payment to be stopped.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
      customer advises that the debit was unauthorized.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
      payee is deceased.
    - `beneficiary_or_account_holder_deceased` - The account holder is deceased.
    - `credit_entry_refused_by_receiver` - The customer refused a credit entry.
    - `duplicate_entry` - The account holder identified this transaction as a
      duplicate.
    - `corporate_customer_advised_not_authorized` - The corporate customer no longer
      authorizes this transaction.
    """

    receiver_id_number: Optional[str] = None
    """The id of the receiver of the transfer."""

    receiver_name: Optional[str] = None
    """The name of the receiver of the transfer."""

    trace_number: str
    """The trace number of the transfer."""

    type: Literal["ach_decline"]
    """A constant representing the object's type.

    For this resource it will always be `ach_decline`.
    """


class SourceCardDeclineAdditionalAmountsClinic(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsDental(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsPrescription(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsSurcharge(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsTotalCumulative(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsTotalHealthcare(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsTransit(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsUnknown(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmountsVision(BaseModel):
    amount: int
    """The amount in minor units of the `currency` field."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the additional
    amount's currency.
    """


class SourceCardDeclineAdditionalAmounts(BaseModel):
    clinic: Optional[SourceCardDeclineAdditionalAmountsClinic] = None
    """The part of this transaction amount that was for clinic-related services."""

    dental: Optional[SourceCardDeclineAdditionalAmountsDental] = None
    """The part of this transaction amount that was for dental-related services."""

    prescription: Optional[SourceCardDeclineAdditionalAmountsPrescription] = None
    """The part of this transaction amount that was for healthcare prescriptions."""

    surcharge: Optional[SourceCardDeclineAdditionalAmountsSurcharge] = None
    """The surcharge amount charged for this transaction by the merchant."""

    total_cumulative: Optional[SourceCardDeclineAdditionalAmountsTotalCumulative] = None
    """
    The total amount of a series of incremental authorizations, optionally provided.
    """

    total_healthcare: Optional[SourceCardDeclineAdditionalAmountsTotalHealthcare] = None
    """The total amount of healthcare-related additional amounts."""

    transit: Optional[SourceCardDeclineAdditionalAmountsTransit] = None
    """The part of this transaction amount that was for transit-related services."""

    unknown: Optional[SourceCardDeclineAdditionalAmountsUnknown] = None
    """An unknown additional amount."""

    vision: Optional[SourceCardDeclineAdditionalAmountsVision] = None
    """The part of this transaction amount that was for vision-related services."""


class SourceCardDeclineNetworkDetailsVisa(BaseModel):
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


class SourceCardDeclineNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[SourceCardDeclineNetworkDetailsVisa] = None
    """Fields specific to the `visa` network."""


class SourceCardDeclineNetworkIdentifiers(BaseModel):
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


class SourceCardDeclineVerificationCardVerificationCode(BaseModel):
    result: Literal["not_checked", "match", "no_match"]
    """The result of verifying the Card Verification Code.

    - `not_checked` - No card verification code was provided in the authorization
      request.
    - `match` - The card verification code matched the one on file.
    - `no_match` - The card verification code did not match the one on file.
    """


class SourceCardDeclineVerificationCardholderAddress(BaseModel):
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


class SourceCardDeclineVerification(BaseModel):
    card_verification_code: SourceCardDeclineVerificationCardVerificationCode
    """
    Fields related to verification of the Card Verification Code, a 3-digit code on
    the back of the card.
    """

    cardholder_address: SourceCardDeclineVerificationCardholderAddress
    """
    Cardholder address provided in the authorization request and the address on file
    we verified it against.
    """


class SourceCardDecline(BaseModel):
    id: str
    """The Card Decline identifier."""

    actioner: Literal["user", "increase", "network"]
    """
    Whether this authorization was approved by Increase, the card network through
    stand-in processing, or the user through a real-time decision.

    - `user` - This object was actioned by the user through a real-time decision.
    - `increase` - This object was actioned by Increase without user intervention.
    - `network` - This object was actioned by the network, through stand-in
      processing.
    """

    additional_amounts: SourceCardDeclineAdditionalAmounts
    """
    Additional amounts associated with the card authorization, such as ATM
    surcharges fees. These are usually a subset of the `amount` field and are used
    to provide more detailed information about the transaction.
    """

    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: str
    """The ID of the Card Payment this transaction belongs to."""

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

    declined_transaction_id: str
    """The identifier of the declined transaction created for this Card Decline."""

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

    incremented_card_authorization_id: Optional[str] = None
    """
    The identifier of the card authorization this request attempted to incrementally
    authorize.
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

    network_details: SourceCardDeclineNetworkDetails
    """Fields specific to the `network`."""

    network_identifiers: SourceCardDeclineNetworkIdentifiers
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
    The declined amount in the minor unit of the transaction's presentment currency.
    """

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

    real_time_decision_reason: Optional[
        Literal[
            "insufficient_funds",
            "transaction_never_allowed",
            "exceeds_approval_limit",
            "card_temporarily_disabled",
            "suspected_fraud",
            "other",
        ]
    ] = None
    """
    This is present if a specific decline reason was given in the real-time
    decision.

    - `insufficient_funds` - The cardholder does not have sufficient funds to cover
      the transaction. The merchant may attempt to process the transaction again.
    - `transaction_never_allowed` - This type of transaction is not allowed for this
      card. This transaction should not be retried.
    - `exceeds_approval_limit` - The transaction amount exceeds the cardholder's
      approval limit. The merchant may attempt to process the transaction again.
    - `card_temporarily_disabled` - The card has been temporarily disabled or not
      yet activated. The merchant may attempt to process the transaction again.
    - `suspected_fraud` - The transaction is suspected to be fraudulent. The
      merchant may attempt to process the transaction again.
    - `other` - The transaction was declined for another reason. The merchant may
      attempt to process the transaction again. This should be used sparingly.
    """

    reason: Literal[
        "account_closed",
        "card_not_active",
        "card_canceled",
        "physical_card_not_active",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "cvv2_mismatch",
        "pin_mismatch",
        "card_expiration_mismatch",
        "transaction_not_allowed",
        "breaches_limit",
        "webhook_declined",
        "webhook_timed_out",
        "declined_by_stand_in_processing",
        "invalid_physical_card",
        "missing_original_authorization",
        "failed_3ds_authentication",
        "suspected_card_testing",
        "suspected_fraud",
    ]
    """Why the transaction was declined.

    - `account_closed` - The account has been closed.
    - `card_not_active` - The Card was not active.
    - `card_canceled` - The Card has been canceled.
    - `physical_card_not_active` - The Physical Card was not active.
    - `entity_not_active` - The account's entity was not active.
    - `group_locked` - The account was inactive.
    - `insufficient_funds` - The Card's Account did not have a sufficient available
      balance.
    - `cvv2_mismatch` - The given CVV2 did not match the card's value.
    - `pin_mismatch` - The given PIN did not match the card's value.
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
    - `failed_3ds_authentication` - The transaction was declined because the 3DS
      authentication failed.
    - `suspected_card_testing` - The transaction was suspected to be used by a card
      tester to test for valid card numbers.
    - `suspected_fraud` - The transaction was suspected to be fraudulent. Please
      reach out to support@increase.com for more information.
    """

    terminal_id: Optional[str] = None
    """
    The terminal identifier (commonly abbreviated as TID) of the terminal the card
    is transacting with.
    """

    verification: SourceCardDeclineVerification
    """Fields related to verification of cardholder-provided values."""


class SourceCheckDecline(BaseModel):
    amount: int
    """The declined amount in USD cents."""

    auxiliary_on_us: Optional[str] = None
    """
    A computer-readable number printed on the MICR line of business checks, usually
    the check number. This is useful for positive pay checks, but can be unreliably
    transmitted by the bank of first deposit.
    """

    back_image_file_id: Optional[str] = None
    """
    The identifier of the API File object containing an image of the back of the
    declined check.
    """

    check_transfer_id: Optional[str] = None
    """The identifier of the Check Transfer object associated with this decline."""

    front_image_file_id: Optional[str] = None
    """
    The identifier of the API File object containing an image of the front of the
    declined check.
    """

    inbound_check_deposit_id: Optional[str] = None
    """
    The identifier of the Inbound Check Deposit object associated with this decline.
    """

    reason: Literal[
        "ach_route_disabled",
        "ach_route_canceled",
        "altered_or_fictitious",
        "breaches_limit",
        "endorsement_irregular",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "stop_payment_requested",
        "duplicate_presentment",
        "not_authorized",
        "amount_mismatch",
        "not_our_item",
        "no_account_number_found",
        "refer_to_image",
        "unable_to_process",
        "unusable_image",
        "user_initiated",
    ]
    """Why the check was declined.

    - `ach_route_disabled` - The account number is disabled.
    - `ach_route_canceled` - The account number is canceled.
    - `altered_or_fictitious` - The deposited check was altered or fictitious.
    - `breaches_limit` - The transaction would cause a limit to be exceeded.
    - `endorsement_irregular` - The check was not endorsed by the payee.
    - `entity_not_active` - The account's entity is not active.
    - `group_locked` - Your account is inactive.
    - `insufficient_funds` - Your account contains insufficient funds.
    - `stop_payment_requested` - Stop payment requested for this check.
    - `duplicate_presentment` - The check was a duplicate deposit.
    - `not_authorized` - The check was not authorized.
    - `amount_mismatch` - The amount the receiving bank is attempting to deposit
      does not match the amount on the check.
    - `not_our_item` - The check attempting to be deposited does not belong to
      Increase.
    - `no_account_number_found` - The account number on the check does not exist at
      Increase.
    - `refer_to_image` - The check is not readable. Please refer to the image.
    - `unable_to_process` - The check cannot be processed. This is rare: please
      contact support.
    - `unusable_image` - The check image is unusable.
    - `user_initiated` - Your integration declined this check via the API.
    """


class SourceCheckDepositRejection(BaseModel):
    amount: int
    """The rejected amount in the minor unit of check's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The identifier of the Check Deposit that was rejected."""

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

    declined_transaction_id: str
    """The identifier of the associated declined transaction."""

    reason: Literal[
        "incomplete_image",
        "duplicate",
        "poor_image_quality",
        "incorrect_amount",
        "incorrect_recipient",
        "not_eligible_for_mobile_deposit",
        "missing_required_data_elements",
        "suspected_fraud",
        "deposit_window_expired",
        "requested_by_user",
        "unknown",
    ]
    """Why the check deposit was rejected.

    - `incomplete_image` - The check's image is incomplete.
    - `duplicate` - This is a duplicate check submission.
    - `poor_image_quality` - This check has poor image quality.
    - `incorrect_amount` - The check was deposited with the incorrect amount.
    - `incorrect_recipient` - The check is made out to someone other than the
      account holder.
    - `not_eligible_for_mobile_deposit` - This check was not eligible for mobile
      deposit.
    - `missing_required_data_elements` - This check is missing at least one required
      field.
    - `suspected_fraud` - This check is suspected to be fraudulent.
    - `deposit_window_expired` - This check's deposit window has expired.
    - `requested_by_user` - The check was rejected at the user's request.
    - `unknown` - The check was rejected for an unknown reason.
    """

    rejected_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was rejected.
    """


class SourceInboundRealTimePaymentsTransferDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    creditor_name: str
    """The name the sender of the transfer specified as the recipient of the transfer."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the declined
    transfer's currency. This will always be "USD" for a Real-Time Payments
    transfer.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    debtor_account_number: str
    """The account number of the account that sent the transfer."""

    debtor_name: str
    """The name provided by the sender of the transfer."""

    debtor_routing_number: str
    """The routing number of the account that sent the transfer."""

    reason: Literal[
        "account_number_canceled",
        "account_number_disabled",
        "account_restricted",
        "group_locked",
        "entity_not_active",
        "real_time_payments_not_enabled",
    ]
    """Why the transfer was declined.

    - `account_number_canceled` - The account number is canceled.
    - `account_number_disabled` - The account number is disabled.
    - `account_restricted` - Your account is restricted.
    - `group_locked` - Your account is inactive.
    - `entity_not_active` - The account's entity is not active.
    - `real_time_payments_not_enabled` - Your account is not enabled to receive
      Real-Time Payments transfers.
    """

    remittance_information: Optional[str] = None
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real-Time Payments network identification of the declined transfer."""

    transfer_id: str
    """The identifier of the Real-Time Payments Transfer that led to this Transaction."""


class SourceWireDecline(BaseModel):
    inbound_wire_transfer_id: str
    """The identifier of the Inbound Wire Transfer that was declined."""

    reason: Literal[
        "account_number_canceled",
        "account_number_disabled",
        "entity_not_active",
        "group_locked",
        "no_account_number",
        "transaction_not_allowed",
    ]
    """Why the wire transfer was declined.

    - `account_number_canceled` - The account number is canceled.
    - `account_number_disabled` - The account number is disabled.
    - `entity_not_active` - The account's entity is not active.
    - `group_locked` - Your account is inactive.
    - `no_account_number` - The beneficiary account number does not exist.
    - `transaction_not_allowed` - The transaction is not allowed per Increase's
      terms.
    """


class Source(BaseModel):
    ach_decline: Optional[SourceACHDecline] = None
    """An ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_decline`.
    """

    card_decline: Optional[SourceCardDecline] = None
    """A Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_decline`.
    """

    category: Literal[
        "ach_decline",
        "card_decline",
        "check_decline",
        "inbound_real_time_payments_transfer_decline",
        "wire_decline",
        "check_deposit_rejection",
        "other",
    ]
    """The type of the resource.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `ach_decline` - ACH Decline: details will be under the `ach_decline` object.
    - `card_decline` - Card Decline: details will be under the `card_decline`
      object.
    - `check_decline` - Check Decline: details will be under the `check_decline`
      object.
    - `inbound_real_time_payments_transfer_decline` - Inbound Real-Time Payments
      Transfer Decline: details will be under the
      `inbound_real_time_payments_transfer_decline` object.
    - `wire_decline` - Wire Decline: details will be under the `wire_decline`
      object.
    - `check_deposit_rejection` - Check Deposit Rejection: details will be under the
      `check_deposit_rejection` object.
    - `other` - The Declined Transaction was made for an undocumented or deprecated
      reason.
    """

    check_decline: Optional[SourceCheckDecline] = None
    """A Check Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_decline`.
    """

    check_deposit_rejection: Optional[SourceCheckDepositRejection] = None
    """A Check Deposit Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_rejection`.
    """

    inbound_real_time_payments_transfer_decline: Optional[SourceInboundRealTimePaymentsTransferDecline] = None
    """An Inbound Real-Time Payments Transfer Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_decline`.
    """

    other: Optional[object] = None
    """
    If the category of this Transaction source is equal to `other`, this field will
    contain an empty object, otherwise it will contain null.
    """

    wire_decline: Optional[SourceWireDecline] = None
    """A Wire Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_decline`.
    """


class DeclinedTransaction(BaseModel):
    id: str
    """The Declined Transaction identifier."""

    account_id: str
    """The identifier for the Account the Declined Transaction belongs to."""

    amount: int
    """The Declined Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the
    Transaction occurred.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Declined
    Transaction's currency. This will match the currency on the Declined
    Transaction's Account.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    description: str
    """This is the description the vendor provides."""

    route_id: Optional[str] = None
    """The identifier for the route this Declined Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card", "lockbox"]] = None
    """The type of the route this Declined Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    - `lockbox` - A Lockbox.
    """

    source: Source
    """
    This is an object giving more details on the network-level event that caused the
    Declined Transaction. For example, for a card transaction this lists the
    merchant's industry and location. Note that for backwards compatibility reasons,
    additional undocumented keys may appear in this object. These should be treated
    as deprecated and will be removed in the future.
    """

    type: Literal["declined_transaction"]
    """A constant representing the object's type.

    For this resource it will always be `declined_transaction`.
    """
