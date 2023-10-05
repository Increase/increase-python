# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CardPayment",
    "Element",
    "ElementCardAuthorization",
    "ElementCardAuthorizationNetworkDetails",
    "ElementCardAuthorizationNetworkDetailsVisa",
    "ElementCardAuthorizationExpiration",
    "ElementCardDecline",
    "ElementCardDeclineNetworkDetails",
    "ElementCardDeclineNetworkDetailsVisa",
    "ElementCardIncrement",
    "ElementCardRefund",
    "ElementCardRefundPurchaseDetails",
    "ElementCardRefundPurchaseDetailsCarRental",
    "ElementCardRefundPurchaseDetailsLodging",
    "ElementCardRefundPurchaseDetailsTravel",
    "ElementCardRefundPurchaseDetailsTravelAncillary",
    "ElementCardRefundPurchaseDetailsTravelAncillaryService",
    "ElementCardRefundPurchaseDetailsTravelTripLeg",
    "ElementCardReversal",
    "ElementCardSettlement",
    "ElementCardSettlementPurchaseDetails",
    "ElementCardSettlementPurchaseDetailsCarRental",
    "ElementCardSettlementPurchaseDetailsLodging",
    "ElementCardSettlementPurchaseDetailsTravel",
    "ElementCardSettlementPurchaseDetailsTravelAncillary",
    "ElementCardSettlementPurchaseDetailsTravelAncillaryService",
    "ElementCardSettlementPurchaseDetailsTravelTripLeg",
    "ElementCardValidation",
    "ElementCardValidationNetworkDetails",
    "ElementCardValidationNetworkDetailsVisa",
    "State",
]


class ElementCardAuthorizationNetworkDetailsVisa(BaseModel):
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
    ]
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
    ]
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


class ElementCardAuthorizationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[ElementCardAuthorizationNetworkDetailsVisa]
    """Fields specific to the `visa` network."""


class ElementCardAuthorization(BaseModel):
    id: str
    """The Card Authorization identifier."""

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

    digital_wallet_token_id: Optional[str]
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

    merchant_category_code: Optional[str]
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: Optional[str]
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    network_details: ElementCardAuthorizationNetworkDetails
    """Fields specific to the `network`."""

    pending_transaction_id: Optional[str]
    """The identifier of the Pending Transaction associated with this Transaction."""

    physical_card_id: Optional[str]
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    real_time_decision_id: Optional[str]
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    type: Literal["card_authorization"]
    """A constant representing the object's type.

    For this resource it will always be `card_authorization`.
    """


class ElementCardAuthorizationExpiration(BaseModel):
    id: str
    """The Card Authorization Expiration identifier."""

    card_authorization_id: str
    """The identifier for the Card Authorization this reverses."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the reversal's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    expired_amount: int
    """
    The amount of this authorization expiration in the minor unit of the
    transaction's currency. For dollars, for example, this is cents.
    """

    network: Literal["visa"]
    """The card network used to process this card authorization.

    - `visa` - Visa
    """

    type: Literal["card_authorization_expiration"]
    """A constant representing the object's type.

    For this resource it will always be `card_authorization_expiration`.
    """


class ElementCardDeclineNetworkDetailsVisa(BaseModel):
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
    ]
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
    ]
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


class ElementCardDeclineNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[ElementCardDeclineNetworkDetailsVisa]
    """Fields specific to the `visa` network."""


class ElementCardDecline(BaseModel):
    id: str
    """The Card Decline identifier."""

    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    card_payment_id: Optional[str]
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

    digital_wallet_token_id: Optional[str]
    """
    If the authorization was made via a Digital Wallet Token (such as an Apple Pay
    purchase), the identifier of the token that was used.
    """

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: Optional[str]
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: Optional[str]
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    merchant_state: Optional[str]
    """The state the merchant resides in."""

    network_details: ElementCardDeclineNetworkDetails
    """Fields specific to the `network`."""

    physical_card_id: Optional[str]
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    real_time_decision_id: Optional[str]
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


class ElementCardIncrement(BaseModel):
    id: str
    """The Card Increment identifier."""

    amount: int
    """The amount of this increment in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    card_authorization_id: str
    """The identifier for the Card Authorization this reverses."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the increment's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    network: Literal["visa"]
    """The card network used to process this card authorization.

    - `visa` - Visa
    """

    real_time_decision_id: Optional[str]
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    incremental authorization.
    """

    type: Literal["card_increment"]
    """A constant representing the object's type.

    For this resource it will always be `card_increment`.
    """

    updated_authorization_amount: int
    """
    The updated authorization amount after this increment, in the minor unit of the
    transaction's currency. For dollars, for example, this is cents.
    """


