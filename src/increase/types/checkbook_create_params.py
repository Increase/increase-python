# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["CheckbookCreateParams", "MailingAddress", "Payer"]


class CheckbookCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number that the checks will draw from.

    The Account Number must be active.
    """

    mailing_address: Required[MailingAddress]
    """The destination address that the Checkbook will be mailed to."""

    payer: Required[Iterable[Payer]]
    """The payer of the checks.

    This will be printed on the top-left corner of each check. This should be an
    array of up to 4 elements, each of which represents a line of the payer.
    """


class MailingAddress(TypedDict, total=False):
    """The destination address that the Checkbook will be mailed to."""

    city: Required[str]
    """The city of the destination address."""

    line1: Required[str]
    """The first line of the destination address."""

    name: Required[str]
    """The recipient at the destination address."""

    postal_code: Required[str]
    """The postal code of the destination address."""

    state: Required[str]
    """The US state of the destination address."""

    line2: str
    """The second line of the destination address."""


class Payer(TypedDict, total=False):
    contents: Required[str]
    """The contents of the line."""
