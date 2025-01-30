# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CheckTransferCreateParams",
    "PhysicalCheck",
    "PhysicalCheckMailingAddress",
    "PhysicalCheckReturnAddress",
    "ThirdParty",
]


class CheckTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in USD cents."""

    fulfillment_method: Required[Literal["physical_check", "third_party"]]
    """Whether Increase will print and mail the check or if you will do it yourself.

    - `physical_check` - Increase will print and mail a physical check.
    - `third_party` - Increase will not print a check; you are responsible for
      printing and mailing a check with the provided account number, routing number,
      check number, and amount.
    """

    source_account_number_id: Required[str]
    """
    The identifier of the Account Number from which to send the transfer and print
    on the check.
    """

    physical_check: PhysicalCheck
    """Details relating to the physical check that Increase will print and mail.

    This is required if `fulfillment_method` is equal to `physical_check`. It must
    not be included if any other `fulfillment_method` is provided.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    third_party: ThirdParty
    """Details relating to the custom fulfillment you will perform.

    This is required if `fulfillment_method` is equal to `third_party`. It must not
    be included if any other `fulfillment_method` is provided.
    """


class PhysicalCheckMailingAddress(TypedDict, total=False):
    city: Required[str]
    """The city component of the check's destination address."""

    line1: Required[str]
    """The first line of the address component of the check's destination address."""

    postal_code: Required[str]
    """The postal code component of the check's destination address."""

    state: Required[str]
    """The US state component of the check's destination address."""

    line2: str
    """The second line of the address component of the check's destination address."""

    name: str
    """The name component of the check's destination address.

    Defaults to the provided `recipient_name` parameter.
    """


class PhysicalCheckReturnAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the return address."""

    line1: Required[str]
    """The first line of the return address."""

    name: Required[str]
    """The name of the return address."""

    postal_code: Required[str]
    """The postal code of the return address."""

    state: Required[str]
    """The US state of the return address."""

    line2: str
    """The second line of the return address."""


class PhysicalCheck(TypedDict, total=False):
    mailing_address: Required[PhysicalCheckMailingAddress]
    """Details for where Increase will mail the check."""

    memo: Required[str]
    """The descriptor that will be printed on the memo field on the check."""

    recipient_name: Required[str]
    """The name that will be printed on the check in the 'To:' field."""

    note: str
    """The descriptor that will be printed on the letter included with the check."""

    return_address: PhysicalCheckReturnAddress
    """The return address to be printed on the check.

    If omitted this will default to an Increase-owned address that will mark checks
    as delivery failed and shred them.
    """

    signature_text: str
    """The text that will appear as the signature on the check in cursive font.

    If not provided, the check will be printed with 'No signature required'.
    """


class ThirdParty(TypedDict, total=False):
    check_number: str
    """The check number you will print on the check.

    This should not contain leading zeroes. If this is omitted, Increase will
    generate a check number for you; you should inspect the response and use that
    check number.
    """
