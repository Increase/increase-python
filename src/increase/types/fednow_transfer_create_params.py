# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FednowTransferCreateParams", "CreditorAddress", "DebtorAddress"]


class FednowTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The amount, in minor units, to send to the creditor."""

    creditor_name: Required[str]
    """The creditor's name."""

    debtor_name: Required[str]
    """The debtor's name."""

    source_account_number_id: Required[str]
    """The Account Number to include in the transfer as the debtor's account number."""

    unstructured_remittance_information: Required[str]
    """Unstructured remittance information to include in the transfer."""

    account_number: str
    """The creditor's account number."""

    creditor_address: CreditorAddress
    """The creditor's address."""

    debtor_address: DebtorAddress
    """The debtor's address."""

    external_account_id: str
    """The ID of an External Account to initiate a transfer to.

    If this parameter is provided, `account_number` and `routing_number` must be
    absent.
    """

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""

    routing_number: str
    """The creditor's bank account routing number."""


class CreditorAddress(TypedDict, total=False):
    city: Required[str]
    """The city, district, town, or village of the address."""

    postal_code: Required[str]
    """The postal code component of the address."""

    state: Required[str]
    """The US state component of the address."""

    line1: str
    """The first line of the address. This is usually the street number and street."""


class DebtorAddress(TypedDict, total=False):
    city: Required[str]
    """The city, district, town, or village of the address."""

    postal_code: Required[str]
    """The postal code component of the address."""

    state: Required[str]
    """The US state component of the address."""

    line1: str
    """The first line of the address. This is usually the street number and street."""
