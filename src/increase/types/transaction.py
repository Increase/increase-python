# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
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
    "SourceCardSettlementNetworkIdentifiers",
    "SourceCardSettlementPurchaseDetails",
    "SourceCardSettlementPurchaseDetailsCarRental",
    "SourceCardSettlementPurchaseDetailsLodging",
    "SourceCardSettlementPurchaseDetailsTravel",
    "SourceCardSettlementPurchaseDetailsTravelAncillary",
    "SourceCardSettlementPurchaseDetailsTravelAncillaryService",
    "SourceCardSettlementPurchaseDetailsTravelTripLeg",
    "SourceCheckDepositAcceptance",
    "SourceCheckDepositReturn",
    "SourceCheckTransferDeposit",
    "SourceCheckTransferIntention",
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


class SourceCardRefundNetworkIdentifiers(BaseModel):
    acquirer_business_id: str
    """
    A network assigned business ID that identifies the acquirer that processed this
    transaction.
    """

    acquirer_reference_number: str
    """A globally unique identifier for this settlement."""

    transaction_id: Optional[str]
    """
    A globally unique transaction identifier provided by the card network, used
    across multiple life-cycle requests.
    """


class SourceCardRefundPurchaseDetailsCarRental(BaseModel):
    car_class_code: Optional[str]
    """Code indicating the vehicle's class."""

    checkout_date: Optional[date]
    """
    Date the customer picked up the car or, in the case of a no-show or pre-pay
    transaction, the scheduled pick up date.
    """

    daily_rental_rate_amount: Optional[int]
    """Daily rate being charged for the vehicle."""

    daily_rental_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily rental
    rate.
    """

    days_rented: Optional[int]
    """Number of days the vehicle was rented."""

    extra_charges: Optional[
        Literal["no_extra_charge", "gas", "extra_mileage", "late_return", "one_way_service_fee", "parking_violation"]
    ]
    """Additional charges (gas, late fee, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `gas` - Gas
    - `extra_mileage` - Extra mileage
    - `late_return` - Late return
    - `one_way_service_fee` - One way service fee
    - `parking_violation` - Parking violation
    """

    fuel_charges_amount: Optional[int]
    """Fuel charges for the vehicle."""

    fuel_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the fuel charges
    assessed.
    """

    insurance_charges_amount: Optional[int]
    """Any insurance being charged for the vehicle."""

    insurance_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the insurance
    charges assessed.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show_for_specialized_vehicle"]]
    """
    An indicator that the cardholder is being billed for a reserved vehicle that was
    not actually rented (that is, a "no-show" charge).

    - `not_applicable` - Not applicable
    - `no_show_for_specialized_vehicle` - No show for specialized vehicle
    """

    one_way_drop_off_charges_amount: Optional[int]
    """
    Charges for returning the vehicle at a different location than where it was
    picked up.
    """

    one_way_drop_off_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the one-way
    drop-off charges assessed.
    """

    renter_name: Optional[str]
    """Name of the person renting the vehicle."""

    weekly_rental_rate_amount: Optional[int]
    """Weekly rate being charged for the vehicle."""

    weekly_rental_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the weekly
    rental rate.
    """


class SourceCardRefundPurchaseDetailsLodging(BaseModel):
    check_in_date: Optional[date]
    """Date the customer checked in."""

    daily_room_rate_amount: Optional[int]
    """Daily rate being charged for the room."""

    daily_room_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily room
    rate.
    """

    extra_charges: Optional[
        Literal["no_extra_charge", "restaurant", "gift_shop", "mini_bar", "telephone", "other", "laundry"]
    ]
    """Additional charges (phone, late check-out, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `restaurant` - Restaurant
    - `gift_shop` - Gift shop
    - `mini_bar` - Mini bar
    - `telephone` - Telephone
    - `other` - Other
    - `laundry` - Laundry
    """

    folio_cash_advances_amount: Optional[int]
    """Folio cash advances for the room."""

    folio_cash_advances_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the folio cash
    advances.
    """

    food_beverage_charges_amount: Optional[int]
    """Food and beverage charges for the room."""

    food_beverage_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the food and
    beverage charges.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show"]]
    """
    Indicator that the cardholder is being billed for a reserved room that was not
    actually used.

    - `not_applicable` - Not applicable
    - `no_show` - No show
    """

    prepaid_expenses_amount: Optional[int]
    """Prepaid expenses being charged for the room."""

    prepaid_expenses_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the prepaid
    expenses.
    """

    room_nights: Optional[int]
    """Number of nights the room was rented."""

    total_room_tax_amount: Optional[int]
    """Total room tax being charged."""

    total_room_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total room
    tax.
    """

    total_tax_amount: Optional[int]
    """Total tax being charged for the room."""

    total_tax_currency: Optional[str]
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
    ]
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

    sub_category: Optional[str]
    """Sub-category of the ancillary service, free-form."""


class SourceCardRefundPurchaseDetailsTravelAncillary(BaseModel):
    connected_ticket_document_number: Optional[str]
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
    ]
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `other` - Other
    """

    passenger_name_or_description: Optional[str]
    """Name of the passenger or description of the ancillary purchase."""

    services: List[SourceCardRefundPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str]
    """Ticket document number."""


class SourceCardRefundPurchaseDetailsTravelTripLeg(BaseModel):
    carrier_code: Optional[str]
    """Carrier code (e.g., United Airlines, Jet Blue, etc.)."""

    destination_city_airport_code: Optional[str]
    """Code for the destination city or airport."""

    fare_basis_code: Optional[str]
    """Fare basis code."""

    flight_number: Optional[str]
    """Flight number."""

    service_class: Optional[str]
    """Service class (e.g., first class, business class, etc.)."""

    stop_over_code: Optional[Literal["none", "stop_over_allowed", "stop_over_not_allowed"]]
    """Indicates whether a stopover is allowed on this ticket.

    - `none` - None
    - `stop_over_allowed` - Stop over allowed
    - `stop_over_not_allowed` - Stop over not allowed
    """


class SourceCardRefundPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[SourceCardRefundPurchaseDetailsTravelAncillary]
    """Ancillary purchases in addition to the airfare."""

    computerized_reservation_system: Optional[str]
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
    ]
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

    departure_date: Optional[date]
    """Date of departure."""

    origination_city_airport_code: Optional[str]
    """Code for the originating city or airport."""

    passenger_name: Optional[str]
    """Name of the passenger."""

    restricted_ticket_indicator: Optional[Literal["no_restrictions", "restricted_non_refundable_ticket"]]
    """Indicates whether this ticket is non-refundable.

    - `no_restrictions` - No restrictions
    - `restricted_non_refundable_ticket` - Restricted non-refundable ticket
    """

    ticket_change_indicator: Optional[Literal["none", "change_to_existing_ticket", "new_ticket"]]
    """Indicates why a ticket was changed.

    - `none` - None
    - `change_to_existing_ticket` - Change to existing ticket
    - `new_ticket` - New ticket
    """

    ticket_number: Optional[str]
    """Ticket number."""

    travel_agency_code: Optional[str]
    """Code for the travel agency if the ticket was issued by a travel agency."""

    travel_agency_name: Optional[str]
    """Name of the travel agency if the ticket was issued by a travel agency."""

    trip_legs: Optional[List[SourceCardRefundPurchaseDetailsTravelTripLeg]]
    """Fields specific to each leg of the journey."""


class SourceCardRefundPurchaseDetails(BaseModel):
    car_rental: Optional[SourceCardRefundPurchaseDetailsCarRental]
    """Fields specific to car rentals."""

    customer_reference_identifier: Optional[str]
    """An identifier from the merchant for the customer or consumer."""

    local_tax_amount: Optional[int]
    """The state or provincial tax amount in minor units."""

    local_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    lodging: Optional[SourceCardRefundPurchaseDetailsLodging]
    """Fields specific to lodging."""

    national_tax_amount: Optional[int]
    """The national tax amount in minor units."""

    national_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    purchase_identifier: Optional[str]
    """An identifier from the merchant for the purchase to the issuer and cardholder."""

    purchase_identifier_format: Optional[
        Literal["free_text", "order_number", "rental_agreement_number", "hotel_folio_number", "invoice_number"]
    ]
    """The format of the purchase identifier.

    - `free_text` - Free text
    - `order_number` - Order number
    - `rental_agreement_number` - Rental agreement number
    - `hotel_folio_number` - Hotel folio number
    - `invoice_number` - Invoice number
    """

    travel: Optional[SourceCardRefundPurchaseDetailsTravel]
    """Fields specific to travel."""


class SourceCardRefund(BaseModel):
    id: str
    """The Card Refund identifier."""

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: Optional[str]
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

    network_identifiers: SourceCardRefundNetworkIdentifiers
    """Network-specific identifiers for this refund."""

    purchase_details: Optional[SourceCardRefundPurchaseDetails]
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

    transacted_on_account_id: Optional[str]
    """The account the card belonged to."""


class SourceCardSettlementNetworkIdentifiers(BaseModel):
    acquirer_business_id: str
    """
    A network assigned business ID that identifies the acquirer that processed this
    transaction.
    """

    acquirer_reference_number: str
    """A globally unique identifier for this settlement."""

    transaction_id: Optional[str]
    """
    A globally unique transaction identifier provided by the card network, used
    across multiple life-cycle requests.
    """


class SourceCardSettlementPurchaseDetailsCarRental(BaseModel):
    car_class_code: Optional[str]
    """Code indicating the vehicle's class."""

    checkout_date: Optional[date]
    """
    Date the customer picked up the car or, in the case of a no-show or pre-pay
    transaction, the scheduled pick up date.
    """

    daily_rental_rate_amount: Optional[int]
    """Daily rate being charged for the vehicle."""

    daily_rental_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily rental
    rate.
    """

    days_rented: Optional[int]
    """Number of days the vehicle was rented."""

    extra_charges: Optional[
        Literal["no_extra_charge", "gas", "extra_mileage", "late_return", "one_way_service_fee", "parking_violation"]
    ]
    """Additional charges (gas, late fee, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `gas` - Gas
    - `extra_mileage` - Extra mileage
    - `late_return` - Late return
    - `one_way_service_fee` - One way service fee
    - `parking_violation` - Parking violation
    """

    fuel_charges_amount: Optional[int]
    """Fuel charges for the vehicle."""

    fuel_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the fuel charges
    assessed.
    """

    insurance_charges_amount: Optional[int]
    """Any insurance being charged for the vehicle."""

    insurance_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the insurance
    charges assessed.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show_for_specialized_vehicle"]]
    """
    An indicator that the cardholder is being billed for a reserved vehicle that was
    not actually rented (that is, a "no-show" charge).

    - `not_applicable` - Not applicable
    - `no_show_for_specialized_vehicle` - No show for specialized vehicle
    """

    one_way_drop_off_charges_amount: Optional[int]
    """
    Charges for returning the vehicle at a different location than where it was
    picked up.
    """

    one_way_drop_off_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the one-way
    drop-off charges assessed.
    """

    renter_name: Optional[str]
    """Name of the person renting the vehicle."""

    weekly_rental_rate_amount: Optional[int]
    """Weekly rate being charged for the vehicle."""

    weekly_rental_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the weekly
    rental rate.
    """


class SourceCardSettlementPurchaseDetailsLodging(BaseModel):
    check_in_date: Optional[date]
    """Date the customer checked in."""

    daily_room_rate_amount: Optional[int]
    """Daily rate being charged for the room."""

    daily_room_rate_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the daily room
    rate.
    """

    extra_charges: Optional[
        Literal["no_extra_charge", "restaurant", "gift_shop", "mini_bar", "telephone", "other", "laundry"]
    ]
    """Additional charges (phone, late check-out, etc.) being billed.

    - `no_extra_charge` - No extra charge
    - `restaurant` - Restaurant
    - `gift_shop` - Gift shop
    - `mini_bar` - Mini bar
    - `telephone` - Telephone
    - `other` - Other
    - `laundry` - Laundry
    """

    folio_cash_advances_amount: Optional[int]
    """Folio cash advances for the room."""

    folio_cash_advances_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the folio cash
    advances.
    """

    food_beverage_charges_amount: Optional[int]
    """Food and beverage charges for the room."""

    food_beverage_charges_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the food and
    beverage charges.
    """

    no_show_indicator: Optional[Literal["not_applicable", "no_show"]]
    """
    Indicator that the cardholder is being billed for a reserved room that was not
    actually used.

    - `not_applicable` - Not applicable
    - `no_show` - No show
    """

    prepaid_expenses_amount: Optional[int]
    """Prepaid expenses being charged for the room."""

    prepaid_expenses_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the prepaid
    expenses.
    """

    room_nights: Optional[int]
    """Number of nights the room was rented."""

    total_room_tax_amount: Optional[int]
    """Total room tax being charged."""

    total_room_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total room
    tax.
    """

    total_tax_amount: Optional[int]
    """Total tax being charged for the room."""

    total_tax_currency: Optional[str]
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
    ]
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

    sub_category: Optional[str]
    """Sub-category of the ancillary service, free-form."""


class SourceCardSettlementPurchaseDetailsTravelAncillary(BaseModel):
    connected_ticket_document_number: Optional[str]
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
    ]
    """Indicates the reason for a credit to the cardholder.

    - `no_credit` - No credit
    - `passenger_transport_ancillary_purchase_cancellation` - Passenger transport
      ancillary purchase cancellation
    - `airline_ticket_and_passenger_transport_ancillary_purchase_cancellation` -
      Airline ticket and passenger transport ancillary purchase cancellation
    - `other` - Other
    """

    passenger_name_or_description: Optional[str]
    """Name of the passenger or description of the ancillary purchase."""

    services: List[SourceCardSettlementPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str]
    """Ticket document number."""


class SourceCardSettlementPurchaseDetailsTravelTripLeg(BaseModel):
    carrier_code: Optional[str]
    """Carrier code (e.g., United Airlines, Jet Blue, etc.)."""

    destination_city_airport_code: Optional[str]
    """Code for the destination city or airport."""

    fare_basis_code: Optional[str]
    """Fare basis code."""

    flight_number: Optional[str]
    """Flight number."""

    service_class: Optional[str]
    """Service class (e.g., first class, business class, etc.)."""

    stop_over_code: Optional[Literal["none", "stop_over_allowed", "stop_over_not_allowed"]]
    """Indicates whether a stopover is allowed on this ticket.

    - `none` - None
    - `stop_over_allowed` - Stop over allowed
    - `stop_over_not_allowed` - Stop over not allowed
    """


class SourceCardSettlementPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[SourceCardSettlementPurchaseDetailsTravelAncillary]
    """Ancillary purchases in addition to the airfare."""

    computerized_reservation_system: Optional[str]
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
    ]
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

    departure_date: Optional[date]
    """Date of departure."""

    origination_city_airport_code: Optional[str]
    """Code for the originating city or airport."""

    passenger_name: Optional[str]
    """Name of the passenger."""

    restricted_ticket_indicator: Optional[Literal["no_restrictions", "restricted_non_refundable_ticket"]]
    """Indicates whether this ticket is non-refundable.

    - `no_restrictions` - No restrictions
    - `restricted_non_refundable_ticket` - Restricted non-refundable ticket
    """

    ticket_change_indicator: Optional[Literal["none", "change_to_existing_ticket", "new_ticket"]]
    """Indicates why a ticket was changed.

    - `none` - None
    - `change_to_existing_ticket` - Change to existing ticket
    - `new_ticket` - New ticket
    """

    ticket_number: Optional[str]
    """Ticket number."""

    travel_agency_code: Optional[str]
    """Code for the travel agency if the ticket was issued by a travel agency."""

    travel_agency_name: Optional[str]
    """Name of the travel agency if the ticket was issued by a travel agency."""

    trip_legs: Optional[List[SourceCardSettlementPurchaseDetailsTravelTripLeg]]
    """Fields specific to each leg of the journey."""


class SourceCardSettlementPurchaseDetails(BaseModel):
    car_rental: Optional[SourceCardSettlementPurchaseDetailsCarRental]
    """Fields specific to car rentals."""

    customer_reference_identifier: Optional[str]
    """An identifier from the merchant for the customer or consumer."""

    local_tax_amount: Optional[int]
    """The state or provincial tax amount in minor units."""

    local_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    lodging: Optional[SourceCardSettlementPurchaseDetailsLodging]
    """Fields specific to lodging."""

    national_tax_amount: Optional[int]
    """The national tax amount in minor units."""

    national_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the local tax
    assessed.
    """

    purchase_identifier: Optional[str]
    """An identifier from the merchant for the purchase to the issuer and cardholder."""

    purchase_identifier_format: Optional[
        Literal["free_text", "order_number", "rental_agreement_number", "hotel_folio_number", "invoice_number"]
    ]
    """The format of the purchase identifier.

    - `free_text` - Free text
    - `order_number` - Order number
    - `rental_agreement_number` - Rental agreement number
    - `hotel_folio_number` - Hotel folio number
    - `invoice_number` - Invoice number
    """

    travel: Optional[SourceCardSettlementPurchaseDetailsTravel]
    """Fields specific to travel."""


class SourceCardSettlement(BaseModel):
    id: str
    """The Card Settlement identifier."""

    amount: int
    """The amount in the minor unit of the transaction's settlement currency.

    For dollars, for example, this is cents.
    """

    card_authorization: Optional[str]
    """
    The Card Authorization that was created prior to this Card Settlement, if one
    exists.
    """

    card_payment_id: Optional[str]
    """The ID of the Card Payment this transaction belongs to."""

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

    network_identifiers: SourceCardSettlementNetworkIdentifiers
    """Network-specific identifiers for this refund."""

    pending_transaction_id: Optional[str]
    """The identifier of the Pending Transaction associated with this Transaction."""

    presentment_amount: int
    """The amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
    """

    purchase_details: Optional[SourceCardSettlementPurchaseDetails]
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
    Why this check was returned by the bank holding the account it was drawn
    against.

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

    bank_of_first_deposit_routing_number: Optional[str]
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    bank depositing this check. In some rare cases, this is not transmitted via
    Check21 and the value will be null.
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

    transfer_id: str
    """The identifier of the Check Transfer object that was deposited."""

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


class SourceCheckTransferStopPaymentRequest(BaseModel):
    reason: Literal["mail_delivery_failed", "rejected_by_increase", "unknown"]
    """The reason why this transfer was stopped.

    - `mail_delivery_failed` - The check could not be delivered.
    - `rejected_by_increase` - The check was canceled by an Increase operator who
      will provide details out-of-band.
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
    """The description of the date of the transfer, usually in the format `YYMMDD`."""

    originator_company_discretionary_data: Optional[str]
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

    receiver_id_number: Optional[str]
    """The originator's identifier for the transfer receipient."""

    receiver_name: Optional[str]
    """The name of the transfer recipient.

    This value is informational and not verified by Increase.
    """

    trace_number: str
    """
    A 15 digit number recorded in the Nacha file and available to both the
    originating and receiving bank. Along with the amount, date, and originating
    routing number, this can be used to identify the ACH transfer at either bank.
    ACH trace numbers are not unique, but are
    [used to correlate returns](https://increase.com/documentation/ach#returns).
    """

    transfer_id: str
    """The inbound ach transfer's identifier."""


class SourceInboundCheck(BaseModel):
    amount: int
    """The amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    bank_of_first_deposit_routing_number: Optional[str]
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    bank depositing this check. In some rare cases, this is not transmitted via
    Check21 and the value will be null.
    """

    check_front_image_file_id: Optional[str]
    """The front image of the check. This is a black and white TIFF image file."""

    check_number: Optional[str]
    """The number of the check.

    This field is set by the depositing bank and can be unreliable.
    """

    check_rear_image_file_id: Optional[str]
    """The rear image of the check. This is a black and white TIFF image file."""

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

    foreign_exchange_reference: Optional[str]
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

    foreign_trace_number: Optional[str]
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

    originator_postal_code: Optional[str]
    """A portion of the originator address. This may be incomplete."""

    originator_state_or_province: Optional[str]
    """A portion of the originator address. This may be incomplete."""

    originator_street_address: str
    """A portion of the originator address. This may be incomplete."""

    payment_related_information: Optional[str]
    """A description field set by the originator."""

    payment_related_information2: Optional[str]
    """A description field set by the originator."""

    receiver_city: str
    """A portion of the receiver address. This may be incomplete."""

    receiver_country: str
    """A portion of the receiver address.

    The [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), Alpha-2
    country code of the receiver country.
    """

    receiver_identification_number: Optional[str]
    """An identification number the originator uses for the receiver."""

    receiver_postal_code: Optional[str]
    """A portion of the receiver address. This may be incomplete."""

    receiver_state_or_province: Optional[str]
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

    remittance_information: Optional[str]
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real-Time Payments network identification of the transfer."""


class SourceInboundWireDrawdownPayment(BaseModel):
    amount: int
    """The amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    beneficiary_address_line1: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_address_line2: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_address_line3: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_name: Optional[str]
    """A name set by the sender."""

    beneficiary_reference: Optional[str]
    """A free-form reference string set by the sender, to help identify the transfer."""

    description: str
    """An Increase-constructed description of the transfer."""

    input_message_accountability_data: Optional[str]
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the receiving bank.
    """

    originator_address_line1: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_address_line2: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_address_line3: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_name: Optional[str]
    """The originator of the wire, set by the sending bank."""

    originator_routing_number: Optional[str]
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    originator_to_beneficiary_information: Optional[str]
    """An Increase-created concatenation of the Originator-to-Beneficiary lines."""

    originator_to_beneficiary_information_line1: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line2: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line3: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line4: Optional[str]
    """A free-form message set by the wire originator."""


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

    originator_routing_number: Optional[str]
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

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
    """The amount that was reversed in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the reversal was created.
    """

    description: str
    """
    The description on the reversal message from Fedwire, set by the reversing bank.
    """

    financial_institution_to_financial_institution_information: Optional[str]
    """Additional financial institution information included in the wire reversal."""

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

    originator_routing_number: Optional[str]
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    previous_message_input_cycle_date: date
    """
    The Fedwire cycle date for the wire transfer that is being reversed by this
    message.
    """

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

    transaction_id: str
    """The ID for the Transaction associated with the transfer reversal."""

    wire_transfer_id: str
    """The ID for the Wire Transfer that is being reversed."""


class SourceInboundWireTransfer(BaseModel):
    amount: int
    """The amount in USD cents."""

    beneficiary_address_line1: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_address_line2: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_address_line3: Optional[str]
    """A free-form address field set by the sender."""

    beneficiary_name: Optional[str]
    """A name set by the sender."""

    beneficiary_reference: Optional[str]
    """A free-form reference string set by the sender, to help identify the transfer."""

    description: str
    """An Increase-constructed description of the transfer."""

    input_message_accountability_data: Optional[str]
    """
    A unique identifier available to the originating and receiving banks, commonly
    abbreviated as IMAD. It is created when the wire is submitted to the Fedwire
    service and is helpful when debugging wires with the originating bank.
    """

    originator_address_line1: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_address_line2: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_address_line3: Optional[str]
    """The address of the wire originator, set by the sending bank."""

    originator_name: Optional[str]
    """The originator of the wire, set by the sending bank."""

    originator_routing_number: Optional[str]
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    originator_to_beneficiary_information: Optional[str]
    """An Increase-created concatenation of the Originator-to-Beneficiary lines."""

    originator_to_beneficiary_information_line1: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line2: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line3: Optional[str]
    """A free-form message set by the wire originator."""

    originator_to_beneficiary_information_line4: Optional[str]
    """A free-form message set by the wire originator."""


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
        "check_adjustment",
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
    """An Internal Source is a transaction between you and Increase.

    This describes the reason for the transaction.

    - `account_closure` - Account closure
    - `bank_migration` - Bank migration
    - `cashback` - Cashback
    - `check_adjustment` - Check adjustment
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
    """The identifier of the Real-Time Payments Transfer that led to this Transaction."""


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
    """The identifier of the Wire Transfer that led to this Transaction."""


class SourceWireTransferRejection(BaseModel):
    transfer_id: str
    """The identifier of the Wire Transfer that led to this Transaction."""


class Source(BaseModel):
    account_transfer_intention: Optional[SourceAccountTransferIntention]
    """An Account Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_intention`.
    """

    ach_transfer_intention: Optional[SourceACHTransferIntention]
    """An ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_intention`.
    """

    ach_transfer_rejection: Optional[SourceACHTransferRejection]
    """An ACH Transfer Rejection object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_rejection`.
    """

    ach_transfer_return: Optional[SourceACHTransferReturn]
    """An ACH Transfer Return object.

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
        "card_settlement",
        "card_revenue_payment",
        "check_deposit_acceptance",
        "check_deposit_return",
        "check_transfer_deposit",
        "check_transfer_intention",
        "check_transfer_stop_payment_request",
        "fee_payment",
        "inbound_ach_transfer",
        "inbound_ach_transfer_return_intention",
        "inbound_check",
        "inbound_international_ach_transfer",
        "inbound_real_time_payments_transfer_confirmation",
        "inbound_wire_drawdown_payment_reversal",
        "inbound_wire_drawdown_payment",
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
    - `card_dispute_acceptance` - Card Dispute Acceptance: details will be under the
      `card_dispute_acceptance` object.
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
    - `check_transfer_intention` - Check Transfer Intention: details will be under
      the `check_transfer_intention` object.
    - `check_transfer_stop_payment_request` - Check Transfer Stop Payment Request:
      details will be under the `check_transfer_stop_payment_request` object.
    - `fee_payment` - Fee Payment: details will be under the `fee_payment` object.
    - `inbound_ach_transfer` - Inbound ACH Transfer Intention: details will be under
      the `inbound_ach_transfer` object.
    - `inbound_ach_transfer_return_intention` - Inbound ACH Transfer Return
      Intention: details will be under the `inbound_ach_transfer_return_intention`
      object.
    - `inbound_check` - Inbound Check: details will be under the `inbound_check`
      object.
    - `inbound_international_ach_transfer` - Inbound International ACH Transfer:
      details will be under the `inbound_international_ach_transfer` object.
    - `inbound_real_time_payments_transfer_confirmation` - Inbound Real-Time
      Payments Transfer Confirmation: details will be under the
      `inbound_real_time_payments_transfer_confirmation` object.
    - `inbound_wire_drawdown_payment_reversal` - Inbound Wire Drawdown Payment
      Reversal: details will be under the `inbound_wire_drawdown_payment_reversal`
      object.
    - `inbound_wire_drawdown_payment` - Inbound Wire Drawdown Payment: details will
      be under the `inbound_wire_drawdown_payment` object.
    - `inbound_wire_reversal` - Inbound Wire Reversal: details will be under the
      `inbound_wire_reversal` object.
    - `inbound_wire_transfer` - Inbound Wire Transfer: details will be under the
      `inbound_wire_transfer` object.
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
    - `wire_transfer_rejection` - Wire Transfer Rejection: details will be under the
      `wire_transfer_rejection` object.
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
    """An Inbound ACH Transfer Intention object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_ach_transfer`.
    """

    inbound_check: Optional[SourceInboundCheck]
    """An Inbound Check object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_check`.
    """

    inbound_international_ach_transfer: Optional[SourceInboundInternationalACHTransfer]
    """An Inbound International ACH Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_international_ach_transfer`.
    """

    inbound_real_time_payments_transfer_confirmation: Optional[SourceInboundRealTimePaymentsTransferConfirmation]
    """An Inbound Real-Time Payments Transfer Confirmation object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_confirmation`.
    """

    inbound_wire_drawdown_payment: Optional[SourceInboundWireDrawdownPayment]
    """An Inbound Wire Drawdown Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment`.
    """

    inbound_wire_drawdown_payment_reversal: Optional[SourceInboundWireDrawdownPaymentReversal]
    """An Inbound Wire Drawdown Payment Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_drawdown_payment_reversal`.
    """

    inbound_wire_reversal: Optional[SourceInboundWireReversal]
    """An Inbound Wire Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_reversal`.
    """

    inbound_wire_transfer: Optional[SourceInboundWireTransfer]
    """An Inbound Wire Transfer object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_wire_transfer`.
    """

    interest_payment: Optional[SourceInterestPayment]
    """An Interest Payment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `interest_payment`.
    """

    internal_source: Optional[SourceInternalSource]
    """An Internal Source object.

    This field will be present in the JSON response if and only if `category` is
    equal to `internal_source`.
    """

    real_time_payments_transfer_acknowledgement: Optional[SourceRealTimePaymentsTransferAcknowledgement]
    """A Real-Time Payments Transfer Acknowledgement object.

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
