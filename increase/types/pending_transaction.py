# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SourceAccountTransferInstruction",
    "SourceACHTransferInstruction",
    "SourceCardAuthorization",
    "SourceCheckDepositInstruction",
    "SourceCheckTransferInstruction",
    "SourceCardRouteAuthorization",
    "SourceWireDrawdownPaymentInstruction",
    "SourceWireTransferInstruction",
    "Source",
    "PendingTransaction",
]


class SourceAccountTransferInstruction(BaseModel):
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


class SourceACHTransferInstruction(BaseModel):
    amount: int
    """The pending amount in the minor unit of the transaction's currency.

    For dollars, for example, this is cents.
    """

    transfer_id: str
    """The identifier of the ACH Transfer that led to this Pending Transaction."""


class SourceCardAuthorization(BaseModel):
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


class SourceCheckTransferInstruction(BaseModel):
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


class SourceCardRouteAuthorization(BaseModel):
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
