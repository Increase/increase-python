# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "SwiftTransfer",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "CreditorAddress",
    "DebtorAddress",
]


class CreatedByAPIKey(BaseModel):
    """If present, details about the API key that created the transfer."""

    description: Optional[str] = None
    """The description set for the API key when it was created."""


class CreatedByOAuthApplication(BaseModel):
    """If present, details about the OAuth Application that created the transfer."""

    name: str
    """The name of the OAuth Application."""


class CreatedByUser(BaseModel):
    """If present, details about the User that created the transfer."""

    email: str
    """The email address of the User."""


class CreatedBy(BaseModel):
    """What object created the transfer, either via the API or the dashboard."""

    api_key: Optional[CreatedByAPIKey] = None
    """If present, details about the API key that created the transfer."""

    category: Literal["api_key", "oauth_application", "user"]
    """The type of object that created this transfer.

    - `api_key` - An API key. Details will be under the `api_key` object.
    - `oauth_application` - An OAuth application you connected to Increase. Details
      will be under the `oauth_application` object.
    - `user` - A User in the Increase dashboard. Details will be under the `user`
      object.
    """

    oauth_application: Optional[CreatedByOAuthApplication] = None
    """If present, details about the OAuth Application that created the transfer."""

    user: Optional[CreatedByUser] = None
    """If present, details about the User that created the transfer."""


class CreditorAddress(BaseModel):
    """The creditor's address."""

    city: Optional[str] = None
    """The city, district, town, or village of the address."""

    country: str
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    postal_code: Optional[str] = None
    """The ZIP or postal code of the address."""

    state: Optional[str] = None
    """The state, province, or region of the address. Required in certain countries."""


class DebtorAddress(BaseModel):
    """The debtor's address."""

    city: Optional[str] = None
    """The city, district, town, or village of the address."""

    country: str
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    postal_code: Optional[str] = None
    """The ZIP or postal code of the address."""

    state: Optional[str] = None
    """The state, province, or region of the address. Required in certain countries."""


class SwiftTransfer(BaseModel):
    """Swift Transfers send funds internationally."""

    id: str
    """The Swift transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The creditor's account number."""

    amount: int
    """The transfer amount in USD cents."""

    bank_identification_code: str
    """The bank identification code (BIC) of the creditor."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: CreatedBy
    """What object created the transfer, either via the API or the dashboard."""

    creditor_address: CreditorAddress
    """The creditor's address."""

    creditor_name: str
    """The creditor's name."""

    debtor_address: DebtorAddress
    """The debtor's address."""

    debtor_name: str
    """The debtor's name."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    instructed_amount: int
    """
    The amount that was instructed to be transferred in minor units of the
    `instructed_currency`.
    """

    instructed_currency: Literal["USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the
    instructed amount.

    - `USD` - United States Dollar
    """

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer."""

    routing_number: Optional[str] = None
    """The creditor's bank account routing or transit number.

    Required in certain countries.
    """

    source_account_number_id: str
    """The Account Number included in the transfer as the debtor's account number."""

    status: Literal[
        "pending_approval",
        "canceled",
        "pending_reviewing",
        "requires_attention",
        "pending_initiating",
        "initiated",
        "rejected",
        "returned",
    ]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is pending approval.
    - `canceled` - The transfer has been canceled.
    - `pending_reviewing` - The transfer is pending review by Increase.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `pending_initiating` - The transfer is pending initiation.
    - `initiated` - The transfer has been initiated.
    - `rejected` - The transfer has been rejected by Increase.
    - `returned` - The transfer has been returned.
    """

    transaction_id: Optional[str] = None
    """The ID for the transaction funding the transfer.

    This will be populated after the transfer is initiated.
    """

    type: Literal["swift_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `swift_transfer`.
    """

    unique_end_to_end_transaction_reference: str
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    for the transfer.
    """

    unstructured_remittance_information: str
    """The unstructured remittance information that was included with the transfer."""
