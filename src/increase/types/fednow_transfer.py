# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FednowTransfer",
    "Acknowledgement",
    "CreatedBy",
    "CreatedByAPIKey",
    "CreatedByOAuthApplication",
    "CreatedByUser",
    "CreditorAddress",
    "DebtorAddress",
    "Rejection",
    "Return",
    "Submission",
]


class Acknowledgement(BaseModel):
    """
    If the transfer is acknowledged by the recipient bank, this will contain supplemental details.
    """

    acknowledged_at: datetime
    """When the transfer was acknowledged."""


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

    category: Literal["api_key", "oauth_application", "user"]
    """The type of object that created this transfer.

    - `api_key` - An API key. Details will be under the `api_key` object.
    - `oauth_application` - An OAuth application you connected to Increase. Details
      will be under the `oauth_application` object.
    - `user` - A User in the Increase dashboard. Details will be under the `user`
      object.
    """

    api_key: Optional[CreatedByAPIKey] = None
    """If present, details about the API key that created the transfer."""

    oauth_application: Optional[CreatedByOAuthApplication] = None
    """If present, details about the OAuth Application that created the transfer."""

    user: Optional[CreatedByUser] = None
    """If present, details about the User that created the transfer."""


class CreditorAddress(BaseModel):
    """The creditor's address."""

    city: Optional[str] = None
    """The city, district, town, or village of the address."""

    line1: Optional[str] = None
    """The first line of the address."""

    postal_code: Optional[str] = None
    """The ZIP code of the address."""

    state: Optional[str] = None
    """The address state."""


class DebtorAddress(BaseModel):
    """The debtor's address."""

    city: Optional[str] = None
    """The city, district, town, or village of the address."""

    line1: Optional[str] = None
    """The first line of the address."""

    postal_code: Optional[str] = None
    """The ZIP code of the address."""

    state: Optional[str] = None
    """The address state."""


class Rejection(BaseModel):
    """
    If the transfer is rejected by FedNow or the destination financial institution, this will contain supplemental details.
    """

    reject_reason_additional_information: Optional[str] = None
    """Additional information about the rejection provided by the recipient bank."""

    reject_reason_code: Literal[
        "account_closed",
        "account_blocked",
        "invalid_creditor_account_type",
        "invalid_creditor_account_number",
        "invalid_creditor_financial_institution_identifier",
        "end_customer_deceased",
        "narrative",
        "transaction_forbidden",
        "transaction_type_not_supported",
        "amount_exceeds_bank_limits",
        "invalid_creditor_address",
        "invalid_debtor_address",
        "timeout",
        "processing_error",
        "other",
    ]
    """
    The reason the transfer was rejected as provided by the recipient bank or the
    FedNow network.

    - `account_closed` - The destination account is closed. Corresponds to the
      FedNow reason code `AC04`.
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the FedNow reason code `AC06`.
    - `invalid_creditor_account_type` - The destination account is ineligible to
      receive FedNow transfers. Corresponds to the FedNow reason code `AC14`.
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the FedNow reason code `AC03`.
    - `invalid_creditor_financial_institution_identifier` - The destination routing
      number is invalid. Corresponds to the FedNow reason code `RC04`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the FedNow reason code `MD07`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field. Corresponds to the FedNow reason code `NARR`.
    - `transaction_forbidden` - FedNow transfers are not allowed to the destination
      account. Corresponds to the FedNow reason code `AG01`.
    - `transaction_type_not_supported` - FedNow transfers are not enabled for the
      destination account. Corresponds to the FedNow reason code `AG03`.
    - `amount_exceeds_bank_limits` - The amount is higher than the recipient is
      authorized to send or receive. Corresponds to the FedNow reason code `E990`.
    - `invalid_creditor_address` - The creditor's address is required, but missing
      or invalid. Corresponds to the FedNow reason code `BE04`.
    - `invalid_debtor_address` - The debtor's address is required, but missing or
      invalid. Corresponds to the FedNow reason code `BE07`.
    - `timeout` - There was a timeout processing the transfer. Corresponds to the
      FedNow reason code `E997`.
    - `processing_error` - The transfer was rejected due to an internal Increase
      issue. We have been notified.
    - `other` - Some other error or issue has occurred.
    """

    rejected_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was rejected.
    """


class Return(BaseModel):
    """
    A FedNow Transfer Return is created when a FedNow Transfer sent from Increase is returned by the recipient's bank.
    """

    amount: int
    """The returned amount in USD cents. This is always a positive number."""

    return_reason_additional_information: Optional[str] = None
    """Additional information about the return provided by the recipient's bank."""

    return_reason_code: Literal[
        "account_closed",
        "account_blocked",
        "invalid_agent",
        "invalid_creditor_account_number",
        "incorrect_account_number",
        "end_customer_deceased",
        "transaction_forbidden",
        "regulatory_reason",
        "fraud",
        "duplication",
        "wrong_amount",
        "requested_by_customer",
        "unable_to_apply",
        "not_specified",
        "narrative",
        "other",
    ]
    """The reason the transfer was returned as provided by the recipient's bank.

    - `account_closed` - The destination account is closed. Corresponds to the
      FedNow reason codes `AC04` and `AC07`.
    - `account_blocked` - The destination account is currently blocked from
      receiving transactions. Corresponds to the FedNow reason code `AC06`.
    - `invalid_agent` - The recipient's bank was not a valid agent for this
      transfer. Corresponds to the FedNow reason codes `AC14` and `AGNT`.
    - `invalid_creditor_account_number` - The destination account does not exist.
      Corresponds to the FedNow reason code `AC03`.
    - `incorrect_account_number` - The destination account number was incorrect.
      Corresponds to the FedNow reason code `AC01`.
    - `end_customer_deceased` - The destination account holder is deceased.
      Corresponds to the FedNow reason code `MD07`.
    - `transaction_forbidden` - The transfer was not permitted by the recipient's
      bank. Corresponds to the FedNow reason code `AG01`.
    - `regulatory_reason` - The transfer was returned for a regulatory reason at the
      recipient's bank. Corresponds to the FedNow reason code `RR04`.
    - `fraud` - The transfer was reported as fraudulent. Corresponds to the FedNow
      reason code `FR01`.
    - `duplication` - The transfer duplicated another transfer. Corresponds to the
      FedNow reason codes `AM05` and `DUPL`.
    - `wrong_amount` - The transfer amount was incorrect. Corresponds to the FedNow
      reason code `AM09`.
    - `requested_by_customer` - The transfer was returned at the request of the
      recipient's customer. Corresponds to the FedNow reason code `CUST`.
    - `unable_to_apply` - The recipient's bank could not apply the funds.
      Corresponds to the FedNow reason code `RUTA`.
    - `not_specified` - The recipient's bank did not specify a reason. Corresponds
      to the FedNow reason codes `MS02` and `MS03`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field. Corresponds to the FedNow reason code `NARR`.
    - `other` - The transfer was returned for some other reason.
    """

    transfer_id: str
    """The identifier of the FedNow Transfer that led to this Transaction."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Submission(BaseModel):
    """
    After the transfer is submitted to FedNow, this will contain supplemental details.
    """

    message_identification: str
    """The FedNow network identification of the message submitted."""

    submitted_at: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was submitted to FedNow.
    """


