# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Transaction",
    "Source",
    "SourceAccountRevenuePayment",
    "SourceAccountTransferIntention",
    "SourceACHTransferIntention",
    "SourceACHTransferRejection",
    "SourceACHTransferReturn",
    "SourceCardDisputeAcceptance",
    "SourceCardDisputeFinancial",
    "SourceCardDisputeFinancialVisa",
    "SourceCardDisputeLoss",
    "SourceCardPushTransferAcceptance",
    "SourceCardRefund",
    "SourceCardRefundCashback",
    "SourceCardRefundInterchange",
    "SourceCardRefundNetworkIdentifiers",
    "SourceCardRefundPurchaseDetails",
    "SourceCardRefundPurchaseDetailsCarRental",
    "SourceCardRefundPurchaseDetailsLodging",
    "SourceCardRefundPurchaseDetailsTravel",
    "SourceCardRefundPurchaseDetailsTravelAncillary",
    "SourceCardRefundPurchaseDetailsTravelAncillaryService",
    "SourceCardRefundPurchaseDetailsTravelTripLeg",
    "SourceCardRevenuePayment",
    "SourceCardSettlement",
    "SourceCardSettlementCashback",
    "SourceCardSettlementInterchange",
    "SourceCardSettlementNetworkIdentifiers",
    "SourceCardSettlementPurchaseDetails",
    "SourceCardSettlementPurchaseDetailsCarRental",
    "SourceCardSettlementPurchaseDetailsLodging",
    "SourceCardSettlementPurchaseDetailsTravel",
    "SourceCardSettlementPurchaseDetailsTravelAncillary",
    "SourceCardSettlementPurchaseDetailsTravelAncillaryService",
    "SourceCardSettlementPurchaseDetailsTravelTripLeg",
    "SourceCashbackPayment",
    "SourceCheckDepositAcceptance",
    "SourceCheckDepositReturn",
    "SourceCheckTransferDeposit",
    "SourceFeePayment",
    "SourceInboundACHTransfer",
    "SourceInboundACHTransferAddenda",
    "SourceInboundACHTransferAddendaFreeform",
    "SourceInboundACHTransferAddendaFreeformEntry",
    "SourceInboundACHTransferReturnIntention",
    "SourceInboundCheckAdjustment",
    "SourceInboundCheckDepositReturnIntention",
    "SourceInboundRealTimePaymentsTransferConfirmation",
    "SourceInboundWireReversal",
    "SourceInboundWireTransfer",
    "SourceInboundWireTransferReversal",
    "SourceInterestPayment",
    "SourceInternalSource",
    "SourceRealTimePaymentsTransferAcknowledgement",
    "SourceSampleFunds",
    "SourceSwiftTransferIntention",
    "SourceSwiftTransferReturn",
    "SourceWireTransferIntention",
]


class SourceAccountRevenuePayment(BaseModel):
    accrued_on_account_id: str
    """The account on which the account revenue was accrued."""

    period_end: datetime
    """The end of the period for which this transaction paid account revenue."""

    period_start: datetime
    """The start of the period for which this transaction paid account revenue."""


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
    """The account number for the destination account."""

    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    statement_descriptor: str
    """A description set when the ACH Transfer was created."""

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

    This reason code is sent by the receiving bank back to Increase.

    - `insufficient_fund` - Code R01. Insufficient funds in the receiving account.
      Sometimes abbreviated to NSF.
    - `no_account` - Code R03. The account does not exist or the receiving bank was
      unable to locate it.
    - `account_closed` - Code R02. The account is closed at the receiving bank.
    - `invalid_account_number_structure` - Code R04. The account number is invalid
      at the receiving bank.
    - `account_frozen_entry_returned_per_ofac_instruction` - Code R16. The account
      at the receiving bank was frozen per the Office of Foreign Assets Control.
    - `credit_entry_refused_by_receiver` - Code R23. The receiving bank account
      refused a credit transfer.
    - `unauthorized_debit_to_consumer_account_using_corporate_sec_code` - Code R05.
      The receiving bank rejected because of an incorrect Standard Entry Class code.
    - `corporate_customer_advised_not_authorized` - Code R29. The corporate customer
      at the receiving bank reversed the transfer.
    - `payment_stopped` - Code R08. The receiving bank stopped payment on this
      transfer.
    - `non_transaction_account` - Code R20. The receiving bank account does not
      perform transfers.
    - `uncollected_funds` - Code R09. The receiving bank account does not have
      enough available balance for the transfer.
    - `routing_number_check_digit_error` - Code R28. The routing number is
      incorrect.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - Code R10.
      The customer at the receiving bank reversed the transfer.
    - `amount_field_error` - Code R19. The amount field is incorrect or too large.
    - `authorization_revoked_by_customer` - Code R07. The customer at the receiving
      institution informed their bank that they have revoked authorization for a
      previously authorized transfer.
    - `invalid_ach_routing_number` - Code R13. The routing number is invalid.
    - `file_record_edit_criteria` - Code R17. The receiving bank is unable to
      process a field in the transfer.
    - `enr_invalid_individual_name` - Code R45. The individual name field was
      invalid.
    - `returned_per_odfi_request` - Code R06. The originating financial institution
      asked for this transfer to be returned. The receiving bank is complying with
      the request.
    - `limited_participation_dfi` - Code R34. The receiving bank's regulatory
      supervisor has limited their participation in the ACH network.
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
      originating financial institution made a mistake and this return corrects it.
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
    - `trace_number_error` - Code R27. A rare return reason. An ACH return's trace
      number does not match an originated ACH.
    - `untimely_dishonored_return` - Code R72. A rare return reason. The dishonored
      return was sent too late.
    - `untimely_return` - Code R68. A rare return reason. The return was sent too
      late.
    """

    trace_number: str
    """A 15 digit number that was generated by the bank that initiated the return.

    The trace number of the return is different than that of the original transfer.
    ACH trace numbers are not unique, but along with the amount and date this number
    can be used to identify the ACH return at the bank that initiated it.
    """

    transaction_id: str
    """The identifier of the Transaction associated with this return."""

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


class SourceCardDisputeFinancialVisa(BaseModel):
    event_type: Literal[
        "chargeback_submitted",
        "merchant_prearbitration_decline_submitted",
        "merchant_prearbitration_received",
        "represented",
        "user_prearbitration_decline_received",
        "user_prearbitration_submitted",
        "user_withdrawal_submitted",
    ]
    """The type of card dispute financial event.

    - `chargeback_submitted` - The user's chargeback was submitted.
    - `merchant_prearbitration_decline_submitted` - The user declined the merchant's
      pre-arbitration submission.
    - `merchant_prearbitration_received` - The merchant's pre-arbitration submission
      was received.
    - `represented` - The transaction was re-presented by the merchant.
    - `user_prearbitration_decline_received` - The user's pre-arbitration was
      declined by the merchant.
    - `user_prearbitration_submitted` - The user's pre-arbitration was submitted.
    - `user_withdrawal_submitted` - The user withdrew from the dispute.
    """


class SourceCardDisputeFinancial(BaseModel):
    amount: int
    """The amount of the financial event."""

    card_dispute_id: str
    """The identifier of the Card Dispute the financial event is associated with."""

    network: Literal["visa"]
    """The network that the Card Dispute is associated with.

    - `visa` - Visa: details will be under the `visa` object.
    """

    transaction_id: str
    """
    The identifier of the Transaction that was created to credit or debit the
    disputed funds to or from your account.
    """

    visa: Optional[SourceCardDisputeFinancialVisa] = None
    """
    Information for events related to card dispute for card payments processed over
    Visa's network. This field will be present in the JSON response if and only if
    `network` is equal to `visa`.
    """


class SourceCardDisputeLoss(BaseModel):
    card_dispute_id: str
    """The identifier of the Card Dispute that was lost."""

    explanation: str
    """Why the Card Dispute was lost."""

    lost_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was lost.
    """

    transaction_id: str
    """
    The identifier of the Transaction that was created to debit the disputed funds
    from your account.
    """


