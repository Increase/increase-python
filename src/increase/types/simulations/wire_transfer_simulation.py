# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "WireTransferSimulation",
    "Transaction",
    "TransactionSource",
    "TransactionSourceAccountTransferIntention",
    "TransactionSourceACHTransferIntention",
    "TransactionSourceACHTransferRejection",
    "TransactionSourceACHTransferReturn",
    "TransactionSourceCardDisputeAcceptance",
    "TransactionSourceCardRefund",
    "TransactionSourceCardRevenuePayment",
    "TransactionSourceCardSettlement",
    "TransactionSourceCheckDepositAcceptance",
    "TransactionSourceCheckDepositReturn",
    "TransactionSourceCheckTransferDeposit",
    "TransactionSourceCheckTransferIntention",
    "TransactionSourceCheckTransferRejection",
    "TransactionSourceCheckTransferReturn",
    "TransactionSourceCheckTransferStopPaymentRequest",
    "TransactionSourceFeePayment",
    "TransactionSourceInboundACHTransfer",
    "TransactionSourceInboundCheck",
    "TransactionSourceInboundInternationalACHTransfer",
    "TransactionSourceInboundRealTimePaymentsTransferConfirmation",
    "TransactionSourceInboundWireDrawdownPayment",
    "TransactionSourceInboundWireDrawdownPaymentReversal",
    "TransactionSourceInboundWireReversal",
    "TransactionSourceInboundWireTransfer",
    "TransactionSourceInterestPayment",
    "TransactionSourceInternalSource",
    "TransactionSourceRealTimePaymentsTransferAcknowledgement",
    "TransactionSourceSampleFunds",
    "TransactionSourceWireTransferIntention",
    "TransactionSourceWireTransferRejection",
]


