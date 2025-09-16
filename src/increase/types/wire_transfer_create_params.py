# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WireTransferCreateParams", "Remittance", "RemittanceTax", "RemittanceUnstructured"]


class WireTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in USD cents."""

    beneficiary_name: Required[str]
    """The beneficiary's name."""

    account_number: str
    """The account number for the destination account."""

    beneficiary_address_line1: str
    """The beneficiary's address line 1."""

    beneficiary_address_line2: str
    """The beneficiary's address line 2."""

    beneficiary_address_line3: str
    """The beneficiary's address line 3."""

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

    originator_address_line1: str
    """The originator's address line 1.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line2: str
    """The originator's address line 2.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_address_line3: str
    """The originator's address line 3.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    originator_name: str
    """The originator's name.

    This is only necessary if you're transferring from a commingled account.
    Otherwise, we'll use the associated entity's details.
    """

    remittance: Remittance
    """Additional remittance information related to the wire transfer."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """
    The American Bankers' Association (ABA) Routing Transit Number (RTN) for the
    destination account.
    """

    source_account_number_id: str
    """The ID of an Account Number that will be passed to the wire's recipient"""


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
    """The message to the beneficiary."""


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
