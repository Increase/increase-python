# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Transaction",
    "Source",
    "SourceAccountTransferIntention",
    "SourceACHTransferIntention",
    "SourceACHTransferRejection",
    "SourceACHTransferReturn",
    "SourceCardDisputeAcceptance",
    "SourceCardRefund",
    "SourceCardRevenuePayment",
    "SourceCardSettlement",
    "SourceCheckDepositAcceptance",
    "SourceCheckDepositReturn",
    "SourceCheckTransferDeposit",
    "SourceCheckTransferIntention",
    "SourceCheckTransferRejection",
    "SourceCheckTransferStopPaymentRequest",
    "SourceFeePayment",
    "SourceInboundACHTransfer",
    "SourceInboundCheck",
    "SourceInboundInternationalACHTransfer",
    "SourceInboundRealTimePaymentsTransferConfirmation",
    "SourceInboundWireDrawdownPayment",
    "SourceInboundWireDrawdownPaymentReversal",
    "SourceInboundWireReversal",
    "SourceInboundWireTransfer",
    "SourceInterestPayment",
    "SourceInternalSource",
    "SourceRealTimePaymentsTransferAcknowledgement",
    "SourceSampleFunds",
    "SourceWireTransferIntention",
    "SourceWireTransferRejection",
]


class SourceAccountTransferIntention(BaseModel):
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

    description: str
    """The description you chose to give the transfer."""

    destination_account_id: str
    """The identifier of the Account to where the Account Transfer was sent."""

    source_account_id: str
    """The identifier of the Account from where the Account Transfer was sent."""

    transfer_id: str
    """The identifier of the Account Transfer that led to this Pending Transaction."""


class SourceACHTransferIntention(BaseModel):
    account_number: str

    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    routing_number: str

    statement_descriptor: str

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Transaction."""


class SourceACHTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the ACH Transfer that led to this Transaction."""