class ElementCardRefundPurchaseDetailsCarRental(BaseModel):
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


class ElementCardRefundPurchaseDetailsLodging(BaseModel):
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


class ElementCardRefundPurchaseDetailsTravelAncillaryService(BaseModel):
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


class ElementCardRefundPurchaseDetailsTravelAncillary(BaseModel):
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

    services: List[ElementCardRefundPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str]
    """Ticket document number."""


class ElementCardRefundPurchaseDetailsTravelTripLeg(BaseModel):
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


class ElementCardRefundPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[ElementCardRefundPurchaseDetailsTravelAncillary]
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

    trip_legs: Optional[List[ElementCardRefundPurchaseDetailsTravelTripLeg]]
    """Fields specific to each leg of the journey."""


class ElementCardRefundPurchaseDetails(BaseModel):
    car_rental: Optional[ElementCardRefundPurchaseDetailsCarRental]
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

    lodging: Optional[ElementCardRefundPurchaseDetailsLodging]
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

    travel: Optional[ElementCardRefundPurchaseDetailsTravel]
    """Fields specific to travel."""


class ElementCardRefund(BaseModel):
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

    purchase_details: Optional[ElementCardRefundPurchaseDetails]
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


class ElementCardReversal(BaseModel):
    id: str
    """The Card Reversal identifier."""

    card_authorization_id: str
    """The identifier for the Card Authorization this reverses."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the reversal's
    currency.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    network: Literal["visa"]
    """The card network used to process this card authorization.

    - `visa` - Visa
    """

    reversal_amount: int
    """The amount of this reversal in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    type: Literal["card_reversal"]
    """A constant representing the object's type.

    For this resource it will always be `card_reversal`.
    """

    updated_authorization_amount: int
    """
    The amount left pending on the Card Authorization in the minor unit of the
    transaction's currency. For dollars, for example, this is cents.
    """


class ElementCardSettlementPurchaseDetailsCarRental(BaseModel):
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


class ElementCardSettlementPurchaseDetailsLodging(BaseModel):
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


class ElementCardSettlementPurchaseDetailsTravelAncillaryService(BaseModel):
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


class ElementCardSettlementPurchaseDetailsTravelAncillary(BaseModel):
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

    services: List[ElementCardSettlementPurchaseDetailsTravelAncillaryService]
    """Additional travel charges, such as baggage fees."""

    ticket_document_number: Optional[str]
    """Ticket document number."""


class ElementCardSettlementPurchaseDetailsTravelTripLeg(BaseModel):
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


class ElementCardSettlementPurchaseDetailsTravel(BaseModel):
    ancillary: Optional[ElementCardSettlementPurchaseDetailsTravelAncillary]
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

    trip_legs: Optional[List[ElementCardSettlementPurchaseDetailsTravelTripLeg]]
    """Fields specific to each leg of the journey."""


class ElementCardSettlementPurchaseDetails(BaseModel):
    car_rental: Optional[ElementCardSettlementPurchaseDetailsCarRental]
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

    lodging: Optional[ElementCardSettlementPurchaseDetailsLodging]
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

    travel: Optional[ElementCardSettlementPurchaseDetailsTravel]
    """Fields specific to travel."""


