# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "TransactionSourceAccountTransferIntention",
    "TransactionSourceACHCheckConversionReturn",
    "TransactionSourceACHCheckConversion",
    "TransactionSourceACHTransferIntention",
    "TransactionSourceACHTransferRejection",
    "TransactionSourceACHTransferReturn",
    "TransactionSourceCardDisputeAcceptance",
    "TransactionSourceCardRefund",
    "TransactionSourceCardSettlement",
    "TransactionSourceCheckDepositAcceptance",
    "TransactionSourceCheckDepositReturn",
    "TransactionSourceCheckTransferIntention",
    "TransactionSourceCheckTransferRejection",
    "TransactionSourceCheckTransferStopPaymentRequest",
    "TransactionSourceDisputeResolution",
    "TransactionSourceEmpyrealCashDeposit",
    "TransactionSourceInboundACHTransfer",
    "TransactionSourceInboundCheck",
    "TransactionSourceInboundInternationalACHTransfer",
    "TransactionSourceInboundWireDrawdownPaymentReversal",
    "TransactionSourceInboundWireDrawdownPayment",
    "TransactionSourceInboundWireReversal",
    "TransactionSourceInboundWireTransfer",
    "TransactionSourceInternalSource",
    "TransactionSourceCardRouteRefund",
    "TransactionSourceCardRouteSettlement",
    "TransactionSourceWireDrawdownPaymentIntention",
    "TransactionSourceWireDrawdownPaymentRejection",
    "TransactionSourceWireTransferIntention",
    "TransactionSourceWireTransferRejection",
    "TransactionSource",
    "Transaction",
    "WireTransferSimulation",
]


