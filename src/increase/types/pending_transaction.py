# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = [
    "PendingTransaction",
    "Source",
    "SourceAccountTransferInstruction",
    "SourceACHTransferInstruction",
    "SourceCardAuthorization",
    "SourceCardAuthorizationNetworkDetails",
    "SourceCardAuthorizationNetworkDetailsVisa",
    "SourceCheckDepositInstruction",
    "SourceCheckTransferInstruction",
    "SourceInboundFundsHold",
    "SourceCardRouteAuthorization",
    "SourceRealTimePaymentsTransferInstruction",
    "SourceWireDrawdownPaymentInstruction",
    "SourceWireTransferInstruction",
]


class SourceAccountTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the destination
    account currency.
    """

    transfer_id: str
    """The identifier of the Account Transfer that led to this Pending Transaction."""


class SourceACHTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Pending Transaction."""


class SourceCardAuthorizationNetworkDetailsVisa(BaseModel):
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


class SourceCardAuthorizationNetworkDetails(BaseModel):
    visa: SourceCardAuthorizationNetworkDetailsVisa
    """Fields specific to the `visa` network"""


class SourceCardAuthorization(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    digital_wallet_token_id: Optional[str]
    """
    If the authorization was made via a Digital Wallet Token (such as an Apple Pay
    purchase), the identifier of the token that was used.
    """

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) when this authorization
    will expire and the pending transaction will be released.
    """

    id: str
    """The Card Authorization identifier."""

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

    network: Literal["visa"]
    """The payment network used to process this card authorization"""

    network_details: SourceCardAuthorizationNetworkDetails
    """Fields specific to the `network`"""

    pending_transaction_id: Optional[str]
    """The identifier of the Pending Transaction associated with this Transaction."""

    real_time_decision_id: Optional[str]
    """
    The identifier of the Real-Time Decision sent to approve or decline this
    transaction.
    """

    type: Literal["card_authorization"]
    """A constant representing the object's type.

    For this resource it will always be `card_authorization`.
    """


class SourceCheckDepositInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    back_image_file_id: Optional[str]
    """
    The identifier of the File containing the image of the back of the check that
    was deposited.
    """

    check_deposit_id: Optional[str]
    """The identifier of the Check Deposit."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the
    transaction's currency.
    """

    front_image_file_id: str
    """
    The identifier of the File containing the image of the front of the check that
    was deposited.
    """


class SourceCheckTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check's
    currency.
    """

    transfer_id: str
    """The identifier of the Check Transfer that led to this Pending Transaction."""


class SourceInboundFundsHold(BaseModel):
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
    """

    held_transaction_id: Optional[str]
    """The ID of the Transaction for which funds were held."""

    pending_transaction_id: Optional[str]
    """The ID of the Pending Transaction representing the held funds."""

    released_at: Optional[datetime]
    """When the hold was released (if it has been released)."""

    status: Literal["held", "complete"]
    """The status of the hold."""


class SourceCardRouteAuthorization(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
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


class SourceRealTimePaymentsTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    transfer_id: str
    """
    The identifier of the Real Time Payments Transfer that led to this Pending
    Transaction.
    """


class SourceWireDrawdownPaymentInstruction(BaseModel):
    account_number: str

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    message_to_recipient: str

    routing_number: str


class SourceWireTransferInstruction(BaseModel):
    account_number: str

    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    message_to_recipient: str

    routing_number: str

    transfer_id: str


class Source(BaseModel):
    account_transfer_instruction: Optional[SourceAccountTransferInstruction]
    """A Account Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `account_transfer_instruction`.
    """

    ach_transfer_instruction: Optional[SourceACHTransferInstruction]
    """A ACH Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `ach_transfer_instruction`.
    """

    card_authorization: Optional[SourceCardAuthorization]
    """A Card Authorization object.

    This field will be present in the JSON response if and only if `category` is
    equal to `card_authorization`.
    """

    card_route_authorization: Optional[SourceCardRouteAuthorization]
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
        "inbound_funds_hold",
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

    check_deposit_instruction: Optional[SourceCheckDepositInstruction]
    """A Check Deposit Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_deposit_instruction`.
    """

    check_transfer_instruction: Optional[SourceCheckTransferInstruction]
    """A Check Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `check_transfer_instruction`.
    """

    inbound_funds_hold: Optional[SourceInboundFundsHold]
    """A Inbound Funds Hold object.

    This field will be present in the JSON response if and only if `category` is
    equal to `inbound_funds_hold`.
    """

    real_time_payments_transfer_instruction: Optional[SourceRealTimePaymentsTransferInstruction]
    """A Real Time Payments Transfer Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `real_time_payments_transfer_instruction`.
    """

    wire_drawdown_payment_instruction: Optional[SourceWireDrawdownPaymentInstruction]
    """A Wire Drawdown Payment Instruction object.

    This field will be present in the JSON response if and only if `category` is
    equal to `wire_drawdown_payment_instruction`.
    """

    wire_transfer_instruction: Optional[SourceWireTransferInstruction]
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

    completed_at: Optional[datetime]
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending
    Transaction was completed.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date on which the Pending
    Transaction occured.
    """

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
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

    route_id: Optional[str]
    """The identifier for the route this Pending Transaction came through.

    Routes are things like cards and ACH details.
    """

    route_type: Optional[Literal["account_number", "card"]]
    """The type of the route this Pending Transaction came through."""

    source: Source
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