class ElementCardSettlement(BaseModel):
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

    pending_transaction_id: Optional[str]
    """The identifier of the Pending Transaction associated with this Transaction."""

    presentment_amount: int
    """The amount in the minor unit of the transaction's presentment currency."""

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's presentment currency.
    """

    purchase_details: Optional[ElementCardSettlementPurchaseDetails]
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


class ElementCardValidationNetworkDetailsVisa(BaseModel):
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
    ]
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
    ]
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


class ElementCardValidationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization.

    - `visa` - Visa
    """

    visa: Optional[ElementCardValidationNetworkDetailsVisa]
    """Fields specific to the `visa` network."""


class ElementCardValidation(BaseModel):
    id: str
    """The Card Validation identifier."""

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

    digital_wallet_token_id: Optional[str]
    """
    If the authorization was made via a Digital Wallet Token (such as an Apple Pay
    purchase), the identifier of the token that was used.
    """

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: Optional[str]
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: Optional[str]
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    network_details: ElementCardValidationNetworkDetails
    """Fields specific to the `network`."""

    physical_card_id: Optional[str]
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    real_time_decision_id: Optional[str]
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    type: Literal["card_validation"]
    """A constant representing the object's type.

    For this resource it will always be `card_validation`.
    """


class Element(BaseModel):
    card_authorization: Optional[ElementCardAuthorization]
    """A Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization`.
    """

    card_authorization_expiration: Optional[ElementCardAuthorizationExpiration]
    """A Card Authorization Expiration object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization_expiration`.
    """

    card_decline: Optional[ElementCardDecline]
    """A Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_decline`.
    """

    card_increment: Optional[ElementCardIncrement]
    """A Card Increment object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_increment`.
    """

    card_refund: Optional[ElementCardRefund]
    """A Card Refund object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_refund`.
    """

    card_reversal: Optional[ElementCardReversal]
    """A Card Reversal object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_reversal`.
    """

    card_settlement: Optional[ElementCardSettlement]
    """A Card Settlement object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_settlement`.
    """

    card_validation: Optional[ElementCardValidation]
    """A Card Validation object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_validation`.
    """

    category: Literal[
        "card_authorization",
        "card_validation",
        "card_decline",
        "card_reversal",
        "card_authorization_expiration",
        "card_increment",
        "card_settlement",
        "card_refund",
        "other",
    ]
    """The type of the resource.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `card_authorization` - Card Authorization: details will be under the
      `card_authorization` object.
    - `card_validation` - Card Validation: details will be under the
      `card_validation` object.
    - `card_decline` - Card Decline: details will be under the `card_decline`
      object.
    - `card_reversal` - Card Reversal: details will be under the `card_reversal`
      object.
    - `card_authorization_expiration` - Card Authorization Expiration: details will
      be under the `card_authorization_expiration` object.
    - `card_increment` - Card Increment: details will be under the `card_increment`
      object.
    - `card_settlement` - Card Settlement: details will be under the
      `card_settlement` object.
    - `card_refund` - Card Refund: details will be under the `card_refund` object.
    - `other` - Unknown card payment element.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the card payment element was created.
    """


class State(BaseModel):
    authorized_amount: int
    """The total authorized amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    incremented_amount: int
    """
    The total incrementally updated authorized amount in the minor unit of the
    transaction's currency. For dollars, for example, this is cents.
    """

    reversed_amount: int
    """The total reversed amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    settled_amount: int
    """
    The total settled or refunded amount in the minor unit of the transaction's
    currency. For dollars, for example, this is cents.
    """


class CardPayment(BaseModel):
    id: str
    """The Card Payment identifier."""

    account_id: str
    """The identifier for the Account the Transaction belongs to."""

    card_id: str
    """The Card identifier for this payment."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Card
    Payment was created.
    """

    elements: List[Element]
    """The interactions related to this card payment."""

    state: State
    """The summarized state of this card payment."""

    type: Literal["card_payment"]
    """A constant representing the object's type.

    For this resource it will always be `card_payment`.
    """
