# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "InboundACHTransfer",
    "Acceptance",
    "Addenda",
    "AddendaFreeform",
    "AddendaFreeformEntry",
    "Decline",
    "NotificationOfChange",
    "TransferReturn",
]


class Acceptance(BaseModel):
    accepted_at: datetime
    """The time at which the transfer was accepted."""

    transaction_id: str
    """The id of the transaction for the accepted transfer."""


class AddendaFreeformEntry(BaseModel):
    payment_related_information: str
    """The payment related information passed in the addendum."""


class AddendaFreeform(BaseModel):
    entries: List[AddendaFreeformEntry]
    """Each entry represents an addendum received from the originator."""


class Addenda(BaseModel):
    category: Literal["freeform"]
    """The type of addendum.

    - `freeform` - Unstructured addendum.
    """

    freeform: Optional[AddendaFreeform] = None
    """Unstructured `payment_related_information` passed through by the originator."""


class Decline(BaseModel):
    declined_at: datetime
    """The time at which the transfer was declined."""

    declined_transaction_id: str
    """The id of the transaction for the declined transfer."""

    reason: Literal[
        "ach_route_canceled",
        "ach_route_disabled",
        "breaches_limit",
        "credit_entry_refused_by_receiver",
        "duplicate_return",
        "entity_not_active",
        "field_error",
        "group_locked",
        "insufficient_funds",
        "misrouted_return",
        "return_of_erroneous_or_reversing_debit",
        "no_ach_route",
        "originator_request",
        "transaction_not_allowed",
        "user_initiated",
    ]
    """The reason for the transfer decline.

    - `ach_route_canceled` - The account number is canceled.
    - `ach_route_disabled` - The account number is disabled.
    - `breaches_limit` - The transaction would cause an Increase limit to be
      exceeded.
    - `credit_entry_refused_by_receiver` - A credit was refused. This is a
      reasonable default reason for decline of credits.
    - `duplicate_return` - A rare return reason. The return this message refers to
      was a duplicate.
    - `entity_not_active` - The account's entity is not active.
    - `field_error` - There was an error with one of the required fields.
    - `group_locked` - Your account is inactive.
    - `insufficient_funds` - Your account contains insufficient funds.
    - `misrouted_return` - A rare return reason. The return this message refers to
      was misrouted.
    - `return_of_erroneous_or_reversing_debit` - The originating financial
      institution made a mistake and this return corrects it.
    - `no_ach_route` - The account number that was debited does not exist.
    - `originator_request` - The originating financial institution asked for this
      transfer to be returned.
    - `transaction_not_allowed` - The transaction is not allowed per Increase's
      terms.
    - `user_initiated` - Your integration declined this transfer via the API.
    """


class NotificationOfChange(BaseModel):
    updated_account_number: Optional[str] = None
    """The new account number provided in the notification of change."""

    updated_routing_number: Optional[str] = None
    """The new account number provided in the notification of change."""


class TransferReturn(BaseModel):
    reason: Literal[
        "insufficient_funds",
        "returned_per_odfi_request",
        "authorization_revoked_by_customer",
        "payment_stopped",
        "customer_advised_unauthorized_improper_ineligible_or_incomplete",
        "representative_payee_deceased_or_unable_to_continue_in_that_capacity",
        "beneficiary_or_account_holder_deceased",
        "credit_entry_refused_by_receiver",
        "duplicate_entry",
        "corporate_customer_advised_not_authorized",
    ]
    """The reason for the transfer return.

    - `insufficient_funds` - The customer's account has insufficient funds. This
      reason is only allowed for debits. The Nacha return code is R01.
    - `returned_per_odfi_request` - The originating financial institution asked for
      this transfer to be returned. The receiving bank is complying with the
      request. The Nacha return code is R06.
    - `authorization_revoked_by_customer` - The customer no longer authorizes this
      transaction. The Nacha return code is R07.
    - `payment_stopped` - The customer asked for the payment to be stopped. This
      reason is only allowed for debits. The Nacha return code is R08.
    - `customer_advised_unauthorized_improper_ineligible_or_incomplete` - The
      customer advises that the debit was unauthorized. The Nacha return code is
      R10.
    - `representative_payee_deceased_or_unable_to_continue_in_that_capacity` - The
      payee is deceased. The Nacha return code is R14.
    - `beneficiary_or_account_holder_deceased` - The account holder is deceased. The
      Nacha return code is R15.
    - `credit_entry_refused_by_receiver` - The customer refused a credit entry. This
      reason is only allowed for credits. The Nacha return code is R23.
    - `duplicate_entry` - The account holder identified this transaction as a
      duplicate. The Nacha return code is R24.
    - `corporate_customer_advised_not_authorized` - The corporate customer no longer
      authorizes this transaction. The Nacha return code is R29.
    """

    returned_at: datetime
    """The time at which the transfer was returned."""

    transaction_id: str
    """The id of the transaction for the returned transfer."""


