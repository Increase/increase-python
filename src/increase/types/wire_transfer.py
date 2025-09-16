# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "WireTransfer",
    "Approval",
    "Cancellation",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "Remittance",
    "RemittanceTax",
    "RemittanceUnstructured",
    "Reversal",
    "Submission",
]


class Approval(BaseModel):
    approved_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was approved.
    """

    approved_by: Optional[str] = None
    """
    If the Transfer was approved by a user in the dashboard, the email address of
    that user.
    """


class Cancellation(BaseModel):
    canceled_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Transfer was canceled.
    """

    canceled_by: Optional[str] = None
    """
    If the Transfer was canceled by a user in the dashboard, the email address of
    that user.
    """


class CreatedByAPIKey(BaseModel):
    description: Optional[str] = None
    """The description set for the API key when it was created."""


class CreatedByOAuthApplication(BaseModel):
    name: str
    """The name of the OAuth Application."""


class CreatedByUser(BaseModel):
    email: str
    """The email address of the User."""


class CreatedBy(BaseModel):
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


class RemittanceTax(BaseModel):
    date: datetime.date
    """The month and year the tax payment is for, in YYYY-MM-DD format.

    The day is ignored.
    """

    identification_number: str
    """
    The 9-digit Tax Identification Number (TIN) or Employer Identification Number
    (EIN).
    """

    type_code: str
    """The 5-character tax type code."""


class RemittanceUnstructured(BaseModel):
    message: str
    """The message to the beneficiary."""


class Remittance(BaseModel):
    category: Literal["unstructured", "tax"]
    """The type of remittance information being passed.

    - `unstructured` - The wire transfer contains unstructured remittance
      information.
    - `tax` - The wire transfer is for tax payment purposes to the Internal Revenue
      Service (IRS).
    """

    tax: Optional[RemittanceTax] = None
    """Internal Revenue Service (IRS) tax repayment information.

    Required if `category` is equal to `tax`.
    """

    unstructured: Optional[RemittanceUnstructured] = None
    """Unstructured remittance information.

    Required if `category` is equal to `unstructured`.
    """


class Reversal(BaseModel):
    amount: int
    """The amount that was reversed in USD cents."""

    created_at: datetime.datetime
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

    input_cycle_date: datetime.date
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

    return_reason_code: Optional[str] = None
    """A code provided by the sending bank giving a reason for the reversal.

    It will generally be one of the codes defined in the ISO20022
    `ExternalReturnReason1Code` code set, but this is not enforced by the network.
    """

    return_reason_code_description: Optional[str] = None
    """An Increase-generated description of the `return_reason_code`."""

    transaction_id: str
    """The ID for the Transaction associated with the transfer reversal."""

    wire_transfer_id: str
    """The ID for the Wire Transfer that is being reversed."""


class Submission(BaseModel):
    input_message_accountability_data: str
    """The accountability data for the submission."""

    submitted_at: datetime.datetime
    """When this wire transfer was submitted to Fedwire."""


class WireTransfer(BaseModel):
    id: str
    """The wire transfer's identifier."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number: str
    """The destination account number."""

    amount: int
    """The transfer amount in USD cents."""

    approval: Optional[Approval] = None
    """
    If your account requires approvals for transfers and the transfer was approved,
    this will contain details of the approval.
    """

    beneficiary_address_line1: Optional[str] = None
    """The beneficiary's address line 1."""

    beneficiary_address_line2: Optional[str] = None
    """The beneficiary's address line 2."""

    beneficiary_address_line3: Optional[str] = None
    """The beneficiary's address line 3."""

    beneficiary_name: Optional[str] = None
    """The beneficiary's name."""

    cancellation: Optional[Cancellation] = None
    """
    If your account requires approvals for transfers and the transfer was not
    approved, this will contain details of the cancellation.
    """

    created_at: datetime.datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the transfer, either via the API or the dashboard."""

    currency: Literal["CAD", "CHF", "EUR", "GBP", "JPY", "USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For wire transfers this is always equal to `usd`.

    - `CAD` - Canadian Dollar (CAD)
    - `CHF` - Swiss Franc (CHF)
    - `EUR` - Euro (EUR)
    - `GBP` - British Pound (GBP)
    - `JPY` - Japanese Yen (JPY)
    - `USD` - US Dollar (USD)
    """

    external_account_id: Optional[str] = None
    """The identifier of the External Account the transfer was made to, if any."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    inbound_wire_drawdown_request_id: Optional[str] = None
    """
    The ID of an Inbound Wire Drawdown Request in response to which this transfer
    was sent.
    """

    message_to_recipient: str
    """The message that will show on the recipient's bank statement."""

    network: Literal["wire"]
    """The transfer's network."""

    originator_address_line1: Optional[str] = None
    """The originator's address line 1."""

    originator_address_line2: Optional[str] = None
    """The originator's address line 2."""

    originator_address_line3: Optional[str] = None
    """The originator's address line 3."""

    originator_name: Optional[str] = None
    """The originator's name."""

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer.

    A pending transaction is created when the transfer
    [requires approval](https://increase.com/documentation/transfer-approvals#transfer-approvals)
    by someone else in your organization.
    """

    remittance: Optional[Remittance] = None
    """Remittance information sent with the wire transfer."""

    reversal: Optional[Reversal] = None
    """If your transfer is reversed, this will contain details of the reversal."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    source_account_number_id: Optional[str] = None
    """The Account Number that was passed to the wire's recipient."""

    status: Literal[
        "pending_approval",
        "canceled",
        "pending_reviewing",
        "rejected",
        "requires_attention",
        "pending_creating",
        "reversed",
        "submitted",
        "complete",
    ]
    """The lifecycle status of the transfer.

    - `pending_approval` - The transfer is pending approval.
    - `canceled` - The transfer has been canceled.
    - `pending_reviewing` - The transfer is pending review by Increase.
    - `rejected` - The transfer has been rejected by Increase.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `pending_creating` - The transfer is pending creation.
    - `reversed` - The transfer has been reversed.
    - `submitted` - The transfer has been submitted to Fedwire.
    - `complete` - The transfer has been acknowledged by Fedwire and can be
      considered complete.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to Fedwire, this will contain supplemental
    details.
    """

    transaction_id: Optional[str] = None
    """The ID for the transaction funding the transfer."""

    type: Literal["wire_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `wire_transfer`.
    """
