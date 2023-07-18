# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CheckTransferCreateParams", "PhysicalCheck", "PhysicalCheckMailingAddress", "PhysicalCheckReturnAddress"]


class CheckTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in cents."""

    fulfillment_method: Literal["physical_check", "third_party"]
    """Whether Increase will print and mail the check or if you will do it yourself.

    - `physical_check` - Increase will print and mail a physical check.
    - `third_party` - Increase will not print a check; you are responsible for
      printing and mailing a check with the provided account number, routing number,
      check number, and amount.
    """

    physical_check: PhysicalCheck
    """Details relating to the physical check that Increase will print and mail.

    This is required if `fulfillment_method` is equal to `physical_check`. It must
    not be included if any other `fulfillment_method` is provided.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    source_account_number_id: str
    """
    The identifier of the Account Number from which to send the transfer and print
    on the check.
    """

    unique_identifier: str
    """A unique identifier you choose for the transfer.

    Reusing this identifer for another transfer will result in an error. You can
    query for the transfer associated with this identifier using the List endpoint.
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

    If omitted this will default to the address of the Entity of the Account used to
    make the Check Transfer.
    """
