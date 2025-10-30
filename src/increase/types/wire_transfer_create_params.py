# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WireTransferCreateParams",
    "Creditor",
    "CreditorAddress",
    "CreditorAddressUnstructured",
    "Remittance",
    "RemittanceTax",
    "RemittanceUnstructured",
    "Debtor",
    "DebtorAddress",
    "DebtorAddressUnstructured",
]


class WireTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in USD cents."""

    creditor: Required[Creditor]
    """The person or business that is receiving the funds from the transfer."""

    remittance: Required[Remittance]
    """Additional remittance information related to the wire transfer."""

    account_number: str
    """The account number for the destination account."""

    debtor: Debtor
    """The person or business whose funds are being transferred.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number` and `routing_number` must be
    absent.
    """

    inbound_wire_drawdown_request_id: str
    """
    The ID of an Inbound Wire Drawdown Request in response to which this transfer is
    being sent.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    source_account_number_id: str
    """The ID of an Account Number that will be passed to the wire's recipient"""


class CreditorAddressUnstructured(TypedDict, total=False):
    line1: Required[str]
    """The address line 1."""

    line2: str
    """The address line 2."""

    line3: str
    """The address line 3."""


class CreditorAddress(TypedDict, total=False):
    unstructured: Required[CreditorAddressUnstructured]
    """Unstructured address lines."""


class Creditor(TypedDict, total=False):
    name: Required[str]
    """The person or business's name."""

    address: CreditorAddress
    """The person or business's address."""


class RemittanceTax(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]
    """The month and year the tax payment is for, in YYYY-MM-DD format.

    The day is ignored.
    """

    identification_number: Required[str]
    """
    The 9-digit Tax Identification Number (TIN) or Employer Identification Number
    (EIN).
    """

    type_code: Required[str]
    """The 5-character tax type code."""


class RemittanceUnstructured(TypedDict, total=False):
    message: Required[str]
    """The information."""


class Remittance(TypedDict, total=False):
    category: Required[Literal["unstructured", "tax"]]
    """The type of remittance information being passed.

    - `unstructured` - The wire transfer contains unstructured remittance
      information.
    - `tax` - The wire transfer is for tax payment purposes to the Internal Revenue
      Service (IRS).
    """

    tax: RemittanceTax
    """Internal Revenue Service (IRS) tax repayment information.

    Required if `category` is equal to `tax`.
    """

    unstructured: RemittanceUnstructured
    """Unstructured remittance information.

    Required if `category` is equal to `unstructured`.
    """


class DebtorAddressUnstructured(TypedDict, total=False):
    line1: Required[str]
    """The address line 1."""

    line2: str
    """The address line 2."""

    line3: str
    """The address line 3."""


class DebtorAddress(TypedDict, total=False):
    unstructured: Required[DebtorAddressUnstructured]
    """Unstructured address lines."""


class Debtor(TypedDict, total=False):
    name: Required[str]
    """The person or business's name."""

    address: DebtorAddress
    """The person or business's address."""
