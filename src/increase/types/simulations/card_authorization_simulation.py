# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CardAuthorizationSimulation",
    "DeclinedTransaction",
    "DeclinedTransactionSource",
    "DeclinedTransactionSourceACHDecline",
    "DeclinedTransactionSourceCardDecline",
    "DeclinedTransactionSourceCardDeclineNetworkDetails",
    "DeclinedTransactionSourceCardDeclineNetworkDetailsVisa",
    "DeclinedTransactionSourceCardDeclineNetworkIdentifiers",
    "DeclinedTransactionSourceCardDeclineVerification",
    "DeclinedTransactionSourceCardDeclineVerificationCardVerificationCode",
    "DeclinedTransactionSourceCardDeclineVerificationCardholderAddress",
    "DeclinedTransactionSourceCheckDecline",
    "DeclinedTransactionSourceInboundRealTimePaymentsTransferDecline",
    "DeclinedTransactionSourceInternationalACHDecline",
    "DeclinedTransactionSourceWireDecline",
    "PendingTransaction",
    "PendingTransactionSource",
    "PendingTransactionSourceAccountTransferInstruction",
    "PendingTransactionSourceACHTransferInstruction",
    "PendingTransactionSourceCardAuthorization",
    "PendingTransactionSourceCardAuthorizationNetworkDetails",
    "PendingTransactionSourceCardAuthorizationNetworkDetailsVisa",
    "PendingTransactionSourceCardAuthorizationNetworkIdentifiers",
    "PendingTransactionSourceCardAuthorizationVerification",
    "PendingTransactionSourceCardAuthorizationVerificationCardVerificationCode",
    "PendingTransactionSourceCardAuthorizationVerificationCardholderAddress",
    "PendingTransactionSourceCheckDepositInstruction",
    "PendingTransactionSourceCheckTransferInstruction",
    "PendingTransactionSourceInboundFundsHold",
    "PendingTransactionSourceRealTimePaymentsTransferInstruction",
    "PendingTransactionSourceWireTransferInstruction",
]


class DeclinedTransactionSourceACHDecline(BaseModel):
    id: str
    """The ACH Decline's identifier."""

    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

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
        "credit_entry_refused_by_receiver",
        "duplicate_return",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "misrouted_return",
        "return_of_erroneous_or_reversing_debit",
        "no_ach_route",
        "originator_request",
        "transaction_not_allowed",
        "user_initiated",
    ]
    """Why the ACH transfer was declined.

    - `ach_route_canceled` - The account number is canceled.
    - `ach_route_disabled` - The account number is disabled.
    - `breaches_limit` - The transaction would cause an Increase limit to be
      exceeded.
    - `credit_entry_refused_by_receiver` - A credit was refused. This is a
      reasonable default reason for decline of credits.
    - `duplicate_return` - A rare return reason. The return this message refers to
      was a duplicate.
    - `entity_not_active` - The account's entity is not active.
    - `group_locked` - Your account is inactive.
    - `insufficient_funds` - Your account contains insufficient funds.
    - `misrouted_return` - A rare return reason. The return this message refers to
      was misrouted.
    - `return_of_erroneous_or_reversing_debit` - The originating financial
      institution made a mistake and this return corrects it.
    - `no_ach_route` - The account number that was debited does not exist.
    - `originator_request` - The originating financial institution asked for this
      transfer to be returned.
    - `transaction_not_allowed` - The transaction is not allowed per Increase's
      terms.
    - `user_initiated` - The user initiated the decline.
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


class DeclinedTransactionSourceCardDeclineNetworkDetailsVisa(BaseModel):
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


class DeclinedTransactionSourceCardDeclineNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[DeclinedTransactionSourceCardDeclineNetworkDetailsVisa] = None
    """Fields specific to the `visa` network."""


class DeclinedTransactionSourceCardDeclineNetworkIdentifiers(BaseModel):
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


class DeclinedTransactionSourceCardDeclineVerificationCardVerificationCode(BaseModel):
    result: Literal["not_checked", "match", "no_match"]
    """The result of verifying the Card Verification Code.

    - `not_checked` - No card verification code was provided in the authorization
      request.
    - `match` - The card verification code matched the one on file.
    - `no_match` - The card verification code did not match the one on file.
    """


class DeclinedTransactionSourceCardDeclineVerificationCardholderAddress(BaseModel):
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

    - `not_checked` - No adress was provided in the authorization request.
    - `postal_code_match_address_not_checked` - Postal code matches, but the street
      address was not verified.
    - `postal_code_match_address_no_match` - Postal code matches, but the street
      address does not match.
    - `postal_code_no_match_address_match` - Postal code does not match, but the
      street address matches.
    - `match` - Postal code and street address match.
    - `no_match` - Postal code and street address do not match.
    """