class FednowTransfer(BaseModel):
    """
    FedNow transfers move funds, within seconds, between your Increase account and any other account supporting FedNow.
    """

    id: str
    """The FedNow Transfer's identifier."""

    account_id: str
    """The Account from which the transfer was sent."""

    account_number: str
    """The destination account number."""

    acknowledgement: Optional[Acknowledgement] = None
    """
    If the transfer is acknowledged by the recipient bank, this will contain
    supplemental details.
    """

    amount: int
    """The transfer amount in USD cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the transfer was created.
    """

    created_by: Optional[CreatedBy] = None
    """What object created the transfer, either via the API or the dashboard."""

    creditor_address: Optional[CreditorAddress] = None
    """The creditor's address."""

    creditor_name: str
    """The name of the transfer's recipient.

    This is set by the sender when creating the transfer.
    """

    currency: Literal["USD"]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transfer's
    currency. For FedNow transfers this is always equal to `USD`.

    - `USD` - US Dollar (USD)
    """

    debtor_address: Optional[DebtorAddress] = None
    """The debtor's address."""

    debtor_name: str
    """The name of the transfer's sender.

    If not provided, defaults to the name of the account's entity.
    """

    external_account_id: Optional[str] = None
    """The identifier of the External Account the transfer was made to, if any."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    pending_transaction_id: Optional[str] = None
    """The ID for the pending transaction representing the transfer."""

    rejection: Optional[Rejection] = None
    """
    If the transfer is rejected by FedNow or the destination financial institution,
    this will contain supplemental details.
    """

    returns: List[Return]
    """
    If the transfer is returned by the recipient's bank, this will contain details
    of each return. FedNow allows returning part of a transfer, so a transfer can be
    returned more than once.
    """

    routing_number: str
    """
    The destination American Bankers' Association (ABA) Routing Transit Number
    (RTN).
    """

    source_account_number_id: str
    """The Account Number the recipient will see as having sent the transfer."""

    status: Literal[
        "pending_submitting",
        "pending_reviewing",
        "canceled",
        "requires_attention",
        "pending_approval",
        "pending_response",
        "complete",
        "rejected",
        "returned",
    ]
    """The lifecycle status of the transfer.

    - `pending_submitting` - The transfer is queued to be submitted to FedNow.
    - `pending_reviewing` - The transfer is pending review by Increase.
    - `canceled` - The transfer has been canceled.
    - `requires_attention` - The transfer requires attention from an Increase
      operator.
    - `pending_approval` - The transfer is pending approval.
    - `pending_response` - The transfer has been submitted and is pending a response
      from FedNow.
    - `complete` - The transfer has been sent successfully and is complete.
    - `rejected` - The transfer was rejected by the network or the recipient's bank.
    - `returned` - The transfer was returned by the recipient's bank.
    """

    submission: Optional[Submission] = None
    """
    After the transfer is submitted to FedNow, this will contain supplemental
    details.
    """

    transaction_id: Optional[str] = None
    """The Transaction funding the transfer once it is complete."""

    type: Literal["fednow_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `fednow_transfer`.
    """

    unique_end_to_end_transaction_reference: str
    """
    The Unique End-to-end Transaction Reference
    ([UETR](https://www.swift.com/payments/what-unique-end-end-transaction-reference-uetr))
    of the transfer.
    """

    unstructured_remittance_information: str
    """Unstructured information that will show on the recipient's bank statement."""