class SourceCardPushTransferAcceptance(BaseModel):
    amount: int
    """The transfer amount in USD cents."""

    transfer_id: str
    """The identifier of the Card Push Transfer that led to this Transaction."""


class SourceCardRefundCashback(BaseModel):
    amount: str
    """The cashback amount given as a string containing a decimal number.

    The amount is a positive number if it will be credited to you (e.g.,
    settlements) and a negative number if it will be debited (e.g., refunds).
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the cashback.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """


class SourceCardRefundInterchange(BaseModel):
    amount: str
    """
    The interchange amount given as a string containing a decimal number in major
    units (so e.g., "3.14" for $3.14). The amount is a positive number if it is
    credited to Increase (e.g., settlements) and a negative number if it is debited
    (e.g., refunds).
    """

    code: Optional[str] = None
    """The card network specific interchange code."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the interchange
    reimbursement.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """


class SourceCardRefundNetworkIdentifiers(BaseModel):
    acquirer_business_id: str
    """
    A network assigned business ID that identifies the acquirer that processed this
    transaction.
    """

    acquirer_reference_number: str
    """A globally unique identifier for this settlement."""

    transaction_id: Optional[str] = None
    """
    A globally unique transaction identifier provided by the card network, used
    across multiple life-cycle requests.
    """