class TransactionSourceAccountTransferIntention(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    description: str
    """The description you chose to give the transfer."""

    destination_account_id: str
    """The identifier of the Account to where the Account Transfer was sent."""

    source_account_id: str
    """The identifier of the Account from where the Account Transfer was sent."""

    transfer_id: str
    """The identifier of the Account Transfer that led to this Pending Transaction."""


class TransactionSourceACHTransferIntention(BaseModel):
    account_number: str

    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    routing_number: str

    statement_descriptor: str

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Transaction."""


class TransactionSourceACHTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the ACH Transfer that led to this Transaction."""


class TransactionSourceACHTransferReturn(BaseModel):
    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    raw_return_reason_code: str
    """The three character ACH return code, in the range R01 to R85."""

    return_reason_code: Literal[
        "insufficient_fund",
        "no_account",
        "account_closed",
        "invalid_account_number_structure",
        "account_frozen_entry_returned_per_ofac_instruction",
        "credit_entry_refused_by_receiver",
        "unauthorized_debit_to_consumer_account_using_corporate_sec_code",
        "corporate_customer_advised_not_authorized",
        "payment_stopped",
        "non_transaction_account",
        "uncollected_funds",
        "routing_number_check_digit_error",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "amount_field_error",
        "authorization_revoked_by_customer",
        "invalid_ach_routing_number",
        "file_record_edit_criteria",
        "enr_invalid_individual_name",
        "returned_per_odfi_request",
        "limited_participation_dfi",
        "incorrectly_coded_outbound_international_payment",
        "account_sold_to_another_dfi",
        "addenda_error",
        "beneficiary_or_account_holder_deceased",
        "customer_advised_not_within_authorization_terms",
        "corrected_return",
        "duplicate_entry",
        "duplicate_return",
        "enr_duplicate_enrollment",
        "enr_invalid_dfi_account_number",
        "enr_invalid_individual_id_number",
        "enr_invalid_representative_payee_indicator",
        "enr_invalid_transaction_code",
        "enr_return_of_enr_entry",
        "enr_routing_number_check_digit_error",
        "entry_not_processed_by_gateway",
        "field_error",
        "foreign_receiving_dfi_unable_to_settle",
        "iat_entry_coding_error",
        "improper_effective_entry_date",
        "improper_source_document_source_document_presented",
        "invalid_company_id",
        "invalid_foreign_receiving_dfi_identification",
        "invalid_individual_id_number",
        "item_and_rck_entry_presented_for_payment",
        "item_related_to_rck_entry_is_ineligible",
        "mandatory_field_error",
        "misrouted_dishonored_return",
        "misrouted_return",
        "no_errors_found",
        "non_acceptance_of_r62_dishonored_return",
        "non_participant_in_iat_program",
        "permissible_return_entry",
        "permissible_return_entry_not_accepted",
        "rdfi_non_settlement",
        "rdfi_participant_in_check_truncation_program",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "return_not_a_duplicate",
        "return_of_erroneous_or_reversing_debit",
        "return_of_improper_credit_entry",
        "return_of_improper_debit_entry",
        "return_of_xck_entry",
        "source_document_presented_for_payment",
        "state_law_affecting_rck_acceptance",
        "stop_payment_on_item_related_to_rck_entry",
        "stop_payment_on_source_document",
        "timely_original_return",
        "trace_number_error",
        "untimely_dishonored_return",
        "untimely_return",
    ]
    """Why the ACH Transfer was returned."""

    transaction_id: str
    """The identifier of the Tranasaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class TransactionSourceCardDisputeAcceptance(BaseModel):
    accepted_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was accepted.
    """

    card_dispute_id: str
    """The identifier of the Card Dispute that was accepted."""

    transaction_id: str
    """
    The identifier of the Transaction that was created to return the disputed funds
    to your account.
    """


class TransactionSourceCardRefund(BaseModel):
    id: str
    """The Card Refund identifier."""

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    merchant_acceptor_id: Optional[str]
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: str
    """The 4-digit MCC describing the merchant's business."""

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_name: Optional[str]
    """The name of the merchant."""

    merchant_state: Optional[str]
    """The state the merchant resides in."""

    type: Literal["card_refund"]
    """A constant representing the object's type.

    For this resource it will always be `card_refund`.
    """


class TransactionSourceCardRevenuePayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.
    """

    period_end: datetime
    """The end of the period for which this transaction paid interest."""

    period_start: datetime
    """The start of the period for which this transaction paid interest."""

    transacted_on_account_id: Optional[str]
    """The account the card belonged to."""


class TransactionSourceCardSettlement(BaseModel):
    id: str
    """The Card Settlement identifier."""

    amount: int
    """The amount in the minor unit of the transaction's settlement currency.

    For dollars, for example, this is cents.
    """

    card_authorization: Optional[str]
    """
    The Card Authorization that was created prior to this Card Settlement, if on
    exists.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's settlement currency.
    """

    merchant_acceptor_id: Optional[str]
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: str
    """The 4-digit MCC describing the merchant's business."""

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_name: Optional[str]
    """The name of the merchant."""

    merchant_state: Optional[str]
    """The state the merchant resides in."""

    pending_transaction_id: Optional[str]
    """The identifier of the Pending Transaction associated with this Transaction."""

    presentment_amount: int
    """The amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
    """

    type: Literal["card_settlement"]
    """A constant representing the object's type.

    For this resource it will always be `card_settlement`.
    """


class TransactionSourceCheckDepositAcceptance(BaseModel):
    account_number: str
    """The account number printed on the check."""

    amount: int
    """The amount to be deposited in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    auxiliary_on_us: Optional[str]
    """An additional line of metadata printed on the check.

    This typically includes the check number for business checks.
    """

    check_deposit_id: str
    """The ID of the Check Deposit that was accepted."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    routing_number: str
    """The routing number printed on the check."""

    serial_number: Optional[str]
    """The check serial number, if present, for consumer checks.

    For business checks, the serial number is usually in the `auxiliary_on_us`
    field.
    """


class TransactionSourceCheckDepositReturn(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The identifier of the Check Deposit that was returned."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    return_reason: Literal[
        "ach_conversion_not_supported",
        "closed_account",
        "duplicate_submission",
        "insufficient_funds",
        "no_account",
        "not_authorized",
        "stale_dated",
        "stop_payment",
        "unknown_reason",
        "unmatched_details",
        "unreadable_image",
        "endorsement_irregular",
    ]

    returned_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was returned.
    """

    transaction_id: str
    """
    The identifier of the transaction that reversed the original check deposit
    transaction.
    """


class TransactionSourceCheckTransferDeposit(BaseModel):
    back_image_file_id: Optional[str]
    """
    The identifier of the API File object containing an image of the back of the
    deposited check.
    """

    deposited_at: datetime
    """When the check was deposited."""

    front_image_file_id: Optional[str]
    """
    The identifier of the API File object containing an image of the front of the
    deposited check.
    """

    type: Literal["check_transfer_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_deposit`.
    """


class TransactionSourceCheckTransferIntention(BaseModel):
    address_city: Optional[str]
    """The city of the check's destination."""

    address_line1: Optional[str]
    """The street address of the check's destination."""

    address_line2: Optional[str]
    """The second line of the address of the check's destination."""

    address_state: Optional[str]
    """The state of the check's destination."""

    address_zip: Optional[str]
    """The postal code of the check's destination."""

    amount: int
    """The transfer amount in USD cents."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    recipient_name: Optional[str]
    """The name that will be printed on the check."""

    transfer_id: str
    """The identifier of the Check Transfer with which this is associated."""


class TransactionSourceCheckTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the Check Transfer that led to this Transaction."""


class TransactionSourceCheckTransferReturn(BaseModel):
    file_id: Optional[str]
    """If available, a document with additional information about the return."""

    reason: Literal["mail_delivery_failure", "refused_by_recipient", "returned_not_authorized"]
    """The reason why the check was returned."""

    returned_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check was returned.
    """

    transaction_id: Optional[str]
    """
    The identifier of the Transaction that was created to credit you for the
    returned check.
    """

    transfer_id: str
    """The identifier of the returned Check Transfer."""


class TransactionSourceCheckTransferStopPaymentRequest(BaseModel):
    requested_at: datetime
    """The time the stop-payment was requested."""

    transaction_id: str
    """The transaction ID of the corresponding credit transaction."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
    """


class TransactionSourceFeePayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.
    """


class TransactionSourceInboundACHTransfer(BaseModel):
    amount: int
    """The amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    originator_company_descriptive_date: Optional[str]

    originator_company_discretionary_data: Optional[str]

    originator_company_entry_description: str

    originator_company_id: str

    originator_company_name: str

    receiver_id_number: Optional[str]

    receiver_name: Optional[str]

    trace_number: str


class TransactionSourceInboundCheck(BaseModel):
    amount: int
    """The amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    check_front_image_file_id: Optional[str]

    check_number: Optional[str]

    check_rear_image_file_id: Optional[str]

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """


class TransactionSourceInboundInternationalACHTransfer(BaseModel):
    amount: int
    """The amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    destination_country_code: str

    destination_currency_code: str

    foreign_exchange_indicator: str

    foreign_exchange_reference: Optional[str]

    foreign_exchange_reference_indicator: str

    foreign_payment_amount: int

    foreign_trace_number: Optional[str]

    international_transaction_type_code: str

    originating_currency_code: str

    originating_depository_financial_institution_branch_country: str

    originating_depository_financial_institution_id: str

    originating_depository_financial_institution_id_qualifier: str

    originating_depository_financial_institution_name: str

    originator_city: str

    originator_company_entry_description: str

    originator_country: str

    originator_identification: str

    originator_name: str

    originator_postal_code: Optional[str]

    originator_state_or_province: Optional[str]

    originator_street_address: str

    payment_related_information: Optional[str]

    payment_related_information2: Optional[str]

    receiver_city: str

    receiver_country: str

    receiver_identification_number: Optional[str]

    receiver_postal_code: Optional[str]

    receiver_state_or_province: Optional[str]

    receiver_street_address: str

    receiving_company_or_individual_name: str

    receiving_depository_financial_institution_country: str

    receiving_depository_financial_institution_id: str

    receiving_depository_financial_institution_id_qualifier: str

    receiving_depository_financial_institution_name: str

    trace_number: str


class TransactionSourceInboundRealTimePaymentsTransferConfirmation(BaseModel):
    amount: int
    """The amount in the minor unit of the transfer's currency.

    For dollars, for example, this is cents.
    """

    creditor_name: str
    """The name the sender of the transfer specified as the recipient of the transfer."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code of the transfer's
    currency. This will always be "USD" for a Real Time Payments transfer.
    """

    debtor_account_number: str
    """The account number of the account that sent the transfer."""

    debtor_name: str
    """The name provided by the sender of the transfer."""

    debtor_routing_number: str
    """The routing number of the account that sent the transfer."""

    remittance_information: Optional[str]
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real Time Payments network identification of the transfer"""


class TransactionSourceInboundWireDrawdownPayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    beneficiary_address_line1: Optional[str]

    beneficiary_address_line2: Optional[str]

    beneficiary_address_line3: Optional[str]

    beneficiary_name: Optional[str]

    beneficiary_reference: Optional[str]

    description: str

    input_message_accountability_data: Optional[str]

    originator_address_line1: Optional[str]

    originator_address_line2: Optional[str]

    originator_address_line3: Optional[str]

    originator_name: Optional[str]

    originator_to_beneficiary_information: Optional[str]


class TransactionSourceInboundWireDrawdownPaymentReversal(BaseModel):
    amount: int
    """The amount that was reversed."""

    description: str
    """The description on the reversal message from Fedwire."""

    input_cycle_date: date
    """The Fedwire cycle date for the wire reversal."""

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    previous_message_input_cycle_date: date
    """The Fedwire cycle date for the wire transfer that was reversed."""

    previous_message_input_message_accountability_data: str
    """The Fedwire transaction identifier for the wire transfer that was reversed."""

    previous_message_input_sequence_number: str
    """The Fedwire sequence number for the wire transfer that was reversed."""

    previous_message_input_source: str
    """The Fedwire input source identifier for the wire transfer that was reversed."""


class TransactionSourceInboundWireReversal(BaseModel):
    amount: int
    """The amount that was reversed."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the reversal was created.
    """

    description: str
    """The description on the reversal message from Fedwire."""

    financial_institution_to_financial_institution_information: Optional[str]
    """Additional financial institution information included in the wire reversal."""

    input_cycle_date: date
    """The Fedwire cycle date for the wire reversal."""

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    previous_message_input_cycle_date: date
    """The Fedwire cycle date for the wire transfer that was reversed."""

    previous_message_input_message_accountability_data: str
    """The Fedwire transaction identifier for the wire transfer that was reversed."""

    previous_message_input_sequence_number: str
    """The Fedwire sequence number for the wire transfer that was reversed."""

    previous_message_input_source: str
    """The Fedwire input source identifier for the wire transfer that was reversed."""

    receiver_financial_institution_information: Optional[str]
    """
    Information included in the wire reversal for the receiving financial
    institution.
    """

    transaction_id: Optional[str]
    """The ID for the Transaction associated with the transfer reversal."""

    wire_transfer_id: str
    """The ID for the Wire Transfer that is being reversed."""


class TransactionSourceInboundWireTransfer(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    beneficiary_address_line1: Optional[str]

    beneficiary_address_line2: Optional[str]

    beneficiary_address_line3: Optional[str]

    beneficiary_name: Optional[str]

    beneficiary_reference: Optional[str]

    description: str

    input_message_accountability_data: Optional[str]

    originator_address_line1: Optional[str]

    originator_address_line2: Optional[str]

    originator_address_line3: Optional[str]

    originator_name: Optional[str]

    originator_to_beneficiary_information: Optional[str]

    originator_to_beneficiary_information_line1: Optional[str]

    originator_to_beneficiary_information_line2: Optional[str]

    originator_to_beneficiary_information_line3: Optional[str]

    originator_to_beneficiary_information_line4: Optional[str]


class TransactionSourceInterestPayment(BaseModel):
    accrued_on_account_id: Optional[str]
    """The account on which the interest was accrued."""

    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.
    """

    period_end: datetime
    """The end of the period for which this transaction paid interest."""

    period_start: datetime
    """The start of the period for which this transaction paid interest."""


class TransactionSourceInternalSource(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.
    """

    reason: Literal[
        "account_closure",
        "bank_migration",
        "cashback",
        "collection_receivable",
        "empyreal_adjustment",
        "error",
        "error_correction",
        "fees",
        "interest",
        "negative_balance_forgiveness",
        "sample_funds",
        "sample_funds_return",
    ]


class TransactionSourceRealTimePaymentsTransferAcknowledgement(BaseModel):
    amount: int
    """The transfer amount in USD cents."""

    destination_account_number: str
    """The destination account number."""

    destination_routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""

    transfer_id: str
    """The identifier of the Real Time Payments Transfer that led to this Transaction."""


class TransactionSourceSampleFunds(BaseModel):
    originator: str
    """Where the sample funds came from."""


class TransactionSourceWireTransferIntention(BaseModel):
    account_number: str
    """The destination account number."""

    amount: int
    """The transfer amount in USD cents."""

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    transfer_id: str


class TransactionSourceWireTransferRejection(BaseModel):
    transfer_id: str


class TransactionSource(BaseModel):
    account_transfer_intention: Optional[TransactionSourceAccountTransferIntention]
    """A Account Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_intention`.
    """

    ach_transfer_intention: Optional[TransactionSourceACHTransferIntention]
    """A ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_intention`.
    """

    ach_transfer_rejection: Optional[TransactionSourceACHTransferRejection]
    """A ACH Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_rejection`.
    """

    ach_transfer_return: Optional[TransactionSourceACHTransferReturn]
    """A ACH Transfer Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_return`.
    """

    card_dispute_acceptance: Optional[TransactionSourceCardDisputeAcceptance]
    """A Card Dispute Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_dispute_acceptance`.
    """

    card_refund: Optional[TransactionSourceCardRefund]
    """A Card Refund object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_refund`.
    """

    card_revenue_payment: Optional[TransactionSourceCardRevenuePayment]
    """A Card Revenue Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_revenue_payment`.
    """

    card_settlement: Optional[TransactionSourceCardSettlement]
    """A Card Settlement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_settlement`.
    """

    category: Literal[
        "account_transfer_intention",
        "ach_transfer_intention",
        "ach_transfer_rejection",
        "ach_transfer_return",
        "card_dispute_acceptance",
        "card_refund",
        "card_revenue_payment",
        "card_settlement",
        "check_deposit_acceptance",
        "check_deposit_return",
        "check_transfer_deposit",
        "check_transfer_intention",
        "check_transfer_rejection",
        "check_transfer_return",
        "check_transfer_stop_payment_request",
        "fee_payment",
        "inbound_ach_transfer",
        "inbound_ach_transfer_return_intention",
        "inbound_check",
        "inbound_international_ach_transfer",
        "inbound_real_time_payments_transfer_confirmation",
        "inbound_wire_drawdown_payment",
        "inbound_wire_drawdown_payment_reversal",
        "inbound_wire_reversal",
        "inbound_wire_transfer",
        "interest_payment",
        "internal_source",
        "real_time_payments_transfer_acknowledgement",
        "sample_funds",
        "wire_transfer_intention",
        "wire_transfer_rejection",
        "other",
    ]
    """The type of transaction that took place.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    check_deposit_acceptance: Optional[TransactionSourceCheckDepositAcceptance]
    """A Check Deposit Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_acceptance`.
    """

    check_deposit_return: Optional[TransactionSourceCheckDepositReturn]
    """A Check Deposit Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_return`.
    """

    check_transfer_deposit: Optional[TransactionSourceCheckTransferDeposit]
    """A Check Transfer Deposit object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_deposit`.
    """

    check_transfer_intention: Optional[TransactionSourceCheckTransferIntention]
    """A Check Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_intention`.
    """

    check_transfer_rejection: Optional[TransactionSourceCheckTransferRejection]
    """A Check Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_rejection`.
    """

    check_transfer_return: Optional[TransactionSourceCheckTransferReturn]
    """A Check Transfer Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_return`.
    """

    check_transfer_stop_payment_request: Optional[TransactionSourceCheckTransferStopPaymentRequest]
    """A Check Transfer Stop Payment Request object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_stop_payment_request`.
    """

    fee_payment: Optional[TransactionSourceFeePayment]
    """A Fee Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `fee_payment`.
    """

    inbound_ach_transfer: Optional[TransactionSourceInboundACHTransfer]
    """A Inbound ACH Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_ach_transfer`.
    """

    inbound_check: Optional[TransactionSourceInboundCheck]
    """A Inbound Check object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_check`.
    """

    inbound_international_ach_transfer: Optional[TransactionSourceInboundInternationalACHTransfer]
    """A Inbound International ACH Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_international_ach_transfer`.
    """

    inbound_real_time_payments_transfer_confirmation: Optional[
        TransactionSourceInboundRealTimePaymentsTransferConfirmation
    ]
    """A Inbound Real Time Payments Transfer Confirmation object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_confirmation`.
    """

    inbound_wire_drawdown_payment: Optional[TransactionSourceInboundWireDrawdownPayment]
    """A Inbound Wire Drawdown Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment`.
    """

    inbound_wire_drawdown_payment_reversal: Optional[TransactionSourceInboundWireDrawdownPaymentReversal]
    """A Inbound Wire Drawdown Payment Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment_reversal`.
    """

    inbound_wire_reversal: Optional[TransactionSourceInboundWireReversal]
    """A Inbound Wire Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_reversal`.
    """

    inbound_wire_transfer: Optional[TransactionSourceInboundWireTransfer]
    """A Inbound Wire Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer`.
    """

    interest_payment: Optional[TransactionSourceInterestPayment]
    """A Interest Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `interest_payment`.
    """

    internal_source: Optional[TransactionSourceInternalSource]
    """A Internal Source object.

    This field will be present in the JSON response if and only if `category` is
    equal to `internal_source`.
    """

    real_time_payments_transfer_acknowledgement: Optional[TransactionSourceRealTimePaymentsTransferAcknowledgement]
    """A Real Time Payments Transfer Acknowledgement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_acknowledgement`.
    """

    sample_funds: Optional[TransactionSourceSampleFunds]
    """A Sample Funds object.

    This field will be present in the JSON response if and only if `category` is
    equal to `sample_funds`.
    """

    wire_transfer_intention: Optional[TransactionSourceWireTransferIntention]
    """A Wire Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_intention`.
    """

    wire_transfer_rejection: Optional[TransactionSourceWireTransferRejection]
    """A Wire Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_rejection`.
    """


class Transaction(BaseModel):
    id: str
    """The Transaction identifier."""

    account_id: str
    """The identifier for the Account the Transaction belongs to."""

    amount: int
    """The Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the
    Transaction occured.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    Transaction's currency. This will match the currency on the Transcation's
    Account.
    """

    description: str
    """For a Transaction related to a transfer, this is the description you provide.

    For a Transaction related to a payment, this is the description the vendor
    provides.
    """

    route_id: Optional[str]
    """The identifier for the route this Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card"]]
    """The type of the route this Transaction came through."""

    source: TransactionSource
    """
    This is an object giving more details on the network-level event that caused the
    Transaction. Note that for backwards compatibility reasons, additional
    undocumented keys may appear in this object. These should be treated as
    deprecated and will be removed in the future.
    """

    type: Literal["transaction"]
    """A constant representing the object's type.

    For this resource it will always be `transaction`.
    """


class WireTransferSimulation(BaseModel):
    transaction: Transaction
    """
    If the Wire Transfer attempt succeeds, this will contain the resulting
    [Transaction](#transactions) object. The Transaction's `source` will be of
    `category: inbound_wire_transfer`.
    """

    type: Literal["inbound_wire_transfer_simulation_result"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_wire_transfer_simulation_result`.
    """