class TransactionSourceAccountTransferIntention(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
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


class TransactionSourceACHCheckConversionReturn(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    return_reason_code: str
    """Why the transfer was returned."""


class TransactionSourceACHCheckConversion(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    file_id: str
    """The identifier of the File containing an image of the returned check."""


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
    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

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
        "addenda_error",
        "limited_participation_dfi",
        "other",
    ]
    """Why the ACH Transfer was returned."""

    transaction_id: str
    """The identifier of the Tranasaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class TransactionSourceCardDisputeAcceptance(BaseModel):
    accepted_at: str
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
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    card_settlement_transaction_id: Optional[str]
    """The identifier for the Transaction this refunds, if any."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    type: Literal["card_refund"]
    """A constant representing the object's type.

    For this resource it will always be `card_refund`.
    """


class TransactionSourceCardSettlement(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    merchant_category_code: str

    merchant_city: Optional[str]

    merchant_country: str

    merchant_name: Optional[str]

    merchant_state: Optional[str]

    type: Literal["card_settlement"]
    """A constant representing the object's type.

    For this resource it will always be `card_settlement`.
    """


class TransactionSourceCheckDepositAcceptance(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The ID of the Check Deposit that led to the Transaction."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """


class TransactionSourceCheckDepositReturn(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    check_deposit_id: str
    """The identifier of the Check Deposit that was returned."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    return_reason: Literal[
        "ach_conversion_not_supported",
        "duplicate_submission",
        "insufficient_funds",
        "no_account",
        "unmatched_details",
        "unreadable_image",
        "unknown_reason",
        "not_authorized",
    ]

    returned_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the check deposit was returned.
    """

    transaction_id: str
    """
    The identifier of the transaction that reversed the original check deposit
    transaction.
    """


class TransactionSourceCheckTransferIntention(BaseModel):
    address_city: str
    """The city of the check's destination."""

    address_line1: str
    """The street address of the check's destination."""

    address_line2: Optional[str]
    """The second line of the address of the check's destination."""

    address_state: str
    """The state of the check's destination."""

    address_zip: str
    """The postal code of the check's destination."""

    amount: int
    """The transfer amount in USD cents."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    recipient_name: str
    """The name that will be printed on the check."""

    transfer_id: str
    """The identifier of the Check Transfer with which this is associated."""


class TransactionSourceCheckTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the Check Transfer that led to this Transaction."""


class TransactionSourceCheckTransferStopPaymentRequest(BaseModel):
    requested_at: str
    """The time the stop-payment was requested."""

    transaction_id: str
    """The transaction ID of the corresponding credit transaction."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
    """


class TransactionSourceDisputeResolution(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    disputed_transaction_id: str
    """The identifier of the Transaction that was disputed."""


class TransactionSourceEmpyrealCashDeposit(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    bag_id: str

    deposit_date: str


class TransactionSourceInboundACHTransfer(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

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
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    check_front_image_file_id: Optional[str]

    check_number: Optional[str]

    check_rear_image_file_id: Optional[str]

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """


class TransactionSourceInboundInternationalACHTransfer(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

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


class TransactionSourceInboundWireDrawdownPaymentReversal(BaseModel):
    amount: int
    """The amount that was reversed."""

    description: str
    """The description on the reversal message from Fedwire."""

    input_cycle_date: str
    """The Fedwire cycle date for the wire reversal."""

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    previous_message_input_cycle_date: str
    """The Fedwire cycle date for the wire transfer that was reversed."""

    previous_message_input_message_accountability_data: str
    """The Fedwire transaction identifier for the wire transfer that was reversed."""

    previous_message_input_sequence_number: str
    """The Fedwire sequence number for the wire transfer that was reversed."""

    previous_message_input_source: str
    """The Fedwire input source identifier for the wire transfer that was reversed."""


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


class TransactionSourceInboundWireReversal(BaseModel):
    amount: int
    """The amount that was reversed."""

    description: str
    """The description on the reversal message from Fedwire."""

    financial_institution_to_financial_institution_information: Optional[str]
    """Additional financial institution information included in the wire reversal."""

    input_cycle_date: str
    """The Fedwire cycle date for the wire reversal."""

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    previous_message_input_cycle_date: str
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


class TransactionSourceInternalSource(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.
    """

    reason: Literal["cashback", "error", "error_correction", "fees", "interest", "sample_funds"]


class TransactionSourceCardRouteRefund(BaseModel):
    amount: int
    """The refunded amount in the minor unit of the refunded currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the refund
    currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: Optional[str]

    merchant_city: Optional[str]

    merchant_country: str

    merchant_descriptor: str

    merchant_state: Optional[str]


class TransactionSourceCardRouteSettlement(BaseModel):
    amount: int
    """The settled amount in the minor unit of the settlement currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the settlement
    currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: Optional[str]

    merchant_city: Optional[str]

    merchant_country: Optional[str]

    merchant_descriptor: str

    merchant_state: Optional[str]


class TransactionSourceWireDrawdownPaymentIntention(BaseModel):
    account_number: str

    amount: int
    """The transfer amount in USD cents."""

    message_to_recipient: str

    routing_number: str

    transfer_id: str


class TransactionSourceWireDrawdownPaymentRejection(BaseModel):
    transfer_id: str


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

    ach_check_conversion: Optional[TransactionSourceACHCheckConversion]
    """A ACH Check Conversion object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_check_conversion`.
    """

    ach_check_conversion_return: Optional[TransactionSourceACHCheckConversionReturn]
    """A ACH Check Conversion Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_check_conversion_return`.
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

    card_route_refund: Optional[TransactionSourceCardRouteRefund]
    """A Deprecated Card Refund object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_route_refund`.
    """

    card_route_settlement: Optional[TransactionSourceCardRouteSettlement]
    """A Deprecated Card Settlement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_route_settlement`.
    """

    card_settlement: Optional[TransactionSourceCardSettlement]
    """A Card Settlement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_settlement`.
    """

    category: Literal[
        "account_transfer_intention",
        "ach_check_conversion_return",
        "ach_check_conversion",
        "ach_transfer_intention",
        "ach_transfer_rejection",
        "ach_transfer_return",
        "card_dispute_acceptance",
        "card_refund",
        "card_settlement",
        "check_deposit_acceptance",
        "check_deposit_return",
        "check_transfer_intention",
        "check_transfer_rejection",
        "check_transfer_stop_payment_request",
        "dispute_resolution",
        "empyreal_cash_deposit",
        "inbound_ach_transfer",
        "inbound_check",
        "inbound_international_ach_transfer",
        "inbound_real_time_payments_transfer_confirmation",
        "inbound_wire_drawdown_payment_reversal",
        "inbound_wire_drawdown_payment",
        "inbound_wire_reversal",
        "inbound_wire_transfer",
        "internal_source",
        "card_route_refund",
        "card_route_settlement",
        "real_time_payments_transfer_acknowledgement",
        "sample_funds",
        "wire_drawdown_payment_intention",
        "wire_drawdown_payment_rejection",
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

    check_transfer_stop_payment_request: Optional[TransactionSourceCheckTransferStopPaymentRequest]
    """A Check Transfer Stop Payment Request object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_stop_payment_request`.
    """

    dispute_resolution: Optional[TransactionSourceDisputeResolution]
    """A Dispute Resolution object.

    This field will be present in the JSON response if and only if `category` is
    equal to `dispute_resolution`.
    """

    empyreal_cash_deposit: Optional[TransactionSourceEmpyrealCashDeposit]
    """A Empyreal Cash Deposit object.

    This field will be present in the JSON response if and only if `category` is
    equal to `empyreal_cash_deposit`.
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

    internal_source: Optional[TransactionSourceInternalSource]
    """A Internal Source object.

    This field will be present in the JSON response if and only if `category` is
    equal to `internal_source`.
    """

    sample_funds: Optional[object]
    """A Sample Funds object.

    This field will be present in the JSON response if and only if `category` is
    equal to `sample_funds`.
    """

    wire_drawdown_payment_intention: Optional[TransactionSourceWireDrawdownPaymentIntention]
    """A Wire Drawdown Payment Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_drawdown_payment_intention`.
    """

    wire_drawdown_payment_rejection: Optional[TransactionSourceWireDrawdownPaymentRejection]
    """A Wire Drawdown Payment Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_drawdown_payment_rejection`.
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
    account_id: str
    """The identifier for the Account the Transaction belongs to."""

    amount: int
    """The Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the
    Transaction occured.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    Transaction's currency. This will match the currency on the Transcation's
    Account.
    """

    description: str
    """
    For a Transaction related to a transfer, this is the description you provide.
    For a Transaction related to a payment, this is the description the vendor
    provides.
    """

    id: str
    """The Transaction identifier."""

    route_id: str
    """The identifier for the route this Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[str]
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