class SourceCardRefundPurchaseDetailsCarRental(BaseModel):
    car_class_code: Optional[str] = None
    """Code indicating the vehicle's class."""

    checkout_date: Optional[date] = None
    """
    Date the customer picked up the car or, in the case of a no-show or pre-pay
    transaction, the scheduled pick up date.
    """

    daily_rental_rate_amount: Optional[int] = None
    """Daily rate being charged for the vehicle."""

    daily_rental_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily rental
    rate.
    """

    days_rented: Optional[int] = None
    """Number of days the vehicle was rented."""

    extra_charges: Optional[
        Literal["no_extra_charge", "gas", "extra_mileage", "late_return", "one_way_service_fee", "parking_violation"]
    ] = None
    """Additional charges (gas, late fee, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `gas` - Gas
    - `extra_mileage` - Extra mileage
    - `late_return` - Late return
    - `one_way_service_fee` - One way service fee
    - `parking_violation` - Parking violation
    """

    fuel_charges_amount: Optional[int] = None
    """Fuel charges for the vehicle."""

    fuel_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the fuel charges
    assessed.
    """

    insurance_charges_amount: Optional[int] = None
    """Any insurance being charged for the vehicle."""

    insurance_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the insurance
    charges assessed.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show_for_specialized_vehicle"]] = None
    """
    An indicator that the cardholder is being billed for a reserved vehicle that was
    not actually rented (that is, a "no-show" charge).

    - `not_applicable` - Not applicable
    - `no_show_for_specialized_vehicle` - No show for specialized vehicle
    """

    one_way_drop_off_charges_amount: Optional[int] = None
    """
    Charges for returning the vehicle at a different location than where it was
    picked up.
    """

    one_way_drop_off_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the one-way
    drop-off charges assessed.
    """

    renter_name: Optional[str] = None
    """Name of the person renting the vehicle."""

    weekly_rental_rate_amount: Optional[int] = None
    """Weekly rate being charged for the vehicle."""

    weekly_rental_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the weekly
    rental rate.
    """


class SourceCardRefundPurchaseDetailsLodging(BaseModel):
    check_in_date: Optional[date] = None
    """Date the customer checked in."""

    daily_room_rate_amount: Optional[int] = None
    """Daily rate being charged for the room."""

    daily_room_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily room
    rate.
    """

    extra_charges: Optional[
        Literal["no_extra_charge", "restaurant", "gift_shop", "mini_bar", "telephone", "other", "laundry"]
    ] = None
    """Additional charges (phone, late check-out, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `restaurant` - Restaurant
    - `gift_shop` - Gift shop
    - `mini_bar` - Mini bar
    - `telephone` - Telephone
    - `other` - Other
    - `laundry` - Laundry
    """

    folio_cash_advances_amount: Optional[int] = None
    """Folio cash advances for the room."""

    folio_cash_advances_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the folio cash
    advances.
    """

    food_beverage_charges_amount: Optional[int] = None
    """Food and beverage charges for the room."""

    food_beverage_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the food and
    beverage charges.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show"]] = None
    """
    Indicator that the cardholder is being billed for a reserved room that was not
    actually used.

    - `not_applicable` - Not applicable
    - `no_show` - No show
    """

    prepaid_expenses_amount: Optional[int] = None
    """Prepaid expenses being charged for the room."""

    prepaid_expenses_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the prepaid
    expenses.
    """

    room_nights: Optional[int] = None
    """Number of nights the room was rented."""

    total_room_tax_amount: Optional[int] = None
    """Total room tax being charged."""

    total_room_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total room
    tax.
    """

    total_tax_amount: Optional[int] = None
    """Total tax being charged for the room."""

    total_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total tax
    assessed.
    """


class SourceCardRefundPurchaseDetailsTravelAncillaryService(BaseModel):
    category: Optional[
        Literal[
            "none",
            "bundled_service",
            "baggage_fee",
            "change_fee",
            "cargo",
            "carbon_offset",
            "frequent_flyer",
            "gift_card",
            "ground_transport",
            "in_flight_entertainment",
            "lounge",
            "medical",
            "meal_beverage",
            "other",
            "passenger_assist_fee",
            "pets",
            "seat_fees",
            "standby",
            "service_fee",
            "store",
            "travel_service",
            "unaccompanied_travel",
            "upgrades",
            "wifi",
        ]
    ] = None
    """Category of the ancillary service.

    - `none` - None
    - `bundled_service` - Bundled service
    - `baggage_fee` - Baggage fee
    - `change_fee` - Change fee
    - `cargo` - Cargo
    - `carbon_offset` - Carbon offset
    - `frequent_flyer` - Frequent flyer
    - `gift_card` - Gift card
    - `ground_transport` - Ground transport
    - `in_flight_entertainment` - In-flight entertainment
    - `lounge` - Lounge
    - `medical` - Medical
    - `meal_beverage` - Meal beverage
    - `other` - Other
    - `passenger_assist_fee` - Passenger assist fee
    - `pets` - Pets
    - `seat_fees` - Seat fees
    - `standby` - Standby
    - `service_fee` - Service fee
    - `store` - Store
    - `travel_service` - Travel service
    - `unaccompanied_travel` - Unaccompanied travel
    - `upgrades` - Upgrades
    - `wifi` - Wi-fi
    """

    sub_category: Optional[str] = None
    """Sub-category of the ancillary service, free-form."""


class SourceCardRefundPurchaseDetailsTravelAncillary(BaseModel):
    connected_ticket_document_number: Optional[str] = None
    """
    If this purchase has a connection or relationship to another purchase, such as a
    baggage fee for a passenger transport ticket, this field should contain the
    ticket document number for the other purchase.
    """

    credit_reason_indicator: Optional[
        Literal[
            "no_credit",
            "passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_and_passenger_transport_ancillary_purchase_cancellation",
            "other",
        ]
    ] = None
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `other` - Other
    """

    passenger_name_or_description: Optional[str] = None
    """Name of the passenger or description of the ancillary purchase."""

    services: List[SourceCardRefundPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str] = None
    """Ticket document number."""


class SourceCardRefundPurchaseDetailsTravelTripLeg(BaseModel):
    carrier_code: Optional[str] = None
    """Carrier code (e.g., United Airlines, Jet Blue, etc.)."""

    destination_city_airport_code: Optional[str] = None
    """Code for the destination city or airport."""

    fare_basis_code: Optional[str] = None
    """Fare basis code."""

    flight_number: Optional[str] = None
    """Flight number."""

    service_class: Optional[str] = None
    """Service class (e.g., first class, business class, etc.)."""

    stop_over_code: Optional[Literal["none", "stop_over_allowed", "stop_over_not_allowed"]] = None
    """Indicates whether a stopover is allowed on this ticket.

    - `none` - None
    - `stop_over_allowed` - Stop over allowed
    - `stop_over_not_allowed` - Stop over not allowed
    """


class SourceCardRefundPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[SourceCardRefundPurchaseDetailsTravelAncillary] = None
    """Ancillary purchases in addition to the airfare."""

    computerized_reservation_system: Optional[str] = None
    """Indicates the computerized reservation system used to book the ticket."""

    credit_reason_indicator: Optional[
        Literal[
            "no_credit",
            "passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_and_passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_cancellation",
            "other",
            "partial_refund_of_airline_ticket",
        ]
    ] = None
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `airline_ticket_cancellation` - Airline ticket cancellation
    - `other` - Other
    - `partial_refund_of_airline_ticket` - Partial refund of airline ticket
    """

    departure_date: Optional[date] = None
    """Date of departure."""

    origination_city_airport_code: Optional[str] = None
    """Code for the originating city or airport."""

    passenger_name: Optional[str] = None
    """Name of the passenger."""

    restricted_ticket_indicator: Optional[Literal["no_restrictions", "restricted_non_refundable_ticket"]] = None
    """Indicates whether this ticket is non-refundable.

    - `no_restrictions` - No restrictions
    - `restricted_non_refundable_ticket` - Restricted non-refundable ticket
    """

    ticket_change_indicator: Optional[Literal["none", "change_to_existing_ticket", "new_ticket"]] = None
    """Indicates why a ticket was changed.

    - `none` - None
    - `change_to_existing_ticket` - Change to existing ticket
    - `new_ticket` - New ticket
    """

    ticket_number: Optional[str] = None
    """Ticket number."""

    travel_agency_code: Optional[str] = None
    """Code for the travel agency if the ticket was issued by a travel agency."""

    travel_agency_name: Optional[str] = None
    """Name of the travel agency if the ticket was issued by a travel agency."""

    trip_legs: Optional[List[SourceCardRefundPurchaseDetailsTravelTripLeg]] = None
    """Fields specific to each leg of the journey."""


class SourceCardRefundPurchaseDetails(BaseModel):
    car_rental: Optional[SourceCardRefundPurchaseDetailsCarRental] = None
    """Fields specific to car rentals."""

    customer_reference_identifier: Optional[str] = None
    """An identifier from the merchant for the customer or consumer."""

    local_tax_amount: Optional[int] = None
    """The state or provincial tax amount in minor units."""

    local_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    lodging: Optional[SourceCardRefundPurchaseDetailsLodging] = None
    """Fields specific to lodging."""

    national_tax_amount: Optional[int] = None
    """The national tax amount in minor units."""

    national_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    purchase_identifier: Optional[str] = None
    """An identifier from the merchant for the purchase to the issuer and cardholder."""

    purchase_identifier_format: Optional[
        Literal["free_text", "order_number", "rental_agreement_number", "hotel_folio_number", "invoice_number"]
    ] = None
    """The format of the purchase identifier.

    - `free_text` - Free text
    - `order_number` - Order number
    - `rental_agreement_number` - Rental agreement number
    - `hotel_folio_number` - Hotel folio number
    - `invoice_number` - Invoice number
    """

    travel: Optional[SourceCardRefundPurchaseDetailsTravel] = None
    """Fields specific to travel."""


class SourceCardRefund(BaseModel):
    id: str
    """The Card Refund identifier."""

    amount: int
    """The amount in the minor unit of the transaction's settlement currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: str
    """The ID of the Card Payment this transaction belongs to."""

    cashback: Optional[SourceCardRefundCashback] = None
    """Cashback debited for this transaction, if eligible.

    Cashback is paid out in aggregate, monthly.
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

    interchange: Optional[SourceCardRefundInterchange] = None
    """Interchange assessed as a part of this transaciton."""

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: str
    """The 4-digit MCC describing the merchant's business."""

    merchant_city: str
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_name: str
    """The name of the merchant."""

    merchant_postal_code: Optional[str] = None
    """The merchant's postal code. For US merchants this is always a 5-digit ZIP code."""

    merchant_state: Optional[str] = None
    """The state the merchant resides in."""

    network_identifiers: SourceCardRefundNetworkIdentifiers
    """Network-specific identifiers for this refund."""

    presentment_amount: int
    """The amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
    """

    purchase_details: Optional[SourceCardRefundPurchaseDetails] = None
    """
    Additional details about the card purchase, such as tax and industry-specific
    fields.
    """

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

    transacted_on_account_id: Optional[str] = None
    """The account the card belonged to."""


class SourceCardSettlementCashback(BaseModel):
    amount: str
    """The cashback amount given as a string containing a decimal number.

    The amount is a positive number if it will be credited to you (e.g.,
    settlements) and a negative number if it will be debited (e.g., refunds).
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the cashback.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """


class SourceCardSettlementInterchange(BaseModel):
    amount: str
    """
    The interchange amount given as a string containing a decimal number in major
    units (so e.g., "3.14" for $3.14). The amount is a positive number if it is
    credited to Increase (e.g., settlements) and a negative number if it is debited
    (e.g., refunds).
    """

    code: Optional[str] = None
    """The card network specific interchange code."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the interchange
    reimbursement.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """


class SourceCardSettlementNetworkIdentifiers(BaseModel):
    acquirer_business_id: str
    """
    A network assigned business ID that identifies the acquirer that processed this
    transaction.
    """

    acquirer_reference_number: str
    """A globally unique identifier for this settlement."""

    transaction_id: Optional[str] = None
    """
    A globally unique transaction identifier provided by the card network, used
    across multiple life-cycle requests.
    """


class SourceCardSettlementPurchaseDetailsCarRental(BaseModel):
    car_class_code: Optional[str] = None
    """Code indicating the vehicle's class."""

    checkout_date: Optional[date] = None
    """
    Date the customer picked up the car or, in the case of a no-show or pre-pay
    transaction, the scheduled pick up date.
    """

    daily_rental_rate_amount: Optional[int] = None
    """Daily rate being charged for the vehicle."""

    daily_rental_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily rental
    rate.
    """

    days_rented: Optional[int] = None
    """Number of days the vehicle was rented."""

    extra_charges: Optional[
        Literal["no_extra_charge", "gas", "extra_mileage", "late_return", "one_way_service_fee", "parking_violation"]
    ] = None
    """Additional charges (gas, late fee, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `gas` - Gas
    - `extra_mileage` - Extra mileage
    - `late_return` - Late return
    - `one_way_service_fee` - One way service fee
    - `parking_violation` - Parking violation
    """

    fuel_charges_amount: Optional[int] = None
    """Fuel charges for the vehicle."""

    fuel_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the fuel charges
    assessed.
    """

    insurance_charges_amount: Optional[int] = None
    """Any insurance being charged for the vehicle."""

    insurance_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the insurance
    charges assessed.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show_for_specialized_vehicle"]] = None
    """
    An indicator that the cardholder is being billed for a reserved vehicle that was
    not actually rented (that is, a "no-show" charge).

    - `not_applicable` - Not applicable
    - `no_show_for_specialized_vehicle` - No show for specialized vehicle
    """

    one_way_drop_off_charges_amount: Optional[int] = None
    """
    Charges for returning the vehicle at a different location than where it was
    picked up.
    """

    one_way_drop_off_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the one-way
    drop-off charges assessed.
    """

    renter_name: Optional[str] = None
    """Name of the person renting the vehicle."""

    weekly_rental_rate_amount: Optional[int] = None
    """Weekly rate being charged for the vehicle."""

    weekly_rental_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the weekly
    rental rate.
    """


class SourceCardSettlementPurchaseDetailsLodging(BaseModel):
    check_in_date: Optional[date] = None
    """Date the customer checked in."""

    daily_room_rate_amount: Optional[int] = None
    """Daily rate being charged for the room."""

    daily_room_rate_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily room
    rate.
    """

    extra_charges: Optional[
        Literal["no_extra_charge", "restaurant", "gift_shop", "mini_bar", "telephone", "other", "laundry"]
    ] = None
    """Additional charges (phone, late check-out, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `restaurant` - Restaurant
    - `gift_shop` - Gift shop
    - `mini_bar` - Mini bar
    - `telephone` - Telephone
    - `other` - Other
    - `laundry` - Laundry
    """

    folio_cash_advances_amount: Optional[int] = None
    """Folio cash advances for the room."""

    folio_cash_advances_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the folio cash
    advances.
    """

    food_beverage_charges_amount: Optional[int] = None
    """Food and beverage charges for the room."""

    food_beverage_charges_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the food and
    beverage charges.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show"]] = None
    """
    Indicator that the cardholder is being billed for a reserved room that was not
    actually used.

    - `not_applicable` - Not applicable
    - `no_show` - No show
    """

    prepaid_expenses_amount: Optional[int] = None
    """Prepaid expenses being charged for the room."""

    prepaid_expenses_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the prepaid
    expenses.
    """

    room_nights: Optional[int] = None
    """Number of nights the room was rented."""

    total_room_tax_amount: Optional[int] = None
    """Total room tax being charged."""

    total_room_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total room
    tax.
    """

    total_tax_amount: Optional[int] = None
    """Total tax being charged for the room."""

    total_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total tax
    assessed.
    """


class SourceCardSettlementPurchaseDetailsTravelAncillaryService(BaseModel):
    category: Optional[
        Literal[
            "none",
            "bundled_service",
            "baggage_fee",
            "change_fee",
            "cargo",
            "carbon_offset",
            "frequent_flyer",
            "gift_card",
            "ground_transport",
            "in_flight_entertainment",
            "lounge",
            "medical",
            "meal_beverage",
            "other",
            "passenger_assist_fee",
            "pets",
            "seat_fees",
            "standby",
            "service_fee",
            "store",
            "travel_service",
            "unaccompanied_travel",
            "upgrades",
            "wifi",
        ]
    ] = None
    """Category of the ancillary service.

    - `none` - None
    - `bundled_service` - Bundled service
    - `baggage_fee` - Baggage fee
    - `change_fee` - Change fee
    - `cargo` - Cargo
    - `carbon_offset` - Carbon offset
    - `frequent_flyer` - Frequent flyer
    - `gift_card` - Gift card
    - `ground_transport` - Ground transport
    - `in_flight_entertainment` - In-flight entertainment
    - `lounge` - Lounge
    - `medical` - Medical
    - `meal_beverage` - Meal beverage
    - `other` - Other
    - `passenger_assist_fee` - Passenger assist fee
    - `pets` - Pets
    - `seat_fees` - Seat fees
    - `standby` - Standby
    - `service_fee` - Service fee
    - `store` - Store
    - `travel_service` - Travel service
    - `unaccompanied_travel` - Unaccompanied travel
    - `upgrades` - Upgrades
    - `wifi` - Wi-fi
    """

    sub_category: Optional[str] = None
    """Sub-category of the ancillary service, free-form."""


class SourceCardSettlementPurchaseDetailsTravelAncillary(BaseModel):
    connected_ticket_document_number: Optional[str] = None
    """
    If this purchase has a connection or relationship to another purchase, such as a
    baggage fee for a passenger transport ticket, this field should contain the
    ticket document number for the other purchase.
    """

    credit_reason_indicator: Optional[
        Literal[
            "no_credit",
            "passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_and_passenger_transport_ancillary_purchase_cancellation",
            "other",
        ]
    ] = None
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `other` - Other
    """

    passenger_name_or_description: Optional[str] = None
    """Name of the passenger or description of the ancillary purchase."""

    services: List[SourceCardSettlementPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str] = None
    """Ticket document number."""


class SourceCardSettlementPurchaseDetailsTravelTripLeg(BaseModel):
    carrier_code: Optional[str] = None
    """Carrier code (e.g., United Airlines, Jet Blue, etc.)."""

    destination_city_airport_code: Optional[str] = None
    """Code for the destination city or airport."""

    fare_basis_code: Optional[str] = None
    """Fare basis code."""

    flight_number: Optional[str] = None
    """Flight number."""

    service_class: Optional[str] = None
    """Service class (e.g., first class, business class, etc.)."""

    stop_over_code: Optional[Literal["none", "stop_over_allowed", "stop_over_not_allowed"]] = None
    """Indicates whether a stopover is allowed on this ticket.

    - `none` - None
    - `stop_over_allowed` - Stop over allowed
    - `stop_over_not_allowed` - Stop over not allowed
    """


class SourceCardSettlementPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[SourceCardSettlementPurchaseDetailsTravelAncillary] = None
    """Ancillary purchases in addition to the airfare."""

    computerized_reservation_system: Optional[str] = None
    """Indicates the computerized reservation system used to book the ticket."""

    credit_reason_indicator: Optional[
        Literal[
            "no_credit",
            "passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_and_passenger_transport_ancillary_purchase_cancellation",
            "airline_ticket_cancellation",
            "other",
            "partial_refund_of_airline_ticket",
        ]
    ] = None
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `airline_ticket_cancellation` - Airline ticket cancellation
    - `other` - Other
    - `partial_refund_of_airline_ticket` - Partial refund of airline ticket
    """

    departure_date: Optional[date] = None
    """Date of departure."""

    origination_city_airport_code: Optional[str] = None
    """Code for the originating city or airport."""

    passenger_name: Optional[str] = None
    """Name of the passenger."""

    restricted_ticket_indicator: Optional[Literal["no_restrictions", "restricted_non_refundable_ticket"]] = None
    """Indicates whether this ticket is non-refundable.

    - `no_restrictions` - No restrictions
    - `restricted_non_refundable_ticket` - Restricted non-refundable ticket
    """

    ticket_change_indicator: Optional[Literal["none", "change_to_existing_ticket", "new_ticket"]] = None
    """Indicates why a ticket was changed.

    - `none` - None
    - `change_to_existing_ticket` - Change to existing ticket
    - `new_ticket` - New ticket
    """

    ticket_number: Optional[str] = None
    """Ticket number."""

    travel_agency_code: Optional[str] = None
    """Code for the travel agency if the ticket was issued by a travel agency."""

    travel_agency_name: Optional[str] = None
    """Name of the travel agency if the ticket was issued by a travel agency."""

    trip_legs: Optional[List[SourceCardSettlementPurchaseDetailsTravelTripLeg]] = None
    """Fields specific to each leg of the journey."""


class SourceCardSettlementPurchaseDetails(BaseModel):
    car_rental: Optional[SourceCardSettlementPurchaseDetailsCarRental] = None
    """Fields specific to car rentals."""

    customer_reference_identifier: Optional[str] = None
    """An identifier from the merchant for the customer or consumer."""

    local_tax_amount: Optional[int] = None
    """The state or provincial tax amount in minor units."""

    local_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    lodging: Optional[SourceCardSettlementPurchaseDetailsLodging] = None
    """Fields specific to lodging."""

    national_tax_amount: Optional[int] = None
    """The national tax amount in minor units."""

    national_tax_currency: Optional[str] = None
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    purchase_identifier: Optional[str] = None
    """An identifier from the merchant for the purchase to the issuer and cardholder."""

    purchase_identifier_format: Optional[
        Literal["free_text", "order_number", "rental_agreement_number", "hotel_folio_number", "invoice_number"]
    ] = None
    """The format of the purchase identifier.

    - `free_text` - Free text
    - `order_number` - Order number
    - `rental_agreement_number` - Rental agreement number
    - `hotel_folio_number` - Hotel folio number
    - `invoice_number` - Invoice number
    """

    travel: Optional[SourceCardSettlementPurchaseDetailsTravel] = None
    """Fields specific to travel."""


class SourceCardSettlement(BaseModel):
    id: str
    """The Card Settlement identifier."""

    amount: int
    """The amount in the minor unit of the transaction's settlement currency.

    For dollars, for example, this is cents.
    """

    card_authorization: Optional[str] = None
    """
    The Card Authorization that was created prior to this Card Settlement, if one
    exists.
    """

    card_payment_id: str
    """The ID of the Card Payment this transaction belongs to."""

    cashback: Optional[SourceCardSettlementCashback] = None
    """Cashback earned on this transaction, if eligible.

    Cashback is paid out in aggregate, monthly.
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

    interchange: Optional[SourceCardSettlementInterchange] = None
    """Interchange assessed as a part of this transaction."""

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: str
    """The 4-digit MCC describing the merchant's business."""

    merchant_city: str
    """The city the merchant resides in."""

    merchant_country: str
    """The country the merchant resides in."""

    merchant_name: str
    """The name of the merchant."""

    merchant_postal_code: Optional[str] = None
    """The merchant's postal code. For US merchants this is always a 5-digit ZIP code."""

    merchant_state: Optional[str] = None
    """The state the merchant resides in."""

    network: Literal["visa"]
    """The card network on which this transaction was processed.

    - `visa` - Visa
    """

    network_identifiers: SourceCardSettlementNetworkIdentifiers
    """Network-specific identifiers for this refund."""

    pending_transaction_id: Optional[str] = None
    """The identifier of the Pending Transaction associated with this Transaction."""

    presentment_amount: int
    """The amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
    """

    purchase_details: Optional[SourceCardSettlementPurchaseDetails] = None
    """
    Additional details about the card purchase, such as tax and industry-specific
    fields.
    """

    transaction_id: str
    """The identifier of the Transaction associated with this Transaction."""

    type: Literal["card_settlement"]
    """A constant representing the object's type.

    For this resource it will always be `card_settlement`.
    """


class SourceCashbackPayment(BaseModel):
    accrued_on_card_id: Optional[str] = None
    """The card on which the cashback was accrued."""

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
    """The end of the period for which this transaction paid cashback."""

    period_start: datetime
    """The start of the period for which this transaction paid cashback."""


class SourceCheckDepositAcceptance(BaseModel):
    account_number: str
    """The account number printed on the check."""

    amount: int
    """The amount to be deposited in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    auxiliary_on_us: Optional[str] = None
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

    serial_number: Optional[str] = None
    """The check serial number, if present, for consumer checks.

    For business checks, the serial number is usually in the `auxiliary_on_us`
    field.
    """


class SourceCheckDepositReturn(BaseModel):
    amount: int
    """The returned amount in USD cents."""

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
        "altered_or_fictitious_item",
        "frozen_or_blocked_account",
        "post_dated",
        "endorsement_missing",
        "signature_missing",
        "stop_payment_suspect",
        "unusable_image",
        "image_fails_security_check",
        "cannot_determine_amount",
        "signature_irregular",
        "non_cash_item",
        "unable_to_process",
        "item_exceeds_dollar_limit",
        "branch_or_account_sold",
    ]
    """
    Why this check was returned by the bank holding the account it was drawn
    against.

    - `ach_conversion_not_supported` - The check doesn't allow ACH conversion.
    - `closed_account` - The account is closed. (Check21 return code `D`)
    - `duplicate_submission` - The check has already been deposited. (Check21 return
      code `Y`)
    - `insufficient_funds` - Insufficient funds (Check21 return code `A`)
    - `no_account` - No account was found matching the check details. (Check21
      return code `E`)
    - `not_authorized` - The check was not authorized. (Check21 return code `Q`)
    - `stale_dated` - The check is too old. (Check21 return code `G`)
    - `stop_payment` - The payment has been stopped by the account holder. (Check21
      return code `C`)
    - `unknown_reason` - The reason for the return is unknown.
    - `unmatched_details` - The image doesn't match the details submitted.
    - `unreadable_image` - The image could not be read. (Check21 return code `U`)
    - `endorsement_irregular` - The check endorsement was irregular. (Check21 return
      code `J`)
    - `altered_or_fictitious_item` - The check present was either altered or fake.
      (Check21 return code `N`)
    - `frozen_or_blocked_account` - The account this check is drawn on is frozen.
      (Check21 return code `F`)
    - `post_dated` - The check is post dated. (Check21 return code `H`)
    - `endorsement_missing` - The endorsement was missing. (Check21 return code `I`)
    - `signature_missing` - The check signature was missing. (Check21 return code
      `K`)
    - `stop_payment_suspect` - The bank suspects a stop payment will be placed.
      (Check21 return code `T`)
    - `unusable_image` - The bank cannot read the image. (Check21 return code `U`)
    - `image_fails_security_check` - The check image fails the bank's security
      check. (Check21 return code `V`)
    - `cannot_determine_amount` - The bank cannot determine the amount. (Check21
      return code `W`)
    - `signature_irregular` - The signature is inconsistent with prior signatures.
      (Check21 return code `L`)
    - `non_cash_item` - The check is a non-cash item and cannot be drawn against the
      account. (Check21 return code `M`)
    - `unable_to_process` - The bank is unable to process this check. (Check21
      return code `O`)
    - `item_exceeds_dollar_limit` - The check exceeds the bank or customer's limit.
      (Check21 return code `P`)
    - `branch_or_account_sold` - The bank sold this account and no longer services
      this customer. (Check21 return code `R`)
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
    back_image_file_id: Optional[str] = None
    """
    The identifier of the API File object containing an image of the back of the
    deposited check.
    """

    bank_of_first_deposit_routing_number: Optional[str] = None
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    bank depositing this check. In some rare cases, this is not transmitted via
    Check21 and the value will be null.
    """

    deposited_at: datetime
    """When the check was deposited."""

    front_image_file_id: Optional[str] = None
    """
    The identifier of the API File object containing an image of the front of the
    deposited check.
    """

    inbound_check_deposit_id: Optional[str] = None
    """
    The identifier of the Inbound Check Deposit object associated with this
    transaction.
    """

    transaction_id: Optional[str] = None
    """The identifier of the Transaction object created when the check was deposited."""

    transfer_id: Optional[str] = None
    """The identifier of the Check Transfer object that was deposited."""

    type: Literal["check_transfer_deposit"]
    """A constant representing the object's type.

    For this resource it will always be `check_transfer_deposit`.
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

    program_id: Optional[str] = None
    """The Program for which this fee was incurred."""


class SourceInboundACHTransferAddendaFreeformEntry(BaseModel):
    payment_related_information: str
    """The payment related information passed in the addendum."""


class SourceInboundACHTransferAddendaFreeform(BaseModel):
    entries: List[SourceInboundACHTransferAddendaFreeformEntry]
    """Each entry represents an addendum received from the originator."""


class SourceInboundACHTransferAddenda(BaseModel):
    category: Literal["freeform"]
    """The type of addendum.

    - `freeform` - Unstructured addendum.
    """

    freeform: Optional[SourceInboundACHTransferAddendaFreeform] = None
    """Unstructured `payment_related_information` passed through by the originator."""


class SourceInboundACHTransfer(BaseModel):
    addenda: Optional[SourceInboundACHTransferAddenda] = None
    """Additional information sent from the originator."""

    amount: int
    """The transfer amount in USD cents."""

    originator_company_descriptive_date: Optional[str] = None
    """The description of the date of the transfer, usually in the format `YYMMDD`."""

    originator_company_discretionary_data: Optional[str] = None
    """Data set by the originator."""

    originator_company_entry_description: str
    """An informational description of the transfer."""

    originator_company_id: str
    """An identifier for the originating company.

    This is generally, but not always, a stable identifier across multiple
    transfers.
    """

    originator_company_name: str
    """A name set by the originator to identify themselves."""

    receiver_id_number: Optional[str] = None
    """The originator's identifier for the transfer recipient."""

    receiver_name: Optional[str] = None
    """The name of the transfer recipient.

    This value is informational and not verified by Increase.
    """

    trace_number: str
    """
    A 15 digit number recorded in the Nacha file and available to both the
    originating and receiving bank. Along with the amount, date, and originating
    routing number, this can be used to identify the ACH transfer at either bank.
    ACH trace numbers are not unique, but are
    [used to correlate returns](https://increase.com/documentation/ach-returns#ach-returns).
    """

    transfer_id: str
    """The Inbound ACH Transfer's identifier."""


class SourceInboundACHTransferReturnIntention(BaseModel):
    inbound_ach_transfer_id: str
    """The ID of the Inbound ACH Transfer that is being returned."""


class SourceInboundCheckAdjustment(BaseModel):
    adjusted_transaction_id: str
    """The ID of the transaction that was adjusted."""

    amount: int
    """The amount of the check adjustment."""

    reason: Literal["late_return", "wrong_payee_credit", "adjusted_amount", "non_conforming_item"]
    """The reason for the adjustment.

    - `late_return` - The return was initiated too late and the receiving
      institution has responded with a Late Return Claim.
    - `wrong_payee_credit` - The check was deposited to the wrong payee and the
      depositing institution has reimbursed the funds with a Wrong Payee Credit.
    - `adjusted_amount` - The check was deposited with a different amount than what
      was written on the check.
    - `non_conforming_item` - The recipient was not able to process the check. This
      usually happens for e.g., low quality images.
    """


class SourceInboundCheckDepositReturnIntention(BaseModel):
    inbound_check_deposit_id: str
    """The ID of the Inbound Check Deposit that is being returned."""

    transfer_id: Optional[str] = None
    """The identifier of the Check Transfer object that was deposited."""


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
    currency. This will always be "USD" for a Real-Time Payments transfer.

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

    remittance_information: Optional[str] = None
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real-Time Payments network identification of the transfer."""

    transfer_id: str
    """The identifier of the Real-Time Payments Transfer that led to this Transaction."""


class SourceInboundWireReversal(BaseModel):
    amount: int
    """The amount that was reversed in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the reversal was created.
    """

    debtor_routing_number: Optional[str] = None
    """The debtor's routing number."""

    description: str
    """
    The description on the reversal message from Fedwire, set by the reversing bank.
    """

    input_cycle_date: date
    """The Fedwire cycle date for the wire reversal.

    The "Fedwire day" begins at 9:00 PM Eastern Time on the evening before the
    `cycle date`.
    """

    input_message_accountability_data: str
    """The Fedwire transaction identifier."""

    input_sequence_number: str
    """The Fedwire sequence number."""

    input_source: str
    """The Fedwire input source identifier."""

    instruction_identification: Optional[str] = None
    """The sending bank's identifier for the reversal."""

    return_reason_additional_information: Optional[str] = None
    """Additional information about the reason for the reversal."""

    transaction_id: str
    """The ID for the Transaction associated with the transfer reversal."""

    wire_transfer_id: str
    """The ID for the Wire Transfer that is being reversed."""


class SourceInboundWireTransfer(BaseModel):
    amount: int
    """The amount in USD cents."""

    creditor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    creditor_name: Optional[str] = None
    """A name set by the sender."""

    debtor_address_line1: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line2: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_address_line3: Optional[str] = None
    """A free-form address field set by the sender."""

    debtor_name: Optional[str] = None
    """A name set by the sender."""

    description: str
    """An Increase-constructed description of the transfer."""

    end_to_end_identification: Optional[str] = None
    """A free-form reference string set by the sender, to help identify the transfer."""

    input_message_accountability_data: Optional[str] = None
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the originating bank.
    """

    instructing_agent_routing_number: Optional[str] = None
    """
    The American Banking Association (ABA) routing number of the bank that sent the
    wire.
    """

    instruction_identification: Optional[str] = None
    """The sending bank's identifier for the wire transfer."""

    transfer_id: str
    """The ID of the Inbound Wire Transfer object that resulted in this Transaction."""

    unique_end_to_end_transaction_reference: Optional[str] = None
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the transfer.
    """

    unstructured_remittance_information: Optional[str] = None
    """A free-form message set by the sender."""


class SourceInboundWireTransferReversal(BaseModel):
    inbound_wire_transfer_id: str
    """The ID of the Inbound Wire Transfer that is being reversed."""


class SourceInterestPayment(BaseModel):
    accrued_on_account_id: str
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
        "bank_drawn_check",
        "bank_drawn_check_credit",
        "bank_migration",
        "check_adjustment",
        "collection_payment",
        "collection_receivable",
        "empyreal_adjustment",
        "error",
        "error_correction",
        "fees",
        "interest",
        "negative_balance_forgiveness",
        "sample_funds",
        "sample_funds_return",
        "account_revenue_payment_distribution",
    ]
    """An Internal Source is a transaction between you and Increase.

    This describes the reason for the transaction.

    - `account_closure` - Account closure
    - `bank_drawn_check` - Bank-drawn check
    - `bank_drawn_check_credit` - Bank-drawn check credit
    - `bank_migration` - Bank migration
    - `check_adjustment` - Check adjustment
    - `collection_payment` - Collection payment
    - `collection_receivable` - Collection receivable
    - `empyreal_adjustment` - Empyreal adjustment
    - `error` - Error
    - `error_correction` - Error correction
    - `fees` - Fees
    - `interest` - Interest
    - `negative_balance_forgiveness` - Negative balance forgiveness
    - `sample_funds` - Sample funds
    - `sample_funds_return` - Sample funds return
    - `account_revenue_payment_distribution` - Account revenue payment distribution
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
    """The identifier of the Real-Time Payments Transfer that led to this Transaction."""


class SourceSampleFunds(BaseModel):
    originator: str
    """Where the sample funds came from."""


class SourceSwiftTransferIntention(BaseModel):
    transfer_id: str
    """The identifier of the Swift Transfer that led to this Transaction."""


class SourceSwiftTransferReturn(BaseModel):
    transfer_id: str
    """The identifier of the Swift Transfer that led to this Transaction."""


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
    """The identifier of the Wire Transfer that led to this Transaction."""


class Source(BaseModel):
    account_revenue_payment: Optional[SourceAccountRevenuePayment] = None
    """An Account Revenue Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_revenue_payment`. An Account Revenue Payment represents a
    payment made to an account from the bank. Account revenue is a type of
    non-interest income.
    """

    account_transfer_intention: Optional[SourceAccountTransferIntention] = None
    """An Account Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_intention`. Two Account Transfer Intentions are
    created from each Account Transfer. One decrements the source account, and the
    other increments the destination account.
    """

    ach_transfer_intention: Optional[SourceACHTransferIntention] = None
    """An ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_intention`. An ACH Transfer Intention is created from an
    ACH Transfer. It reflects the intention to move money into or out of an Increase
    account via the ACH network.
    """

    ach_transfer_rejection: Optional[SourceACHTransferRejection] = None
    """An ACH Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_rejection`. An ACH Transfer Rejection is created when an
    ACH Transfer is rejected by Increase. It offsets the ACH Transfer Intention.
    These rejections are rare.
    """

    ach_transfer_return: Optional[SourceACHTransferReturn] = None
    """An ACH Transfer Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_return`. An ACH Transfer Return is created when an ACH
    Transfer is returned by the receiving bank. It offsets the ACH Transfer
    Intention. ACH Transfer Returns usually occur within the first two business days
    after the transfer is initiated, but can occur much later.
    """

    card_dispute_acceptance: Optional[SourceCardDisputeAcceptance] = None
    """A Card Dispute Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_dispute_acceptance`. Contains the details of a successful Card
    Dispute.
    """

    card_dispute_financial: Optional[SourceCardDisputeFinancial] = None
    """A Card Dispute Financial object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_dispute_financial`. Financial event related to a Card Dispute.
    """

    card_dispute_loss: Optional[SourceCardDisputeLoss] = None
    """A Card Dispute Loss object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_dispute_loss`. Contains the details of a lost Card Dispute.
    """

    card_push_transfer_acceptance: Optional[SourceCardPushTransferAcceptance] = None
    """A Card Push Transfer Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_push_transfer_acceptance`. A Card Push Transfer Acceptance is
    created when an Outbound Card Push Transfer sent from Increase is accepted by
    the receiving bank.
    """

    card_refund: Optional[SourceCardRefund] = None
    """A Card Refund object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_refund`. Card Refunds move money back to the cardholder. While
    they are usually connected to a Card Settlement an acquirer can also refund
    money directly to a card without relation to a transaction.
    """

    card_revenue_payment: Optional[SourceCardRevenuePayment] = None
    """A Card Revenue Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_revenue_payment`. Card Revenue Payments reflect earnings from
    fees on card transactions.
    """

    card_settlement: Optional[SourceCardSettlement] = None
    """A Card Settlement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_settlement`. Card Settlements are card transactions that have
    cleared and settled. While a settlement is usually preceded by an authorization,
    an acquirer can also directly clear a transaction without first authorizing it.
    """

    cashback_payment: Optional[SourceCashbackPayment] = None
    """A Cashback Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `cashback_payment`. A Cashback Payment represents the cashback paid to
    a cardholder for a given period. Cashback is usually paid monthly for the prior
    month's transactions.
    """

    category: Literal[
        "account_transfer_intention",
        "ach_transfer_intention",
        "ach_transfer_rejection",
        "ach_transfer_return",
        "cashback_payment",
        "card_dispute_acceptance",
        "card_dispute_financial",
        "card_dispute_loss",
        "card_refund",
        "card_settlement",
        "card_revenue_payment",
        "check_deposit_acceptance",
        "check_deposit_return",
        "check_transfer_deposit",
        "fee_payment",
        "inbound_ach_transfer",
        "inbound_ach_transfer_return_intention",
        "inbound_check_deposit_return_intention",
        "inbound_check_adjustment",
        "inbound_real_time_payments_transfer_confirmation",
        "inbound_wire_reversal",
        "inbound_wire_transfer",
        "inbound_wire_transfer_reversal",
        "interest_payment",
        "internal_source",
        "real_time_payments_transfer_acknowledgement",
        "sample_funds",
        "wire_transfer_intention",
        "swift_transfer_intention",
        "swift_transfer_return",
        "card_push_transfer_acceptance",
        "account_revenue_payment",
        "other",
    ]
    """The type of the resource.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `account_transfer_intention` - Account Transfer Intention: details will be
      under the `account_transfer_intention` object.
    - `ach_transfer_intention` - ACH Transfer Intention: details will be under the
      `ach_transfer_intention` object.
    - `ach_transfer_rejection` - ACH Transfer Rejection: details will be under the
      `ach_transfer_rejection` object.
    - `ach_transfer_return` - ACH Transfer Return: details will be under the
      `ach_transfer_return` object.
    - `cashback_payment` - Cashback Payment: details will be under the
      `cashback_payment` object.
    - `card_dispute_acceptance` - Card Dispute Acceptance: details will be under the
      `card_dispute_acceptance` object.
    - `card_dispute_financial` - Card Dispute Financial: details will be under the
      `card_dispute_financial` object.
    - `card_dispute_loss` - Card Dispute Loss: details will be under the
      `card_dispute_loss` object.
    - `card_refund` - Card Refund: details will be under the `card_refund` object.
    - `card_settlement` - Card Settlement: details will be under the
      `card_settlement` object.
    - `card_revenue_payment` - Card Revenue Payment: details will be under the
      `card_revenue_payment` object.
    - `check_deposit_acceptance` - Check Deposit Acceptance: details will be under
      the `check_deposit_acceptance` object.
    - `check_deposit_return` - Check Deposit Return: details will be under the
      `check_deposit_return` object.
    - `check_transfer_deposit` - Check Transfer Deposit: details will be under the
      `check_transfer_deposit` object.
    - `fee_payment` - Fee Payment: details will be under the `fee_payment` object.
    - `inbound_ach_transfer` - Inbound ACH Transfer Intention: details will be under
      the `inbound_ach_transfer` object.
    - `inbound_ach_transfer_return_intention` - Inbound ACH Transfer Return
      Intention: details will be under the `inbound_ach_transfer_return_intention`
      object.
    - `inbound_check_deposit_return_intention` - Inbound Check Deposit Return
      Intention: details will be under the `inbound_check_deposit_return_intention`
      object.
    - `inbound_check_adjustment` - Inbound Check Adjustment: details will be under
      the `inbound_check_adjustment` object.
    - `inbound_real_time_payments_transfer_confirmation` - Inbound Real-Time
      Payments Transfer Confirmation: details will be under the
      `inbound_real_time_payments_transfer_confirmation` object.
    - `inbound_wire_reversal` - Inbound Wire Reversal: details will be under the
      `inbound_wire_reversal` object.
    - `inbound_wire_transfer` - Inbound Wire Transfer Intention: details will be
      under the `inbound_wire_transfer` object.
    - `inbound_wire_transfer_reversal` - Inbound Wire Transfer Reversal Intention:
      details will be under the `inbound_wire_transfer_reversal` object.
    - `interest_payment` - Interest Payment: details will be under the
      `interest_payment` object.
    - `internal_source` - Internal Source: details will be under the
      `internal_source` object.
    - `real_time_payments_transfer_acknowledgement` - Real-Time Payments Transfer
      Acknowledgement: details will be under the
      `real_time_payments_transfer_acknowledgement` object.
    - `sample_funds` - Sample Funds: details will be under the `sample_funds`
      object.
    - `wire_transfer_intention` - Wire Transfer Intention: details will be under the
      `wire_transfer_intention` object.
    - `swift_transfer_intention` - Swift Transfer Intention: details will be under
      the `swift_transfer_intention` object.
    - `swift_transfer_return` - Swift Transfer Return: details will be under the
      `swift_transfer_return` object.
    - `card_push_transfer_acceptance` - Card Push Transfer Acceptance: details will
      be under the `card_push_transfer_acceptance` object.
    - `account_revenue_payment` - Account Revenue Payment: details will be under the
      `account_revenue_payment` object.
    - `other` - The Transaction was made for an undocumented or deprecated reason.
    """

    check_deposit_acceptance: Optional[SourceCheckDepositAcceptance] = None
    """A Check Deposit Acceptance object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_acceptance`. A Check Deposit Acceptance is created when
    a Check Deposit is processed and its details confirmed. Check Deposits may be
    returned by the receiving bank, which will appear as a Check Deposit Return.
    """

    check_deposit_return: Optional[SourceCheckDepositReturn] = None
    """A Check Deposit Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_return`. A Check Deposit Return is created when a Check
    Deposit is returned by the bank holding the account it was drawn against. Check
    Deposits may be returned for a variety of reasons, including insufficient funds
    or a mismatched account number. Usually, checks are returned within the first 7
    days after the deposit is made.
    """

    check_transfer_deposit: Optional[SourceCheckTransferDeposit] = None
    """A Check Transfer Deposit object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_deposit`. An Inbound Check is a check drawn on an
    Increase account that has been deposited by an external bank account. These
    types of checks are not pre-registered.
    """

    fee_payment: Optional[SourceFeePayment] = None
    """A Fee Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `fee_payment`. A Fee Payment represents a payment made to Increase.
    """

    inbound_ach_transfer: Optional[SourceInboundACHTransfer] = None
    """An Inbound ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_ach_transfer`. An Inbound ACH Transfer Intention is created
    when an ACH transfer is initiated at another bank and received by Increase.
    """

    inbound_ach_transfer_return_intention: Optional[SourceInboundACHTransferReturnIntention] = None
    """An Inbound ACH Transfer Return Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_ach_transfer_return_intention`. An Inbound ACH Transfer Return
    Intention is created when an ACH transfer is initiated at another bank and
    returned by Increase.
    """

    inbound_check_adjustment: Optional[SourceInboundCheckAdjustment] = None
    """An Inbound Check Adjustment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_check_adjustment`. An Inbound Check Adjustment is created when
    Increase receives an adjustment for a check or return deposited through Check21.
    """

    inbound_check_deposit_return_intention: Optional[SourceInboundCheckDepositReturnIntention] = None
    """An Inbound Check Deposit Return Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_check_deposit_return_intention`. An Inbound Check Deposit
    Return Intention is created when Increase receives an Inbound Check and the User
    requests that it be returned.
    """

    inbound_real_time_payments_transfer_confirmation: Optional[SourceInboundRealTimePaymentsTransferConfirmation] = None
    """An Inbound Real-Time Payments Transfer Confirmation object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_confirmation`. An Inbound
    Real-Time Payments Transfer Confirmation is created when a Real-Time Payments
    transfer is initiated at another bank and received by Increase.
    """

    inbound_wire_reversal: Optional[SourceInboundWireReversal] = None
    """An Inbound Wire Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_reversal`. An Inbound Wire Reversal represents a reversal
    of a wire transfer that was initiated via Increase. The other bank is sending
    the money back. This most often happens when the original destination account
    details were incorrect.
    """

    inbound_wire_transfer: Optional[SourceInboundWireTransfer] = None
    """An Inbound Wire Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer`. An Inbound Wire Transfer Intention is created
    when a wire transfer is initiated at another bank and received by Increase.
    """

    inbound_wire_transfer_reversal: Optional[SourceInboundWireTransferReversal] = None
    """An Inbound Wire Transfer Reversal Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer_reversal`. An Inbound Wire Transfer Reversal
    Intention is created when Increase has received a wire and the User requests
    that it be reversed.
    """

    interest_payment: Optional[SourceInterestPayment] = None
    """An Interest Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `interest_payment`. An Interest Payment represents a payment of
    interest on an account. Interest is usually paid monthly.
    """

    internal_source: Optional[SourceInternalSource] = None
    """An Internal Source object.

    This field will be present in the JSON response if and only if `category` is
    equal to `internal_source`. A transaction between the user and Increase. See the
    `reason` attribute for more information.
    """

    other: Optional[object] = None
    """
    If the category of this Transaction source is equal to `other`, this field will
    contain an empty object, otherwise it will contain null.
    """

    real_time_payments_transfer_acknowledgement: Optional[SourceRealTimePaymentsTransferAcknowledgement] = None
    """A Real-Time Payments Transfer Acknowledgement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_acknowledgement`. A Real-Time Payments
    Transfer Acknowledgement is created when a Real-Time Payments Transfer sent from
    Increase is acknowledged by the receiving bank.
    """

    sample_funds: Optional[SourceSampleFunds] = None
    """A Sample Funds object.

    This field will be present in the JSON response if and only if `category` is
    equal to `sample_funds`. Sample funds for testing purposes.
    """

    swift_transfer_intention: Optional[SourceSwiftTransferIntention] = None
    """A Swift Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `swift_transfer_intention`. A Swift Transfer initiated via Increase.
    """

    swift_transfer_return: Optional[SourceSwiftTransferReturn] = None
    """A Swift Transfer Return object.

    This field will be present in the JSON response if and only if `category` is
    equal to `swift_transfer_return`. A Swift Transfer Return is created when a
    Swift Transfer is returned by the receiving bank.
    """

    wire_transfer_intention: Optional[SourceWireTransferIntention] = None
    """A Wire Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_intention`. A Wire Transfer initiated via Increase and
    sent to a different bank.
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
    Transaction occurred.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    Transaction's currency. This will match the currency on the Transaction's
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

    route_id: Optional[str] = None
    """The identifier for the route this Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card", "lockbox"]] = None
    """The type of the route this Transaction came through.

    - `account_number` - An Account Number.
    - `card` - A Card.
    - `lockbox` - A Lockbox.
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
