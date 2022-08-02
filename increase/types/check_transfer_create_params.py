# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckTransferCreateParams"]


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
    """The descriptor that will be printed on the check."""

    recipient_name: Required[str]
    """The name that will be printed on the check."""

    address_line2: str
    """The second line of the address of the check's destination."""
