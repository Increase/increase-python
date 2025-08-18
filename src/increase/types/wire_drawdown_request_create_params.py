# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireDrawdownRequestCreateParams", "CreditorAddress", "DebtorAddress"]


class WireDrawdownRequestCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The Account Number to which the debtor should send funds."""

    amount: Required[int]
    """The amount requested from the debtor, in USD cents."""

    creditor_address: Required[CreditorAddress]
    """The creditor's address."""

    creditor_name: Required[str]
    """The creditor's name."""

    debtor_address: Required[DebtorAddress]
    """The debtor's address."""

    debtor_name: Required[str]
    """The debtor's name."""

    unstructured_remittance_information: Required[str]
    """Remittance information the debtor will see as part of the request."""

    debtor_account_number: str
    """The debtor's account number."""

    debtor_external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `debtor_account_number` and
    `debtor_routing_number` must be absent.
    """

    debtor_routing_number: str
    """The debtor's routing number."""


class CreditorAddress(TypedDict, total=False):
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
    """The ZIP code of the address."""

    state: str
    """The address state."""


class DebtorAddress(TypedDict, total=False):
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
    """The ZIP code of the address."""

    state: str
    """The address state."""