class InboundACHTransfer(BaseModel):
    id: str
    """The inbound ACH transfer's identifier."""

    acceptance: Optional[Acceptance] = None
    """If your transfer is accepted, this will contain details of the acceptance."""

    account_id: str
    """The Account to which the transfer belongs."""

    account_number_id: str
    """The identifier of the Account Number to which this transfer was sent."""

    addenda: Optional[Addenda] = None
    """Additional information sent from the originator."""

    amount: int
    """The transfer amount in USD cents."""

    automatically_resolves_at: datetime
    """The time at which the transfer will be automatically resolved."""

    decline: Optional[Decline] = None
    """If your transfer is declined, this will contain details of the decline."""

    direction: Literal["credit", "debit"]
    """The direction of the transfer.

    - `credit` - Credit
    - `debit` - Debit
    """

    notification_of_change: Optional[NotificationOfChange] = None
    """
    If you initiate a notification of change in response to the transfer, this will
    contain its details.
    """

    originator_company_descriptive_date: Optional[str] = None
    """The descriptive date of the transfer."""

    originator_company_discretionary_data: Optional[str] = None
    """The additional information included with the transfer."""

    originator_company_entry_description: str
    """The description of the transfer."""

    originator_company_id: str
    """The id of the company that initiated the transfer."""

    originator_company_name: str
    """The name of the company that initiated the transfer."""

    originator_routing_number: str
    """
    The American Banking Association (ABA) routing number of the bank originating
    the transfer.
    """

    receiver_id_number: Optional[str] = None
    """The id of the receiver of the transfer."""

    receiver_name: Optional[str] = None
    """The name of the receiver of the transfer."""

    standard_entry_class_code: Literal[
        "corporate_credit_or_debit",
        "corporate_trade_exchange",
        "prearranged_payments_and_deposit",
        "internet_initiated",
        "point_of_sale",
        "telephone_initiated",
        "customer_initiated",
        "accounts_receivable",
        "machine_transfer",
        "shared_network_transaction",
        "represented_check",
        "back_office_conversion",
        "point_of_purchase",
        "check_truncation",
        "destroyed_check",
    ]
    """The Standard Entry Class (SEC) code of the transfer.

    - `corporate_credit_or_debit` - Corporate Credit and Debit (CCD).
    - `corporate_trade_exchange` - Corporate Trade Exchange (CTX).
    - `prearranged_payments_and_deposit` - Prearranged Payments and Deposits (PPD).
    - `internet_initiated` - Internet Initiated (WEB).
    - `point_of_sale` - Point of Sale (POS).
    - `telephone_initiated` - Telephone Initiated (TEL).
    - `customer_initiated` - Customer Initiated (CIE).
    - `accounts_receivable` - Accounts Receivable (ARC).
    - `machine_transfer` - Machine Transfer (MTE).
    - `shared_network_transaction` - Shared Network Transaction (SHR).
    - `represented_check` - Represented Check (RCK).
    - `back_office_conversion` - Back Office Conversion (BOC).
    - `point_of_purchase` - Point of Purchase (POP).
    - `check_truncation` - Check Truncation (TRC).
    - `destroyed_check` - Destroyed Check (XCK).
    """

    status: Literal["pending", "declined", "accepted", "returned"]
    """The status of the transfer.

    - `pending` - The Inbound ACH Transfer is awaiting action, will transition
      automatically if no action is taken.
    - `declined` - The Inbound ACH Transfer has been declined.
    - `accepted` - The Inbound ACH Transfer is accepted.
    - `returned` - The Inbound ACH Transfer has been returned.
    """

    trace_number: str
    """The trace number of the transfer."""

    transfer_return: Optional[TransferReturn] = None
    """If your transfer is returned, this will contain details of the return."""

    type: Literal["inbound_ach_transfer"]
    """A constant representing the object's type.

    For this resource it will always be `inbound_ach_transfer`.
    """
