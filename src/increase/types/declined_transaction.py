# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = [
    "DeclinedTransaction",
    "Source",
    "SourceACHDecline",
    "SourceCardDecline",
    "SourceCardDeclineNetworkDetails",
    "SourceCardDeclineNetworkDetailsVisa",
    "SourceCheckDecline",
    "SourceInboundRealTimePaymentsTransferDecline",
    "SourceInternationalACHDecline",
    "SourceCardRouteDecline",
    "SourceWireDecline",
]


class SourceACHDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    originator_company_descriptive_date: Optional[str]

    originator_company_discretionary_data: Optional[str]

    originator_company_id: str

    originator_company_name: str

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
        "no_ach_route",
        "originator_request",
        "transaction_not_allowed",
    ]
    """Why the ACH transfer was declined."""

    receiver_id_number: Optional[str]

    receiver_name: Optional[str]

    trace_number: str


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
    ]
    """
    For electronic commerce transactions, this identifies the level of security used
    in obtaining the customer's payment credential. For mail or telephone order
    transactions, identifies the type of mail or telephone order.
    """

    point_of_service_entry_mode: Optional[shared.PointOfServiceEntryMode]
    """
    The method used to enter the cardholder's primary account number and card
    expiration date
    """


class SourceCardDeclineNetworkDetails(BaseModel):
    visa: SourceCardDeclineNetworkDetailsVisa
    """Fields specific to the `visa` network"""


class SourceCardDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    digital_wallet_token_id: Optional[str]
    """
    If the authorization was attempted using a Digital Wallet Token (such as an
    Apple Pay purchase), the identifier of the token that was used.
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

    network: Literal["visa"]
    """The payment network used to process this card authorization"""

    network_details: SourceCardDeclineNetworkDetails
    """Fields specific to the `network`"""

    real_time_decision_id: Optional[str]
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    reason: Literal[
        "card_not_active",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "cvv2_mismatch",
        "transaction_not_allowed",
        "breaches_internal_limit",
        "breaches_limit",
        "webhook_declined",
        "webhook_timed_out",
        "declined_by_stand_in_processing",
        "invalid_physical_card",
        "missing_original_authorization",
    ]
    """Why the transaction was declined."""


class SourceCheckDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    auxiliary_on_us: Optional[str]

    reason: Literal[
        "ach_route_canceled",
        "ach_route_disabled",
        "breaches_limit",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "unable_to_locate_account",
        "unable_to_process",
        "refer_to_image",
        "stop_payment_requested",
        "returned",
        "duplicate_presentment",
        "not_authorized",
        "altered_or_fictitious",
    ]
    """Why the check was declined."""


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
    transfer's currency. This will always be "USD" for a Real Time Payments
    transfer.
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
    """Why the transfer was declined."""

    remittance_information: Optional[str]
    """Additional information included with the transfer."""

    transaction_identification: str
    """The Real Time Payments network identification of the declined transfer."""


class SourceInternationalACHDecline(BaseModel):
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


class SourceCardRouteDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: Optional[str]

    merchant_city: Optional[str]

    merchant_country: str

    merchant_descriptor: str

    merchant_state: Optional[str]


class SourceWireDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

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

    originator_to_beneficiary_information_line1: Optional[str]

    originator_to_beneficiary_information_line2: Optional[str]

    originator_to_beneficiary_information_line3: Optional[str]

    originator_to_beneficiary_information_line4: Optional[str]

    reason: Literal[
        "account_number_canceled",
        "account_number_disabled",
        "entity_not_active",
        "group_locked",
        "no_account_number",
        "transaction_not_allowed",
    ]
    """Why the wire transfer was declined."""


class Source(BaseModel):
    ach_decline: Optional[SourceACHDecline]
    """A ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_decline`.
    """

    card_decline: Optional[SourceCardDecline]
    """A Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_decline`.
    """

    card_route_decline: Optional[SourceCardRouteDecline]
    """A Deprecated Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_route_decline`.
    """

    category: Literal[
        "ach_decline",
        "card_decline",
        "check_decline",
        "inbound_real_time_payments_transfer_decline",
        "international_ach_decline",
        "card_route_decline",
        "wire_decline",
        "other",
    ]
    """The type of decline that took place.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    check_decline: Optional[SourceCheckDecline]
    """A Check Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_decline`.
    """

    inbound_real_time_payments_transfer_decline: Optional[SourceInboundRealTimePaymentsTransferDecline]
    """A Inbound Real Time Payments Transfer Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_real_time_payments_transfer_decline`.
    """

    international_ach_decline: Optional[SourceInternationalACHDecline]
    """A International ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `international_ach_decline`.
    """

    wire_decline: Optional[SourceWireDecline]
    """A Wire Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_decline`.
    """


class DeclinedTransaction(BaseModel):
    account_id: str
    """The identifier for the Account the Declined Transaction belongs to."""

    amount: int
    """The Declined Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the
    Transaction occured.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Declined
    Transaction's currency. This will match the currency on the Declined
    Transcation's Account.
    """

    description: str
    """This is the description the vendor provides."""

    id: str
    """The Declined Transaction identifier."""

    route_id: Optional[str]
    """The identifier for the route this Declined Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card"]]
    """The type of the route this Declined Transaction came through."""

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