class SourceACHTransferReturn(BaseModel):
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
    """Why the ACH Transfer was returned.

    - `insufficient_fund` - Code R01. Insufficient funds in the source account.
    - `no_account` - Code R03. The account does not exist or the receiving bank was
      unable to locate it.
    - `account_closed` - Code R02. The account is closed.
    - `invalid_account_number_structure` - Code R04. The account number is invalid
      at the receiving bank.
    - `account_frozen_entry_returned_per_ofac_instruction` - Code R16. The account
      was frozen per the Office of Foreign Assets Control.
    - `credit_entry_refused_by_receiver` - Code R23. The receiving bank account
      refused a credit transfer.
    - `unauthorized_debit_to_consumer_account_using_corporate_sec_code` - Code R05.
      The receiving bank rejected because of an incorrect Standard Entry Class code.
    - `corporate_customer_advised_not_authorized` - Code R29. The corporate customer
      reversed the transfer.
    - `payment_stopped` - Code R08. The receiving bank stopped payment on this
      transfer.
    - `non_transaction_account` - Code R20. The receiving bank account does not
      perform transfers.
    - `uncollected_funds` - Code R09. The receiving bank account does not have
      enough available balance for the transfer.
    - `routing_number_check_digit_error` - Code R28. The routing number is
      incorrect.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - Code R10.
      The customer reversed the transfer.
    - `amount_field_error` - Code R19. The amount field is incorrect or too large.
    - `authorization_revoked_by_customer` - Code R07. The customer who initiated the
      transfer revoked authorization.
    - `invalid_ach_routing_number` - Code R13. The routing number is invalid.
    - `file_record_edit_criteria` - Code R17. The receiving bank is unable to
      process a field in the transfer.
    - `enr_invalid_individual_name` - Code R45. The individual name field was
      invalid.
    - `returned_per_odfi_request` - Code R06. The originating financial institution
      reversed the transfer.
    - `limited_participation_dfi` - Code R34. The receiving bank's regulatory
      supervisor has limited their participation.
    - `incorrectly_coded_outbound_international_payment` - Code R85. The outbound
      international ACH transfer was incorrect.
    - `account_sold_to_another_dfi` - Code R12. A rare return reason. The account
      was sold to another bank.
    - `addenda_error` - Code R25. The addenda record is incorrect or missing.
    - `beneficiary_or_account_holder_deceased` - Code R15. A rare return reason. The
      account holder is deceased.
    - `customer_advised_not_within_authorization_terms` - Code R11. A rare return
      reason. The customer authorized some payment to the sender, but this payment
      was not in error.
    - `corrected_return` - Code R74. A rare return reason. Sent in response to a
      return that was returned with code `field_error`. The latest return should
      include the corrected field(s).
    - `duplicate_entry` - Code R24. A rare return reason. The receiving bank
      received an exact duplicate entry with the same trace number and amount.
    - `duplicate_return` - Code R67. A rare return reason. The return this message
      refers to was a duplicate.
    - `enr_duplicate_enrollment` - Code R47. A rare return reason. Only used for US
      Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_dfi_account_number` - Code R43. A rare return reason. Only used
      for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_individual_id_number` - Code R44. A rare return reason. Only used
      for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_representative_payee_indicator` - Code R46. A rare return reason.
      Only used for US Government agency non-monetary automatic enrollment messages.
    - `enr_invalid_transaction_code` - Code R41. A rare return reason. Only used for
      US Government agency non-monetary automatic enrollment messages.
    - `enr_return_of_enr_entry` - Code R40. A rare return reason. Only used for US
      Government agency non-monetary automatic enrollment messages.
    - `enr_routing_number_check_digit_error` - Code R42. A rare return reason. Only
      used for US Government agency non-monetary automatic enrollment messages.
    - `entry_not_processed_by_gateway` - Code R84. A rare return reason. The
      International ACH Transfer cannot be processed by the gateway.
    - `field_error` - Code R69. A rare return reason. One or more of the fields in
      the ACH were malformed.
    - `foreign_receiving_dfi_unable_to_settle` - Code R83. A rare return reason. The
      Foreign receiving bank was unable to settle this ACH transfer.
    - `iat_entry_coding_error` - Code R80. A rare return reason. The International
      ACH Transfer is malformed.
    - `improper_effective_entry_date` - Code R18. A rare return reason. The ACH has
      an improper effective entry date field.
    - `improper_source_document_source_document_presented` - Code R39. A rare return
      reason. The source document related to this ACH, usually an ACH check
      conversion, was presented to the bank.
    - `invalid_company_id` - Code R21. A rare return reason. The Company ID field of
      the ACH was invalid.
    - `invalid_foreign_receiving_dfi_identification` - Code R82. A rare return
      reason. The foreign receiving bank identifier for an International ACH
      Transfer was invalid.
    - `invalid_individual_id_number` - Code R22. A rare return reason. The
      Individual ID number field of the ACH was invalid.
    - `item_and_rck_entry_presented_for_payment` - Code R53. A rare return reason.
      Both the Represented Check ("RCK") entry and the original check were presented
      to the bank.
    - `item_related_to_rck_entry_is_ineligible` - Code R51. A rare return reason.
      The Represented Check ("RCK") entry is ineligible.
    - `mandatory_field_error` - Code R26. A rare return reason. The ACH is missing a
      required field.
    - `misrouted_dishonored_return` - Code R71. A rare return reason. The receiving
      bank does not recognize the routing number in a dishonored return entry.
    - `misrouted_return` - Code R61. A rare return reason. The receiving bank does
      not recognize the routing number in a return entry.
    - `no_errors_found` - Code R76. A rare return reason. Sent in response to a
      return, the bank does not find the errors alleged by the returning bank.
    - `non_acceptance_of_r62_dishonored_return` - Code R77. A rare return reason.
      The receiving bank does not accept the return of the erroneous debit. The
      funds are not available at the receiving bank.
    - `non_participant_in_iat_program` - Code R81. A rare return reason. The
      receiving bank does not accept International ACH Transfers.
    - `permissible_return_entry` - Code R31. A rare return reason. A return that has
      been agreed to be accepted by the receiving bank, despite falling outside of
      the usual return timeframe.
    - `permissible_return_entry_not_accepted` - Code R70. A rare return reason. The
      receiving bank had not approved this return.
    - `rdfi_non_settlement` - Code R32. A rare return reason. The receiving bank
      could not settle this transaction.
    - `rdfi_participant_in_check_truncation_program` - Code R30. A rare return
      reason. The receiving bank does not accept Check Truncation ACH transfers.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - Code
      R14. A rare return reason. The payee is deceased.
    - `return_not_a_duplicate` - Code R75. A rare return reason. The originating
      bank disputes that an earlier `duplicate_entry` return was actually a
      duplicate.
    - `return_of_erroneous_or_reversing_debit` - Code R62. A rare return reason. The
      originating bank made a mistake earlier and this return corrects it.
    - `return_of_improper_credit_entry` - Code R36. A rare return reason. Return of
      a malformed credit entry.
    - `return_of_improper_debit_entry` - Code R35. A rare return reason. Return of a
      malformed debit entry.
    - `return_of_xck_entry` - Code R33. A rare return reason. Return of a Destroyed
      Check ("XKC") entry.
    - `source_document_presented_for_payment` - Code R37. A rare return reason. The
      source document related to this ACH, usually an ACH check conversion, was
      presented to the bank.
    - `state_law_affecting_rck_acceptance` - Code R50. A rare return reason. State
      law prevents the bank from accepting the Represented Check ("RCK") entry.
    - `stop_payment_on_item_related_to_rck_entry` - Code R52. A rare return reason.
      A stop payment was issued on a Represented Check ("RCK") entry.
    - `stop_payment_on_source_document` - Code R38. A rare return reason. The source
      attached to the ACH, usually an ACH check conversion, includes a stop payment.
    - `timely_original_return` - Code R73. A rare return reason. The bank receiving
      an `untimely_return` believes it was on time.
    - `trace_number_error` - Code R27. A rare return reason. An ACH Return's trace
      number does not match an originated ACH.
    - `untimely_dishonored_return` - Code R72. A rare return reason. The dishonored
      return was sent too late.
    - `untimely_return` - Code R68. A rare return reason. The return was sent too
      late.
    """

    transaction_id: str
    """The identifier of the Tranasaction associated with this return."""

    transfer_id: str
    """The identifier of the ACH Transfer associated with this return."""