class DeclinedTransactionSourceCardDeclineVerification(BaseModel):
    card_verification_code: DeclinedTransactionSourceCardDeclineVerificationCardVerificationCode
    """
    Fields related to verification of the Card Verification Code, a 3-digit code on
    the back of the card.
    """

    cardholder_address: DeclinedTransactionSourceCardDeclineVerificationCardholderAddress
    """
    Cardholder address provided in the authorization request and the address on file
    we verified it against.
    """


class DeclinedTransactionSourceCardDecline(BaseModel):
    id: str
    """The Card Decline identifier."""

    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: Optional[str] = None
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

    digital_wallet_token_id: Optional[str] = None
    """
    If the authorization was made via a Digital Wallet Token (such as an Apple Pay
    purchase), the identifier of the token that was used.
    """

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: Optional[str] = None
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str] = None
    """The city the merchant resides in."""

    merchant_country: Optional[str] = None
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    merchant_state: Optional[str] = None
    """The state the merchant resides in."""

    network_details: DeclinedTransactionSourceCardDeclineNetworkDetails
    """Fields specific to the `network`."""

    network_identifiers: DeclinedTransactionSourceCardDeclineNetworkIdentifiers
    """Network-specific identifiers for a specific request or transaction."""

    physical_card_id: Optional[str] = None
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    processing_category: Literal[
        "account_funding", "automatic_fuel_dispenser", "bill_payment", "purchase", "quasi_cash", "refund"
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
    - `purchase` - A regular purchase.
    - `quasi_cash` - Quasi-cash transactions represent purchases of items which may
      be convertible to cash.
    - `refund` - A refund card authorization, sometimes referred to as a credit
      voucher authorization, where funds are credited to the cardholder.
    """

    real_time_decision_id: Optional[str] = None
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    reason: Literal[
        "card_not_active",
        "physical_card_not_active",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "cvv2_mismatch",
        "transaction_not_allowed",
        "breaches_limit",
        "webhook_declined",
        "webhook_timed_out",
        "declined_by_stand_in_processing",
        "invalid_physical_card",
        "missing_original_authorization",
        "suspected_fraud",
    ]
    """Why the transaction was declined.

    - `card_not_active` - The Card was not active.
    - `physical_card_not_active` - The Physical Card was not active.
    - `entity_not_active` - The account's entity was not active.
    - `group_locked` - The account was inactive.
    - `insufficient_funds` - The Card's Account did not have a sufficient available
      balance.
    - `cvv2_mismatch` - The given CVV2 did not match the card's value.
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

    verification: DeclinedTransactionSourceCardDeclineVerification
    """Fields related to verification of cardholder-provided values."""


class DeclinedTransactionSourceCheckDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

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

    front_image_file_id: Optional[str] = None
    """
    The identifier of the API File object containing an image of the front of the
    declined check.
    """

    reason: Literal[
        "ach_route_disabled",
        "ach_route_canceled",
        "breaches_limit",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "stop_payment_requested",
        "duplicate_presentment",
        "not_authorized",
        "amount_mismatch",
        "not_our_item",
        "no_account_number_found",
    ]
    """Why the check was declined.

    - `ach_route_disabled` - The account number is disabled.
    - `ach_route_canceled` - The account number is canceled.
    - `breaches_limit` - The transaction would cause a limit to be exceeded.
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
    """


class DeclinedTransactionSourceInboundRealTimePaymentsTransferDecline(BaseModel):
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


class DeclinedTransactionSourceInternationalACHDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    destination_country_code: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the destination country.
    """

    destination_currency_code: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
    destination bank account.
    """

    foreign_exchange_indicator: Literal["fixed_to_variable", "variable_to_fixed", "fixed_to_fixed"]
    """A description of how the foreign exchange rate was calculated.

    - `fixed_to_variable` - The originator chose an amount in their own currency.
      The settled amount in USD was converted using the exchange rate.
    - `variable_to_fixed` - The originator chose an amount to settle in USD. The
      originator's amount was variable; known only after the foreign exchange
      conversion.
    - `fixed_to_fixed` - The amount was originated and settled as a fixed amount in
      USD. There is no foreign exchange conversion.
    """

    foreign_exchange_reference: Optional[str] = None
    """
    Depending on the `foreign_exchange_reference_indicator`, an exchange rate or a
    reference to a well-known rate.
    """

    foreign_exchange_reference_indicator: Literal["foreign_exchange_rate", "foreign_exchange_reference_number", "blank"]
    """
    An instruction of how to interpret the `foreign_exchange_reference` field for
    this Transaction.

    - `foreign_exchange_rate` - The ACH file contains a foreign exchange rate.
    - `foreign_exchange_reference_number` - The ACH file contains a reference to a
      well-known foreign exchange rate.
    - `blank` - There is no foreign exchange for this transfer, so the
      `foreign_exchange_reference` field is blank.
    """

    foreign_payment_amount: int
    """The amount in the minor unit of the foreign payment currency.

    For dollars, for example, this is cents.
    """

    foreign_trace_number: Optional[str] = None
    """A reference number in the foreign banking infrastructure."""

    international_transaction_type_code: Literal[
        "annuity",
        "business_or_commercial",
        "deposit",
        "loan",
        "miscellaneous",
        "mortgage",
        "pension",
        "remittance",
        "rent_or_lease",
        "salary_or_payroll",
        "tax",
        "accounts_receivable",
        "back_office_conversion",
        "machine_transfer",
        "point_of_purchase",
        "point_of_sale",
        "represented_check",
        "shared_network_transaction",
        "telphone_initiated",
        "internet_initiated",
    ]
    """The type of transfer. Set by the originator.

    - `annuity` - Sent as `ANN` in the Nacha file.
    - `business_or_commercial` - Sent as `BUS` in the Nacha file.
    - `deposit` - Sent as `DEP` in the Nacha file.
    - `loan` - Sent as `LOA` in the Nacha file.
    - `miscellaneous` - Sent as `MIS` in the Nacha file.
    - `mortgage` - Sent as `MOR` in the Nacha file.
    - `pension` - Sent as `PEN` in the Nacha file.
    - `remittance` - Sent as `REM` in the Nacha file.
    - `rent_or_lease` - Sent as `RLS` in the Nacha file.
    - `salary_or_payroll` - Sent as `SAL` in the Nacha file.
    - `tax` - Sent as `TAX` in the Nacha file.
    - `accounts_receivable` - Sent as `ARC` in the Nacha file.
    - `back_office_conversion` - Sent as `BOC` in the Nacha file.
    - `machine_transfer` - Sent as `MTE` in the Nacha file.
    - `point_of_purchase` - Sent as `POP` in the Nacha file.
    - `point_of_sale` - Sent as `POS` in the Nacha file.
    - `represented_check` - Sent as `RCK` in the Nacha file.
    - `shared_network_transaction` - Sent as `SHR` in the Nacha file.
    - `telphone_initiated` - Sent as `TEL` in the Nacha file.
    - `internet_initiated` - Sent as `WEB` in the Nacha file.
    """

    originating_currency_code: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
    originating bank account.
    """

    originating_depository_financial_institution_branch_country: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the originating branch country.
    """

    originating_depository_financial_institution_id: str
    """An identifier for the originating bank.

    One of an International Bank Account Number (IBAN) bank identifier, SWIFT Bank
    Identification Code (BIC), or a domestic identifier like a US Routing Number.
    """

    originating_depository_financial_institution_id_qualifier: Literal[
        "national_clearing_system_number", "bic_code", "iban"
    ]
    """
    An instruction of how to interpret the
    `originating_depository_financial_institution_id` field for this Transaction.

    - `national_clearing_system_number` - A domestic clearing system number. In the
      US, for example, this is the American Banking Association (ABA) routing
      number.
    - `bic_code` - The SWIFT Bank Identifier Code (BIC) of the bank.
    - `iban` - An International Bank Account Number.
    """

    originating_depository_financial_institution_name: str
    """The name of the originating bank.

    Sometimes this will refer to an American bank and obscure the correspondent
    foreign bank.
    """

    originator_city: str
    """A portion of the originator address. This may be incomplete."""

    originator_company_entry_description: str
    """A description field set by the originator."""

    originator_country: str
    """A portion of the originator address.

    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the originator country.
    """

    originator_identification: str
    """An identifier for the originating company.

    This is generally stable across multiple ACH transfers.
    """

    originator_name: str
    """Either the name of the originator or an intermediary money transmitter."""

    originator_postal_code: Optional[str] = None
    """A portion of the originator address. This may be incomplete."""

    originator_state_or_province: Optional[str] = None
    """A portion of the originator address. This may be incomplete."""

    originator_street_address: str
    """A portion of the originator address. This may be incomplete."""

    payment_related_information: Optional[str] = None
    """A description field set by the originator."""

    payment_related_information2: Optional[str] = None
    """A description field set by the originator."""

    receiver_city: str
    """A portion of the receiver address. This may be incomplete."""

    receiver_country: str
    """A portion of the receiver address.

    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the receiver country.
    """

    receiver_identification_number: Optional[str] = None
    """An identification number the originator uses for the receiver."""

    receiver_postal_code: Optional[str] = None
    """A portion of the receiver address. This may be incomplete."""

    receiver_state_or_province: Optional[str] = None
    """A portion of the receiver address. This may be incomplete."""

    receiver_street_address: str
    """A portion of the receiver address. This may be incomplete."""

    receiving_company_or_individual_name: str
    """The name of the receiver of the transfer. This is not verified by Increase."""

    receiving_depository_financial_institution_country: str
    """
    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the receiving bank country.
    """

    receiving_depository_financial_institution_id: str
    """An identifier for the receiving bank.

    One of an International Bank Account Number (IBAN) bank identifier, SWIFT Bank
    Identification Code (BIC), or a domestic identifier like a US Routing Number.
    """

    receiving_depository_financial_institution_id_qualifier: Literal[
        "national_clearing_system_number", "bic_code", "iban"
    ]
    """
    An instruction of how to interpret the
    `receiving_depository_financial_institution_id` field for this Transaction.

    - `national_clearing_system_number` - A domestic clearing system number. In the
      US, for example, this is the American Banking Association (ABA) routing
      number.
    - `bic_code` - The SWIFT Bank Identifier Code (BIC) of the bank.
    - `iban` - An International Bank Account Number.
    """

    receiving_depository_financial_institution_name: str
    """The name of the receiving bank, as set by the sending financial institution."""

    trace_number: str
    """
    A 15 digit number recorded in the Nacha file and available to both the
    originating and receiving bank. Along with the amount, date, and originating
    routing number, this can be used to identify the ACH transfer at either bank.
    ACH trace numbers are not unique, but are
    [used to correlate returns](https://increase.com/documentation/ach#returns).
    """


class DeclinedTransactionSourceWireDecline(BaseModel):
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


class DeclinedTransactionSource(BaseModel):
    ach_decline: Optional[DeclinedTransactionSourceACHDecline] = None
    """An ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_decline`.
    """

    card_decline: Optional[DeclinedTransactionSourceCardDecline] = None
    """A Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_decline`.
    """

    category: Literal[
        "ach_decline",
        "card_decline",
        "check_decline",
        "inbound_real_time_payments_transfer_decline",
        "international_ach_decline",
        "wire_decline",
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
    - `international_ach_decline` - International ACH Decline: details will be under
      the `international_ach_decline` object.
    - `wire_decline` - Wire Decline: details will be under the `wire_decline`
      object.
    - `other` - The Declined Transaction was made for an undocumented or deprecated
      reason.
    """

    check_decline: Optional[DeclinedTransactionSourceCheckDecline] = None
    """A Check Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_decline`.
    """

    inbound_real_time_payments_transfer_decline: Optional[
        DeclinedTransactionSourceInboundRealTimePaymentsTransferDecline
    ] = None
    """An Inbound Real-Time Payments Transfer Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_decline`.
    """

    international_ach_decline: Optional[DeclinedTransactionSourceInternationalACHDecline] = None
    """An International ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `international_ach_decline`.
    """

    wire_decline: Optional[DeclinedTransactionSourceWireDecline] = None
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

    route_type: Optional[Literal["account_number", "card"]] = None
    """The type of the route this Declined Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    """

    source: DeclinedTransactionSource
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


class PendingTransactionSourceAccountTransferInstruction(BaseModel):
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


class PendingTransactionSourceACHTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Pending Transaction."""


class PendingTransactionSourceCardAuthorizationNetworkDetailsVisa(BaseModel):
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


class PendingTransactionSourceCardAuthorizationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[PendingTransactionSourceCardAuthorizationNetworkDetailsVisa] = None
    """Fields specific to the `visa` network."""


class PendingTransactionSourceCardAuthorizationNetworkIdentifiers(BaseModel):
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


class PendingTransactionSourceCardAuthorizationVerificationCardVerificationCode(BaseModel):
    result: Literal["not_checked", "match", "no_match"]
    """The result of verifying the Card Verification Code.

    - `not_checked` - No card verification code was provided in the authorization
      request.
    - `match` - The card verification code matched the one on file.
    - `no_match` - The card verification code did not match the one on file.
    """


class PendingTransactionSourceCardAuthorizationVerificationCardholderAddress(BaseModel):
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

    - `not_checked` - No adress was provided in the authorization request.
    - `postal_code_match_address_not_checked` - Postal code matches, but the street
      address was not verified.
    - `postal_code_match_address_no_match` - Postal code matches, but the street
      address does not match.
    - `postal_code_no_match_address_match` - Postal code does not match, but the
      street address matches.
    - `match` - Postal code and street address match.
    - `no_match` - Postal code and street address do not match.
    """


class PendingTransactionSourceCardAuthorizationVerification(BaseModel):
    card_verification_code: PendingTransactionSourceCardAuthorizationVerificationCardVerificationCode
    """
    Fields related to verification of the Card Verification Code, a 3-digit code on
    the back of the card.
    """

    cardholder_address: PendingTransactionSourceCardAuthorizationVerificationCardholderAddress
    """
    Cardholder address provided in the authorization request and the address on file
    we verified it against.
    """


class PendingTransactionSourceCardAuthorization(BaseModel):
    id: str
    """The Card Authorization identifier."""

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: Optional[str] = None
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
    The direction descibes the direction the funds will move, either from the
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

    merchant_category_code: Optional[str] = None
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str] = None
    """The city the merchant resides in."""

    merchant_country: Optional[str] = None
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    network_details: PendingTransactionSourceCardAuthorizationNetworkDetails
    """Fields specific to the `network`."""

    network_identifiers: PendingTransactionSourceCardAuthorizationNetworkIdentifiers
    """Network-specific identifiers for a specific request or transaction."""

    pending_transaction_id: Optional[str] = None
    """The identifier of the Pending Transaction associated with this Transaction."""

    physical_card_id: Optional[str] = None
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    processing_category: Literal[
        "account_funding", "automatic_fuel_dispenser", "bill_payment", "purchase", "quasi_cash", "refund"
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
    - `purchase` - A regular purchase.
    - `quasi_cash` - Quasi-cash transactions represent purchases of items which may
      be convertible to cash.
    - `refund` - A refund card authorization, sometimes referred to as a credit
      voucher authorization, where funds are credited to the cardholder.
    """

    real_time_decision_id: Optional[str] = None
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    type: Literal["card_authorization"]
    """A constant representing the object's type.

    For this resource it will always be `card_authorization`.
    """

    verification: PendingTransactionSourceCardAuthorizationVerification
    """Fields related to verification of cardholder-provided values."""


class PendingTransactionSourceCheckDepositInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

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


class PendingTransactionSourceCheckTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

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


class PendingTransactionSourceInboundFundsHold(BaseModel):
    id: str
    """The Inbound Funds Hold identifier."""

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


class PendingTransactionSourceRealTimePaymentsTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    transfer_id: str
    """
    The identifier of the Real-Time Payments Transfer that led to this Pending
    Transaction.
    """


class PendingTransactionSourceWireTransferInstruction(BaseModel):
    account_number: str
    """The account number for the destination account."""

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    transfer_id: str
    """The identifier of the Wire Transfer that led to this Pending Transaction."""


class PendingTransactionSource(BaseModel):
    account_transfer_instruction: Optional[PendingTransactionSourceAccountTransferInstruction] = None
    """An Account Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_instruction`.
    """

    ach_transfer_instruction: Optional[PendingTransactionSourceACHTransferInstruction] = None
    """An ACH Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_instruction`.
    """

    card_authorization: Optional[PendingTransactionSourceCardAuthorization] = None
    """A Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization`.
    """

    category: Literal[
        "account_transfer_instruction",
        "ach_transfer_instruction",
        "card_authorization",
        "check_deposit_instruction",
        "check_transfer_instruction",
        "inbound_funds_hold",
        "real_time_payments_transfer_instruction",
        "wire_transfer_instruction",
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
    - `real_time_payments_transfer_instruction` - Real-Time Payments Transfer
      Instruction: details will be under the
      `real_time_payments_transfer_instruction` object.
    - `wire_transfer_instruction` - Wire Transfer Instruction: details will be under
      the `wire_transfer_instruction` object.
    - `other` - The Pending Transaction was made for an undocumented or deprecated
      reason.
    """

    check_deposit_instruction: Optional[PendingTransactionSourceCheckDepositInstruction] = None
    """A Check Deposit Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_instruction`.
    """

    check_transfer_instruction: Optional[PendingTransactionSourceCheckTransferInstruction] = None
    """A Check Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_instruction`.
    """

    inbound_funds_hold: Optional[PendingTransactionSourceInboundFundsHold] = None
    """An Inbound Funds Hold object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_funds_hold`.
    """

    real_time_payments_transfer_instruction: Optional[
        PendingTransactionSourceRealTimePaymentsTransferInstruction
    ] = None
    """A Real-Time Payments Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_instruction`.
    """

    wire_transfer_instruction: Optional[PendingTransactionSourceWireTransferInstruction] = None
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

    route_type: Optional[Literal["account_number", "card"]] = None
    """The type of the route this Pending Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    """

    source: PendingTransactionSource
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


class CardAuthorizationSimulation(BaseModel):
    declined_transaction: Optional[DeclinedTransaction] = None
    """
    If the authorization attempt fails, this will contain the resulting
    [Declined Transaction](#declined-transactions) object. The Declined
    Transaction's `source` will be of `category: card_decline`.
    """

    pending_transaction: Optional[PendingTransaction] = None
    """
    If the authorization attempt succeeds, this will contain the resulting Pending
    Transaction object. The Pending Transaction's `source` will be of
    `category: card_authorization`.
    """

    type: Literal["inbound_card_authorization_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be
    `inbound_card_authorization_simulation_result`.
    """
