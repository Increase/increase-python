# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SwiftTransferCreateParams", "CreditorAddress", "DebtorAddress"]


class SwiftTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    account_number: Required[str]
    """The creditor's account number."""

    bank_identification_code: Required[str]
    """The bank identification code (BIC) of the creditor.

    If it ends with the three-character branch code, this must be 11 characters
    long. Otherwise this must be 8 characters and the branch code will be assumed to
    be `XXX`.
    """

    creditor_address: Required[CreditorAddress]
    """The creditor's address."""

    creditor_name: Required[str]
    """The creditor's name."""

    debtor_address: Required[DebtorAddress]
    """The debtor's address."""

    debtor_name: Required[str]
    """The debtor's name."""

    instructed_amount: Required[int]
    """The amount, in minor units of `instructed_currency`, to send to the creditor."""

    instructed_currency: Required[Literal["USD"]]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the
    instructed amount.

    - `USD` - United States Dollar
    """

    source_account_number_id: Required[str]
    """The Account Number to include in the transfer as the debtor's account number."""

    unstructured_remittance_information: Required[str]
    """Unstructured remittance information to include in the transfer."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """The creditor's bank account routing or transit number.

    Required in certain countries.
    """


class CreditorAddress(TypedDict, total=False):
    """The creditor's address."""

    city: Required[str]
    """The city, district, town, or village of the address."""

    country: Required[str]
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: Required[str]
    """The first line of the address. This is usually the street number and street."""

    line2: str
    """The second line of the address. This might be the floor or room number."""

    postal_code: str
    """The ZIP or postal code of the address. Required in certain countries."""

    state: str
    """The state, province, or region of the address. Required in certain countries."""


class DebtorAddress(TypedDict, total=False):
    """The debtor's address."""

    city: Required[str]
    """The city, district, town, or village of the address."""

    country: Required[str]
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: Required[str]
    """The first line of the address. This is usually the street number and street."""

    line2: str
    """The second line of the address. This might be the floor or room number."""

    postal_code: str
    """The ZIP or postal code of the address. Required in certain countries."""

    state: str
    """The state, province, or region of the address. Required in certain countries."""
