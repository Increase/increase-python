# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckTransferCreateParams", "ReturnAddress"]


class CheckTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    address_city: Required[str]
    """The city of the check's destination."""

    address_line1: Required[str]
    """The street address of the check's destination."""

    address_state: Required[str]
    """The state of the check's destination."""

    address_zip: Required[str]
    """The postal code of the check's destination."""

    amount: Required[int]
    """The transfer amount in cents."""

    message: Required[str]
    """The descriptor that will be printed on the memo field on the check."""

    recipient_name: Required[str]
    """The name that will be printed on the check."""

    address_line2: str
    """The second line of the address of the check's destination."""

    note: str
    """The descriptor that will be printed on the letter included with the check."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    return_address: ReturnAddress
    """The return address to be printed on the check.

    If omitted this will default to the address of the Entity of the Account used to
    make the Check Transfer.
    """


class ReturnAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the return address."""

    line1: Required[str]
    """The first line of the return address."""

    name: Required[str]
    """The name of the return address."""

    state: Required[str]
    """The US state of the return address."""

    zip: Required[str]
    """The postal code of the return address."""

    line2: str
    """The second line of the return address."""
