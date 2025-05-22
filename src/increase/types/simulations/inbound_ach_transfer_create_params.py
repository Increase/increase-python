# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InboundACHTransferCreateParams", "Addenda", "AddendaFreeform", "AddendaFreeformEntry"]


class InboundACHTransferCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the inbound ACH Transfer is for."""

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    addenda: Addenda
    """Additional information to include in the transfer."""

    company_descriptive_date: str
    """The description of the date of the transfer."""

    company_discretionary_data: str
    """Data associated with the transfer set by the sender."""

    company_entry_description: str
    """The description of the transfer set by the sender."""

    company_id: str
    """The sender's company ID."""

    company_name: str
    """The name of the sender."""

    receiver_id_number: str
    """The ID of the receiver of the transfer."""

    receiver_name: str
    """The name of the receiver of the transfer."""

    resolve_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time at which the transfer should be resolved.

    If not provided will resolve immediately.
    """

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
        "international_ach_transaction",
    ]
    """The standard entry class code for the transfer.

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
    - `international_ach_transaction` - International ACH Transaction (IAT).
    """


class AddendaFreeformEntry(TypedDict, total=False):
    payment_related_information: Required[str]
    """The payment related information passed in the addendum."""


class AddendaFreeform(TypedDict, total=False):
    entries: Required[Iterable[AddendaFreeformEntry]]
    """Each entry represents an addendum sent with the transfer."""


class Addenda(TypedDict, total=False):
    category: Required[Literal["freeform"]]
    """The type of addenda to simulate being sent with the transfer.

    - `freeform` - Unstructured `payment_related_information` passed through with
      the transfer.
    """

    freeform: AddendaFreeform
    """Unstructured `payment_related_information` passed through with the transfer."""