class SourceCardDisputeAcceptance(BaseModel):
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


class SourceCardRefund(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
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

    transaction_id: str
    """The identifier of the Transaction associated with this Transaction."""

    type: Literal["card_refund"]
    """A constant representing the object's type.

    For this resource it will always be `card_refund`.
    """


class SourceCardRevenuePayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    period_end: datetime
    """The end of the period for which this transaction paid interest."""

    period_start: datetime
    """The start of the period for which this transaction paid interest."""

    transacted_on_account_id: Optional[str]
    """The account the card belonged to."""


class SourceCardSettlement(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
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

    transaction_id: str
    """The identifier of the Transaction associated with this Transaction."""

    type: Literal["card_settlement"]
    """A constant representing the object's type.

    For this resource it will always be `card_settlement`.
    """


class SourceCheckDepositAcceptance(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    routing_number: str
    """The routing number printed on the check."""

    serial_number: Optional[str]
    """The check serial number, if present, for consumer checks.

    For business checks, the serial number is usually in the `auxiliary_on_us`
    field.
    """


class SourceCheckDepositReturn(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
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
    """
    - `ach_conversion_not_supported` - The check doesn't allow ACH conversion.
    - `closed_account` - The account is closed.
    - `duplicate_submission` - The check has already been deposited.
    - `insufficient_funds` - Insufficient funds
    - `no_account` - No account was found matching the check details.
    - `not_authorized` - The check was not authorized.
    - `stale_dated` - The check is too old.
    - `stop_payment` - The payment has been stopped by the account holder.
    - `unknown_reason` - The reason for the return is unknown.
    - `unmatched_details` - The image doesn't match the details submitted.
    - `unreadable_image` - The image could not be read.
    - `endorsement_irregular` - The check endorsement was irregular.
    """

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


class SourceCheckTransferDeposit(BaseModel):
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

    transaction_id: Optional[str]
    """The identifier of the Transaction object created when the check was deposited."""

    type: Literal["check_transfer_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_deposit`.
    """


class SourceCheckTransferIntention(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    recipient_name: Optional[str]
    """The name that will be printed on the check."""

    transfer_id: str
    """The identifier of the Check Transfer with which this is associated."""


class SourceCheckTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the Check Transfer that led to this Transaction."""


class SourceCheckTransferStopPaymentRequest(BaseModel):
    reason: Literal["mail_delivery_failed", "unknown"]
    """The reason why this transfer was stopped.

    - `mail_delivery_failed` - The check could not be delivered.
    - `unknown` - The check was stopped for another reason.
    """

    requested_at: datetime
    """The time the stop-payment was requested."""

    transfer_id: str
    """The ID of the check transfer that was stopped."""

    type: Literal["check_transfer_stop_payment_request"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_stop_payment_request`.
    """


class SourceFeePayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    fee_period_start: date
    """The start of this payment's fee period, usually the first day of a month."""


class SourceInboundACHTransfer(BaseModel):
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


class SourceInboundCheck(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """


class SourceInboundInternationalACHTransfer(BaseModel):
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


class SourceInboundRealTimePaymentsTransferConfirmation(BaseModel):
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

    remittance_information: Optional[str]
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real Time Payments network identification of the transfer"""


class SourceInboundWireDrawdownPayment(BaseModel):
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


class SourceInboundWireDrawdownPaymentReversal(BaseModel):
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


class SourceInboundWireReversal(BaseModel):
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


class SourceInboundWireTransfer(BaseModel):
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


class SourceInterestPayment(BaseModel):
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    period_end: datetime
    """The end of the period for which this transaction paid interest."""

    period_start: datetime
    """The start of the period for which this transaction paid interest."""


class SourceInternalSource(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
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
    """
    - `account_closure` - Account closure
    - `bank_migration` - Bank migration
    - `cashback` - Cashback
    - `collection_receivable` - Collection receivable
    - `empyreal_adjustment` - Empyreal adjustment
    - `error` - Error
    - `error_correction` - Error correction
    - `fees` - Fees
    - `interest` - Interest
    - `negative_balance_forgiveness` - Negative balance forgiveness
    - `sample_funds` - Sample funds
    - `sample_funds_return` - Sample funds return
    """


class SourceRealTimePaymentsTransferAcknowledgement(BaseModel):
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


class SourceSampleFunds(BaseModel):
    originator: str
    """Where the sample funds came from."""


class SourceWireTransferIntention(BaseModel):
    account_number: str
    """The destination account number."""

    amount: int
    """The transfer amount in USD cents."""

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    transfer_id: str


class SourceWireTransferRejection(BaseModel):
    transfer_id: str


class Source(BaseModel):
    account_transfer_intention: Optional[SourceAccountTransferIntention]
    """A Account Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_intention`.
    """

    ach_transfer_intention: Optional[SourceACHTransferIntention]
    """A ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_intention`.
    """

    ach_transfer_rejection: Optional[SourceACHTransferRejection]
    """A ACH Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_rejection`.
    """

    ach_transfer_return: Optional[SourceACHTransferReturn]
    """A ACH Transfer Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_return`.
    """

    card_dispute_acceptance: Optional[SourceCardDisputeAcceptance]
    """A Card Dispute Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_dispute_acceptance`.
    """

    card_refund: Optional[SourceCardRefund]
    """A Card Refund object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_refund`.
    """

    card_revenue_payment: Optional[SourceCardRevenuePayment]
    """A Card Revenue Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_revenue_payment`.
    """

    card_settlement: Optional[SourceCardSettlement]
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

    - `account_transfer_intention` - The Transaction was created by a Account
      Transfer Intention object. Details will be under the
      `account_transfer_intention` object.
    - `ach_transfer_intention` - The Transaction was created by a ACH Transfer
      Intention object. Details will be under the `ach_transfer_intention` object.
    - `ach_transfer_rejection` - The Transaction was created by a ACH Transfer
      Rejection object. Details will be under the `ach_transfer_rejection` object.
    - `ach_transfer_return` - The Transaction was created by a ACH Transfer Return
      object. Details will be under the `ach_transfer_return` object.
    - `card_dispute_acceptance` - The Transaction was created by a Card Dispute
      Acceptance object. Details will be under the `card_dispute_acceptance` object.
    - `card_refund` - The Transaction was created by a Card Refund object. Details
      will be under the `card_refund` object.
    - `card_revenue_payment` - The Transaction was created by a Card Revenue Payment
      object. Details will be under the `card_revenue_payment` object.
    - `card_settlement` - The Transaction was created by a Card Settlement object.
      Details will be under the `card_settlement` object.
    - `check_deposit_acceptance` - The Transaction was created by a Check Deposit
      Acceptance object. Details will be under the `check_deposit_acceptance`
      object.
    - `check_deposit_return` - The Transaction was created by a Check Deposit Return
      object. Details will be under the `check_deposit_return` object.
    - `check_transfer_deposit` - The Transaction was created by a Check Transfer
      Deposit object. Details will be under the `check_transfer_deposit` object.
    - `check_transfer_intention` - The Transaction was created by a Check Transfer
      Intention object. Details will be under the `check_transfer_intention` object.
    - `check_transfer_rejection` - The Transaction was created by a Check Transfer
      Rejection object. Details will be under the `check_transfer_rejection` object.
    - `check_transfer_stop_payment_request` - The Transaction was created by a Check
      Transfer Stop Payment Request object. Details will be under the
      `check_transfer_stop_payment_request` object.
    - `fee_payment` - The Transaction was created by a Fee Payment object. Details
      will be under the `fee_payment` object.
    - `inbound_ach_transfer` - The Transaction was created by a Inbound ACH Transfer
      object. Details will be under the `inbound_ach_transfer` object.
    - `inbound_ach_transfer_return_intention` - The Transaction was created by a
      Inbound ACH Transfer Return Intention object. Details will be under the
      `inbound_ach_transfer_return_intention` object.
    - `inbound_check` - The Transaction was created by a Inbound Check object.
      Details will be under the `inbound_check` object.
    - `inbound_international_ach_transfer` - The Transaction was created by a
      Inbound International ACH Transfer object. Details will be under the
      `inbound_international_ach_transfer` object.
    - `inbound_real_time_payments_transfer_confirmation` - The Transaction was
      created by a Inbound Real Time Payments Transfer Confirmation object. Details
      will be under the `inbound_real_time_payments_transfer_confirmation` object.
    - `inbound_wire_drawdown_payment` - The Transaction was created by a Inbound
      Wire Drawdown Payment object. Details will be under the
      `inbound_wire_drawdown_payment` object.
    - `inbound_wire_drawdown_payment_reversal` - The Transaction was created by a
      Inbound Wire Drawdown Payment Reversal object. Details will be under the
      `inbound_wire_drawdown_payment_reversal` object.
    - `inbound_wire_reversal` - The Transaction was created by a Inbound Wire
      Reversal object. Details will be under the `inbound_wire_reversal` object.
    - `inbound_wire_transfer` - The Transaction was created by a Inbound Wire
      Transfer object. Details will be under the `inbound_wire_transfer` object.
    - `interest_payment` - The Transaction was created by a Interest Payment object.
      Details will be under the `interest_payment` object.
    - `internal_source` - The Transaction was created by a Internal Source object.
      Details will be under the `internal_source` object.
    - `real_time_payments_transfer_acknowledgement` - The Transaction was created by
      a Real Time Payments Transfer Acknowledgement object. Details will be under
      the `real_time_payments_transfer_acknowledgement` object.
    - `sample_funds` - The Transaction was created by a Sample Funds object. Details
      will be under the `sample_funds` object.
    - `wire_transfer_intention` - The Transaction was created by a Wire Transfer
      Intention object. Details will be under the `wire_transfer_intention` object.
    - `wire_transfer_rejection` - The Transaction was created by a Wire Transfer
      Rejection object. Details will be under the `wire_transfer_rejection` object.
    - `other` - The Transaction was made for an undocumented or deprecated reason.
    """

    check_deposit_acceptance: Optional[SourceCheckDepositAcceptance]
    """A Check Deposit Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_acceptance`.
    """

    check_deposit_return: Optional[SourceCheckDepositReturn]
    """A Check Deposit Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_return`.
    """

    check_transfer_deposit: Optional[SourceCheckTransferDeposit]
    """A Check Transfer Deposit object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_deposit`.
    """

    check_transfer_intention: Optional[SourceCheckTransferIntention]
    """A Check Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_intention`.
    """

    check_transfer_rejection: Optional[SourceCheckTransferRejection]
    """A Check Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_rejection`.
    """

    check_transfer_stop_payment_request: Optional[SourceCheckTransferStopPaymentRequest]
    """A Check Transfer Stop Payment Request object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_stop_payment_request`.
    """

    fee_payment: Optional[SourceFeePayment]
    """A Fee Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `fee_payment`.
    """

    inbound_ach_transfer: Optional[SourceInboundACHTransfer]
    """A Inbound ACH Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_ach_transfer`.
    """

    inbound_check: Optional[SourceInboundCheck]
    """A Inbound Check object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_check`.
    """

    inbound_international_ach_transfer: Optional[SourceInboundInternationalACHTransfer]
    """A Inbound International ACH Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_international_ach_transfer`.
    """

    inbound_real_time_payments_transfer_confirmation: Optional[SourceInboundRealTimePaymentsTransferConfirmation]
    """A Inbound Real Time Payments Transfer Confirmation object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_confirmation`.
    """

    inbound_wire_drawdown_payment: Optional[SourceInboundWireDrawdownPayment]
    """A Inbound Wire Drawdown Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment`.
    """

    inbound_wire_drawdown_payment_reversal: Optional[SourceInboundWireDrawdownPaymentReversal]
    """A Inbound Wire Drawdown Payment Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment_reversal`.
    """

    inbound_wire_reversal: Optional[SourceInboundWireReversal]
    """A Inbound Wire Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_reversal`.
    """

    inbound_wire_transfer: Optional[SourceInboundWireTransfer]
    """A Inbound Wire Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer`.
    """

    interest_payment: Optional[SourceInterestPayment]
    """A Interest Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `interest_payment`.
    """

    internal_source: Optional[SourceInternalSource]
    """A Internal Source object.

    This field will be present in the JSON response if and only if `category` is
    equal to `internal_source`.
    """

    real_time_payments_transfer_acknowledgement: Optional[SourceRealTimePaymentsTransferAcknowledgement]
    """A Real Time Payments Transfer Acknowledgement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_acknowledgement`.
    """

    sample_funds: Optional[SourceSampleFunds]
    """A Sample Funds object.

    This field will be present in the JSON response if and only if `category` is
    equal to `sample_funds`.
    """

    wire_transfer_intention: Optional[SourceWireTransferIntention]
    """A Wire Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_intention`.
    """

    wire_transfer_rejection: Optional[SourceWireTransferRejection]
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

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    description: str
    """An informational message describing this transaction.

    Use the fields in `source` to get more detailed information. This field appears
    as the line-item on the statement.
    """

    route_id: Optional[str]
    """The identifier for the route this Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card"]]
    """The type of the route this Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    """

    source: Source
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
