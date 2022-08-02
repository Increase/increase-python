# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PendingTransactionSourceAccountTransferInstruction",
    "PendingTransactionSourceACHTransferInstruction",
    "PendingTransactionSourceCardAuthorization",
    "PendingTransactionSourceCheckDepositInstruction",
    "PendingTransactionSourceCheckTransferInstruction",
    "PendingTransactionSourceCardRouteAuthorization",
    "PendingTransactionSourceWireDrawdownPaymentInstruction",
    "PendingTransactionSourceWireTransferInstruction",
    "PendingTransactionSource",
    "PendingTransaction",
    "DeclinedTransactionSourceACHDecline",
    "DeclinedTransactionSourceCardDecline",
    "DeclinedTransactionSourceCheckDecline",
    "DeclinedTransactionSourceInternationalACHDecline",
    "DeclinedTransactionSourceCardRouteDecline",
    "DeclinedTransactionSource",
    "DeclinedTransaction",
    "CardAuthorizationSimulation",
]


class PendingTransactionSourceAccountTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
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


class PendingTransactionSourceCardAuthorization(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: str

    merchant_city: Optional[str]

    merchant_country: str

    merchant_descriptor: str


class PendingTransactionSourceCheckDepositInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    back_image_file_id: Optional[str]
    """
    The identifier of the File containing the image of the back of the check that
    was deposited.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
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

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    transfer_id: str
    """The identifier of the Check Transfer that led to this Pending Transaction."""


class PendingTransactionSourceCardRouteAuthorization(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: str

    merchant_city: Optional[str]

    merchant_country: str

    merchant_descriptor: str

    merchant_state: Optional[str]


class PendingTransactionSourceWireDrawdownPaymentInstruction(BaseModel):
    account_number: str

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    message_to_recipient: str

    routing_number: str


class PendingTransactionSourceWireTransferInstruction(BaseModel):
    account_number: str

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    message_to_recipient: str

    routing_number: str

    transfer_id: str


class PendingTransactionSource(BaseModel):
    account_transfer_instruction: Optional[PendingTransactionSourceAccountTransferInstruction]
    """A Account Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_instruction`.
    """

    ach_transfer_instruction: Optional[PendingTransactionSourceACHTransferInstruction]
    """A ACH Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_instruction`.
    """

    card_authorization: Optional[PendingTransactionSourceCardAuthorization]
    """A Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization`.
    """

    card_route_authorization: Optional[PendingTransactionSourceCardRouteAuthorization]
    """A Deprecated Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_route_authorization`.
    """

    category: Literal[
        "account_transfer_instruction",
        "ach_transfer_instruction",
        "card_authorization",
        "check_deposit_instruction",
        "check_transfer_instruction",
        "card_route_authorization",
        "real_time_payments_transfer_instruction",
        "wire_drawdown_payment_instruction",
        "wire_transfer_instruction",
        "other",
    ]
    """The type of transaction that took place.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    check_deposit_instruction: Optional[PendingTransactionSourceCheckDepositInstruction]
    """A Check Deposit Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_instruction`.
    """

    check_transfer_instruction: Optional[PendingTransactionSourceCheckTransferInstruction]
    """A Check Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_instruction`.
    """

    wire_drawdown_payment_instruction: Optional[PendingTransactionSourceWireDrawdownPaymentInstruction]
    """A Wire Drawdown Payment Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_drawdown_payment_instruction`.
    """

    wire_transfer_instruction: Optional[PendingTransactionSourceWireTransferInstruction]
    """A Wire Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_transfer_instruction`.
    """


class PendingTransaction(BaseModel):
    account_id: str
    """The identifier for the account this Pending Transaction belongs to."""

    amount: int
    """The Pending Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending
    Transaction occured.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Pending
    Transaction's currency. This will match the currency on the Pending
    Transcation's Account.
    """

    description: str
    """
    For a Pending Transaction related to a transfer, this is the description you
    provide. For a Pending Transaction related to a payment, this is the description
    the vendor provides.
    """

    id: str
    """The Pending Transaction identifier."""

    route_id: str
    """The identifier for the route this Pending Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[str]
    """The type of the route this Pending Transaction came through."""

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
    """

    type: Literal["pending_transaction"]
    """A constant representing the object's type.

    For this resource it will always be `pending_transaction`.
    """


class DeclinedTransactionSourceACHDecline(BaseModel):
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
        "no_ach_route",
        "breaches_limit",
        "credit_entry_refused_by_receiver",
        "group_locked",
        "entity_not_active",
        "insufficient_funds",
        "originator_request",
    ]
    """Why the ACH transfer was declined."""

    receiver_id_number: Optional[str]

    receiver_name: Optional[str]

    trace_number: str


class DeclinedTransactionSourceCardDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    merchant_acceptor_id: str

    merchant_category_code: Optional[str]

    merchant_city: Optional[str]

    merchant_country: Optional[str]

    merchant_descriptor: str

    merchant_state: Optional[str]

    reason: Literal[
        "card_not_active",
        "entity_not_active",
        "group_locked",
        "insufficient_funds",
        "breaches_limit",
        "webhook_declined",
        "webhook_timed_out",
    ]
    """Why the transaction was declined."""


class DeclinedTransactionSourceCheckDecline(BaseModel):
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
    ]
    """Why the check was declined."""


class DeclinedTransactionSourceInternationalACHDecline(BaseModel):
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


class DeclinedTransactionSourceCardRouteDecline(BaseModel):
    amount: int
    """The declined amount in the minor unit of the destination account currency.

    For dollars, for example, this is cents.
    """

    currency: str
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


class DeclinedTransactionSource(BaseModel):
    ach_decline: Optional[DeclinedTransactionSourceACHDecline]
    """A ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_decline`.
    """

    card_decline: Optional[DeclinedTransactionSourceCardDecline]
    """A Card Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_decline`.
    """

    card_route_decline: Optional[DeclinedTransactionSourceCardRouteDecline]
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
        "other",
    ]
    """The type of decline that took place.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    check_decline: Optional[DeclinedTransactionSourceCheckDecline]
    """A Check Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_decline`.
    """

    international_ach_decline: Optional[DeclinedTransactionSourceInternationalACHDecline]
    """A International ACH Decline object.

    This field will be present in the JSON response if and only if `category` is
    equal to `international_ach_decline`.
    """


class DeclinedTransaction(BaseModel):
    account_id: str
    """The identifier for the Account the Declined Transaction belongs to."""

    amount: int
    """The Declined Transaction amount in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    created_at: str
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the
    Transaction occured.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the Declined
    Transaction's currency. This will match the currency on the Declined
    Transcation's Account.
    """

    description: str
    """This is the description the vendor provides."""

    id: str
    """The Declined Transaction identifier."""

    route_id: str
    """The identifier for the route this Declined Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[str]
    """The type of the route this Declined Transaction came through."""

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


class CardAuthorizationSimulation(BaseModel):
    declined_transaction: Optional[DeclinedTransaction]
    """
    If the authorization attempt fails, this will contain the resulting
    [Declined Transaction](#declined-transactions) object. The Declined
    Transaction's `source` will be of `category: card_decline`.
    """

    pending_transaction: Optional[PendingTransaction]
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
